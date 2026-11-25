from lxml import etree

NS = {
    'office': 'urn:oasis:names:tc:opendocument:xmlns:office:1.0',
    'style': 'urn:oasis:names:tc:opendocument:xmlns:style:1.0',
    'text': 'urn:oasis:names:tc:opendocument:xmlns:text:1.0',
    'fo': 'urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0',
    'table': 'urn:oasis:names:tc:opendocument:xmlns:table:1.0',
    'svg': 'urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0',
}
FONT = 'Liberation Sans'
INK, GREY, INDIGO, TEAL = '#16152B', '#5A5872', '#3B34C7', '#00958C'
LINE, CARDBG, PH = '#D9D7E8', '#F6F5FB', '#7C7A96'


def q(pre, tag):
    return '{%s}%s' % (NS[pre], tag)


def el(parent, pre, tag, **attrs):
    e = etree.SubElement(parent, q(pre, tag))
    for k, v in attrs.items():
        p, n = k.split('__')
        e.set(q(p, n.replace('_', '-')), str(v))
    return e


class Doc:
    def __init__(self):
        self.root = etree.Element(q('office', 'document'), nsmap=NS)
        self.root.set(q('office', 'version'), '1.2')
        self.root.set(q('office', 'mimetype'), 'application/vnd.oasis.opendocument.text')
        ff = el(self.root, 'office', 'font-face-decls')
        el(ff, 'style', 'font-face', style__name=FONT, svg__font_family="'%s'" % FONT,
           style__font_family_generic='swiss', style__font_pitch='variable')
        self.styles = el(self.root, 'office', 'styles')
        self.auto = el(self.root, 'office', 'automatic-styles')
        pl = el(self.auto, 'style', 'page-layout', style__name='pm1')
        el(pl, 'style', 'page-layout-properties',
           fo__page_width='21cm', fo__page_height='29.7cm',
           fo__margin_top='2cm', fo__margin_bottom='2cm',
           fo__margin_left='2cm', fo__margin_right='2cm')
        ms = el(self.root, 'office', 'master-styles')
        el(ms, 'style', 'master-page', style__name='Standard', style__page_layout_name='pm1')
        body = el(self.root, 'office', 'body')
        self.text_el = el(body, 'office', 'text')
        self.n = 0

    # ---------- estilos ----------
    def para(self, name, size=10.5, color=INK, bold=False, italic=False, after=0.15,
             before=0, line=145, align='start', bg=None, border_left=None, border_bottom=None,
             brk=False):
        s = el(self.styles, 'style', 'style', style__name=name, style__family='paragraph')
        pp = el(s, 'style', 'paragraph-properties',
                fo__text_align=align, fo__margin_top='%scm' % before,
                fo__margin_bottom='%scm' % after, fo__line_height='%s%%' % line)
        if bg:
            pp.set(q('fo', 'background-color'), bg)
        if border_left:
            pp.set(q('fo', 'border-left'), border_left)
            pp.set(q('fo', 'padding-left'), '0.35cm')
            pp.set(q('fo', 'padding-top'), '0.15cm')
            pp.set(q('fo', 'padding-bottom'), '0.15cm')
            pp.set(q('fo', 'padding-right'), '0.3cm')
        if border_bottom:
            pp.set(q('fo', 'border-bottom'), border_bottom)
            pp.set(q('fo', 'padding-bottom'), '0.1cm')
        if brk:
            pp.set(q('fo', 'break-before'), 'page')
        el(s, 'style', 'text-properties', style__font_name=FONT,
           fo__font_size='%spt' % size, fo__color=color,
           fo__font_weight='bold' if bold else 'normal',
           fo__font_style='italic' if italic else 'normal')
        return name

    def tstyle(self, name, size=None, color=None, bold=False):
        s = el(self.styles, 'style', 'style', style__name=name, style__family='text')
        props = el(s, 'style', 'text-properties', style__font_name=FONT,
                   fo__color=color or INK,
                   fo__font_weight='bold' if bold else 'normal')
        if size:
            props.set(q('fo', 'font-size'), '%spt' % size)
        return name

    def cellstyle(self, name, bg=None, border='0.5pt solid %s' % LINE):
        s = el(self.auto, 'style', 'style', style__name=name, style__family='table-cell')
        props = el(s, 'style', 'table-cell-properties', fo__padding='0.13cm',
                   fo__background_color=bg or '#FFFFFF',
                   fo__vertical_align='top')
        if border:
            props.set(q('fo', 'border'), border)
        return name

    def colstyle(self, name, width):
        s = el(self.auto, 'style', 'style', style__name=name, style__family='table-column')
        el(s, 'style', 'table-column-properties', style__column_width='%scm' % width)
        return name

    def setup(self):
        ts = el(self.styles, 'style', 'style', style__name='Table1', style__family='table')
        el(ts, 'style', 'table-properties', style__width='17cm', table__align='margins')
        lb = el(self.styles, 'text', 'list-style', style__name='LB')
        b = el(lb, 'text', 'list-level-style-bullet', text__level='1', text__bullet_char='•')
        el(b, 'style', 'list-level-properties', text__space_before='0.5cm',
           text__min_label_width='0.5cm')
        el(b, 'style', 'text-properties', fo__font_size='10.5pt', fo__color=INDIGO)
        return self

    def _runs(self, p, text):
        import re
        for part in re.split(r'(\[[^\]]*\])', text):
            if not part:
                continue
            if part.startswith('[') and part.endswith(']'):
                sp = el(p, 'text', 'span', text__style_name='PhSpan')
                sp.text = part
            elif len(p) == 0 and p.text is None:
                p.text = part
            else:
                if len(p):
                    p[-1].tail = (p[-1].tail or '') + part
                else:
                    p.text = (p.text or '') + part

    def h1(self, text):
        h = el(self.text_el, 'text', 'h', text__style_name='H1', text__outline_level='1')
        self._runs(h, text)

    def h2(self, text):
        h = el(self.text_el, 'text', 'h', text__style_name='H2', text__outline_level='2')
        self._runs(h, text)

    def p(self, text, style='Body'):
        e = el(self.text_el, 'text', 'p', text__style_name=style)
        self._runs(e, text)

    def bullets(self, items, style='Body'):
        lst = el(self.text_el, 'text', 'list', text__style_name='LB')
        for it in items:
            li = el(lst, 'text', 'list-item')
            e = el(li, 'text', 'p', text__style_name=style)
            self._runs(e, it)

    def pagebreak(self):
        el(self.text_el, 'text', 'p', text__style_name='PB')

    def table(self, rows, widths, head=True):
        self.n += 1
        t = el(self.text_el, 'table', 'table', table__name='T%d' % self.n,
               table__style_name='Table1')
        for i, w in enumerate(widths):
            cn = 'co%d_%d' % (self.n, i)
            self.colstyle(cn, w)
            el(t, 'table', 'table-column', table__style_name=cn)
        for ri, row in enumerate(rows):
            tr = el(t, 'table', 'table-row')
            for cell in row:
                ishead = head and ri == 0
                tc = el(tr, 'table', 'table-cell',
                        table__style_name='CellHead' if ishead else 'Cell',
                        office__value_type='string')
                e = el(tc, 'text', 'p',
                       text__style_name='TableHeadP' if ishead else 'TableCellP')
                self._runs(e, cell)

    def save(self, path):
        data = etree.tostring(self.root, xml_declaration=True, encoding='UTF-8', pretty_print=True)
        open(path, 'wb').write(data)

