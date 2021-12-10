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

# pyremark
**a python package for converting markdown to remark.js slides**

a sister project of pyreveal

<!--
## a demo
[![pyreveal demo video](http://wcchin.github.io/images/pyrev_demo_vimeo.png)](https://vimeo.com/226295024)
-->


## Install

```sh

git clone https://github.com/wcchin/pyremark_slides.git
cd pyremark_slides
pip install -e .

```

## Using

1. cd your_slides_dir
2. create a file named whatever.md (with .md extension)
3. follow the instruction in the following sections and write the slides content inside the whatever.md
4. run the command, see the following "usage" section
5. if the '-w' is used in the command, the slides will change according to the modification of the whatever.md file (and custom.css).
6. done

# Documentation

## slides configuration

pyreveal will read the first several lines of the whatever.md file and get the metadata as the configs, using the <a href="https://github.com/waylan/docdata" target="blank">**docdata**</a> package .

```markdown

slide_title: testing remarkjs
custom_css: custom.css
remarkjs_path: remarkjs/remark-0.15.0.js

```

Please try.
