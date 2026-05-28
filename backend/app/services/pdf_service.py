import fitz  # PyMuPDF
import re
from fastapi import UploadFile, HTTPException

# -------------------------------
# 🔍 Expresiones regulares (compiladas para rendimiento)
# -------------------------------
automotorExpReg = {
    key: re.compile(pattern, re.IGNORECASE | re.MULTILINE)
    for key, pattern in {
        "dominio": r"dominio\s+(\S+)",
        "procedencia": r"Procedencia:\s+(\S+)",
        "fechaInscripcion": r"Fecha Inscripción Inicial:\s+(.{10})",
        "aduana": r"Aduana:\s+(.*?)(?=\s*Dominio Anterior)",
        "codigoAutomotor": r"Código Automotor:\s+(.*?)(?=\s*Vto\.|\s)",
        "marca": r"Marca:\s+\S+-(.*?)(?=\s*Modelo)",  
        "modelo": r"Modelo:\s+\S+-(.*?)(?=\s*Tipo)",
        "tipo": r"Tipo:\s+\S+-(.*?)(?=\s*Mca)",
        "mcaMotor": r"Mca\.Motor:\s+(.*?)(?=\s*Nro\.Motor)",
        "nroMotor": r"Nro\.Motor:\s+(\S+)",
        "mcaChasis": r"Mca\. Chasis:\s+(.*?)(?=\s*Nro)",
        "nroChasis": r"Nro\. Chasis:\s+(\S+)",
        "fabricacion": r"Fabricación Año:\s+(.*?)(?=\s*Modelo\.|\s)",
        "modeloAnio": r"Modelo Año:\s+(.*?)(?=\s*Fecha\.|\s)",
        "fechaAdquisicion": r"Fecha de Adquisición:\s+(.{10})",
        "carroceria": r"Carrocería:\s+(.*?)(?=\s*Condición)",
        "condicion": r"Condición:\s+(.*?)(?=\s*Uso)",
        "uso": r"Uso:\s+(.*?)(?=\s*Cantidad)",
        "cantidadPlacas": r"Cantidad de Placas:\s+(.*?)(?=\s*Peso)",
        "peso": r"Peso:\s+(.*?)(?=\s*Carga)",
        "carga": r"Carga:\s+(.*?)(?=\s*Número)",
        "nroTitulo": r"Número de Título:\s+(\S+)",
        "obleaRTO": r"Oblea RTO Nro\.:?\s+(.*?)(?=\s*VTO)",
        "vto": r"VTO\.:\s+(.{10})",
        "obleaME": r"N°31\/14 Nro\.:?\s+(.*?)(?=\s*ASG)",
        "asg": r"ASG\.:\s+(.*?)(?=\s*Régimen)",
        "registroSeccional": r"Registro Seccional:\s+(.*?)(?=\s*,|\s)",
        "nroTramite": r"Número de Trámite\s?:\s?(\d+)",
        "controlWeb": r"Control Web:\s+(\S+)",
    }.items()
}

# -------------------------------
# 📦 Objeto de salida base
# -------------------------------
automotorBase = {key: "" for key in automotorExpReg}


# ----------------------------------------------------
# 🧠 Servicio: Procesar PDF
# ----------------------------------------------------
async def procesar_pdf(file: UploadFile) -> dict:
    """
    Procesa un PDF del vehículo, valida que tenga solo texto
    y realiza búsquedas. Devuelve un JSON estructurado.
    """

    # -------------------------------
    # 📌 Validar tipo MIME
    # -------------------------------
    if file.content_type not in ["application/pdf"]:
        raise HTTPException(400, "El archivo debe ser un PDF válido.")

    # -------------------------------
    # 📌 Leer bytes
    # -------------------------------
    try:
        pdf_bytes = await file.read()
    except Exception:
        raise HTTPException(400, "Error leyendo el archivo PDF.")

    if not pdf_bytes or len(pdf_bytes) < 20:
        raise HTTPException(400, "Archivo PDF vacío o inválido.")

    # -------------------------------
    # 📌 Abrir PDF
    # -------------------------------
    try:
        doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    except Exception:
        raise HTTPException(400, "El archivo PDF está corrupto o no es válido.")

    try:
        texto_total = []
        contiene_imagenes = False

        # -------------------------------
        # 📌 Recorrer una sola vez
        # -------------------------------
        for page in doc:
            if page.get_images(full=True):
                contiene_imagenes = True

            page_text = page.get_text("text")
            if page_text:
                texto_total.append(page_text)

        if contiene_imagenes:
            raise HTTPException(
                400,
                "El PDF contiene imágenes. Solo se permiten PDFs con texto."
            )

        texto = "\n".join(texto_total).strip()

        if not texto:
            raise HTTPException(400, "El PDF no contiene texto válido.")

        # -------------------------------
        # 🔍 Buscar coincidencias
        # -------------------------------
        resultado = automotorBase.copy()

        for key, regex in automotorExpReg.items():
            match = regex.search(texto)
            resultado[key] = match.group(1).strip() if match else ""

         # ❌ Validar dominio obligatorio
        if not resultado["dominio"]:
            raise HTTPException(status_code=400, detail="PDF inválido: no se encontró el dominio.")


        return {
            "ok": True,
            "paginas": len(doc),
            "resultado": resultado,
        }

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, f"Error procesando el PDF: {str(e)}")
    finally:
        doc.close()
