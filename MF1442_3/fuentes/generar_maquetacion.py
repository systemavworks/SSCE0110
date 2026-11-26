import sys
import os
import re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from docgen import Doc, INK, GREY, INDIGO, TEAL, CARDBG, PH

HTML_FICHA = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'modulo_MF1442_3.html')


def cargar_autoevaluaciones(ruta):
    """Extrae las autoevaluaciones de la ficha HTML: una sola fuente de verdad."""
    html = open(ruta, encoding='utf-8').read()
    bloque = re.search(r'const autoevaluaciones = \{(.*?)\n  \};', html, re.S).group(1)
    datos = {}
    for ud in ('ud1', 'ud2', 'ud3', 'ud4'):
        m = re.search(r'%s: \[(.*?)\n    \]' % ud, bloque, re.S)
        preguntas = []
        for bm in re.finditer(r'q: "(.*?)",\s*opts: \[(.*?)\],\s*correct: (\d+),\s*exp: "(.*?)"',
                              m.group(1), re.S):
            preguntas.append({
                'q': bm.group(1),
                'opts': re.findall(r'"([^"]*)"', bm.group(2)),
                'correct': int(bm.group(3)),
                'exp': bm.group(4),
            })
        datos[ud] = preguntas
    return datos


AUTOS = cargar_autoevaluaciones(HTML_FICHA)
assert all(len(AUTOS[ud]) == 10 for ud in AUTOS), 'Cada unidad debe tener 10 preguntas'

d = Doc()
d.setup()
d.para('Kicker', 8.5, TEAL, bold=True, after=0.35)
d.para('H1', 19, INK, bold=True, after=0.2, line=118)
d.para('H2', 12.5, INDIGO, bold=True, before=0.75, after=0.25,
       border_bottom='0.05cm solid #3B34C7')
d.para('Sub', 10.5, GREY, after=0.35)
d.para('Body', 10.5, INK, after=0.18, line=145)
d.para('Small', 8.5, GREY, after=0.2, line=130)
d.para('SmallGap', 8.5, GREY, before=0.25, after=0.2, line=130)
d.para('MiniHead', 10.5, INDIGO, bold=True, before=0.4, after=0.15)
d.para('Note', 9, '#4A4860', after=0.5, line=135, bg=CARDBG,
       border_left='0.12cm solid #3B34C7')
d.para('TableHeadP', 8.5, '#FFFFFF', bold=True, after=0, line=115)
d.para('TableCellP', 9, INK, after=0, line=120)
d.para('PB', 10.5, INK, after=0, brk=True)
d.tstyle('PhSpan', None, PH)
d.cellstyle('Cell', '#FFFFFF')
d.cellstyle('CellHead', '#16152B', border='0.02cm solid #16152B')

W = 17.0  # ancho útil

d.p('SSCE0110 · MF1442_3 · PLANTILLA DE MAQUETACIÓN', 'Kicker')
d.h1('Programación didáctica de una acción formativa para el empleo')
d.p('Documento para rellenar · 60 h · 9 sesiones · 24/11/2026 → 04/12/2026 · CEFI Formación (Almonte)', 'Sub')
d.p('Autor/a: [nombre y apellidos] · Curso: SSCE0110 · Docencia de la Formación Profesional para el Empleo · Módulo: MF1442_3 (UC1442_3)', 'Body')
d.p('Versión: [v1] · Fecha: [dd/mm/aaaa] · Entrega: [nombre del archivo.pdf]', 'Body')
d.p('Todo lo que aparece entre [corchetes] es un hueco: borra el corchete cuando escribas. Si queda uno, se nota.', 'Small')

d.h2('0 · Cómo usar esta plantilla')
d.p('Cinco reglas. (1) No borres los títulos numerados: son los apartados que se evalúan. (2) Sustituye todos los corchetes. (3) Escribe en primera persona y en presente. (4) Cada afirmación debe poder demostrarse con una evidencia del aula o de la entrega. (5) Exporta a PDF con el mismo nombre que el archivo editable.', 'Note')
d.bullets([
    'Extensión orientativa: 10–16 páginas sin anexos. Si te pasas de 20, recorta antes la teoría que las tablas.',
    'Formato: A4, márgenes de 2 cm, cuerpo 10,5 pt, interlineado 1,45. Títulos en el orden de esta plantilla.',
    'Nomenclatura del archivo: MF1442_3_programacion_apellido.pdf',
])

d.h2('1 · Datos de la acción formativa')
d.table([
    ['Dato', 'Contenido'],
    ['Denominación de la acción', '[Programación didáctica de acciones formativas para el empleo]'],
    ['Certificado de profesionalidad', 'SSCE0110 · Docencia de la formación profesional para el empleo (nivel 3)'],
    ['Módulo formativo / UC', 'MF1442_3 · UC1442_3 · [60 h]'],
    ['Familia profesional', 'Servicios Socioculturales y a la Comunidad'],
    ['Centro / entidad', 'CEFI Formación S.L. · Pol. Ind. Los Taranjales II, 58 · Almonte (Huelva)'],
    ['Modalidad y horario', '[Presencial] · [Lunes a viernes, 9:00–15:00]'],
    ['Fechas', 'Del [24/11/2026] al [04/12/2026] · 9 sesiones'],
    ['Destinatarios', '[Colectivo, nº de alumnos, requisitos de acceso]'],
    ['Formador/a y tutor/a', '[Nombre] · [Correo y teléfono de contacto]'],
], [5.4, 11.6])

d.pagebreak()
d.h2('2 · Justificación y contexto')
d.p('Explica en tres párrafos cortos por qué esta acción formativa tiene sentido para este grupo y este centro.', 'Body')
d.table([
    ['Aspecto', 'Qué escribir'],
    ['Necesidad detectada', '[Necesidad formativa del sector, del centro o de la empresa; fuente del dato]'],
    ['Contexto del centro', '[Recursos, ubicación, experiencia, concertación con empresas]'],
    ['Perfil del alumnado', '[Nivel académico, experiencia, competencia digital, accesibilidad]'],
    ['Normativa aplicable', 'LO 5/2002 · RD 34/2008 (modificado por RD 189/2011) · RD 1697/2011, Anexo IV, actualizado por RD 625/2013 · Orden ESS/1897/2013 · LO 3/2022 y RD 659/2023'],
    ['Resultado esperado', '[Qué podrá hacer el alumnado al terminar, en una frase medible]'],
], [5.0, 12.0])

d.h2('3 · Objetivos y criterios de evaluación')
d.p('Cada objetivo se apoya en un criterio de evaluación del certificado y en un indicador que se pueda ver.', 'Body')
d.table([
    ['Tipo', 'Objetivo', 'Criterio de evaluación', 'Indicador observable'],
    ['General', '[Elaborar la programación didáctica de una acción formativa, integrando objetivos, contenidos, metodología, recursos y evaluación]', '[CE n del certificado]', '[Entrega completa y coherente]'],
    ['Específico 1', '[Analizar el contexto y detectar necesidades formativas]', '[CE n]', '[Ficha del grupo con datos y conclusiones]'],
    ['Específico 2', '[Secuenciar los contenidos en unidades didácticas]', '[CE n]', '[Tabla de secuenciación con tiempos]'],
    ['Específico 3', '[Diseñar actividades y su evaluación]', '[CE n]', '[Rúbrica aplicada a una actividad]'],
], [2.4, 6.0, 4.0, 4.6])

d.pagebreak()
d.h2('4 · Contenidos y unidades didácticas')
d.table([
    ['Unidad', 'Título', 'Contenidos', 'Horas', 'Ses.'],
    ['U1', 'Estructura de la formación profesional', 'Sistema Nacional de Cualificaciones (CNCP, formación modular y niveles); FP reglada (FP Básica y ciclos); FPE (modalidades, destinatarios, demanda y oferta); programas y proyectos formativos', '12', '2'],
    ['U2', 'Certificados de profesionalidad', 'Definición y vías de adquisición; estructura (perfil profesional y referente formativo, prescripciones de formadores, espacios y equipamientos); presencial y en línea', '14', '2'],
    ['U3', 'Elaboración de la programación didáctica', 'Función, aspectos claves y ventajas; formación por competencias; objetivos; contenidos; secuenciación; actividades; metodología; recursos; criterios de evaluación y ponderaciones', '20', '3'],
    ['U4', 'Elaboración de la programación temporalizada', 'Temporalización diaria; secuenciación de contenidos y actividades; guía del alumno para la modalidad en línea', '14', '2'],
    ['Total', '', '', '60', '9'],
], [1.4, 5.2, 8.0, 1.2, 1.2])
d.p('Horas orientativas: el certificado solo fija las 60 h del módulo; el reparto 12/14/20/14 y las 9 sesiones son la propuesta del centro.', 'Note')
d.pagebreak()
d.h2('4.1 · Reparto de los 22 apartados del manual')
d.p('Cada apartado del manual cae en una sesión concreta. La numeración es la del índice del libro (pp. 19–147).', 'Body')
d.table([
    ['UD', 'Apartados', 'Qué se trabaja', 'Sesiones'],
    ['U1', '1.1–1.5', '1.1 Sistema Nacional de Cualificaciones · 1.2 FP reglada (PCPI y ciclos) · 1.3 FPE (demanda y oferta) · 1.4 programas formativos · 1.5 proyectos en alternancia', 'S1 (1.1–1.3) · S2 (1.4–1.5)'],
    ['U2', '2.1–2.2', '2.1 certificado: características, vías, perfil y referente formativo, prescripciones y espacios · 2.2 programación vinculada a la certificación', 'S3 (2.1) · S4 (2.2)'],
    ['U3', '3.1–3.12', '3.1 función y ventajas · 3.2 competencias · 3.3 características · 3.4 objetivos · 3.5 contenidos · 3.6 secuenciación · 3.7 actividades · 3.8 metodología (3.8.1 y 3.8.2) · 3.9 modalidades · 3.10 recursos · 3.11 evaluación · 3.12 mejora', 'S5 (3.1–3.4) · S6 (3.5–3.7) · S7 (3.8–3.12)'],
    ['U4', '4.1–4.3', '4.1 temporalización diaria (4.1.1 estructura) · 4.2 secuenciación y actividades · 4.3 guía del alumno en línea', 'S8 (4.1–4.2) · S9 (4.3 y cierre)'],
], [1.2, 2.0, 10.6, 3.2])
d.p('Cada unidad del manual cierra con introducción, resumen de la unidad y autoevaluación: son el mejor repaso antes de cada entrega.', 'Note')

d.h2('4.2 · Ideas clave de las cuatro unidades')
d.p('Estas ocho ideas son las que más se preguntan y las que más se olvidan al redactar. Van antes que el detalle: si no están claras, el resto del documento se cae.', 'Body')
d.bullets([
    'Formación ≠ educación: la formación es práctica, a corto plazo y orientada a resolver problemas del puesto; la educación busca valores y desarrollo a largo plazo.',
    'LO 3/2022, doble escala: cinco grados ascendentes de oferta (A, B, C, D y E) y tres niveles de competencia (1, 2 y 3), medidos por conocimientos, iniciativa, autonomía y complejidad.',
    'FP reglada: PCPI (mayores de 16 sin ESO, nivel 1; hoy FP Básica), Grado Medio (Técnico, nivel 2) y Grado Superior (Técnico Superior, nivel 3).',
    'FPE de demanda: la empresa la organiza, la bonifica en la Seguridad Social y el trabajador puede usar el Permiso Individual de Formación (PIF). FPE de oferta: la programan las comunidades autónomas como política activa de empleo.',
    'Certificado de profesionalidad: acredita una cualificación con validez en todo el territorio nacional. Se estructura en perfil profesional, formación (módulos y prácticas no laborales) y prescripciones (formadores, espacios y equipamiento).',
    'Cadena de concreción: UC → RA → CE. Cada unidad de competencia se desglosa en resultados de aprendizaje y cada resultado, en criterios de evaluación.',
    'Contenidos: conceptuales (saber), procedimentales (saber hacer) y actitudinales (saber ser y estar).',
    'Evaluación: criterios + tipo (inicial, continua y final) + instrumento (rúbrica, prueba, observación) + ponderación; y un apartado de revisión y mejora.',
])

d.p('Los tres catálogos: de la competencia del puesto a tu programación', 'Body')
d.table([
    ['Catálogo', 'Qué ordena', 'Qué aporta a tu programación'],
    ['Estándares de Competencias Profesionales', 'Las competencias que exige el sistema productivo, por familia y nivel.', 'El referente de lo que el alumnado debe saber hacer.'],
    ['Modular de Formación Profesional', 'Los módulos formativos asociados a cada estándar de competencia.', 'La base del módulo: duración, capacidades y criterios.'],
    ['Ofertas de Formación Profesional', 'Todas las ofertas reconocidas y acreditables del sistema.', 'Dónde encaja tu acción: certificado, curso o acreditación parcial.'],
], [5.4, 6.0, 5.6])
d.p('El manual conserva la redacción de 2011 (CNCP y catálogo modular); la LO 3/2022 renombra los catálogos y añade el de Ofertas. Cita la norma vigente y, si el tribunal pide el manual, explica la equivalencia.', 'Note')

d.p('Tres escalas que no hay que confundir', 'Body')
d.table([
    ['Escala', 'Cuántos', 'Qué mide', 'Dónde se usa'],
    ['Niveles del CNCP', '5 (1–5)', 'Complejidad de la cualificación profesional', 'Clasificar cualificaciones y certificados'],
    ['Niveles de competencia (LO 3/2022)', '3 (1–3)', 'Conocimientos, iniciativa, autonomía y complejidad', 'Situar cada oferta y su acceso'],
    ['Grados de oferta (LO 3/2022)', '5 (A–E)', 'Tipo de oferta: de la acreditación parcial al curso de especialización', 'Saber qué se obtiene al terminar'],
], [5.6, 2.4, 5.6, 3.4])
d.p('El SSCE0110 es de nivel 3 del CNCP y se corresponde con el grado C (certificado profesional) de la LO 3/2022.', 'SmallGap')

d.p('Si la acción es en línea, la guía del alumno (apartado 4.3) debe detallar como mínimo:', 'Body')
d.table([
    ['Elemento', 'Qué debe quedar escrito'],
    ['Plataforma', 'Nombre, acceso, navegación y requisitos técnicos.'],
    ['Tiempos de respuesta', 'Plazo máximo del tutor en foros y mensajes.'],
    ['Foros', 'Cuáles hay, para qué sirven y normas de participación.'],
    ['Síncrono y asíncrono', 'Sesiones en directo, grabaciones y actividades a ritmo del alumno.'],
    ['Soporte técnico', 'Canal, horario y responsable de las incidencias.'],
], [4.6, 12.4])

d.pagebreak()
d.h2('4.3 · Autoevaluaciones de las cuatro unidades')
d.p('El manual cierra cada unidad con una autoevaluación. Aquí tienes las cuarenta preguntas con su clave comentada: contesta sin mirar y comprueba después. La versión interactiva (corrige al instante y explica el porqué) está en la ficha del módulo, dentro del temario.', 'Body')
d.p('Criterio de uso: menos de tres fallos, adelante; entre tres y cinco, repasa las ideas clave de la unidad; más de cinco, vuelve al apartado del manual antes de seguir.', 'Note')

UDS = [
    ('ud1', 'UD 1 · Estructura de la Formación Profesional'),
    ('ud2', 'UD 2 · Certificados de profesionalidad'),
    ('ud3', 'UD 3 · Elaboración de la programación didáctica'),
    ('ud4', 'UD 4 · Programación temporalizada y guía en línea'),
]
LETRAS = 'abcdef'
for ud, titulo in UDS:
    d.p(titulo, 'MiniHead')
    filas = [['Nº', 'Pregunta y opciones', 'Clave y porqué']]
    for i, q in enumerate(AUTOS[ud], 1):
        opciones = '\n'.join('%s) %s' % (LETRAS[j], o) for j, o in enumerate(q['opts']))
        filas.append([str(i), '%s\n%s' % (q['q'], opciones),
                      '%s) %s' % (LETRAS[q['correct']], q['exp'])])
    d.table(filas, [0.8, 8.4, 7.8])
d.p('Las preguntas 1 a 7 de la UD 1 y las que citan porcentajes remiten a la LO 3/2022 y al RD 659/2023: si el manual que estudias conserva la redacción de 2011, comprueba la cifra con la norma vigente antes de llevarla a tu programación.', 'Small')

d.h2('5 · Metodología')
d.bullets([
    'Enfoque: [aprendizaje basado en la práctica y en casos reales del sector].',
    'Alineación constructiva: cada objetivo tiene una actividad y una evidencia; cada evidencia se corrige con un criterio declarado.',
    'Atención a la diversidad (DUA): [varias formas de acceso al contenido y de expresión del aprendizaje].',
    'Feedback: [cuándo y cómo se devuelve, en grupo y por escrito].',
])
d.table([
    ['Momento', 'Técnica', 'Agrupamiento', 'Tiempo', 'Recurso'],
    ['Inicio', '[Pregunta inicial y mapa de ideas]', 'Grupo completo', '15 min', '[Pizarra y plantilla]'],
    ['Desarrollo', '[Taller guiado con caso]', 'Parejas', '60 min', '[Ordenador y guía]'],
    ['Cierre', '[Puesta en común y checklist]', 'Grupo completo', '15 min', '[Proyector]'],
], [2.6, 5.4, 3.4, 1.8, 3.8])

d.pagebreak()
d.h2('6 · Temporalización')
d.p('Nueve sesiones entre el 24/11/2026 y el 04/12/2026: 60 h en total, es decir 6 h 40 min por sesión (o 6 h diarias más 6 h de trabajo tutorizado si el centro fija jornada de 6 h). Si el centro mueve una fecha, actualízala aquí y en el portfolio del repositorio.', 'Body')
d.table([
    ['Sesión', 'Fecha', 'Contenido (apartados del manual)', 'Actividad y evidencia'],
    ['1', '24/11/2026', '1.1–1.3 · Sistema Nacional de Cualificaciones; FP reglada; FPE (demanda y oferta)', 'Ficha del grupo y mapa del sistema de FP'],
    ['2', '25/11/2026', '1.4–1.5 · Programas formativos y proyectos en alternancia (repaso UD 1)', 'Análisis de un programa formativo real'],
    ['3', '26/11/2026', '2.1 · Certificado: características, vías y estructura (perfil, referente formativo, formadores, espacios)', 'Mapa del certificado SSCE0110'],
    ['4', '27/11/2026', '2.2 · Programación vinculada a la certificación (repaso UD 2)', 'Tabla apartados ↔ criterios del módulo'],
    ['5', '30/11/2026', '3.1–3.4 · Función y ventajas; competencias; características; objetivos', 'Tres objetivos observables'],
    ['6', '01/12/2026', '3.5–3.7 · Contenidos; secuenciación; actividades', 'Tabla de contenidos y secuencia'],
    ['7', '02/12/2026', '3.8–3.12 · Metodología; modalidades; recursos; evaluación y mejora', 'Rúbrica y criterios ponderados'],
    ['8', '03/12/2026', '4.1–4.2 · Temporalización diaria; secuenciación de actividades', 'Cronograma y guion minuteado'],
    ['9', '04/12/2026', '4.3 · Guía del alumno en línea, repaso y entrega', 'Guía del alumno y programación final'],
], [1.8, 2.6, 7.4, 5.2])
d.p('Los días 7 y 8 de diciembre, 24 y 25 de diciembre, 31 de diciembre y 1, 5 y 6 de enero son no lectivos en el cronograma del centro, fuera ya de esta ventana.', 'Small')

d.pagebreak()
d.h2('7 · Recursos y materiales')
d.table([
    ['Recurso', 'Tipo', 'Uso didáctico', 'Ubicación'],
    ['[Guía de la programación]', 'Documento', '[Soporte de trabajo de las sesiones 1–9]', '[Carpeta compartida]'],
    ['[Plantilla de programación]', 'Plantilla', '[Producto que se rellena en clase]', '[Aula virtual]'],
    ['[Ordenadores y proyector]', 'Equipamiento', '[Búsqueda de normativa y puestas en común]', '[Aula 2]'],
    ['[Ejemplos reales de programaciones]', 'Material', '[Análisis crítico y comparación]', '[Carpeta del curso]'],
], [5.2, 2.8, 6.0, 3.0])

d.h2('8 · Evaluación')
d.table([
    ['Tipo', 'Momento', 'Instrumento', 'Criterio que mide', 'Peso'],
    ['Diagnóstica', 'Sesión 1', '[Cuestionario de ideas previas + ficha del grupo]', '[CE n]', '0 %'],
    ['Formativa', 'Sesiones 2–8', '[Observación con lista de cotejo y entregas parciales]', '[CE n]', '40 %'],
    ['Sumativa', 'Sesión 9', '[Programación didáctica + defensa con rúbrica]', '[CE n]', '60 %'],
], [2.6, 3.0, 6.6, 3.2, 1.6])
d.p('Regla de oro: si un criterio no aparece en la rúbrica con un descriptor observable, no se puede calificar. Nada de «participa bien» o «trabaja en equipo» sin indicador.', 'Note')

d.h2('9 · Rúbrica de la actividad práctica')
d.table([
    ['Criterio', 'Insuficiente (0–4)', 'Suficiente (5–6)', 'Notable (7–8)', 'Excelente (9–10)'],
    ['Contexto y necesidades', '[No identifica el grupo]', '[Describe el grupo]', '[Analiza y justifica]', '[Ajusta la propuesta al grupo]'],
    ['Objetivos y CE', '[Genéricos]', '[Claros y medibles]', '[Alineados con actividades]', '[Verificables con evidencia]'],
    ['Contenidos', '[Lista sin secuencia]', '[Secuencia lógica]', '[Secuencia con tiempos]', '[UD completa y flexible]'],
    ['Metodología', '[Solo clase magistral]', '[Alguna técnica activa]', '[Técnicas variadas]', '[Justifica la elección]'],
    ['Evaluación', '[Solo prueba final]', '[Instrumentos básicos]', '[Diagnóstica, formativa y sumativa]', '[Rúbrica completa y coherente]'],
], [4.0, 3.2, 3.2, 3.3, 3.3])

d.h2('10 · Alineación constructiva')
d.table([
    ['Objetivo', 'Actividad', 'Evidencia', 'Criterio'],
    ['[OG1 · Analizar el contexto]', '[Estudio de caso + debate guiado]', '[Ficha del grupo]', '[CE1]'],
    ['[OE2 · Secuenciar contenidos]', '[Taller de unidades didácticas]', '[Tabla de secuenciación]', '[CE2]'],
    ['[OE3 · Diseñar la evaluación]', '[Prueba práctica + rúbrica]', '[Rúbrica aplicada]', '[CE3]'],
], [5.2, 5.4, 4.0, 2.4])

d.h2('11 · Seguimiento y tutorización')
d.bullets([
    'Canal: [aula, correo y aula virtual; horario de respuesta].',
    'Registro: [hoja de seguimiento con fecha, entrega, devolución y acuerdos].',
    'Alumnado con dificultades: [medida concreta y plazo].',
    'Evidencias: cada entrega se guarda en [carpeta del módulo] con la nomenclatura acordada.',
])

d.h2('12 · Riesgos y plan B')
d.table([
    ['Riesgo', 'Medida prevista', 'Responsable'],
    ['[Falta de tiempo]', '[Recortar una actividad, nunca la evaluación]', '[Formador/a]'],
    ['[Grupo muy heterogéneo]', '[Itinerario B y apoyo entre iguales]', '[Formador/a]'],
    ['[Fallo técnico o sin internet]', '[Guía impresa, materiales descargados y pizarra]', '[Formador/a]'],
], [5.0, 8.4, 3.6])

d.h2('13 · Bibliografía y anexos')
d.p('Cita en ISO 690 o APA 7. Incluye normativa, manuales y recursos digitales con fecha de consulta.', 'Small')
d.bullets([
    'Real Decreto 1697/2011, de 18 de noviembre (BOE 24/12/2011). Anexo IV · Docencia de la formación profesional para el empleo.',
    'Real Decreto 625/2013, de 2 de agosto (BOE 18/09/2013). Actualización del Anexo IV: prescripción de los formadores.',
    'Orden ESS/1897/2013, de 10 de octubre. Modelo de programación didáctica de los certificados de profesionalidad.',
    '[Ley Orgánica 3/2022 y Real Decreto 659/2023: ordenación del Sistema de Formación Profesional].',
    '[Bibliografía específica del módulo, con autor, año, título y editorial].',
])
d.p('Anexos: [Anexo I · Ficha del grupo] · [Anexo II · Cronograma] · [Anexo III · Rúbrica] · [Anexo IV · Instrumentos]', 'Body')

d.h2('14 · Checklist de entrega')
d.p('Marca cada casilla antes de exportar el PDF. Son los entregables que recoge la ficha del módulo en el portfolio.', 'Body')
d.table([
    ['✔', 'Entregable', 'Dónde está'],
    ['☐', 'Normativa aplicable analizada', '[archivo]'],
    ['☐', 'Ficha del perfil del alumnado', '[archivo]'],
    ['☐', 'Documento de coordinación del equipo docente', '[archivo]'],
    ['☐', 'Programación didáctica completa', '[archivo]'],
    ['☐', 'Tabla de secuenciación de unidades didácticas', '[archivo]'],
    ['☐', 'Listado detallado de materiales y recursos', '[archivo]'],
    ['☐', 'Temporalización (cronograma)', '[archivo]'],
    ['☐', 'Guion didáctico minuteado de una sesión', '[archivo]'],
    ['☐', 'Instrumentos de evaluación (diagnóstica, formativa, sumativa)', '[archivo]'],
    ['☐', 'Rúbrica de una actividad práctica', '[archivo]'],
    ['☐', 'Bibliografía y webgrafía normalizada', '[archivo]'],
    ['☐', 'Plan B para fallos técnicos o imprevistos', '[archivo]'],
    ['☐', 'Análisis de la estructura de un certificado real', '[archivo]'],
    ['☐', 'Tabla de niveles de cualificación y vías de adquisición', '[archivo]'],
    ['☐', 'Guía del alumno para la modalidad en línea', '[archivo]'],
], [1.0, 11.0, 5.0])
d.p('Plantilla de maquetación · MF1442_3 · SSCE0110 · CEFI Formación (Almonte) · v1.0 · 25/11/2026', 'Small')
d.p('Material de estudio propio del portfolio: no reproduce el manual comercial del curso y no sustituye la documentación oficial del centro.', 'Small')

d.save('maquetacion_MF1442_3.fodt')
print('ok')
