#!/bin/bash
#echo "First arg: $1"
#echo "Second arg: $2"

echo "make sure to run a python server before export pdf: python -m http.server"
echo "the port number should be 8000"

echo

echo "usage: ./gen_pdf.sh -s filename"
echo "filename should not include .slides.html, just the front part"
echo "-s is an optional flag for slimming"
echo "e.g.: ./gen_pdf.sh -s test"

if [[ $# -eq 0 ]] ; then
    echo 'no valid argument, stop here'
    exit 0
fi

echo
echo "start processing..."

while [ True ]; do
if [ "$1" = "--sliming" -o "$1" = "-s" ]; then
    SLIMING=1
    shift 1
else
    break
fi
done

decktape "http://0.0.0.0:8000/$1.slides.html" "$1.slides.pdf"

echo "done export to $1.slides.pdf"

if [[ "$SLIMING" -eq 1 ]]; then
    echo "slimming file: $1.slides.pdf"
    gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook -dNOPAUSE -dQUIET -dBATCH -sOutputFile="$1.slides_slim.pdf" "$1.slides.pdf"
    echo "done sliming"
    echo "exported to $1.slides_slim.pdf"
fi

echo "DONE exporting file"
echo "Remember to turn off the server"
