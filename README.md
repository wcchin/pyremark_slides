---
top_title: pyremark, a python package for converting markdown to remark.js slides
project_name: pyremark_slides
smart_title: a markdown to remark.js engine
author: wcchin
short_description: a python package for converting markdown to remark.js slides
keywords: [remark.js, markdown, python]
three_concepts: [':typcn-lightbulb:', ':fab-markdown:', ':fas-chart-area:']
three_desc: [get some idea, write with markdown, and present it]
concept_color: '#33C3F0'
project_url: https://github.com/wcchin/pyremark_slides
project_url_title: go to project page
theme: skeleton
carlae_dir: carlae_page
---

# pyremark_slides
**a python package for converting markdown to remark.js slides**

a sister project of <a href="https://github.com/wcchin/pyreveal" target="_blank">pyreveal</a>.

This project is done to put the markdown content to a base template file which is styled using jinja2, and also use the yaml header to do the config for each file. 

In other words, the purpose of this project focused on separating the heavy html/css configs from the markdown content, and keep only a minimal config setup using the yaml way on top of the markdown file. 

Please try.


## Install

    git clone https://github.com/wcchin/pyremark_slides.git
    cd pyremark_slides
    pip install -e .


## Using

    cd slides_dir
    pyremark -i a_file.md -w

a file name `a_file.slides.html` will be generated, open it with a browser.


## The markdown file template


    slide_title: testing remarkjs
    custom_css: custom.css
    remarkjs_path: remarkjs/remark-0.15.0.js

    # Some title

    ---

    second page


Note:

- custom_css: this will be used to style the remark.js slides. 
- remarkjs_path: this is the local path for offline presentation, default to the online latest remark-latest.js file provided by the original repos. 
- slide_title: this is the title to be shown on the header of the presentation. 


custom.css file default to this:

    @import url(https://fonts.googleapis.com/css?family=Yanone+Kaffeesatz);
    @import url(https://fonts.googleapis.com/css?family=Droid+Serif:400,700,400italic);
    @import url(https://fonts.googleapis.com/css?family=Ubuntu+Mono:400,700,400italic);

    body { font-family: 'Droid Serif'; }
    h1, h2, h3 {
      font-family: 'Yanone Kaffeesatz';
      font-weight: normal;
    }
    .remark-code, .remark-inline-code { font-family: 'Ubuntu Mono'; }



