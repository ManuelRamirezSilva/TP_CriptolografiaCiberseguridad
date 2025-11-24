#!/bin/bash
# SCRIPT DE COMPILACIÓN - INFORME CRIPTOGRAFÍA Y CIBERSEGURIDAD
# Este script compila el archivo LaTeX a PDF

echo "================================"
echo "COMPILANDO INFORME LaTeX → PDF"
echo "================================"
echo ""

# Directorio del informe
INFORME_DIR="/Users/maxi/Documents/Udesa/Crypto/TP_CriptolografiaCiberseguridad/INFORME"
ARCHIVO="informe_sistema_login_seguro_final.tex"

# Cambiar al directorio
cd "$INFORME_DIR" || exit

echo "📁 Directorio: $INFORME_DIR"
echo "📄 Archivo: $ARCHIVO"
echo ""

# Verificar que el archivo existe
if [ ! -f "$ARCHIVO" ]; then
    echo "❌ Error: Archivo $ARCHIVO no encontrado"
    exit 1
fi

echo "🔄 Primera pasada LaTeX..."
pdflatex -interaction=nonstopmode "$ARCHIVO" > /tmp/latex1.log 2>&1
if [ $? -eq 0 ]; then
    echo "✅ Primera pasada: OK"
else
    echo "⚠️  Primera pasada: Completada con advertencias"
fi

echo ""
echo "🔄 Segunda pasada LaTeX (para referencias)..."
pdflatex -interaction=nonstopmode "$ARCHIVO" > /tmp/latex2.log 2>&1
if [ $? -eq 0 ]; then
    echo "✅ Segunda pasada: OK"
else
    echo "⚠️  Segunda pasada: Completada con advertencias"
fi

echo ""

# Verificar que se generó el PDF
PDF_FILE="${ARCHIVO%.tex}.pdf"
if [ -f "$PDF_FILE" ]; then
    SIZE=$(du -h "$PDF_FILE" | cut -f1)
    echo "✅ PDF generado exitosamente"
    echo "📊 Archivo: $PDF_FILE"
    echo "📦 Tamaño: $SIZE"
    echo ""
    echo "✨ La compilación fue exitosa"
else
    echo "❌ Error: No se generó el PDF"
    exit 1
fi

# Limpiar archivos temporales
echo ""
echo "🧹 Limpiando archivos temporales..."
rm -f *.aux *.log *.out *.toc

echo "✅ Limpieza completada"
echo ""
echo "================================"
echo "✅ COMPILACIÓN COMPLETADA"
echo "================================"
