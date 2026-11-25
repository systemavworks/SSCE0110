# MF1442_3 · Maquetación y presentación demo

Material de trabajo del módulo **MF1442_3 · Programación didáctica de acciones formativas para el empleo**
(SSCE0110, CEFI Formación · 24/11/2026 → 04/12/2026).

Dos piezas listas para rellenar: **una plantilla de documento** (la programación didáctica) y **una
presentación demo** (14 diapositivas). Todo está en formato editable y también en PDF para entregar.

## Qué hay en esta carpeta

| Archivo | Qué es | Para qué |
|---|---|---|
| `maquetacion_MF1442_3.docx` | Plantilla del documento | Rellenar la programación didáctica (Word, Google Docs, LibreOffice) |
| `maquetacion_MF1442_3.pdf` | Vista previa del documento | Ver cómo queda antes de escribir; imprimir |
| `presentacion_demo_MF1442_3.pptx` | Presentación de 14 diapositivas | Rellenar y exponer (PowerPoint, Google Slides, Canva) |
| `presentacion_demo_MF1442_3.pdf` | Vista previa de la presentación | Ensayar y proyectar sin depender de fuentes |
| `fuentes/` | Archivos origen (`.fodt`, `.fodp`) y generadores | Regenerar o personalizar la plantilla |

## Cómo abrir cada formato

**PowerPoint** — abre `presentacion_demo_MF1442_3.pptx` y guarda una copia con tu nombre.
**Google Slides** — `drive.google.com` → *Nuevo* → *Subir archivo* → elige el `.pptx` → ábrelo con
Google Slides. Para descargarlo otra vez: *Archivo → Descargar → Microsoft PowerPoint (.pptx)*.
**Canva** — *Crear un diseño → Importar archivo* y sube el `.pptx` (Canva convierte cada diapositiva en
una página editable).
**Word / Google Docs / LibreOffice** — abre `maquetacion_MF1442_3.docx` y trabaja sobre una copia.

> Consejo: cambia el nombre del archivo antes de empezar. Formato recomendado:
> `MF1442_3_programacion_apellido.docx` y `MF1442_3_presentacion_apellido.pptx`.
> La versión que se entrega es siempre el **PDF** con ese mismo nombre.

## Estructura de la presentación (14 diapositivas)

**1** Portada · **2** Cómo usar la plantilla · **3** El módulo (60 h, 9 sesiones, fechas) · **4** Objetivos ·
**5** Perfil del alumnado · **6** Contenidos (4 bloques) · **7** Metodología · **8** Temporalización de las 9 sesiones ·
**9** Recursos · **10** Evaluación · **11** Rúbrica · **12** Alineación constructiva · **13** Riesgos y plan B · **14** Cierre.

Todas las diapositivas siguen la misma rejilla: barra de color a la izquierda, antetítulo en verde azulado,
título grande y contenido en tarjetas o tablas. Si necesitas más espacio, **duplica** una diapositiva en
lugar de reducir el cuerpo de texto.

## Estructura del documento (14 apartados)

**0** Cómo usar la plantilla · **1** Datos de la acción formativa · **2** Justificación y contexto ·
**3** Objetivos y criterios de evaluación · **4** Contenidos y unidades didácticas · **5** Metodología ·
**6** Temporalización · **7** Recursos y materiales · **8** Evaluación · **9** Rúbrica · **10** Alineación constructiva ·
**11** Seguimiento y tutorización · **12** Riesgos y plan B · **13** Bibliografía y anexos · **14** Checklist de entrega.

Los apartados 1 a 6 coinciden con los entregables de la ficha del módulo en `portfolio.html`; el resto son
los que suelen pedir los tribunales. Las tablas ya traen las **fechas reales del cronograma de CEFI**
(24/11 → 04/12/2026) y los **12 entregables** de la checklist.

## Regenerar los archivos

Los originales están en `fuentes/` como documentos planos de LibreOffice:

```bash
cd MF1442_3/fuentes
soffice --headless --convert-to docx:"MS Word 2007 XML" maquetacion_MF1442_3.fodt
soffice --headless --convert-to pptx presentacion_demo_MF1442_3.fodp
soffice --headless --convert-to pdf maquetacion_MF1442_3.fodt presentacion_demo_MF1442_3.fodp
```

Y si quieres cambiar textos y volver a construir todo desde cero:

```bash
cd MF1442_3/fuentes
python3 generar_maquetacion.py   # escribe el .fodt
python3 generar_presentacion.py  # escribe el .fodp
```

Los generadores parten de `docgen.py` y `deck.py` y necesitan **LibreOffice** y **lxml** para producir los
`.docx`/`.pptx`. No dependen de internet ni de plantillas externas.

## Antes de entregar

- [ ] No queda ningún `[corchete]` sin rellenar.
- [ ] Las fechas coinciden con el cronograma del centro (24/11 → 04/12/2026).
- [ ] Cada objetivo tiene su criterio de evaluación y su evidencia.
- [ ] La rúbrica tiene descriptores observables, no adjetivos.
- [ ] PDF exportado con el mismo nombre que el archivo editable.

> Material de estudio propio del portfolio: no reproduce el manual comercial del curso y no sustituye la
> documentación oficial de CEFI Formación ni del certificado.
