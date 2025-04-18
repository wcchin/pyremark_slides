
# pyremark_slides
**a python package for converting markdown to [remarkjs](https://github.com/gnab/remark) slides**.

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


​    
## Available themes
### Demo
- Catppuccin: [Latte](testing/demo_0-Catppuccin_latte.slides.html) | [Mocha](testing/demo_1-Catppuccin_mocha.slides.html)
- Rose Pine: [Dawn](testing/demo_2-RosePine-dawn.slides.html) | [Moon](testing/demo_3-RosePine-moon.slides.html)
- Nord: [Polar](testing/demo_4-Nord-polar.slides.html) | [Storm](testing/demo_5-Nord-storm.slides.html)
- Evergreen: [Day](testing/demo_6-Everforest-day.slides.html) | [Night](testing/demo_7-Everforest-night.slides.html)

### Screenshot

<table>
    <tr>
        <td>Theme</td>
        <td>Style</td>
        <td>Title page</td>
        <td>Content page</td>
    </tr>
    <tr>
        <td>Catppuccin</td>
        <td>Mocha  (dark)</td>
        <td><a href="theme_demo/demo-Catppuccin-Mocha-title.png"><img src="theme_demo/demo-Catppuccin-Mocha-title.tb.png" alt="Catppuccin - Mocha - title" style="max-width: 100%;"></a></td>
        <td><a href="theme_demo/demo-Catppuccin-Mocha-content.png"><img src="theme_demo/demo-Catppuccin-Mocha-content.tb.png" alt="Catppuccin - Mocha - content" style="max-width: 100%;"></a></td>
    </tr>
    <tr>
        <td>Catppuccin</td>
        <td>Latte  (light)</td>
        <td><a href="theme_demo/demo-Catppuccin-Latte-title.png"><img src="theme_demo/demo-Catppuccin-Latte-title.tb.png" alt="Catppuccin - Latte - title" style="max-width: 100%;"></a></td>
        <td><a href="theme_demo/demo-Catppuccin-Latte-content.png"><img src="theme_demo/demo-Catppuccin-Latte-content.tb.png" alt="Catppuccin - Latte - content" style="max-width: 100%;"></a></td>
    </tr>
    <tr>
        <td>Rosepine</td>
        <td>Moon (dark)</td>
        <td><a href="theme_demo/demo-Rosepine-Moon-title.png"><img src="theme_demo/demo-Rosepine-Moon-title.tb.png" alt="Rosepine - Moon - title" style="max-width: 100%;"></a></td>
        <td><a href="theme_demo/demo-Rosepine-Moon-content.png"><img src="theme_demo/demo-Rosepine-Moon-content.tb.png" alt="Rosepine - Moon - content" style="max-width: 100%;"></a></td>
    </tr>
    <tr>
        <td>Rosepine</td>
        <td>Dawn (light)</td>
        <td><a href="theme_demo/demo-Rosepine-Dawn-title.png"><img src="theme_demo/demo-Rosepine-Dawn-title.tb.png" alt="Rosepine - Dawn - title" style="max-width: 100%;"></a></td>
        <td><a href="theme_demo/demo-Rosepine-Dawn-content.png"><img src="theme_demo/demo-Rosepine-Dawn-content.tb.png" alt="Rosepine - Dawn - content" style="max-width: 100%;"></a></td>
    </tr>
    <tr>
        <td>Everforest</td>
        <td>Night (dark)</td>
        <td><a href="theme_demo/demo-Everforest-Night-title.png"><img src="theme_demo/demo-Everforest-Night-title.tb.png" alt="Everforest - Night - title" style="max-width: 100%;"></a></td>
        <td><a href="theme_demo/demo-Everforest-Night-content.png"><img src="theme_demo/demo-Everforest-Night-content.tb.png" alt="Everforest - Night - content" style="max-width: 100%;"></a></td>
    </tr>
    <tr>
        <td>Everforest</td>
        <td>Day (light)</td>
        <td><a href="theme_demo/demo-Everforest-Day-title.png"><img src="theme_demo/demo-Everforest-Day-title.tb.png" alt="Everforest - Day - title" style="max-width: 100%;"></a></td>
        <td><a href="theme_demo/demo-Everforest-Day-content.png"><img src="theme_demo/demo-Everforest-Day-content.tb.png" alt="Everforest - Day - content" style="max-width: 100%;"></a></td>
    </tr>
    <tr>
        <td>Nord</td>
        <td>Polar (dark)</td>
        <td><a href="theme_demo/demo-Nord-Polar-title.png"><img src="theme_demo/demo-Nord-Polar-title.tb.png" alt="Nord - Polar - title" style="max-width: 100%;"></a></td>
        <td><a href="theme_demo/demo-Nord-Polar-content.png"><img src="theme_demo/demo-Nord-Polar-content.tb.png" alt="Nord - Polar - content" style="max-width: 100%;"></a></td>
    </tr>
    <tr>
        <td>Nord</td>
        <td>Storm (light)</td>
        <td><a href="theme_demo/demo-Nord-Storm-title.png"><img src="theme_demo/demo-Nord-Storm-title.tb.png" alt="Nord - Storm - title" style="max-width: 100%;"></a></td>
        <td><a href="theme_demo/demo-Nord-Storm-content.png"><img src="theme_demo/demo-Nord-Storm-content.tb.png" alt="Nord - Storm - content" style="max-width: 100%;"></a></td>
    </tr>
</table>




## Added more themes (2025-03-26)
- make the Catppuccin theme to be generic, and added one dark theme based on Catppuccin
- added Rose Pine, Nord, and Everforest series themes
- added demo of the 4x2 themes.
- and fixed "the mathjax \_ not show properly issue"

## Update (2024-01-11)

- added catppuccin style, which use Montserrat as default font. 
- added gen_pdf.sh bash script in the testing folder, the to_generate_pdf.md is also updated to show the usage. [Decktape](https://github.com/astefanutti/decktape) is required. 


## Some additional feature (2023/2/13)

- press `s` to access the search function. 
- press `q` for the table of content.  

These features were in testing stage. 

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

