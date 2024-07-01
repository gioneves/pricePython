# require
from shiny import App, Inputs, Outputs, Session, reactive, render, ui
from shinylive import *
from pathlib import Path
from PIL import Image

# html modules
headerApp = Path("docs/html/header/headerApp.html").read_text()
dropdownStart = Path("docs/html/dropdowns/dropdownStart.html").read_text()

htmlContent = headerApp + dropdownStart

# css/ js
css_file = Path("docs/css/app.css")
js_file = Path("docs/js/app.js")
image = Path("docs/images/brazilLang.png")

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
    ui.tags.script(src='https://cdnjs.cloudflare.com/ajax/libs/intro.js/4.3.0/intro.min.js'),
    ui.tags.script(src='https://cdnjs.cloudflare.com/ajax/libs/annyang/2.6.0/annyang.min.js'),
    ui.tags.link(rel='stylesheet', href='https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css'),
    ui.tags.link(rel='stylesheet', href='https://cdnjs.cloudflare.com/ajax/libs/bttn.css/0.2.4/bttn.min.css'),
    ui.tags.script(src='https://cdnjs.cloudflare.com/ajax/libs/echarts/5.5.0/echarts.min.js'),
    ui.tags.script(src='https://cdn.jsdelivr.net/npm/wnumb@1.2.0/wNumb.min.js'),
    ui.tags.script(src='https://cdnjs.cloudflare.com/ajax/libs/noUiSlider/14.6.3/nouislider.min.js'),
    ui.tags.link(rel='stylesheet', href='https://cdnjs.cloudflare.com/ajax/libs/noUiSlider/14.6.3/nouislider.min.css'),
    ui.tags.script(src='https://unpkg.com/@popperjs/core@2/dist/umd/popper.min.js'),
    ui.tags.script(src='https://unpkg.com/tippy.js@6/dist/tippy-bundle.umd.js'),
    ui.tags.link(rel='stylesheet', href='https://unpkg.com/tippy.js@6/animations/scale.css'),
    ui.include_css(css_file),
    ui.include_js(js_file)
  ),
  # body (html modules)
  ui.HTML(f"<body>{htmlContent}</body>"),
  ui.output_ui("code"),
  ui.output_text("code2"),
  ui.HTML("<input id='value' min='0' max='100' value='50' type='range' oninput='Shiny.setInputValue(`value`, Number($(`#value`).val()), { priority: `event`})'> <div id='myChart' style='width: 450px; height: 500px;'></div>")
)

# server
def server(input, output, session):

  @output
  @render.text
  def code():
    return ui.HTML(
    """
    <script>
    const myChartUse = echarts.init(document.getElementById('myChart'));
    
    function update1 (value1) {
      const option = {
        series: [{
          type: 'gauge',
          data: [{
            name: 'Pressure',
            value: value1
          }]
        }]
      };
      myChartUse.setOption(option);
    }
      
    update1();
      
    function update2 () {
      const value1 = Number(document.getElementById('value').value);
      update1(value1)
    }
      
    document.getElementById('value').addEventListener('input', update2);
    </script>
    """
    )
  
  @reactive.calc
  def reac2():
    return (input.value() + 5) / 2

  @output
  @render.text
  def code2():
    return reac2()
      
  @reactive.effect
  @reactive.event(input.setBttnLang)
  def _():
    ui.modal_show(
      ui.modal(
        ui.HTML(
          """
          <div class='gridClass'>
          <div class='gridTwelve'>
          <div class='gridClass'>
          <div class='gridTwelve' style='text-align: center; font-size: 20px;'>
          Select your preferred language:</div>
          <br>
          <div class='gridTwelve' style='text-align: center;'>
          <button class='i18nBttnClass' onclick='changeLanguageAndInit(`en`);'>English</button>
          <button class='i18nBttnClass' onclick='changeLanguageAndInit(`es`);'>Español</button>
          <button class='i18nBttnClass' onclick='changeLanguageAndInit(`ru`);'>Русский</button>
          </div>
          <br>
          <div class='gridTwelve' style='text-align: center;'>
          <button class='i18nBttnClass' onclick='changeLanguageAndInit(`ch`);'>中国人</button>
          <button class='i18nBttnClass' onclick='changeLanguageAndInit(`jp`);'>日本語</button>
          <button class='i18nBttnClass' onclick='changeLanguageAndInit(`pt`);'>Portugu\u00EAs</button>
          </div>
          </div>
          </div>
          </div>
          """
        ),
        title=ui.HTML(
          """
          <div><i class='fas fa-earth-americas' style='position: relative;
          inset: 4px 0 0 -2px; font-size: 37px; color: #54cede;
          text-shadow: 2px 0 #020202;'></i> Change language</div>
          """
        ),
        easy_close=True,
        footer=None
      )
    )

app = App(app_ui, server)

app.run()

