import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from deck import Deck, Slide, INK, GREY, LINE, CARDBG

INDIGO, TEAL, MAGENTA, AMBER = '#3B34C7', '#00958C', '#D6218C', '#F2A20C'
PAPER = '#FBFAFF'

d = Deck()
d.ensure_frames()

# --- párrafos ---
d.para('Kicker', 9.5, TEAL, bold=True, after=0.2)
d.para('Title', 26, INK, bold=True, after=0.15, line=105)
d.para('TitleBig', 33, '#FFFFFF', bold=True, after=0.2, line=105)
d.para('Subtitle', 12.5, GREY, after=0.1)
d.para('SubLight', 12.5, '#C9C7DE', after=0.1)
d.para('H2', 15, INK, bold=True, after=0.12)
d.para('Body', 12, INK, after=0.14, line=125)
d.para('BodyS', 11, INK, after=0.12, line=125)
d.para('Small', 9.5, GREY, after=0.1, line=120)
d.para('Tiny', 8.5, GREY, after=0.05)
d.para('Footer', 8, GREY, after=0)
d.para('CardTitle', 12, INK, bold=True, after=0.05)
d.para('CardBody', 10.5, GREY, after=0.1, line=125)
d.para('BigNum', 26, INDIGO, bold=True, after=0)
d.para('BigNumS', 23, INDIGO, bold=True, after=0)
d.para('KpiLabel', 9, GREY, bold=False, after=0)
d.para('PillText', 9, '#FFFFFF', bold=True, after=0)
d.para('CellText', 9.5, INK, after=0, line=110)
d.para('CellTextB', 9.5, INK, bold=True, after=0, line=110)
d.para('CellHeadText', 8.5, '#FFFFFF', bold=True, after=0)
d.para('CellSm', 8.5, INK, after=0, line=105)
d.para('CellSmHead', 8, '#FFFFFF', bold=True, after=0)

# --- spans ---
d.tstyle('AccentSpan', 11, INDIGO, bold=True)
d.tstyle('TealSpan', 11, TEAL, bold=True)
d.tstyle('WhiteSpan', 12, '#FFFFFF', bold=True)
d.tstyle('BigWhite', 33, '#FFFFFF', bold=True)

# --- formas ---
d.graphic('Accent', fill=INDIGO)
d.graphic('Accent2', fill=TEAL)
d.graphic('Dark', fill=INK)
d.graphic('Paper', fill=PAPER)
d.graphic('CardBg', fill=CARDBG, stroke=LINE)
d.graphic('CardW', fill='#FFFFFF', stroke=LINE)
d.graphic('CellBgW', fill='#FFFFFF', stroke=LINE)
d.graphic('CellBgAlt', fill=CARDBG, stroke=LINE)
d.graphic('CellBgHead', fill=INK, stroke=INK)
d.graphic('PillIndigo', fill=INDIGO)
d.graphic('PillTeal', fill=TEAL)
d.graphic('PillMagenta', fill=MAGENTA)
d.graphic('PillAmber', fill=AMBER)


def head(s, kicker, title, subtitle=None):
    s.rect('Accent', 0, 0, 0.45, 19.05)
    s.text(2.0, 1.7, 29.0, 0.9, [{'s': 'Kicker', 'r': [(kicker, None)]}])
    s.text(2.0, 2.3, 29.6, 2.9, [{'s': 'Title', 'r': [(title, None)]}])
    if subtitle:
        s.text(2.0, 4.9, 28.0, 1.0, [{'s': 'Subtitle', 'r': [(subtitle, None)]}])


def card(s, x, y, w, h, title, body, pill='PillIndigo'):
    s.rect('CardW', x, y, w, h)
    s.rect(pill, x, y, 0.14, h)
    s.text(x + 0.45, y + 0.3, w - 0.9, 0.8, [{'s': 'CardTitle', 'r': [(title, None)]}])
    s.text(x + 0.45, y + 1.15, w - 0.95, h - 1.35, body)


def kpi(s, x, y, w, num, label, color='BigNum'):
    s.rect('CardW', x, y, w, 2.9)
    s.text(x + 0.4, y + 0.35, w - 0.8, 1.4, [{'s': color, 'r': [(num, None)]}])
    s.text(x + 0.4, y + 1.85, w - 0.8, 0.8, [{'s': 'KpiLabel', 'r': [(label, None)]}])

# ---------- 1 · PORTADA ----------
s = Slide(d, 'Portada')
s.rect('Dark', 0, 0, 33.867, 19.05)
s.rect('Accent', 0, 0, 0.55, 19.05)
s.rect('Accent2', 0.55, 0, 0.18, 19.05)
s.rect('PillMagenta', 25.8, 1.75, 5.9, 1.15)
s.text(26.15, 1.97, 5.2, 0.8, [{'s': 'PillText', 'r': [('PLANTILLA DEMO', None)]}])
s.text(2.3, 3.2, 22.0, 0.9, [{'s': 'Kicker', 'r': [('SSCE0110 · MÓDULO FORMATIVO · NIVEL 3', None)]}])
s.text(2.3, 3.85, 23.6, 6.2, [{'s': 'TitleBig', 'r': [('Programación didáctica de acciones formativas para el empleo', None)]}])
s.text(2.3, 10.5, 26.0, 1.8, [{'s': 'SubLight', 'r': [('MF1442_3 · 60 horas · 9 sesiones · Unidad de competencia UC1442_3', None)]}])
s.text(2.3, 15.4, 27.0, 0.9, [{'s': 'SubLight', 'r': [('CEFI Formación (Almonte) · 24/11/2026 → 04/12/2026', None)]}])
s.text(2.3, 16.3, 27.0, 0.9, [{'s': 'Small', 'r': [('Sustituye los textos entre [corchetes]. Una idea por diapositiva.', None)]}])

# ---------- 2 · CÓMO USAR ----------
s = Slide(d, 'Como usar')
head(s, '00 · ANTES DE EMPEZAR', 'Cómo usar esta plantilla',
     'Cuatro pasos y la presentación queda lista para la defensa del módulo.')
card(s, 2.0, 6.2, 14.3, 4.5, '1 · Duplica el archivo',
     [{'s': 'CardBody', 'r': [('Guarda una copia como ', None), ('MF1442_3_presentacion_[tunombre].pptx', 'AccentSpan'), ('. También puedes subirlo a Google Slides (Archivo → Abrir → Subir) o a Canva (Importar archivo).', None)]}])
card(s, 17.5, 6.2, 14.3, 4.5, '2 · Rellena los corchetes',
     [{'s': 'CardBody', 'r': [('Todo lo que aparece entre [corchetes] es un hueco: datos del grupo, objetivos, contenidos, criterios y evidencias. Borra el corchete cuando lo escribas.', None)]}], 'PillTeal')
card(s, 2.0, 11.1, 14.3, 4.5, '3 · Una idea por diapositiva',
     [{'s': 'CardBody', 'r': [('Máximo 6 líneas y 2 niveles de lista. Si necesitas más, duplica la diapositiva: la plantilla está hecha para crecer.', None)]}], 'PillMagenta')
card(s, 17.5, 11.1, 14.3, 4.5, '4 · Exporta en dos formatos',
     [{'s': 'CardBody', 'r': [('PDF para entregar y PPTX para seguir editando. En Google Slides: Archivo → Descargar → Microsoft PowerPoint (.pptx).', None)]}], 'PillAmber')
s.footer('MF1442_3 · Plantilla demo', '2')

# ---------- 3 · EL MÓDULO ----------
s = Slide(d, 'Modulo')
head(s, '01 · EL MÓDULO', 'Situación, horas y ventana del curso',
     'Lo que el tribunal o el formador espera ver en la primera diapositiva.')
x = 2.0
for num, label, pill in (('60 h', 'Duración oficial', 'BigNum'),
                         ('9', 'Sesiones en el cronograma', 'BigNum'),
                         ('Nivel 3', 'Cualificación', 'BigNum'),
                         ('4', 'Unidades del temario', 'BigNum')):
    kpi(s, x, 6.3, 7.3, num, label, pill)
    x += 7.8
s.text(2.0, 10.0, 29.5, 6.4, [
    {'s': 'Body', 'r': [('Ventana oficial: ', 'TealSpan'), ('24/11/2026 → 04/12/2026', 'AccentSpan'), (' (9 sesiones de 6 h, de lunes a viernes).', None)]},
    {'s': 'Body', 'r': [('Centro: ', 'TealSpan'), ('CEFI Formación S.L. · Pol. Ind. Los Taranjales II, 58 · Almonte (Huelva).', None)]},
    {'s': 'Body', 'r': [('Familia profesional: ', 'TealSpan'), ('Servicios Socioculturales y a la Comunidad · UC1442_3.', None)]},
    {'s': 'Body', 'r': [('Marco: ', 'TealSpan'), ('RD 1697/2011, Anexo IV, actualizado por el RD 625/2013 (apartado IV, prescripción de formadores).', None)]},
])
s.footer('MF1442_3 · Plantilla demo', '3')

# ---------- 4 · OBJETIVOS ----------
s = Slide(d, 'Objetivos')
head(s, '02 · OBJETIVOS', 'Qué tiene que ser capaz de hacer el alumnado',
     'Objetivo general, objetivos específicos y su criterio de evaluación.')
card(s, 2.0, 6.4, 9.6, 9.0, 'Objetivo general',
     [{'s': 'CardBody', 'r': [('[Elaborar la programación didáctica de una acción formativa para el empleo, integrando objetivos, contenidos, metodología, recursos y evaluación.]', None)]}])
card(s, 12.1, 6.4, 9.6, 9.0, 'Objetivos específicos',
     [{'t': 'ul', 'items': [
         {'s': 'CardBody', 'r': [('[Analizar el contexto y detectar necesidades formativas.]', None)]},
         {'s': 'CardBody', 'r': [('[Secuenciar contenidos en unidades didácticas.]', None)]},
         {'s': 'CardBody', 'r': [('[Diseñar actividades y su evaluación.]', None)]},
     ]}], 'PillTeal')
card(s, 22.2, 6.4, 9.6, 9.0, 'Criterio de evaluación',
     [{'s': 'CardBody', 'r': [('CE [n]: [enunciado literal del criterio del certificado].', None)]},
      {'s': 'Small', 'r': [('Indicador observable: [qué se ve en el aula o en la entrega].', None)]}], 'PillMagenta')
s.footer('MF1442_3 · Plantilla demo', '4')

# ---------- 5 · PERFIL ----------
s = Slide(d, 'Perfil')
head(s, '03 · DESTINATARIOS', 'Perfil del alumnado y punto de partida',
     'Quién aprende, con qué nivel llega y qué necesita para seguir la acción formativa.')
s.rect('CardW', 2.0, 6.3, 15.2, 9.2)
s.text(2.5, 6.6, 14.2, 8.6, [
    {'s': 'H2', 'r': [('Lo que hay que describir', None)]},
    {'t': 'ul', 'items': [
        {'s': 'BodyS', 'r': [('Nivel académico y experiencia previa del grupo.', None)]},
        {'s': 'BodyS', 'r': [('Competencia digital y acceso a equipos.', None)]},
        {'s': 'BodyS', 'r': [('Situación laboral y expectativas.', None)]},
        {'s': 'BodyS', 'r': [('Necesidades de accesibilidad o conciliación.', None)]},
        {'s': 'BodyS', 'r': [('Conocimientos previos detectados en la prueba inicial.', None)]},
    ]},
])
s.grid(18.4, 6.3, [5.0, 9.4], [
    [('Dato', 'CellHeadText'), ('Valor', 'CellHeadText')],
    [('Colectivo', 'CellSm'), ('[Desempleados / ocupados / mixto]', 'CellSm')],
    [('Nº de alumnos', 'CellSm'), ('[15]', 'CellSm')],
    [('Modalidad', 'CellSm'), ('[Presencial en aula]', 'CellSm')],
    [('Horario', 'CellSm'), ('[Lunes a viernes, 9:00–15:00]', 'CellSm')],
    [('Nivel de partida', 'CellSm'), ('[Medio: usan ofimática, no programan]', 'CellSm')],
], row_h=1.5, head_h=1.05, name='perfil')
s.footer('MF1442_3 · Plantilla demo', '5')

# ---------- 6 · CONTENIDOS ----------
s = Slide(d, 'Contenidos')
head(s, '04 · CONTENIDOS', 'Las cuatro unidades del temario',
     'Cada unidad se mide con una actividad y una evidencia.')
card(s, 2.0, 6.3, 14.3, 4.6, 'U1 · Estructura de la formación profesional',
     [{'s': 'CardBody', 'r': [('[Sistema de FP y normativa; tipos de acciones formativas; entidades y requisitos previos de espacios y equipamiento.]', None)]}])
card(s, 17.5, 6.3, 14.3, 4.6, 'U2 · Certificados de profesionalidad',
     [{'s': 'CardBody', 'r': [('[Grados A, B y C; módulos, UF y UC; criterios de evaluación; acreditación de competencias e itinerarios.]', None)]}], 'PillTeal')
card(s, 2.0, 11.2, 14.3, 4.6, 'U3 · Programación didáctica',
     [{'s': 'CardBody', 'r': [('[Contexto y perfil; objetivos operativos; contenidos; metodología, actividades y unidades didácticas.]', None)]}], 'PillMagenta')
card(s, 17.5, 11.2, 14.3, 4.6, 'U4 · Programación temporalizada',
     [{'s': 'CardBody', 'r': [('[Cronograma y guion minuteado; evaluación diagnóstica, formativa y sumativa; coordinación y mejora.]', None)]}], 'PillAmber')
s.footer('MF1442_3 · Plantilla demo', '6')

# ---------- 7 · METODOLOGÍA ----------
s = Slide(d, 'Metodologia')
head(s, '05 · METODOLOGÍA', 'Cómo se enseña y cómo se agrupa el aula',
     'Declara el enfoque y luego demuéstralo con la secuencia de actividades.')
s.text(2.0, 6.2, 14.5, 9.4, [
    {'s': 'H2', 'r': [('Principios', None)]},
    {'t': 'ul', 'items': [
        {'s': 'BodyS', 'r': [('Aprendizaje basado en la práctica y en casos reales.', None)]},
        {'s': 'BodyS', 'r': [('Alineación constructiva: objetivo → actividad → evidencia.', None)]},
        {'s': 'BodyS', 'r': [('Atención a la diversidad (DUA): varias formas de acceso y de expresión.', None)]},
        {'s': 'BodyS', 'r': [('Feedback frecuente y evaluación formativa.', None)]},
    ]},
])
s.grid(17.4, 6.3, [4.6, 7.4, 4.7, 2.6], [
    [('Momento', 'CellSmHead'), ('Técnica', 'CellSmHead'), ('Agrupamiento', 'CellSmHead'), ('Tiempo', 'CellSmHead')],
    [('Inicio', 'CellSm'), ('[Pregunta inicial y mapa]', 'CellSm'), ('Grupo completo', 'CellSm'), ('15 min', 'CellSm')],
    [('Desarrollo', 'CellSm'), ('[Taller guiado]', 'CellSm'), ('Parejas', 'CellSm'), ('60 min', 'CellSm')],
    [('Cierre', 'CellSm'), ('[Puesta en común]', 'CellSm'), ('Grupo completo', 'CellSm'), ('15 min', 'CellSm')],
], row_h=1.5, head_h=1.05, name='met')
s.footer('MF1442_3 · Plantilla demo', '7')

# ---------- 8 · TEMPORALIZACIÓN ----------
s = Slide(d, 'Temporalizacion')
head(s, '06 · TEMPORALIZACIÓN', 'Nueve sesiones, del 24/11 al 04/12 de 2026',
     'Cambia las fechas si el centro mueve el calendario: están en el README del repositorio.')
rows = [[('Sesión', 'CellHeadText'), ('Contenido de la sesión', 'CellHeadText'), ('Evidencia que se entrega', 'CellHeadText')]]
plan = [
    ('1 · 24/11', 'U1 · Estructura de la formación profesional', 'Ficha del grupo'),
    ('2 · 25/11', 'U1 · Tipos de acciones formativas y requisitos', 'Análisis de normativa'),
    ('3 · 26/11', 'U2 · Certificados: módulos, UF y UC', 'Mapa del certificado'),
    ('4 · 27/11', 'U2 · Criterios de evaluación y acreditación', 'Tabla de objetivos y CE'),
    ('5 · 30/11', 'U3 · Contexto y perfil del alumnado', 'Ficha del perfil'),
    ('6 · 01/12', 'U3 · Objetivos y contenidos', 'Programación (borrador)'),
    ('7 · 02/12', 'U3 · Metodología, actividades y UD', 'Tabla de secuenciación'),
    ('8 · 03/12', 'U4 · Temporalización y guion minuteado', 'Cronograma y guion'),
    ('9 · 04/12', 'U4 · Evaluación, rúbrica y cierre', 'Rúbrica y programación final'),
]
for a, b, c in plan:
    rows.append([(a, 'CellTextB'), (b, 'CellSm'), (c, 'CellSm')])
s.grid(2.0, 6.2, [3.6, 14.4, 11.3], rows, row_h=1.03, name='temp')
s.footer('MF1442_3 · Plantilla demo', '8')

# ---------- 9 · RECURSOS ----------
s = Slide(d, 'Recursos')
head(s, '07 · RECURSOS', 'Qué necesitas tener preparado',
     'Recursos del aula y recursos digitales; y un plan B para cada uno.')
card(s, 2.0, 6.3, 14.3, 6.4, 'Aula',
     [{'t': 'ul', 'items': [
         {'s': 'CardBody', 'r': [('[Aula con proyector y pizarra.]', None)]},
         {'s': 'CardBody', 'r': [('[Ordenadores: uno por pareja.]', None)]},
         {'s': 'CardBody', 'r': [('[Plantillas impresas de la programación.]', None)]},
         {'s': 'CardBody', 'r': [('[Copia en papel de los criterios de evaluación.]', None)]},
     ]}])
card(s, 17.5, 6.3, 14.3, 6.4, 'Digital',
     [{'t': 'ul', 'items': [
         {'s': 'CardBody', 'r': [('[Carpeta compartida del curso.]', None)]},
         {'s': 'CardBody', 'r': [('[Plantilla de programación en .docx y .pptx.]', None)]},
         {'s': 'CardBody', 'r': [('[Formulario de autoevaluación.]', None)]},
         {'s': 'CardBody', 'r': [('[Vídeos y ejemplos descargados, no en streaming.]', None)]},
     ]}], 'PillTeal')
s.rect('CardBg', 2.0, 13.2, 29.8, 3.4)
s.text(2.4, 13.5, 29.0, 2.9, [{'s': 'Small', 'r': [('Plan B: ', 'AccentSpan'), ('si falla el proyector o internet, la sesión sigue con la guía impresa y la pizarra. Ese plan también se escribe en la programación: no se improvisa.', None)]}])
s.footer('MF1442_3 · Plantilla demo', '9')

# ---------- 10 · EVALUACIÓN ----------
s = Slide(d, 'Evaluacion')
head(s, '08 · EVALUACIÓN', 'Tres momentos y un instrumento por momento',
     'Si no hay instrumento, no hay evidencia; y sin evidencia no hay nota.')
s.grid(2.0, 6.3, [5.0, 7.4, 12.0, 4.9], [
    [('Tipo', 'CellSmHead'), ('Momento', 'CellSmHead'), ('Instrumento y criterio', 'CellSmHead'), ('Peso', 'CellSmHead')],
    [('Diagnóstica', 'CellTextB'), ('Sesión 1', 'CellSm'), ('[Cuestionario de ideas previas + ficha del grupo]', 'CellSm'), ('0 %', 'CellSm')],
    [('Formativa', 'CellTextB'), ('Sesiones 2–8', 'CellSm'), ('[Observación con lista de cotejo y entregas parciales]', 'CellSm'), ('40 %', 'CellSm')],
    [('Sumativa', 'CellTextB'), ('Sesión 9', 'CellSm'), ('[Programación didáctica + defensa con rúbrica]', 'CellSm'), ('60 %', 'CellSm')],
], row_h=1.75, head_h=1.05, name='eval')
s.text(2.0, 14.6, 29.5, 1.6, [{'s': 'Small', 'r': [('Recuerda: ', 'AccentSpan'), ('cada criterio de evaluación debe aparecer en la rúbrica con un descriptor observable. Nada de «participa bien».', None)]}])
s.footer('MF1442_3 · Plantilla demo', '10')

# ---------- 11 · RÚBRICA ----------
s = Slide(d, 'Rubrica')
head(s, '09 · RÚBRICA', 'Cuatro niveles por criterio',
     'Sustituye los descriptores por lo que se ve en la entrega, no por adjetivos.')
s.grid(2.0, 6.2, [6.2, 7.6, 7.6, 8.4], [
    [('Criterio', 'CellSmHead'), ('Insuficiente (0–4)', 'CellSmHead'), ('Suficiente (5–6)', 'CellSmHead'), ('Notable / Excelente (7–10)', 'CellSmHead')],
    [('Contexto y necesidades', 'CellTextB'), ('[No identifica el grupo]', 'CellSm'), ('[Describe el grupo]', 'CellSm'), ('[Analiza y justifica decisiones]', 'CellSm')],
    [('Objetivos y CE', 'CellTextB'), ('[Genéricos]', 'CellSm'), ('[Claros y medibles]', 'CellSm'), ('[Alineados y verificables]', 'CellSm')],
    [('Contenidos', 'CellTextB'), ('[Lista sin secuencia]', 'CellSm'), ('[Secuencia lógica]', 'CellSm'), ('[Secuencia con tiempos y UD]', 'CellSm')],
    [('Evaluación', 'CellTextB'), ('[Solo prueba final]', 'CellSm'), ('[Instrumentos básicos]', 'CellSm'), ('[Rúbrica completa y coherente]', 'CellSm')],
], row_h=1.95, head_h=1.05, name='rub')
s.footer('MF1442_3 · Plantilla demo', '11')

# ---------- 12 · ALINEACIÓN ----------
s = Slide(d, 'Alineacion')
head(s, '10 · ALINEACIÓN CONSTRUCTIVA', 'Objetivo → actividad → evidencia',
     'La prueba de que la programación no es una lista: todo apunta al mismo criterio.')
s.grid(2.0, 6.3, [8.6, 10.4, 10.3], [
    [('Objetivo', 'CellSmHead'), ('Actividad', 'CellSmHead'), ('Evidencia y criterio', 'CellSmHead')],
    [('[OG1 · Analizar el contexto]', 'CellTextB'), ('[Estudio de caso + debate guiado]', 'CellSm'), ('[Ficha del grupo · CE1]', 'CellSm')],
    [('[OE2 · Secuenciar contenidos]', 'CellTextB'), ('[Taller de unidades didácticas]', 'CellSm'), ('[Tabla de secuenciación · CE2]', 'CellSm')],
    [('[OE3 · Diseñar la evaluación]', 'CellTextB'), ('[Prueba práctica + rúbrica]', 'CellSm'), ('[Rúbrica aplicada · CE3]', 'CellSm')],
], row_h=1.75, head_h=1.05, name='alin')
s.footer('MF1442_3 · Plantilla demo', '12')

# ---------- 13 · RIESGOS ----------
s = Slide(d, 'Riesgos')
head(s, '11 · RIESGOS Y PLAN B', 'Qué puede salir mal y qué harás entonces',
     'Anticipar los problemas es parte de la competencia docente.')
card(s, 2.0, 6.3, 14.3, 4.4, 'En el aula',
     [{'t': 'ul', 'items': [
         {'s': 'CardBody', 'r': [('[Falta de tiempo: recorto una actividad, no la evaluación.]', None)]},
         {'s': 'CardBody', 'r': [('[Grupo muy heterogéneo: itinerario B y apoyo entre iguales.]', None)]},
     ]}], 'PillAmber')
card(s, 17.5, 6.3, 14.3, 4.4, 'Técnicos',
     [{'t': 'ul', 'items': [
         {'s': 'CardBody', 'r': [('[Sin proyector: guía impresa y pizarra.]', None)]},
         {'s': 'CardBody', 'r': [('[Sin internet: materiales descargados y actividad alternativa.]', None)]},
     ]}], 'PillAmber')
s.rect('CardBg', 2.0, 11.2, 29.8, 4.4)
s.text(2.4, 11.5, 29.0, 3.8, [
    {'s': 'H2', 'r': [('Cómo se escribe en la programación', None)]},
    {'s': 'Small', 'r': [('Cada riesgo lleva su medida: una línea con el problema, otra con la respuesta y quién la ejecuta. Así el plan B se evalúa como cualquier otro contenido.', None)]},
])
s.footer('MF1442_3 · Plantilla demo', '13')

# ---------- 14 · CIERRE ----------
s = Slide(d, 'Cierre')
head(s, '12 · CIERRE', 'Qué entregas y cómo lo compruebas',
     'La diapositiva final sirve para que nadie se vaya sin saber qué falta.')
s.text(2.0, 6.2, 15.4, 9.8, [
    {'s': 'H2', 'r': [('Entregables del módulo', None)]},
    {'t': 'ul', 'items': [
        {'s': 'BodyS', 'r': [('☐ Normativa aplicable analizada', None)]},
        {'s': 'BodyS', 'r': [('☐ Ficha del perfil del alumnado', None)]},
        {'s': 'BodyS', 'r': [('☐ Programación didáctica completa', None)]},
        {'s': 'BodyS', 'r': [('☐ Tabla de secuenciación de UD', None)]},
        {'s': 'BodyS', 'r': [('☐ Cronograma y guion minuteado', None)]},
        {'s': 'BodyS', 'r': [('☐ Instrumentos de evaluación y rúbrica', None)]},
    ]},
])
card(s, 18.2, 6.3, 13.6, 9.0, 'Antes de entregar',
     [{'t': 'ul', 'items': [
         {'s': 'CardBody', 'r': [('Nombre y fecha en la portada.', None)]},
         {'s': 'CardBody', 'r': [('PDF con el mismo nombre que el archivo editable.', None)]},
         {'s': 'CardBody', 'r': [('Copia en la carpeta MF1442_3/ del repositorio.', None)]},
         {'s': 'CardBody', 'r': [('Revisa que no queda ningún [corchete].', None)]},
     ]}], 'PillMagenta')
s.footer('MF1442_3 · Plantilla demo · Aj Fonts', '14')

d.save('presentacion_demo_MF1442_3.fodp')
print('slides:', Slide.n)
