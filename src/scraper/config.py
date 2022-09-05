from datetime import date
from datetime import datetime

TODAY = str(date.today())
TIMESTAMP = datetime.timestamp(datetime.now())
SCRAPER_OUTPUT_DIRECTORY = f'output/raw_scrape/'
SCRAPER_OUTPUT_FILE = SCRAPER_OUTPUT_DIRECTORY + f'{TODAY}.json'
SCRAPER_TRANSLATION_OUTPUT_DIRECTORY = f'output/translated_scrape/'
SCRAPER_TRANSLATION_OUTPUT_FILE = SCRAPER_TRANSLATION_OUTPUT_DIRECTORY + f'{TODAY}.json'

ERROR_TRANSLATION_FAILED = 'Failed to translate content'

websites_to_scrape = {
    "Aftonbladet": {
        "url":"https://www.aftonbladet.se/",
        "xpath":"//h2[@class='hyperion-css-19rutrz']",
        "country":"Sweden",
        "newspaper":"Aftonbladet"
    },

    "Welt":
        {
            "url":"https://www.welt.de/",
            "xpath":"//div[@data-qa:'Teaser.Headline']",
            "country":"Germany",
            "newspaper" : "Welt"
        },

    "La Nacion":
        {
            "url":"https://www.lanacion.com.ar/",
            "xpath":"//h1[@class:'com-title --xl']",
            "country":"Argentina",
            "newspaper":"La Nación"
        },

    "The Age":
        {
            "url":"https://www.theage.com.au/",
            "xpath":"//div[@class:'_3nCue']//a[@data-testid:'article-link']",
            "country":"Australia",
            "newspaper":"The Age"
        },

    "The Sydney Morning Herald":
        {
            "url":"https://www.smh.com.au/",
            "xpath":"//div[@class:'_3PjlS']//h3[@class:'_2XVos _1SXCB']",
            "country":"Australia",
            "newspaper":"The Sydney Morning Herald"
        },

    "Die Presse":
        {
            "url":"https://www.diepresse.com/",
            "xpath":"//h1/a",
            "country":"Austria",
            "newspaper":"Die Presse"
        },

    "The Daily Star":
        {
            "url":"https://www.thedailystar.net/",
            "xpath":"//h3/a",
            "country":"Bangladesh",
            "newspaper":"The Daily Star"
        },

    "Le Soir":
        {
            "url":"https://www.lesoir.be/",
            "xpath":"//h3",
            "country":"Belgium",
            "newspaper":"Le Soir"
        },

    "De Standaard":
        {
            "url":"http://www.standaard.be/",
            "xpath":"//h1[@class:'article__header']",
            "country":"Belgium",
            "newspaper":"De Standaard"
        },

    "El Diario":
        {
            "url":"https://www.eldiario.net/portal/",
            "xpath":"//div[@class:'jeg_block_container']//h3[@class:'jeg_post_title']/a",
            "country":"Bolivia",
            "newspaper":"El Diario"
        },

    "O Estadao":
        {
            "url":"https://www.estadao.com.br/",
            "xpath":"//h3[@class:'title']",
            "country":"Brazil",
            "newspaper":"O Estadao"
        },

    "Folha de S.Paulo":
        {
            "url":"https://www1.folha.uol.com.br/",
            "xpath":"//h2[@class:'c-main-headline__title']",
            "country":"Brazil",
            "newspaper":"Folha de S.Paulo"
        },




    "O Globo":
        {
            "url":"https://oglobo.globo.com/",
            "xpath":"//h1[@class:'title']",
            "country":"Brazil",
            "newspaper":"O Globo"
        },




    "Le Devoir":
        {
            "url":"https://www.ledevoir.com/",
            "xpath":"//article//h2",
            "country":"Canada",
            "newspaper":"Le Devoir"
        },




    "The Globe and Mail":
        {
            "url":"https://www.theglobeandmail.com/",
            "xpath":"//div[@class:'Headline__StyledHeadline-sc-1d2q0wc-0 ewTBxn TopPackageBigStory__StyledHeadline-sc-1gza93-4 ePtpIs']",
            "country":"Canada",
            "newspaper":"The Globe and Mail"
        },




    "La Presse":
        {
            "url":"https://www.lapresse.ca/actualites/",
            "xpath":"//span[@class:'headlineCard__title ']",
            "country":"Canada",
            "newspaper":"La Presse"
        },




    "El Mercurio":
        {
            "url":"http://www.emol.com/",
            "xpath":"//h1",
            "country":"Chile",
            "newspaper":"El Mercurio"
        },




    "Al-Ahram":
        {
            "url":"http://www.ahram.org.eg/",
            "xpath":"//h3",
            "country":"Egypt",
            "newspaper":"Al-Ahram"
        },




    "Helsingin Sanomat":
        {
            "url":"https://www.hs.fi/",
            "xpath":"//h2[@class:'teaser-m__title teaser-title-30']",
            "country":"Finland",
            "newspaper":"Helsingin Sanomat"
        },




    "Helsinki Times":
        {
            "url":"http://www.helsinkitimes.fi/",
            "xpath":"//h2[@itemprop:'headline']",
            "country":"Finland related",
            "newspaper":"Helsinki Times"
        },




    "Le Figaro":
        {
            "url":"http://www.lefigaro.fr/",
            "xpath":"//article//p",
            "country":"France",
            "newspaper":"Le Figaro"
        },




    "Libération":
        {
            "url":"https://www.liberation.fr/",
            "xpath":"//h2[@class:'Headline-sc-16el3pa-0 dHUwSB font_lg-libe font_primary font_primary_spacing-0-6 font_normal margin-xs-bottom ']",
            "country":"France",
            "newspaper":"Libération"
        },




    "Frankfurter Allgemeine Zeitung":
        {
            "url":"http://www.faz.net/",
            "xpath":"//header[@class:'tsr-Base_ContentHeader']",
            "country":"Germany",
            "newspaper":"Frankfurter Allgemeine Zeitung"
        },




    "Süddeutsche Zeitung":
        {
            "url":"https://www.sueddeutsche.de/",
            "xpath":"//h3[@class:'sz-teaser__title sz-teaser__title--l-lead-story ']",
            "country":"Germany",
            "newspaper":"Süddeutsche Zeitung"
        },




    "Die Welt":
        {
            "url":"https://www.welt.de/",
            "xpath":"//h2[@class:'StageHeader.Headline']",
            "country":"Germany",
            "newspaper":"Die Welt"
        },




    "Die Zeit":
        {
            #TODO: Javascript
            "url":"https://www.zeit.de/",
            "xpath":"//div",
            "country":"Germany",
            "newspaper":"Die Zeit"
        },




    "Kathimerini":
        {
            "url":"http://www.kathimerini.gr/",
            "xpath":"//div[@class:'design_one_title_big']//h2",
            "country":"Greece",
            "newspaper":"Kathimerini"
        },




    "Kathimerini in English":
        {
            "url":"http://www.ekathimerini.com/",
            "xpath":"//div[@class:'design_one_title_big']//h2",
            "country":"Greece",
            "newspaper":"Kathimerini in English"
        },




    "South China Morning Post":
        {
            "url":"https://www.scmp.com/",
            "xpath":"//div[@class:'article__title article-title']",
            "country":"Hong Kong",
            "newspaper":"South China Morning Post"
        },




    "The Hindu":
        {
            "url":"https://www.thehindu.com/",
            "xpath":"//h1",
            "country":"India",
            "newspaper":"The Hindu"
        },




    "The Times of India":
        {
            "url":"https://timesofindia.indiatimes.com/",
            "xpath":"//div[@class:'_3MUkE ']",
            "country":"India",
            "newspaper":"The Times of India"
        },




    "Kompas":
        {
            "url":"https://kompas.id/",
            "xpath":"//h4",
            "country":"Indonesia",
            "newspaper":"Kompas"
        },




    "The Irish Times":
        {
            "url":"https://www.irishtimes.com/",
            "xpath":"//div[@class:'col-sm-xl-12 flex flex_col width_100 word-break_word      ']",
            "country":"Ireland",
            "newspaper":"The Irish Times"
        },




    "Haaretz":
        {
            "url":"https://www.haaretz.com/",
            "xpath":"//div[@class:'kj kk kl']//h1",
            "country":"Israel",
            "newspaper":"Haaretz"
        },




    "הארץ  ,ישראל":
        {
            "url":"https://www.haaretz.co.il/",
            "xpath":"//div[@class:'kq ae']//h1",
            "country":"Israel",
            "newspaper":"הארץ  ,ישראל"
        },




    "Corriere della Sera":
        {
            "url":"https://www.corriere.it/",
            "xpath":"//h4[@class:'title-art-hp is-xmedium is-line-h-106']",
            "country":"Italy",
            "newspaper":"Corriere della Sera"
        },




    "The Gleaner":
        {
            "url":"http://jamaica-gleaner.com/",
            "xpath":"//li[@class:'first last leaf']",
            "country":"Jamaica",
            "newspaper":"The Gleaner"
        },




    "Asahi Shimbun":
        {
            "url":"http://www.asahi.com/",
            "xpath":"//div[@class:'c-articleModule p-topNews__firstNews']",
            "country":"Japan",
            "newspaper":"Asahi Shimbun"
        },




    "Mainichi Shimbun":
        {
            "url":"https://www.mainichi.co.jp/",
            "xpath":"//div[@class:'main_text_inner']",
            "country":"Japan",
            "newspaper":"Mainichi Shimbun"
        },




    "Daily Nation":
        {
            "url":"https://www.nation.co.ke/",
            "xpath":"//h3[@class:'teaser-image-large_title title-medium']",
            "country":"Kenya",
            "newspaper":"Daily Nation"
        },




    "New Straits Times":
        {
            "url":"https://www.nst.com.my/",
            "xpath":"//div[@class:'field-title']",
            "country":"Malaysia",
            "newspaper":"New Straits Times"
        },




    "NRC Handelsblad":
        {
            "url":"https://www.nrc.nl/",
            "xpath":"//h3[@class:'nmt-item__headline']",
            "country":"Netherlands",
            "newspaper":"NRC Handelsblad"
        },




    "De Volkskrant":
        {
            #TODO: Paywall redirect
            "url":"https://www.volkskrant.nl/",
            "xpath":"//div",
            "country":"Netherlands",
            "newspaper":"De Volkskrant"
        },




    "The New Zealand Herald":
        {
            "url":"https://www.nzherald.co.nz/",
            "xpath":"//h2[@class:'story-card__heading']",
            "country":"New Zealand",
            "newspaper":"The New Zealand Herald"
        },




    "Aftenposten":
        {
            "url":"https://www.aftenposten.no/",
            "xpath":"//h2[@class:'title']",
            "country":"Norway",
            "newspaper":"Aftenposten"
        },




    "El Comercio":
        {
            "url":"https://elcomercio.pe/",
            "xpath":"//h2",
            "country":"Peru",
            "newspaper":"El Comercio"
        },




    "Philippine Daily Inquirer":
        {
            "url":"https://newsinfo.inquirer.net/",
            "xpath":"//h1",
            "country":"Philippines",
            "newspaper":"Philippine Daily Inquirer"
        },




    "Diário de Notícias":
        {
            "url":"https://www.dn.pt/",
            "xpath":"//h2[@class:'t-am-title']/span",
            "country":"Portugal",
            "newspaper":"Diário de Notícias",
        },




    "The Straits Times":
        {
            "url":"https://www.straitstimes.com/",
            "xpath":"//div[@class:'content']",
            "country":"Singapore",
            "newspaper":"The Straits Times",
        },




    "Chosun Ilbo":
        {
            #Javascript
            "url":"http://www.chosun.com/",
            "xpath":"//*",
            "country":"South Korea",
            "newspaper":"Chosun Ilbo"
        },




    "El País":
        {
            "url":"https://elpais.com/",
            "xpath":"//h2/a",
            "country":"Spain",
            "newspaper":"El País"
        },




    "Neue Zürcher Zeitung":
        {
            "url":"https://www.nzz.ch/",
            "xpath":"//div[@class : 'teaser__content teaser__content--2of3']//span",
            "country":"Switzerland",
            "newspaper":"Neue Zürcher Zeitung"
        },




    "Le Temps":
        {
            #TODO: Javascript
            "url":"https://www.letemps.ch/",
            "xpath":"",
            "country":"Switzerland",
            "newspaper":"Le Temps"
        },




    "Hürriyet":
        {
            "url":"https://www.hurriyet.com.tr/dunya/",
            "xpath":"//div[@id:'content']//h2",
            "country":"Turkey",
            "newspaper":"Hürriyet"
        },




    "The Daily Telegraph":
        {
            "url":"https://www.telegraph.co.uk/",
            "xpath":"//span[@class:'list-headline__text']",
            "country":"United Kingdom",
            "newspaper":"The Daily Telegraph"
        },




    "The Times":
        {
            "url":"https://www.thetimes.co.uk/",
            "xpath":"//h3[@class:'Item-headline Headline--xl']",
            "country":"London",
            "newspaper":"The Times"
        },




    "The New York Times":
        {
            #javascript
            "url":"https://www.nytimes.com/",
            "xpath":"",
            "country":"New York",
            "newspaper":"The New York Times"
        },


    "The Washington Post":
        {
            "url":"https://www.washingtonpost.com/",
            "xpath":"//h2/a[@data-pb-local-content-field:'web_headline']",
            "country":"Washington D.C.",
            "newspaper":"The Washington Post"
        }
}