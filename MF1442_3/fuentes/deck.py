from lxml import etree

NS = {
    'office': 'urn:oasis:names:tc:opendocument:xmlns:office:1.0',
    'style': 'urn:oasis:names:tc:opendocument:xmlns:style:1.0',
    'text': 'urn:oasis:names:tc:opendocument:xmlns:text:1.0',
    'draw': 'urn:oasis:names:tc:opendocument:xmlns:drawing:1.0',
    'presentation': 'urn:oasis:names:tc:opendocument:xmlns:presentation:1.0',
    'svg': 'urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0',
    'fo': 'urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0',
    'table': 'urn:oasis:names:tc:opendocument:xmlns:table:1.0',
    'xlink': 'http://www.w3.org/1999/xlink',
}
FONT = 'Liberation Sans'
INK = '#16152B'
GREY = '#5A5872'
LINE = '#E3E1F0'
CARDBG = '#F6F5FB'

W, H = 33.867, 19.05  # cm, 16:9


def q(pre, tag):
    return '{%s}%s' % (NS[pre], tag)


def el(parent, pre, tag, **attrs):
    e = etree.SubElement(parent, q(pre, tag))
    for k, v in attrs.items():
        p, n = k.split('__')
        e.set(q(p, n.replace('_', '-')), str(v))
    return e


class Deck:
    def __init__(self):
        self.root = etree.Element(q('office', 'document'), nsmap=NS)
        self.root.set(q('office', 'version'), '1.2')
        self.root.set(q('office', 'mimetype'), 'application/vnd.oasis.opendocument.presentation')
        ff = el(self.root, 'office', 'font-face-decls')
        for name in (FONT,):
            el(ff, 'style', 'font-face', style__name=name,
               svg__font_family="'%s'" % name, style__font_family_generic='swiss',
               style__font_pitch='variable')
        self.common = el(self.root, 'office', 'styles')
        self.auto = el(self.root, 'office', 'automatic-styles')
        pl = el(self.auto, 'style', 'page-layout', style__name='pm1')
        el(pl, 'style', 'page-layout-properties',
           fo__page_width='%scm' % W, fo__page_height='%scm' % H,
           style__print_orientation='landscape',
           fo__margin_top='0cm', fo__margin_bottom='0cm',
           fo__margin_left='0cm', fo__margin_right='0cm')
        el(pl, 'style', 'drawing-page-properties', draw__fill='solid',
           draw__fill_color='#FFFFFF')
        self.para_styles = {}
        self.graphic_styles = {}
        self.cell_styles = {}
        ls = el(self.auto, 'text', 'list-style', style__name='LB')
        for lvl in (1, 2):
            b = el(ls, 'text', 'list-level-style-bullet', text__level=str(lvl),
                   text__bullet_char='•' if lvl == 1 else '–')
            el(b, 'style', 'list-level-properties',
               text__space_before='%scm' % (0.55 if lvl == 1 else 1.1),
               text__min_label_width='0.5cm',
               fo__text_align='left')
            el(b, 'style', 'text-properties', fo__font_size='%spt' % (13 if lvl == 1 else 12),
               fo__color='#3B34C7')
        body = el(self.root, 'office', 'body')
        ms = etree.Element(q('office', 'master-styles'))
        self.root.insert(list(self.root).index(body), ms)
        el(ms, 'style', 'master-page', style__name='Default', style__page_layout_name='pm1')
        self.pres = el(body, 'office', 'presentation')

    # ---------- estilos ----------
    def para(self, name, size=13, color=INK, bold=False, italic=False,
             align='start', before=0, after=0.1, line=None):
        s = el(self.auto, 'style', 'style', style__name=name, style__family='paragraph')
        el(s, 'style', 'paragraph-properties', fo__text_align=align,
           fo__margin_top='%scm' % before, fo__margin_bottom='%scm' % after,
           fo__line_height='%s%%' % (line or 120))
        el(s, 'style', 'text-properties', style__font_name=FONT,
           fo__font_size='%spt' % size, fo__color=color,
           fo__font_weight='bold' if bold else 'normal',
           fo__font_style='italic' if italic else 'normal')
        self.para_styles[name] = s
        return name

    def graphic(self, name, fill=None, stroke=None, radius=None):
        s = el(self.common, 'style', 'style', style__name=name, style__family='graphic')
        props = el(s, 'style', 'graphic-properties',
                  draw__fill='solid' if fill else 'none',
                  draw__fill_color=fill or '#FFFFFF',
                  draw__stroke='solid' if stroke else 'none',
                  draw__stroke_color=stroke or '#000000',
                  draw__shadow='none')
        if stroke:
            props.set(q('draw', 'stroke-width'), '0.03cm')
        if radius:
            props.set(q('draw', 'corner-radius'), radius)
        self.graphic_styles[name] = s
        return name

    def tstyle(self, name, size=None, color=None, bold=False, italic=False):
        s = el(self.auto, 'style', 'style', style__name=name, style__family='text')
        el(s, 'style', 'text-properties',
           style__font_name=FONT,
           fo__font_size='%spt' % size if size else '12pt',
           fo__color=color or INK,
           fo__font_weight='bold' if bold else 'normal',
           fo__font_style='italic' if italic else 'normal')
        return name

    def cell(self, name, bg=None, border=LINE, bold=False, size=10.5, color=INK, align='start'):
        s = el(self.common, 'style', 'style', style__name=name, style__family='table-cell')
        props = el(s, 'style', 'table-cell-properties',
                   fo__background_color=bg or '#FFFFFF',
                   fo__padding='0.14cm')
        if border:
            props.set(q('fo', 'border'), '0.02cm solid %s' % border)
        self.cell_styles[name] = s
        return name
    # ---------- estilos de marco ----------
    def ensure_frames(self):
        for name, anchor in (('frTop', 'top'), ('frMid', 'middle'), ('frBot', 'bottom')):
            s = el(self.common, 'style', 'style', style__name=name, style__family='graphic')
            el(s, 'style', 'graphic-properties', draw__fill='none', draw__stroke='none',
               draw__textarea_vertical_align=anchor)
        return self

    def column(self, name, width):
        s = el(self.auto, 'style', 'style', style__name=name, style__family='table-column')
        el(s, 'style', 'table-column-properties', style__column_width='%scm' % width)
        return name

    def save(self, path):
        data = etree.tostring(self.root, xml_declaration=True, encoding='UTF-8', pretty_print=True)
        with open(path, 'wb') as f:
            f.write(data)


class Slide:
    n = 0

    def __init__(self, deck, name=None):
        Slide.n += 1
        self.deck = deck
        self.name = name or 'S%d' % Slide.n
        self.page = el(deck.pres, 'draw', 'page', draw__name=self.name,
                       draw__master_page_name='Default')
        self.n = Slide.n

    def rect(self, style, x, y, w, h, name=None):
        el(self.page, 'draw', 'rect', draw__style_name=style,
           draw__name=name or 'r', svg__x='%scm' % x, svg__y='%scm' % y,
           svg__width='%scm' % w, svg__height='%scm' % h)

    def text(self, x, y, w, h, items, anchor='frTop', name=None):
        fr = el(self.page, 'draw', 'frame', draw__style_name=anchor,
                draw__name=name or 'tb', svg__x='%scm' % x, svg__y='%scm' % y,
                svg__width='%scm' % w, svg__height='%scm' % h)
        box = el(fr, 'draw', 'text-box')
        self._fill(box, items)

    def _fill(self, parent, items):
        for it in items:
            if it.get('t') == 'ul':
                lst = el(parent, 'text', 'list', text__style_name='LB')
                for sub in it['items']:
                    li = el(lst, 'text', 'list-item')
                    p = el(li, 'text', 'p', text__style_name=sub.get('s', 'Body'))
                    self._spans(p, sub['r'])
            else:
                p = el(parent, 'text', 'p', text__style_name=it.get('s', 'Body'))
                self._spans(p, it['r'])

    @staticmethod
    def _spans(p, runs):
        for text, sty in runs:
            if sty:
                sp = el(p, 'text', 'span', text__style_name=sty)
                sp.text = text
            else:
                if len(p) == 0 and not p.text:
                    p.text = text
                else:
                    p[-1].tail = (p[-1].tail or '') + text

    def table(self, x, y, w, rows, col_w, head=True, name=None, row_h=None):
        fr = el(self.page, 'draw', 'frame', draw__style_name='frTop',
                draw__name=name or 'tb%d' % self.n,
                svg__x='%scm' % x, svg__y='%scm' % y, svg__width='%scm' % w,
                svg__height='%scm' % (len(rows) * 1.0))
        t = el(fr, 'table', 'table', table__name='T%d' % self.n)
        for i, cw in enumerate(col_w):
            cn = 'c%d_%d' % (self.n, i)
            self.deck.column(cn, cw)
            el(t, 'table', 'table-column', table__style_name=cn)
        for ri, row in enumerate(rows):
            tr = el(t, 'table', 'table-row')
            for cell in row:
                text, cstyle = cell[0], cell[1]
                pstyle = cell[2] if len(cell) > 2 else 'CellText'
                tc = el(tr, 'table', 'table-cell', table__style_name=cstyle)
                p = el(tc, 'text', 'p', text__style_name=pstyle)
                p.text = text

    def grid(self, x, y, col_w, rows, row_h=0.92, head=True, name='g',
             head_bg='CellBgHead', body_bgs=('CellBgW', 'CellBgAlt'), pad=0.16,
             head_h=None):
        yy = y
        for ri, row in enumerate(rows):
            xx = x
            h = head_h if (head and ri == 0 and head_h) else row_h
            bg = head_bg if (head and ri == 0) else body_bgs[(ri - 1) % len(body_bgs)]
            for ci, cell in enumerate(row):
                text, pstyle = cell[0], cell[1] if len(cell) > 1 else 'CellText'
                w = col_w[ci]
                self.rect(bg, xx, yy, w, h, name='%s-c%d-%d' % (name, ri, ci))
                self.text(xx + pad, yy + 0.13, w - 2 * pad, h - 0.2,
                          [{'s': pstyle, 'r': [(text, None)]}],
                          name='%s-t%d-%d' % (name, ri, ci))
                xx += w
            yy += h
        return yy

    def footer(self, left, right):
        self.text(2.0, 17.55, 22.0, 0.9, [{'s': 'Footer', 'r': [(left, None)]}])
        self.text(26.0, 17.55, 6.0, 0.9, [{'s': 'Footer', 'r': [(right, None)]}])
