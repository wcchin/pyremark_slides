slide_title: Note 2022-06-16
custom_css: remarkjs/applestyle.css
aspect_ratio: 16:9
remarkjs_path: remarkjs/remark-0.15.0.js
use_mathjax: true
use_mermaid: false
add_sidebar: true
add_searchbar: true
use_click: false
use_scroll: false

name: inverse
layout: true
class: left, middle, inverse
---
name: Title page
# Note 2022/05/19
On LTA flow data
1. Net-flow (hourly trend)
2. Net-flow (monthly trend)
3. Average trip distance (monthly trend)
4. Work tasks

.footnote[.red.bold[*] .round[Benny@2022-05-19]]

---
name: Chapter 1
class: center, middle, inverse
## I: Net-flow (hourly trend)
To capture IO in one trend line  $F=x^2$.

---
layout: false

$$
F = mc^2
$$

---

$$
\begin{aligned} 
y & = x^4 + 4      \nonumber \\
& = (x^2+2)^2 -4x^2 \nonumber \\
& \le(x^2+2)^2    \nonumber
\end{aligned}
$$

This work, note in code on the slashed underline: 
\begin{align} 
EF &= \frac{A\_{ik} / A\_i}{A\_k / A\_T} \nonumber \\\
&= A\_{ik} \times \frac{A\_T}{A\_i \times A\_k }
\end{align}

This won't work, this happen when the frac and underline is used, if two underlines were detected, it is recognized as the markdown italic:  
\begin{align} 
EF &= \frac{A_{ik} / A_{i}}{A_{k} / A_{T}} \nonumber \\
&= A_{ik} \times \frac{A_{T}}{A_{i}} \times A_{k}} 
\end{align}

\\begin{equation} 
EF = \frac{A_{ik}/A_i}{A_k/A_T}
\\end{equation}

\\begin{equation}
EF = A_{ik} \times \frac{A_T}{A_i \times A_k}
\\end{equation}

some words

\\begin{align}
y &= x^4 + 4      \nonumber \\\
&= (x^2+2)^2 -4x^2 \nonumber \\\
&\le (x^2+2)^2    \nonumber
\\end{align}


---

To capture IO in one trend line
### help you build a culture of excellence.

.round[Testing font]
