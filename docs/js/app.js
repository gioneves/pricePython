// shinySetInputValue

// buttons
document.addEventListener("DOMContentLoaded", function() {
  function shinySetFunction() {
    $("[id^='setBttn']").on("click", function() {
      Shiny.setInputValue(this.id, Math.random(), {priority: "event"});
    });
  };
  shinySetFunction();
});

// change theme
$(document).ready(function() {
  $('#darkTheme').on('click', function() {
    const clique = $(this).data('clique');
    if (clique) {
      $('body, [id^="dropdown"], .modal-content, [id^="autoDrops"]').animate({
        "background-color": "#fafac0",
        "color": "#242832"
      }, "slow");
      $('body').on('show.bs.modal', function() {
        $('.modal-body').css({
          'background-color': '#fafac0',
          'color': '#242832'
        });
      });
    } else {
      $('body, [id^="dropdown"], .modal-content, [id^="autoDrops"]').animate({
        "background-color": "#242832",
        "color": "#fafac0"
      }, "slow");
      $('body').on('show.bs.modal', function() {
        $('.modal-body').css({
          'background-color': '#242832',
          'color': '#fafac0'
        });
      });
    }
    $(this).data('clique', !clique);
  });
});

// i18next
i18next.use(i18nextBrowserLanguageDetector).init({
  fallbackLng: 'en', // pattern language
  debug: true,
  resources: {
    en: {
      translation: {
        "tChangeTheme": "Change theme",
        "tIntroGuide": "Analysis guide",
        "tHowEarn": "HOW MUCH DO YOU EARN?",
        "tHowMuch": "HOW MUCH DO YOU SELL FOR?",
        "tHowQuant": "(AVERAGE) QUANTITY SOLD"
      }
    },
    es: {
      translation: {
        "tChangeTheme": "Cambiar tema",
        "tIntroGuide": "Guía de análisis",
        "tHowEarn": "¿POR CUÁNTO SE VENDE?",
        "tHowMuch": "¿CUÁNTO GANAS POR CADA VENTA?",
        "tHowQuant": "CANTIDAD (MEDIA) VENDIDA"
      }
    },
    ch: {
      translation: {
        "tChangeTheme": "Change theme",
        "tIntroGuide": "分析指南。",
        "tHowEarn": "你们卖多少钱？",
        "tHowMuch": "你收入多少？",
        "tHowQuant": "平均销售数量。"
      }
    },
    ru: {
      translation: {
        "tChangeTheme": "Bonjour le monde",
        "tIntroGuide": "Руководство по анализу",
        "tHowEarn": "ЗА СКОЛЬКО ВЫ ПРОДАЕТЕ?",
        "tHowMuch": "СКОЛЬКО ТЫ ЗАРАБАТЫВАЕШЬ?",
        "tHowQuant": "(СРЕДНЕЕ) КОЛИЧЕСТВО ПРОДАННОГО"
      }
    },
    jp: {
      translation: {
        "tChangeTheme": "Hola Mundo",
        "tIntroGuide": "分析ガイド。",
        "tHowEarn": "いくらで売られていますか？",
        "tHowMuch": "いくら稼いでいますか？",
        "tHowQuant": "(平均) 販売数量"
      }
    },
    pt: {
      translation: {
        "tChangeTheme": "Mudar tema",
        "tIntroGuide": "Analysis guide",
        "tHowEarn": "QUANTO VOCÊ GANHA?",
        "tHowMuch": "POR QUANTO VOCÊ VENDE?",
        "tHowQuant": "Guia de análise"
      }
    }
  }
}, function(err, t) {
  updateContent();
});

function updateContent() {
  document.querySelectorAll('[data-i18n]').forEach(function(element) {
    var key = element.getAttribute('data-i18n');
    element.textContent = i18next.t(key);
  });
}

function changeLanguageAndInit(lng) {
  i18next.changeLanguage(lng, function() {
    updateContent();
    document.getElementById('complexTranslation').click();
  });
}

// voices (annyang)
const voiceCommands = {
  'change': function() {
    const darkAnny = document.getElementById("darkTheme");
    darkAnny.click();
  },
  'container': function() {
    const dropOpenAnny = document.getElementById("dropBttn");
    dropOpenAnny.click();
  }
};

if (annyang) {
  annyang.addCommands(voiceCommands);
  annyang.start();
};
