import html, json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from lightbox import LB_CSS, LB_HTML, LB_JS

OUT = os.path.join(os.path.dirname(__file__), '..', 'html')
T = 'https://64.media.tumblr.com/'

from common import TIPOS as ICONS, icon, head_interior, HEAD_CSS, symbols, MINI_CSS, MINI_JS, temas_html, TEMAS_CSS, en, TIPOS_EN, PAISES_EN, fecha_en, I18N_CSS, I18N_JS, LEGACY, LEGACY_CSS

POSTS = [
 dict(slug='nyt175', tipo='port', medio='The New York Times', pais='Estados Unidos', fecha='18 de septiembre de 2026',
  titulo='Los 175 años del New York Times', acento='175',
  fuente='The New York Daily Times, del 18 de septiembre de 2026', creditos=[], tags=['the new york times','teletipos','medios internacionales','publicidad'],
  temas=['historia del periodismo', 'aniversarios', 'publicidad'],
  texto=['La pasada semana el New York Times cumplió 175 años y, durante estos días, el diario ha ido publicando piezas especiales sobre su propia historia, recopiladas <a href="https://www.nytimes.com/interactive/2026/us/175-nyt-anniversary.html" target="_blank" rel="noopener">en su site especial</a>.',
         'En papel, la celebración ha dejado una reproducción de la primera edición de The New York Daily Times, del 18 de septiembre de 1851, un repaso a los anuncios que marcaron su historia y hasta un test con crucigrama para los lectores.'],
  imgs=['0ccb5dd3cb963f5cde118217dffae2f3/465a726c37b7af6b-50/s1280x1920/e65f8579c23210a5df75bfe48e9ac011bb981020.gif',
        '313549c3182642c3311b817408cb42a1/465a726c37b7af6b-bf/s2048x3072/d01892336abe40a93736a3cd6c51d07155d90a01.png',
        '6780a0ab99b42866149dd71aed83be5e/465a726c37b7af6b-11/s2048x3072/5babb7bab011420004cfe82c7e46a3a5a950db76.png',
        '7d9157933384f78ec35b08ac5a957d98/465a726c37b7af6b-a4/s2048x3072/24a8d5e0cdfdc402666db99781334549afdb4917.png',
        '26dc5455aaeecd354715eb6c6b242b27/465a726c37b7af6b-d4/s1280x1920/d84ef7bad175037338aadf6e7965710c0b17a114.jpg',
        'e98b108ce5d08fee85fa6b6bf8090339/465a726c37b7af6b-82/s500x750/55c88572272678d89791971cc663bbd280ca43c2.png',
        'eeb49e5b7fa35db6292387eb18ff5bde/465a726c37b7af6b-ba/s2048x3072/cd3ce21c0a28268504643c62546ce6bc8a6ecc91.jpg',
        'ac7c325197f1f15486eb2af783ec3297/465a726c37b7af6b-82/s2048x3072/6c6b85f0eb0ce14a646a16860ee7ef22ac384a4f.jpg',
        '1d37ce94ee1bc83c91c314c623499a30/465a726c37b7af6b-59/s2048x3072/0a8047bf815c5a2493d1841a56d6f472b85bc325.png',
        'a4c7cac8d1abe3b1f6c85ba39ca65a93/465a726c37b7af6b-4f/s2048x3072/8b2b7480da8036d38ce39006ab5a33164db57cf4.png',
        '31a3fafcb7eecc9178b4be57916bc255/465a726c37b7af6b-0c/s1280x1920/d211f4fc0e788582bdfcb12d9c71e4581a3c07e7.png',
        'f94e2950422682c558be1b9a602fe563/465a726c37b7af6b-cf/s1280x1920/d827cc206dcc4467a273187c7b9c710b79b22839.png']),
 dict(slug='food101', tipo='ilus', medio='The New York Times', pais='Estados Unidos', fecha='17 de abril de 2026',
  titulo='Doce chefs y un manual para comer lo difícil', acento='manual',
  fuente='The New York Times Style Magazine, del 17 de abril de 2026', creditos=['Ryuto Miyake'], tags=['the new york times','ilustraciones','medios internacionales'],
  temas=['gastronomía'],
  texto=['¿Cómo se come un bogavante sin acabar hecho un cuadro? T Magazine, el suplemento de estilo del New York Times, <a href="https://www.nytimes.com/interactive/2026/04/17/t-magazine/how-to-eat-mango-oyster.html?unlocked_article_code=1.-VA.T0Q2.bCkb7pVfP_FC&amp;smid=url-share" target="_blank" rel="noopener">se ha propuesto ayudarnos a lo grande</a>.',
         'Doce chefs reconocidos explican paso a paso cómo comer platos complicados como el bogavante, las ostras, el cangrejo, el fufu, el pho o el roti, en una serie de instrucciones ilustradas por Ryuto Miyake.'],
  imgs=['4544a4bfb0a98a7ed4b195eef4c2ba28/eb7f9b0849d9ebc9-79/s1280x1920/a251119d8f0827da6c6c89b88cac7f00d12ac35a.png',
        'a09458dd45630fb289d9f5cba80ef40f/eb7f9b0849d9ebc9-a7/s1280x1920/3f8776fc4ad0f3eca0447c7c85f1628f15c336f1.png',
        'e68ff038bd2247e18ba1a5e1bd284f36/eb7f9b0849d9ebc9-43/s2048x3072/32016a9b7db58fccd1895fcf88624858b3d81fa6.png',
        '241e69400e9b582bb305042e636e769e/eb7f9b0849d9ebc9-02/s1280x1920/30af1ef8a8fedda042b445a0f404b5f204190ff2.png',
        '4bea31949f48b9564a187aee83227bd0/eb7f9b0849d9ebc9-35/s2048x3072/ccf145746473a0e5507ea439c0b098b990196f26.png',
        'b97f7b2e4784acab80c5be357d677fb0/eb7f9b0849d9ebc9-b9/s1280x1920/888f06deb6bca0c39c8c5f806492456aab22a71b.png',
        '768945c654190f82318a24abd193bb38/eb7f9b0849d9ebc9-74/s1280x1920/a26aae38d73a3af6fe50f587399e9c4cb65ab206.png',
        '8e5cdb88df0c79128ed1d349a482d3e1/eb7f9b0849d9ebc9-8e/s1280x1920/e6970b9579b4ca3c626fdcf9a0f72ee1c4c0d6dc.png',
        '8c7fae54ab6e30ac4762b772bf43e59f/eb7f9b0849d9ebc9-1d/s1280x1920/459ca5c764b3548668294f3c9fa6262bd1591cbc.png',
        'fa7a523fb38529f54eecf5862225d3e3/eb7f9b0849d9ebc9-97/s1280x1920/43c6883652e18f4f78d2be2dd872750d8cb84855.png',
        '2b29a19c5766c1231ece11c0a85691b9/eb7f9b0849d9ebc9-6e/s1280x1920/bb62f8ceef5d07ff8d2733a802aa724a09f8d95e.png',
        '7a3ce42663040ebd678104f2244f5a12/eb7f9b0849d9ebc9-fa/s1280x1920/f7d2fde590a2e2881fabedd386218eafe632b484.jpg']),
 dict(slug='detallito', temas=['deporte', 'fútbol'], tipo='graf', medio='Marca', pais='España', fecha='21 y 23 de noviembre de 2019', deta=True,
  titulo='Radares futboleros', acento='Radares',
  fuente='Marca, del 21 y 23 de noviembre de 2019', creditos=[], tags=['detallitos','marca','deportes','infografía'],
  texto=['El mundo del fútbol siempre es muy dado al análisis de datos y a visualizar con detalle las estadísticas de equipos y jugadores.',
         'Esta semana hemos visto dos ejemplos similares en las páginas de Marca que utilizan un círculo-radar, con cierto aire de videojuego, para comparar varios factores: el rendimiento de Griezmann en las trece primeras jornadas de liga con la Real Sociedad, el Atlético y el Barcelona, y las estadísticas de Ødegaard frente a las de otros centrocampistas.'],
  imgs=['1120688d652c3852e5a88b371bfb8672/638bbc0bf1d6a12f-32/s500x750/224a545e7fda1890f4239c207029ec46aee225de.png',
        'a87385252bd534f923d044216c972c3d/638bbc0bf1d6a12f-4a/s500x750/cf50e6e41042ee35ebdcddd0f17a14bd5d3027e7.png']),
 dict(slug='liberation', temas=['literatura', 'cultura'], tipo='port', medio='Libération', pais='Francia', fecha='16 de octubre de 2026',
  titulo='Libération se vuelve anárquica por Perec', acento='anárquica',
  fuente='Libération, del 16 de octubre de 2026', creditos=[], tags=['especiales','literatura','Perec','medios internacionales'],
  texto=['Con motivo de una importante exposición en la Biblioteca Nacional de Francia dedicada a la obra de Georges Perec, Libération publicó una nueva de sus ediciones especiales dedicada a la literatura experimental de este célebre escritor y ensayista.',
         'Se trata de una alocada edición con un diseño totalmente anárquico: piezas que forman letras, columnas que no siguen un rumbo fijo, fotografías colocadas del revés… Todo ello como homenaje a la experimentación con lenguaje, las palabras y las restricciones formales que caracteriza a este autor francés. Otra de esas ediciones para guardar.'],
  imgs=['093da2d5a18de7d40895b9ad174fe7ed/dfb73906028a5e2a-ea/s1280x1920/a1ccf50f328829da941a6c0a54c285506f0887c7.jpg',
        '07d0320c9ccc20a6301a24cdef133b51/dfb73906028a5e2a-de/s1280x1920/82ccc5a5a7e850f0c23cf6cb3a92f57a685e543e.jpg',
        'fb2de8f2a971cce8b25e76085b64c06e/dfb73906028a5e2a-50/s1280x1920/f347da7f3d63ebb8ffaca3b6b22c263a9515177d.jpg',
        'c792a75f1a6123338aa2847eda5f4903/dfb73906028a5e2a-d4/s1280x1920/8126b0f27942ed50a9c0d9c9ed188d519577f187.jpg',
        'fc25fe12bd75f109817cb8acfadf0b1d/dfb73906028a5e2a-77/s1280x1920/6ffe6e0511b1cce73d4ced1ed2795f6f545e8aa6.jpg',
        '6c3e734d8e0c070d06111e9d4f2ff61a/dfb73906028a5e2a-03/s1280x1920/b6840ca546cdc59063dbfc3adea8570a2a29c622.jpg',
        '7c0ca4ac50d51e138d8cb21faae94a11/dfb73906028a5e2a-48/s1280x1920/6c72e11a54670530aa612ebabea9b0fc0809000d.jpg',
        'bb70d56933c760d812f6e7fcc334089f/dfb73906028a5e2a-cc/s1280x1920/3890c62b4b764a7b6b27ae1d537fc385492d070f.jpg',
        '6f5e81cb8677a56ac912dfa9f1acc720/dfb73906028a5e2a-eb/s1280x1920/df40d41fa84deab002bcb1ff9c17dfe7161ca2fc.jpg',
        'df92dbb6d384c9b39ee31d06730ccd78/dfb73906028a5e2a-ef/s1280x1920/80dc0d1235dc09412c6d61512ccb010ca93f3c8c.jpg']),
 dict(slug='observer', temas=['ocio', 'pasatiempos'], tipo='ilus', medio='The Observer', pais='Reino Unido', fecha='30 de agosto – 18 de octubre de 2026',
  titulo='Los pasatiempos ilustrados de «Observers needed»', acento='ilustrados',
  fuente='The Observer, del 30 de agosto; 6, 13, 20 y 27 de septiembre; 4 y 18 de octubre de 2026', creditos=[], tags=['ilustración','pasatiempos','medios internacionales'],
  texto=['Las llamativas y artísticas páginas de la sección semanal de pasatiempos en The Observer están siempre entre nuestras favoritas del fin de semana.',
         '«Observers needed» incluye retos divertidos para toda la familia con una gran ilustración en sus páginas centrales en las que hay que encontrar diversos personajillos desplegados por el dibujo. En el último par de meses nos hemos ido de acampada, buceado entre pulpos, hemos ido de picnic con ositos o hemos viajado a una ciudad tematizada con sudokus.'],
  imgs=['d45665cf3bf8a089b877c8659c6b1f92/e00400f802d09bd6-18/s2048x3072/7be4cfc1dad9659582edb25ba488264d5e446f79.jpg',
        '21eb365f319f4326f926bd11c939aa/e00400f802d09bd6-df/s2048x3072/edf37f1c61494ea493f8ec8fef91a57d7cb7d05c.jpg',
        '1f3eabd3264c9c0b76ae2517d03495e4/e00400f802d09bd6-21/s1280x1920/f03f51eeedb7016ea039e3a46cbb09861ef45c29.jpg',
        '07e287c83f54a12359734fb8b3f65d60/e00400f802d09bd6-5a/s1280x1920/40a02a1dd42228066ebca1d6d1c2475963a29cc0.jpg',
        'c2ce7a97ed030a001c2a46b00d1b10a6/e00400f802d09bd6-cd/s1280x1920/ddc4d957f90d18396ebf0a5dea6321dcda81fa36.jpg',
        '5a4bcbd70f852680b6753803b6bc09a4/e00400f802d09bd6-48/s1280x1920/a75496d867593b627272a6fd282435760dfdb5cc.jpg',
        'a9504be8b5a8b0b2e1babde46e9ece33/e00400f802d09bd6-0f/s1280x1920/5b53505cbe531942aaf7f3c57e746cea66fea8ce.jpg',
        'fe0ddfab587e9326454b523560387f3c/e00400f802d09bd6-79/s1280x1920/3dc92013063b1eae87078e6a419006e447b41d88.jpg',
        '47025ceda7c6657bc8d2c9d4a7fece30/e00400f802d09bd6-fd/s1280x1920/233f5378b7ba59b193e7af0b07480ba9d0e5b3fd.jpg']),
 dict(slug='economist', temas=['geopolítica', 'economía'], tipo='graf', medio='The Economist', pais='Reino Unido', fecha='12 de septiembre – 17 de octubre de 2026',
  titulo='Seis semanas de minigráficos y minimapas', acento='minigráficos',
  fuente='The Economist vol. 460 #9.516 - vol. 461 #9.521, del 12, 19 y 26 de septiembre; 3, 10 y 17 de octubre de 2026', creditos=[], tags=['gráficos','mapas','geopolítica','medios internacionales'],
  texto=['Pocas cosas hay que nos gusten tanto como los minigráficos y minimapas con los que cada semana The Economist compacta la actualidad para contextualizar sus densos y profundos reportajes sobre los más diversos temas.',
         'En la oleada de los últimos siete números encontramos trabajos sobre las guerras en Ucrania o Irán, los poderes económicos y militares del tablero geopolítico, la inteligencia artificial, la tasas de obesidad o el armamento de los drones, por poner algunos ejemplos.'],
  extra='« Recopilación anterior (agosto y septiembre)',
  imgs=['1cca87a25ea2e74463f11df61a404519/7302b4dec07e85a6-f5/s1280x1920/5b35b7bbcc9a36f269ace91534ef2739a4e66c8d.png',
        '56abd7ba94e1a853892b852b5b1b685d/7302b4dec07e85a6-99/s1280x1920/937430732e3f52dc08f420e6300041904d89a2e6.png',
        '05e0ff634de1bfe4ea890b1610862913/7302b4dec07e85a6-e7/s1280x1920/58cb1d691c72df50e2a5b085284f79663f1ee4fb.png',
        '729a98367018e3aca6122c62d9da4716/7302b4dec07e85a6-91/s1280x1920/3e45f1ad13fa13ddf6711d5a0ad1dc80dd7536ac.png']),
 dict(slug='pizza', temas=['gastronomía'], tipo='info', medio='The Boston Globe', pais='Estados Unidos', fecha='7 de octubre de 2026',
  titulo='Guía ilustrada de la pizza americana', acento='pizza',
  fuente='The Boston Globe, del 7 de octubre de 2026', creditos=['Melcher Oosterman','Luis G. Rendon','Elizabeth Bomze'], tags=['infografía','gastronomía','ilustración','medios internacionales'],
  texto=['Vamos a dar carpetazo a la semana dándonos un homenaje con el homenaje que le hizo hace unos días la sección gastronómica del Boston Globe a la pizza: un alimento muy americano y mucho americano según ellos (dicen que Ronald Reagan declaró octubre como el “mes de la pizza” en 1984 y de ahí la justificación a este opíparo especial).',
         'Aparte de una pizzística ilustración de portada de Melcher Oosterman, el reportaje contiene los 12 bocados esenciales por la ciudad y una infografía de Luis G. Rendon y Elizabeth Bomze que sirve de guía básica sobre el amante norteamericano de la pizza ideal, con tipos de pizzas, tamaños, masas y bordes.'],
  imgs=['f8c5b539d68801d029de510e9e0cac9d/a9aec96b22ed4747-26/s2048x3072/8c314d152908f71319d9455520387cb70d54dae9.jpg',
        '7ba128bb48781d559c5b602d35fae746/a9aec96b22ed4747-6d/s2048x3072/619ce67679a3a1d25942f82f8922de63969c0138.jpg',
        '61ee328faa4188b9f3f00dc3b334a709/a9aec96b22ed4747-12/s2048x3072/641ecb936b086ab2f4266a15999f5ae820cfafd7.jpg',
        'bbe7c0eccfe58f7dafdc9d825745631a/a9aec96b22ed4747-d0/s1280x1920/f3fcaf93fa15fc9d4c4b1a9509d2e3d32b6b7fce.jpg']),
 dict(slug='nobel', temas=['ciencia', 'premios Nobel'], tipo='info', medio='La Razón (México)', pais='México', fecha='6 – 8 de octubre de 2026',
  titulo='Los Nobel científicos, en infografía', acento='Nobel',
  fuente='La Razón (México), del 6 al 8 de octubre de 2026', creditos=['Armando Armenta','Julio Loyola','Roberto Alvarado'], tags=['infografía','ciencia','nobel','medios internacionales'],
  texto=['Los premios Nobel de este año ya se han anunciado y en el diario mexicano La Razón siguen con su tradición de dedicar amplias infografías a los ganadores de las categorías científicas.',
         'En concreto, le han dedicado infografías a los ganadores del Nobel de Medicina por su técnica optogenética, al de Física por sus hallazgos con los neutrinos y a los de Química, por sus descubrimientos sobre los efectos no lineales en la síntesis orgánica asimétrica. Son trabajos de Armando Armenta, Julio Loyola y Roberto Alvarado.'],
  imgs=['94a4148f19d00aae057d05648da9129b/b61ba2d1d5d93a7d-7b/s1280x1920/9db7f5a9603f595c8fb5b13ce8f64f70ac97d016.png',
        'bd4dd9471fbf4924c0a747e32ec8f78e/b61ba2d1d5d93a7d-b6/s1280x1920/ac3c173275383681698ac7cdbd649e5c90cadd27.png',
        'd434b85b1b05f741d48e5654e81b0e79/b61ba2d1d5d93a7d-97/s1280x1920/b39b21d2f46e5eaaf9285eeedebe418335ed5503.png']),
 dict(slug='cis', temas=['política', 'elecciones', 'vivienda'], tipo='graf', medio='El País', pais='España', fecha='11 de octubre de 2026',
  titulo='Qué preocupa a los votantes de cada partido', acento='preocupa',
  fuente='El País, del 11 de octubre de 2026', creditos=['Daniele Grasso','Yolanda Clemente'], tags=['elecciones 29-N','encuestas','vivienda','datos'],
  especial='Elecciones 29-N',
  texto=['Tambores de elecciones marcan el camino hasta el 29 de noviembre. Eso significa tiempo de campaña electoral y también de encuestas. Me parece un buen punto de partida el de El País, comenzando por el CIS y cómo la preocupación por la vivienda se ha disparado en los últimos dos años.',
         'Esta visual página de Daniele Grasso y Yolanda Clemente analiza la evolución de las principales preocupaciones de los españoles: vivienda, inmigración, economía y problemas políticos tras 75 barómetros del CIS, con datos por distribución de edad o intención de voto. El trabajo cuenta también <a href="https://elpais.com/espana/elecciones-generales/2026-10-11/vivienda-inmigracion-o-gobierno-que-preocupa-mas-a-los-votantes-de-cada-partido.html" target="_blank" rel="noopener">con una versión web</a>.'],
  imgs=['ecc4f5ce19ed114d3cd95545ff3bf759/de2d9184085a3fef-5d/s1280x1920/45f6bbed7ff64ec88566e929ae4981f17445d48f.png']),
]

e = html.escape
EN = {'cis': {'titulo': "What worries each party's voters", 'acento': 'worries', 'fuente': 'El País, 11 October 2026', 'texto': ['Election drums are beating all the way to 29 November. That means campaign season and, with it, polls. El País seems a good starting point to me, beginning with the CIS and how concern about housing has soared over the last two years.', 'This visual page by Daniele Grasso and Yolanda Clemente analyses how Spaniards\' main concerns have evolved — housing, immigration, the economy and political problems — across 75 CIS barometers, with data by age group and voting intention. The piece also has <a href="https://elpais.com/espana/elecciones-generales/2026-10-11/vivienda-inmigracion-o-gobierno-que-preocupa-mas-a-los-votantes-de-cada-partido.html" target="_blank" rel="noopener">a web version</a>.']}, 'liberation': {'titulo': 'Libération goes anarchic for Perec', 'acento': 'anarchic', 'fuente': 'Libération, 16 October 2026', 'texto': ['On the occasion of a major exhibition at the Bibliothèque nationale de France devoted to the work of Georges Perec, Libération published another of its special editions, dedicated to the experimental literature of the celebrated writer and essayist.', 'It is a wild edition with a completely anarchic design: pieces that form letters, columns that follow no fixed course, photographs placed upside down… All of it a tribute to the experimentation with language, words and formal constraints that defines the French author. Another edition to keep.']}, 'pizza': {'titulo': 'An illustrated guide to American pizza', 'acento': 'pizza', 'fuente': 'The Boston Globe, 7 October 2026', 'texto': ["Let's close the week with a treat: the tribute the Boston Globe's food section paid to pizza a few days ago — a very American food, very American indeed according to them (they say Ronald Reagan declared October “pizza month” in 1984, hence the excuse for this lavish special).", "Besides a pizza-tastic cover illustration by Melcher Oosterman, the feature includes the 12 essential bites around the city and an infographic by Luis G. Rendon and Elizabeth Bomze that works as a basic guide to the American pizza lover's ideal pie, with types, sizes, doughs and crusts."]}, 'nobel': {'titulo': 'The science Nobels, in infographics', 'acento': 'Nobels', 'fuente': 'La Razón (Mexico), 6–8 October 2026', 'texto': ["This year's Nobel Prizes have been announced, and Mexican daily La Razón keeps up its tradition of devoting large infographics to the winners in the science categories.", 'Specifically, it covered the Medicine laureates for their optogenetic technique, the Physics laureates for their neutrino discoveries and the Chemistry laureates for their findings on nonlinear effects in asymmetric organic synthesis. The work is by Armando Armenta, Julio Loyola and Roberto Alvarado.']}, 'food101': {'titulo': 'Twelve chefs and a manual for eating the tricky stuff', 'acento': 'manual', 'fuente': 'The New York Times Style Magazine, 17 April 2026', 'texto': ['How do you eat a lobster without making a mess? T Magazine, the New York Times style supplement, <a href="https://www.nytimes.com/interactive/2026/04/17/t-magazine/how-to-eat-mango-oyster.html?unlocked_article_code=1.-VA.T0Q2.bCkb7pVfP_FC&amp;smid=url-share" target="_blank" rel="noopener">has set out to help us in a big way</a>.', 'Twelve renowned chefs explain step by step how to eat complicated dishes such as lobster, oysters, crab, fufu, pho or roti, in a series of instructions illustrated by Ryuto Miyake.']}, 'nyt175': {'titulo': 'The New York Times turns 175', 'acento': '175', 'fuente': 'The New York Daily Times, 18 September 2026', 'texto': ['Last week The New York Times turned 175 and, during these days, the paper has been publishing special pieces about its own history, collected <a href="https://www.nytimes.com/interactive/2026/us/175-nyt-anniversary.html" target="_blank" rel="noopener">on a dedicated site</a>.', 'In print, the celebration brought a reproduction of the first edition of The New York Daily Times from 18 September 1851, a look back at the ads that marked its history and even a crossword quiz for readers.']}}
FICHA_MEDIO = {'El País': 'ficha-medio-el-pais.html', 'The New York Times': 'ficha-medio-nyt.html', 'Libération': 'ficha-medio-liberation.html'}
from medios_assets import logo as m_logo, avatar as m_avatar, avatar_barra as m_avbar
FICHA_AUTOR = {'Daniele Grasso': 'ficha-autor-daniele-grasso.html'}

CSS = """
:root{--paper:#ECE7DC;--ink:#16140F;--accent:#D1006F;--yellow:#FFD400;--muted:#5E5A50}
*{box-sizing:border-box}
body{margin:0;background:var(--paper);color:var(--ink);font-family:'Archivo',sans-serif}
a{color:var(--ink);text-decoration:none}
a:hover{color:var(--accent)}
.page{overflow:hidden}
.wrap{max-width:1360px;margin:0 auto;padding:0 24px}
.soft{font-family:'Fraunces',serif;font-style:italic;font-weight:900;font-variation-settings:'SOFT' 100,'WONK' 1,'opsz' 144}
.caps{font-size:13px;font-weight:800;letter-spacing:2px;text-transform:uppercase}
.k{color:var(--ink)}
.m{color:var(--accent);mix-blend-mode:multiply}
.head{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:12px 24px;padding:14px 24px;border-bottom:2px solid var(--ink)}
.brand{font-size:72px;line-height:.85;letter-spacing:0}
.brand span{color:var(--accent)}
.head nav{display:flex;flex-wrap:wrap;gap:6px 20px;align-items:center;font-size:13px;font-weight:600;letter-spacing:1.5px;text-transform:uppercase}
.btn-ink{background:var(--ink);color:var(--paper);padding:12px 16px;min-height:44px;display:inline-flex;align-items:center}
.btn-ink:hover{color:var(--yellow)}
.crumbs{padding:22px 0;display:flex;flex-wrap:wrap;gap:8px;align-items:center}
.crumbs i{font-style:normal;color:var(--accent)}
.chip-esp{background:var(--ink);color:var(--yellow);padding:6px 10px}
.chip-esp:hover{color:#fff}
.title{display:flex;flex-wrap:wrap;align-items:flex-end;justify-content:space-between;gap:24px;padding:16px 0 52px}
.title h1{margin:0;flex:1 1 680px;font-size:clamp(52px,7.4vw,120px);line-height:.9;letter-spacing:-.03em}
.title h1 em{color:var(--accent)}
.title .big-ico{width:150px;height:150px;flex-shrink:0}
.layout{display:grid;grid-template-columns:repeat(12,minmax(0,1fr));column-gap:44px;padding-bottom:72px;border-bottom:2px solid var(--ink)}
.visual{grid-column:1/9;display:flex;flex-direction:column;gap:40px}
.aside{grid-column:9/13;display:flex;flex-direction:column;gap:32px}
.layout.single .visual{grid-column:1/13}
.layout.single .aside{grid-column:1/13;display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,340px),1fr));align-items:start;gap:40px;margin-top:56px}
.shot{position:relative;display:block;width:100%;padding:0;border:0;font:inherit;color:inherit;text-align:left;cursor:zoom-in;background:#fff radial-gradient(#16140F 1.1px,transparent 1.3px) 0 0/7px 7px}
.shot img{display:block;width:100%;height:auto;background:#fff}
.shot .zoom{position:absolute;right:14px;bottom:14px;background:var(--ink);color:var(--paper);font-size:12px;font-weight:800;letter-spacing:1.5px;text-transform:uppercase;padding:8px 10px;opacity:0;transition:opacity .2s}
.shot:hover .zoom,.shot:focus-visible .zoom{opacity:1}
.main-sheet{position:relative;background:#fff;padding:14px;box-shadow:12px 12px 0 var(--ink);transform:rotate(-1deg)}
.layout.single .main-sheet{transform:none;max-width:1100px;margin:0 auto;width:100%}
.main-sheet .shot{min-height:360px}
.tape{position:absolute;top:-14px;left:50%;width:110px;height:28px;margin-left:-55px;background:rgba(255,212,0,.72);transform:rotate(-4deg);z-index:2}
.sheet-head{display:flex;justify-content:space-between;align-items:baseline;border-top:2px solid var(--ink);padding-top:12px;margin-bottom:14px}
.contact{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px}
.contact.c2{grid-template-columns:repeat(2,minmax(0,1fr))}
.frame{background:#fff;padding:8px;box-shadow:5px 5px 0 var(--ink);transition:transform .2s,box-shadow .2s}
.frame:hover{box-shadow:5px 5px 0 var(--accent);transform:translateY(-3px)}
.frame .shot{height:260px;overflow:hidden}
.contact.c2 .frame .shot{height:380px}
.frame .shot img{height:100%;object-fit:cover;object-position:top}
.frame .n{display:block;padding-top:6px;font-size:12px;font-weight:800;letter-spacing:1px}
.ficha{position:relative;background:#fff;padding:28px 24px 24px;box-shadow:8px 8px 0 var(--ink);transform:rotate(.8deg);display:flex;flex-direction:column;gap:18px}
.logo-slot{border:2px dashed var(--ink);height:76px;display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:700;color:var(--muted)}
.m-id{display:flex;align-items:center;gap:12px;transition:transform .2s}
.m-id:hover{transform:translateY(-2px)}
.m-id .logo-slot{flex:1;min-width:0}
.m-id{justify-content:center;padding:4px 0 10px;border-bottom:1px dashed #CFC8B8}
.m-logo{display:block;max-width:100%;max-height:64px;width:auto;height:auto;object-fit:contain;object-position:center;margin:0 auto}
.m-id:hover .logo-slot{border-color:var(--accent);color:var(--accent)}
.m-av{width:76px;height:76px;flex-shrink:0;outline:1px dashed #B9B2A3;display:flex;align-items:center;justify-content:center;font-size:11px;font-weight:700;color:var(--muted)}
.m-av img{width:100%;height:100%;object-fit:contain;display:block}
.ficha dl{margin:0;display:grid;grid-template-columns:92px minmax(0,1fr);gap:10px 12px;font-size:15px}
.ficha dt{font-weight:800;text-transform:uppercase;font-size:12px;letter-spacing:1.5px;padding-top:2px}
.ficha dd{margin:0}
.ficha dd a{border-bottom:2px solid var(--accent);font-weight:700}
.ficha .credit{font-family:'Fraunces',serif;font-style:italic;font-weight:400;border-bottom-width:1px}
.tags{display:flex;flex-wrap:wrap;gap:8px}
.tags a{border:2px solid var(--ink);padding:8px 12px;font-size:13px;font-weight:700;min-height:40px;display:inline-flex;align-items:center}
.body{display:flex;flex-direction:column;gap:18px;font-family:'Fraunces',serif;font-size:21px;line-height:1.5;font-variation-settings:'opsz' 24}
.body p{margin:0}
.body p a{border-bottom:2px solid var(--accent);font-weight:700}
.body .cap{float:left;font-weight:900;font-size:92px;line-height:.8;padding:6px 10px 0 0;color:var(--accent)}
.fuente{font-family:'Archivo',sans-serif;font-size:16px;font-weight:800;line-height:1.4;background:var(--ink);color:var(--paper);padding:14px 18px;box-shadow:5px 5px 0 var(--accent)}
.fuente{display:flex;align-items:center;gap:16px}
.fuente p{margin:0;flex:1;min-width:0}
.f-av{flex-shrink:0;width:52px;height:52px;display:flex;align-items:center;justify-content:center;transition:transform .2s}
.f-av:hover{transform:scale(1.08)}
.f-av img{width:100%;height:100%;object-fit:contain}
.f-av-slot{width:100%;height:100%;outline:1px dashed #7A766C;display:flex;align-items:center;justify-content:center;font-size:9px;font-weight:700;color:#BDB7AA}
.fuente i{font-style:normal;color:var(--yellow);font-size:22px;margin-right:4px}
.dateline{display:flex;flex-wrap:wrap;align-items:center;gap:10px 24px;border-top:3px solid var(--ink);border-bottom:1px solid var(--ink);padding:14px 0;margin:-24px 0 48px}
.dl-m{font-size:clamp(30px,3.4vw,46px);line-height:1}
.dl-m i{font-style:normal;color:var(--accent)}
.dl-d{font-size:15px;font-weight:800;letter-spacing:2px;text-transform:uppercase;padding-left:24px;border-left:2px solid var(--ink)}
.dl-logo{margin-left:auto;border:2px dashed var(--ink);padding:10px 18px;font-size:12px;font-weight:700;color:var(--muted)}
.share{display:flex;flex-wrap:wrap;gap:8px}
.share a,.share button{background:var(--ink);color:var(--paper);padding:12px 14px;font-family:'Archivo',sans-serif;font-size:13px;font-weight:700;min-height:44px;border:0;cursor:pointer}
.share button{background:transparent;color:var(--ink);border:2px solid var(--ink)}
.support{background:var(--yellow);padding:22px;display:flex;flex-direction:column;gap:8px;transform:rotate(-1deg)}
.support:hover{color:var(--ink)}
.pn{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,380px),1fr));border-bottom:2px solid var(--ink)}
.pn a{padding:32px 24px 32px 0;display:flex;flex-direction:column;gap:8px}
.pn a+a{padding:32px 0 32px 24px;text-align:right;border-left:2px solid var(--ink)}
.pn .t{font-family:'Fraunces',serif;font-weight:700;font-size:30px;line-height:1.05}
.more{padding:72px 0 96px;display:flex;flex-direction:column;gap:44px}
.more h2{margin:0;font-family:'Fraunces',serif;font-weight:900;font-variation-settings:'SOFT' 100,'WONK' 1,'opsz' 144;font-size:clamp(48px,6vw,88px);line-height:.9}
.more h2 em{color:var(--accent)}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,280px),1fr));gap:44px}
.card{position:relative;background:#fff;padding:14px 14px 20px;box-shadow:8px 8px 0 var(--ink);display:flex;flex-direction:column;gap:10px;transition:transform .2s}
.card:hover{transform:translateY(-4px)}
.card .ph{height:280px;overflow:hidden;background:#DAD4C6 radial-gradient(#16140F 1.1px,transparent 1.3px) 0 0/7px 7px}
.card .ph img{width:100%;height:100%;object-fit:cover;object-position:top;display:block}
.card .ico{position:absolute;top:-46px;right:-24px;width:96px;height:96px;z-index:3}
.card .tt{font-family:'Fraunces',serif;font-weight:700;font-size:24px;line-height:1.05}
footer{background:var(--ink);color:var(--paper)}
.cmyk-bar{display:grid;grid-template-columns:repeat(8,1fr);height:18px}
.foot{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:center;gap:20px;padding:28px 24px 40px;font-size:14px}
.dclips{display:flex;flex-wrap:wrap;gap:56px 44px;justify-content:center;padding:30px 0 10px;background:repeating-linear-gradient(0deg,transparent 0 31px,rgba(22,20,15,.06) 31px 32px)}
.dclip{position:relative;width:min(100%,400px);background:#F6F2E6;padding:16px 16px 20px;filter:drop-shadow(5px 6px 0 rgba(22,20,15,.9))}
.dclip:nth-child(odd){transform:rotate(-2.5deg)}.dclip:nth-child(even){transform:rotate(2deg);margin-top:40px}
.dclip::before,.dclip::after{content:"";position:absolute;left:0;right:0;height:10px}
.dclip::before{top:-10px;background:conic-gradient(from -45deg at bottom,#F6F2E6 90deg,transparent 0) 0 0/16px 100%}
.dclip::after{bottom:-10px;background:conic-gradient(from 135deg at top,#F6F2E6 90deg,transparent 0) 0 0/16px 100%}
.dclip .pc{position:absolute;top:-30px;left:26px;width:24px;height:64px;z-index:3}
.dclip .shot{min-height:260px;background:#F6F2E6}
.dsec{display:inline-block;font-family:'Fraunces',serif;font-style:italic;font-weight:900;font-size:22px;color:var(--accent);margin-bottom:6px}

@media (max-width:860px){
.layout{display:flex;flex-direction:column;gap:48px}
.main-sheet,.ficha,.support{transform:none}
.contact{grid-template-columns:repeat(2,minmax(0,1fr))}
.frame .shot,.contact.c2 .frame .shot{height:200px}
.title .big-ico{width:96px;height:96px}
.brand{font-size:56px}
.pn a+a{border-left:0;border-top:2px solid var(--ink);padding-left:0}
}
"""

def page(p, prev, nxt, others):
    tipo_name = ICONS[p['tipo']][0]
    imgs = [T + u for u in p['imgs']]
    n = len(imgs)
    title = e(p['titulo']).replace(e(p['acento']), f"<em>{e(p['acento'])}</em>", 1)
    pen = EN.get(p['slug'])
    title_en = e(pen['titulo']).replace(e(pen['acento']), f"<em>{e(pen['acento'])}</em>", 1) if pen else title
    tit_en = lambda o: EN[o['slug']]['titulo'] if o['slug'] in EN else o['titulo']
    tipo_en = TIPOS_EN[p['tipo']]
    alt = lambda i: e(f"{tipo_name} de {p['medio']}, imagen {i+1} de {n}")
    main = (f'<div class="main-sheet"><span class="tape" aria-hidden="true"></span>'
            f'<button type="button" class="shot" data-lb="0" aria-label="Ampliar imagen 1 de {n}">'
            f'<img src="{imgs[0]}" alt="{alt(0)}" onerror="this.remove()"><span class="zoom" data-en="Enlarge »">Ampliar »</span></button></div>')
    contact = ''
    if n > 1:
        cls = 'contact c2' if n <= 4 else 'contact'
        frames = ''.join(
            f'<div class="frame"><button type="button" class="shot" data-lb="{i}" aria-label="Ampliar imagen {i+1} de {n}">'
            f'<img loading="lazy" src="{u}" alt="{alt(i)}" onerror="this.remove()"><span class="zoom" data-en="Enlarge »">Ampliar »</span></button>'
            f'<span class="n">{i+1} / {n} <span style="color:var(--accent)">▸</span></span></div>'
            for i, u in enumerate(imgs) if i > 0)
        contact = (f'<div><div class="sheet-head"><span class="caps"{en(f"All images · {n}")}>Todas las imágenes · {n}</span>'
                   f'<span style="font-size:13px;font-weight:600"{en("Click to enlarge »")}>Pulsa para ampliar »</span></div><div class="{cls}">{frames}</div></div>')
    if p.get('deta'):
        main = '<div class="dclips">' + ''.join(f'<div class="dclip"><svg class=\"pc\" viewBox=\"0 0 22 58\" aria-hidden=\"true\"><path d=\"M6 4 V42 a5 5 0 0 0 10 0 V10 a3.5 3.5 0 0 0 -7 0 V40\" fill=\"none\" stroke=\"#7A766C\" stroke-width=\"2.4\" stroke-linecap=\"round\"/></svg><button type="button" class="shot" data-lb="{i}" aria-label="Ampliar recorte {i+1} de {n}"><img src="{u}" alt="{alt(i)}" onerror="this.remove()"><span class="zoom" data-en="Enlarge »">Ampliar »</span></button></div>' for i, u in enumerate(imgs)) + '</div>'
        contact = ''
    creditos = ''
    if p['creditos']:
        creditos = ('<dt data-en="Credits">Créditos</dt><dd>' + ', '.join(f'<a class="credit" href="{FICHA_AUTOR.get(c, "#")}">{e(c)}</a>' for c in p['creditos']) + '</dd>')
    body = []
    for i, t in enumerate(p['texto']):
        te = pen['texto'][i] if pen else None
        if i == 0:
            body.append(f'<p class="only-es"><span class="cap">{t[0]}</span>{t[1:]}</p>')
            if te:
                body.append(f'<p class="only-en"><span class="cap">{te[0]}</span>{te[1:]}</p>')
        else:
            body.append(f'<p class="only-es">{t}</p>' + (f'<p class="only-en">{te}</p>' if te else ''))
    if not pen:
        body = [b.replace('class="only-es"', '') for b in body]
    extra = f'<p><a href="#">{e(p["extra"])}</a></p>' if p.get('extra') else ''
    fuente = (f'<div class="fuente"><p><i>»</i> <span{en(pen["fuente"] if pen else fecha_en(p["fuente"]))}>{e(p["fuente"])}</span></p>'
              + (f'<a class="f-av" href="{FICHA_MEDIO.get(p["medio"], "#")}" aria-label="Ficha de {e(p["medio"])}"><img src="{m_avbar(p["medio"])}" alt=""></a>' if m_avatar(p['medio']) else '') + '</div>')
    esp = f'<i>»</i><a class="chip-esp" href="#"{en("Special: " + p["especial"].replace("Elecciones", "Election"))}>Especial {e(p["especial"])}</a>' if p.get('especial') else ''
    cards = ''.join(
        f'<a href="post-{o["slug"]}.html" class="card"><span class="tape" aria-hidden="true"></span>{icon(o["tipo"], "ico")}'
        f'<div class="ph"><img loading="lazy" src="{T + o["imgs"][0]}" alt="" onerror="this.remove()"></div>'
        f'<span class="caps">» {e(o["medio"])}</span><span class="tt"{en(tit_en(o))}>{e(o["titulo"])}</span></a>'
        for o in others)
    lb_list = json.dumps([{'src': u, 'cap': f"{p['medio']} · imagen {i+1} de {n}"} for i, u in enumerate(imgs)], ensure_ascii=False)
    return f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(p['titulo'])} · inconsolata» (maqueta)</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,400..900&family=Fraunces:ital,opsz,wght,SOFT,WONK@0,9..144,100..900,0..100,0..1;1,9..144,100..900,0..100,0..1&display=swap">
<style>{CSS}{HEAD_CSS}{MINI_CSS}{TEMAS_CSS}{I18N_CSS}{LEGACY_CSS}{LB_CSS}</style>
</head>
<body>
<div class="page">
{head_interior()}
<main class="wrap">
<div style="padding-top:20px">{LEGACY}</div>
<div class="crumbs caps"><a href="inconsolata-portada.html"{en('Home')}>Portada</a><i>»</i><a href="#"{'' if p.get('deta') else en(tipo_en)}>{'detallitos' if p.get('deta') else e(tipo_name)}</a><i>»</i><a href="{FICHA_MEDIO.get(p['medio'], '#')}">{e(p['medio'])}</a>{esp}</div>
<section class="title"><h1 class="soft"{en(title_en)}>{title}</h1>{icon(p['tipo'], 'big-ico')}</section>
<section class="layout{' single' if (n == 1 or p.get('deta')) else ''}">
<div class="visual">{main}{contact}</div>
<aside class="aside">
<div class="ficha"><span class="tape" aria-hidden="true"></span><span class="caps"{en('Details »')}>Ficha »</span>
{(f'<a class="m-id" href="{FICHA_MEDIO.get(p["medio"], "#")}" aria-label="Ficha de {e(p["medio"])}"><img class="m-logo" src="{m_logo(p["medio"], 500)}" alt="Logo de {e(p["medio"])}" onerror="this.parentNode.remove()"></a>') if m_logo(p['medio']) else ''}
<dl><dt{en('Outlet')}>Medio</dt><dd><a href="{FICHA_MEDIO.get(p['medio'], '#')}">{e(p['medio'])}</a> · <span{en(PAISES_EN.get(p['pais'], p['pais']))}>{e(p['pais'])}</span></dd><dt{en('Date')}>Fecha</dt><dd{en(fecha_en(p['fecha']))}>{e(p['fecha'])}</dd><dt{en('Type')}>Tipo</dt><dd{en(tipo_en)}>{e(tipo_name)}</dd>{creditos}</dl>
{temas_html(p.get('temas'))}
</div>
<div class="body">{''.join(body)}{extra}{fuente}</div>
<div style="display:flex;flex-direction:column;gap:10px"><span class="caps"{en('Share')}>Compartir</span>
<div class="share"><a href="#">Bluesky</a><a href="#">X</a><a href="#">Reblog</a><button type="button"{en('Copy link')}>Copiar enlace</button></div></div>
<a href="https://buymeacoffee.com/saulcastillo" class="support"><span class="soft" style="font-size:30px;line-height:1"{en('Like what I do?')}>¿Te gusta lo que hago?</span><span style="font-size:15px;line-height:1.4"{en('If you want to help, you can chip in with a contribution.')}>Si quieres ayudarme, puedes hacerlo con una aportación.</span><span class="caps"{en('Support us »')}>Apóyanos »</span></a>
</aside>
</section>
<nav class="pn" aria-label="Posts anterior y siguiente">
<a href="post-{prev['slug']}.html"><span class="caps"{en('« Previous')}>« Anterior</span><span class="t"{en(tit_en(prev))}>{e(prev['titulo'])}</span></a>
<a href="post-{nxt['slug']}.html"><span class="caps"{en('Next »')}>Siguiente »</span><span class="t"{en(tit_en(nxt))}>{e(nxt['titulo'])}</span></a>
</nav>
<section class="more"><h2{en('keep <em class="soft">looking</em>')}>sigue <em class="soft">mirando</em></h2><div class="cards">{cards}</div></section>
</main>
<footer>
<div class="cmyk-bar" aria-hidden="true"><span style="background:#00A0DC"></span><span style="background:#66C6EA"></span><span style="background:#E5007E"></span><span style="background:#EF66B2"></span><span style="background:#FFD400"></span><span style="background:#FFE566"></span><span style="background:#16140F"></span><span style="background:#7A766C"></span></div>
<div class="wrap foot"><span class="soft" style="font-size:56px;line-height:1">inc<span style="color:#D1006F">»</span></span><span>© inconsolata» 2011–2026 · un blog de Saúl Castillo</span></div>
</footer>
</div>
{LB_HTML}
<script>{LB_JS}
initLB({lb_list});
</script>
{MINI_JS}
{I18N_JS}
</body>
</html>
"""

def main():
  for i, p in enumerate(POSTS):
      prev = POSTS[i - 1]
      nxt = POSTS[(i + 1) % len(POSTS)]
      others = [POSTS[(i + k) % len(POSTS)] for k in (2, 3, 4)]
      with open(os.path.join(OUT, f'post-{p["slug"]}.html'), 'w') as f:
          f.write(page(p, prev, nxt, others))
  print('ok', len(POSTS))

if __name__ == '__main__':
    main()
