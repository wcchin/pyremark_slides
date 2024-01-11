## use the script

The below is example to run `gen_pdf.sh` script.

run python server

`python -m http.server`

then, on another shell, run

`./gen_pdf.sh -s a_file`

`-s` flag is optional, for slimming / reducing pdf size. 

`a_file` is the front part of the file, without `.md`/`.slides.html`/`.slides.pdf`

port is assume to be 8000, which is the default for python server. 

the html file is expected under the current directory. relative path or other directory is not tested. 



## manually

use `python -m http.server`

command: 
`decktape http://0.0.0.0:8000/documents/slides/testting_note.slides.html testing.pdf`

example: 

`decktape http://0.0.0.0:8000/documents/slides/meeting_202206.slides.html meeting_202206.slides.pdf`
`decktape http://0.0.0.0:8000/documents/slides/meeting_202208.slides.html meeting_202208.slides.pdf`


reduce size:
gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook -dNOPAUSE -dQUIET -dBATCH -sOutputFile=meeting_202208-b2.slides.pdf meeting_202208-b.slides.pdf
