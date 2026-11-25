import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from docgen import Doc, INK, GREY, INDIGO, TEAL, CARDBG, PH

d = Doc()
d.setup()
d.para('Kicker', 8.5, TEAL, bold=True, after=0.35)
d.para('H1', 19, INK, bold=True, after=0.2, line=118)
d.para('H2', 12.5, INDIGO, bold=True, before=0.75, after=0.25,
       border_bottom='0.05cm solid #3B34C7')
d.para('Sub', 10.5, GREY, after=0.35)
d.para('Body', 10.5, INK, after=0.18, line=145)
d.para('Small', 8.5, GREY, after=0.2, line=130)
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

d.h2('4 · Contenidos y unidades didácticas')
d.table([
    ['Bloque', 'Unidad didáctica', 'Contenidos', 'Horas', 'Ses.'],
    ['B1 · Contexto y programación', 'UD1 · [El contexto formativo]', '[Análisis del contexto, detección de necesidades, normativa, estructura del certificado]', '[12]', '[2]'],
    ['B2 · Diseño y secuenciación', 'UD2 · [Objetivos y contenidos]', '[Objetivos operativos, criterios de evaluación, secuenciación, temporalización]', '[18]', '[3]'],
    ['B3 · Metodología y recursos', 'UD3 · [Metodología y actividades]', '[Métodos activos, agrupamientos, materiales y medios, coordinación docente]', '[18]', '[3]'],
    ['B4 · Evaluación y mejora', 'UD4 · [Evaluación y mejora]', '[Evaluación diagnóstica, formativa y sumativa; instrumentos, rúbricas, análisis y mejora]', '[12]', '[1]'],
    ['Total', '', '', '60', '9'],
], [4.2, 4.4, 6.0, 1.2, 1.2])

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

d.h2('6 · Temporalización')
d.p('Nueve sesiones entre el 24/11/2026 y el 04/12/2026 (6 h por sesión). Si el centro mueve una fecha, actualízala aquí y en el portfolio del repositorio.', 'Body')
d.table([
    ['Sesión', 'Fecha', 'Contenido', 'Actividad y evidencia'],
    ['1', '24/11/2026', 'Presentación del módulo y análisis del contexto', 'Ficha del grupo'],
    ['2', '25/11/2026', 'Marco normativo del certificado y de la FPE', 'Análisis de normativa'],
    ['3', '26/11/2026', 'Detección de necesidades y perfil del alumnado', 'Ficha del perfil'],
    ['4', '27/11/2026', 'Objetivos y criterios de evaluación', 'Tabla de objetivos y CE'],
    ['5', '30/11/2026', 'Contenidos y unidades didácticas', 'Tabla de secuenciación'],
    ['6', '01/12/2026', 'Metodología y diseño de actividades', 'Programación (borrador)'],
    ['7', '02/12/2026', 'Recursos, materiales y coordinación docente', 'Listado de recursos'],
    ['8', '03/12/2026', 'Temporalización y guion minuteado', 'Cronograma y guion'],
    ['9', '04/12/2026', 'Evaluación, rúbrica y cierre', 'Rúbrica y programación final'],
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
], [1.0, 11.0, 5.0])
d.p('Plantilla de maquetación · MF1442_3 · SSCE0110 · CEFI Formación (Almonte) · v1.0 · 25/11/2026', 'Small')
d.p('Material de estudio propio del portfolio: no reproduce el manual comercial del curso y no sustituye la documentación oficial del centro.', 'Small')

d.save('maquetacion_MF1442_3.fodt')
print('ok')
