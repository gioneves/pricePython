# require
from shiny import ui, render, App
from shinylive import *
from pathlib import Path

# html (modules)
headerApp = Path("site/html/header/headerApp.html").read_text()
dropdownStart = Path("site/html/dropdowns/dropdownStart.html").read_text()

htmlContent = headerApp + dropdownStart

# css/ js
css_file = Path("site/css/app.css")
js_file = Path("site/js/app.js")

# ui
app_ui = ui.page_fluid(
    # header
    ui.head_content(
      ui.tags.title('Hello Shiny!'),
      ui.tags.script(src='https://cdnjs.cloudflare.com/ajax/libs/jqueryui/1.13.3/jquery-ui.min.js'),
      ui.tags.link(rel='stylesheet', href='https://cdnjs.cloudflare.com/ajax/libs/jqueryui/1.13.3/themes/base/jquery-ui.min.css'),
      ui.tags.link(rel='stylesheet', href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css'),
      ui.tags.script(src='https://cdnjs.cloudflare.com/ajax/libs/i18next/21.6.6/i18next.min.js'),
      ui.tags.script(src='https://cdnjs.cloudflare.com/ajax/libs/i18next-browser-languagedetector/6.1.1/i18nextBrowserLanguageDetector.min.js'),
      ui.tags.link(rel='stylesheet', href='https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css'),
      ui.tags.link(rel='stylesheet', href='https://cdnjs.cloudflare.com/ajax/libs/bttn.css/0.2.4/bttn.min.css'),
      ui.tags.script(src='https://cdnjs.cloudflare.com/ajax/libs/echarts/5.5.0/echarts.min.js'),
      ui.tags.script(src='https://cdn.jsdelivr.net/npm/wnumb@1.2.0/wNumb.min.js'),
      ui.tags.script(src='https://cdnjs.cloudflare.com/ajax/libs/noUiSlider/14.6.3/nouislider.min.js'),
      ui.tags.link(rel='stylesheet', href='https://cdnjs.cloudflare.com/ajax/libs/noUiSlider/14.6.3/nouislider.min.css'),
      ui.include_css(css_file),
      ui.include_js(js_file)
    ),
    # body modules
    ui.HTML(f"<body>{htmlContent}</body>"),
    ui.output_ui("txt")
)

# server
def server(input, output, session):
    @output
    @render.ui
    def txt():
        return ui.HTML(f'<span>The value of n*2 is <b style="color: #008cba;">{input.slider1() * 2}</b>.</span>')

app = App(app_ui, server)

app.run()
