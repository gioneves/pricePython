// change theme
$(document).ready(function() {
  $('#darkTheme').on('click', function() {
    const clique = $(this).data('clique');
    if (clique) {
      $('body, [id^="dropdown"]').animate({
        "background-color": "#fafac0",
        "color": "#242832"
      }, "slow");
    } else {
      $('body, [id^="dropdown"]').animate({
        "background-color": "#242832",
        "color": "#fafac0"
      }, "slow");
    }
    $(this).data('clique', !clique);
  });
});

// Inicializar i18next
i18next.use(i18nextBrowserLanguageDetector).init({
    fallbackLng: 'en', // Linguagem padrão
    debug: true,
    resources: {
        en: {
          translation: {
            "tChangeTheme": "Change theme"
          }
        },
        es: {
          translation: {
            "tChangeTheme": "Hola Mundo"
          }
        },
        fr: {
          translation: {
            "tChangeTheme": "Bonjour le monde"
          }
        }
    }
}, function(err, t) {
    // Atualizar o conteúdo da página após a inicialização
    updateContent();
});

// Função para atualizar o conteúdo da página com as traduções
function updateContent() {
    document.querySelectorAll('[data-i18n]').forEach(function(element) {
        var key = element.getAttribute('data-i18n');
        element.textContent = i18next.t(key);
    });
}

// Função para mudar o idioma e inicializar a página
function changeLanguageAndInit(lng) {
    // Mudar o idioma
    i18next.changeLanguage(lng, function() {
        // Atualizar o conteúdo da página
        updateContent();
        // Disparar o clique no botão fakeButtonInitPage
        document.getElementById('complexTranslation').click();
    });
}
