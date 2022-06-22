# -*- coding: utf-8 -*-

import os
import time
# import copy
# import re
from shutil import copyfile
from optparse import OptionParser
# import markdown
# from markdown.extensions.toc import TocExtension
import jinja2
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

from pyremark.docdata.mmddata import get_data




def process_a_file(filepath):
    print('processing: '+filepath)
    #try:
    S = slides(filepath)
    htmlfile = S.outputPath
    print('done writing to html: '+htmlfile)
    #pdffile = S.pdffile
    #if S.to_pdf:
    #    export_topdf(htmlfile, pdffile)


class MyHandler2(FileSystemEventHandler):
    def on_modified(self, event):
        filepath = event.src_path
        if filepath[-3:].lower()==".md":
            process_a_file(filepath)
            print("updated slides")

def start_watching_directory(adir):
    print("start watching changes")
    print("to stop watching, press ctrl+c")
    observer = Observer()
    event_handler = MyHandler2()
    observer.schedule(event_handler, adir, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
    print("")
    print("watching stop")


class MyHandler(FileSystemEventHandler):
    def __init__(self, infile):
        self.infile = infile

    def dispatch(self, event):
        slides(self.infile)
        print("updated slides")


def start_watching_a_file(filepath):
    process_a_file(filepath)
    print("start watching changes")
    print("to stop watching, press ctrl+c")
    observer = Observer()
    event_handler = MyHandler(filepath)
    path =  os.path.dirname(os.path.abspath(filepath))
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
    print("")
    print("watching stop")


def gen_list_page(basedir, force):
    outputPath = os.path.join(basedir, "index.html")
    if os.path.exists(outputPath) and not(force):
        print("index.html exists and no forcing option is provided")
        print("NOT generating the index.html file")
        return

    pyrem_path = os.path.dirname(__file__)
    fs = os.listdir(basedir)
    slidelist = []
    md_list = [ f for f in fs if f[-3:].lower()==".md" ]
    html_list = [ f for f in fs if f[-12:].lower()==".slides.html" ]
    for md in md_list:
        ht = md[:-3]+".slides.html"
        if ht in html_list:
            slidelist.append({"mdpath": md, "htmlpath": ht})
        else:
            slidelist.append({"mdpath": md, "htmlpath": "not_generated"})
    dic = {"slidelist": slidelist}

    template_path = os.path.join(pyrem_path,'templates')
    templateLoader = jinja2.FileSystemLoader(searchpath=template_path)
    templateEnv = jinja2.Environment(loader=templateLoader)
    TEMPLATE_FILE = "list.html"
    template = templateEnv.get_template(TEMPLATE_FILE)
    outputText = template.render(dic)
    text_export(outputText, outputPath)
    return


def main():
    parser = OptionParser()
    parser.add_option("-i", "--input",
        dest="filename",
        help="markdown file holding your slides and configs",
        metavar="SLIDES.md")
    parser.add_option("-d", "--directory", dest="directory", default=None, help="watch the current directory")
    parser.add_option("-w", "--watch", action="store_true", dest="watch", default=False, help="watch the file")
    parser.add_option("-f", "--force", action="store_true", dest="force", default=False, help="overlap index file if exist")

    (options, args) = parser.parse_args()

    if options.watch and options.filename:
        start_watching_a_file(options.filename)

    elif options.filename:
        process_a_file(options.filename)

    elif options.directory:
        print(options.directory)
        gen_list_page(options.directory, options.force)
        start_watching_directory(".")

    else:
        print("No file is provided and no option is selected")
        print("Stop and close")

    #print "checking"
    #if S.to_pdf:
    #    export_topdf(htmlfile, pdffile)


def check_mkdir(outpath):
    directory = os.path.dirname(outpath)
    if not os.path.exists(directory):
        print('creating dir: '+directory)
        os.makedirs(directory)


def text_export(outputText, outputPath):
    check_mkdir(outputPath)
    # print 'writing file to:', outputPath
    f = open(outputPath, 'w')
    f.write(outputText)  # .encode("utf-8"))
    f.close()


def copy_directories(static_path_in, static_path_out):
    for dirName, subdirList, fileList in os.walk(static_path_in):
        for fname in fileList:
            inf = os.path.join(dirName, fname)
            relf = os.path.relpath(inf, static_path_in)
            outf = os.path.join(static_path_out, relf)
            check_mkdir(outf)
            copyfile(inf, outf)


class slides():
    def __init__(self, afile):
        doc, config = self.process_md(afile)
        # html = markdown.markdown(doc, extensions=['toc'])
        # print(html)
        content = doc

        base_dir = os.path.abspath(os.path.dirname(afile))
        base_name = os.path.basename(afile)

        output_dir = ''
        if 'output_dir' in config:
            output_dir = config['output_dir']
            del config['output_dir']

        output_fname = '{}.slides.html'.format(base_name.replace('.md', ''))
        if 'output_filename' in config:
            output_fname = config['output_filename']
            del config['output_filename']

        if 'remarkjs_path' in config:
            remjs_path = config['remarkjs_path']
        else:
            remjs_path = None
            config['remarkjs_path'] = None

        if 'custom_css' not in config:
            config['custom_css'] = None

        maindic = {}
        maindic['content'] = content
        maindic.update(config)

        """
        for k,v in maindic.items():
            print(k,v)
        """

        # the source code file directory
        pyrem_path = os.path.dirname(__file__)

        # prepare remark_js path is None or local
        if (remjs_path is None):
            # use online latest remark.js file as written in template file
            # "https://remarkjs.com/downloads/remark-latest.min.js"
            pass
        elif (not(remjs_path[:4] == 'http')):
            remjs_path_dir = os.path.dirname(remjs_path)
            remjs_dir_fullpath = os.path.abspath(os.path.join(base_dir,
                                                 remjs_path_dir))
            # print(remjs_dir_fullpath)
            if not os.path.exists(remjs_dir_fullpath):
                src = os.path.join(pyrem_path, 'remarkjs')
                copy_directories(src, remjs_dir_fullpath)

        template_path = os.path.join(pyrem_path, 'templates')
        templateLoader = jinja2.FileSystemLoader(searchpath=template_path)
        templateEnv = jinja2.Environment(loader=templateLoader)
        TEMPLATE_FILE = "base.html"
        template = templateEnv.get_template(TEMPLATE_FILE)
        outputText = template.render(maindic)
        # print(outputText)

        outputPath = os.path.join(base_dir, output_dir, output_fname)
        self.outputPath = outputPath
        # self.pdffile = outputPath.replace('.html','.pdf')
        # if not pdf_filename is None:
        #    self.pdffile = pdf_filename

        text_export(outputText, outputPath)

    def process_md(self, afile):
        with open(afile, 'r') as f:
            doc = f.read()
        doc, config = get_data(doc)
        config2 = {}
        for k, v in config.items():
            config2[k] = ' '.join(v)
        for line in doc.split('\n'):
            if len(line)>0 and line[0] == '#':
                print(line)
            # print(line)

        return doc, config2


if __name__ == '__main__':
    afile = 'testing/test.md'
    S = slides(afile)
