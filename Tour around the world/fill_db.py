import asyncio
from datetime import datetime
from database.engine import session_maker
from database.models import Tour


async def fill_db():
    tours = [
        Tour(
            in_date=datetime(2024, 12, 15),
            out_date=datetime(2024, 12, 25),
            count_people=2,
            country="Франция",
            city="Париж",
            price=120000,
            description="это город, который не просто очаровывает," 
            " а пленяет своим неповторимым шармом."
            " Он сочетает в себе вековую историю и современный ритм," 
            " роскошь и непринужденность, делая каждый день незабываемым. ",
            seasons="Зима",
            tour_type="Экскурсионный",
            image="https://ru.wikivoyage.org/wiki/%D0%9F%D0%B0%D1%80%D0%B8%D0%B6",
            rating=2.99,
        ),

        Tour(
            in_date=datetime(2024, 7, 10),
            out_date=datetime(2024, 7, 20),
            count_people=4,
            country="Испания",
            city="Барселона",
            price=185000,
            description="Пляжный отдых на побережье Коста Брава. Барселона динамичный и захватывающий город," 
            " который идеально подходит для разнообразных туров." 
            " Он предлагает сочетание богатой истории, яркой культуры," 
            " захватывающей архитектуры и, конечно," 
            " пляжного отдыха на средиземноморском побережье.",
            seasons="Лето",
            tour_type="Пляжный",
            image="https://travelask.ru/spain/barcelona",
            rating=4.56
        ),

            Tour(
            in_date=datetime(2024, 2, 25),
            out_date=datetime(2024, 2, 28),
            count_people=1,
            country="Россия",
            city="Сочи",
            price=95000,
            description="это идеальное место для летнего отдыха," 
            " сочетающее мягкий субтропический климат, чистые пляжи," 
            " живописную природу и развитую инфраструктуру." 
            " Это прекрасный вариант для любителей активного отдыха," 
            " спокойного пляжного отдыха и культурных впечатлений.",
            seasons="Зима",
            tour_type="Пляжный",
            image="https://sochi.ru/press-sluzhba/novosti/65/201939/",
            rating=4.79
        ),

        Tour(
            in_date=datetime(2025, 9, 15),
            out_date=datetime(2025, 9, 22),
            count_people=1,
            country="Италия",
            city="Рим",
            price=120000,
            description= 'столица Италии, огромный многонациональный город,' 
            ' история которого насчитывает почти три тысячи лет.' 
            ' Его архитектура и произведения искусства оказали огромное влияние на мировую культуру.' 
            ' Развалины античного Форума и Колизея демонстрируют былое величие Римской империи.' 
            ' Ватикан, резиденция руководства Римско-католической церкви,' 
            ' пользуется огромной популярностью у туристов благодаря собору Святого Петра и многочисленным музеям.' 
            ' Среди них – Сикстинская капелла, где можно увидеть знаменитые фрески Микеланджело',
            seasons="Осень",
            tour_type="Экскурсионный",
            image="https://tripmydream.com/italy/rome/info",
            rating=5.00
        ),


        Tour(
            in_date=datetime(2025, 11, 10),
            out_date=datetime(2025, 11, 17),
            count_people=4,
            country="Египет",
            city="Гиза",
            price=90000,
            description="это место," 
            " где находится один из самых известных и впечатляющих комплексов памятников древности – пирамиды Гизы и Великий Сфинкс." 
            " Этот регион, расположенный к западу от Каира," 
            " привлекает туристов со всего мира," 
            " желающих прикоснуться к вечности и древней истории." 
            " Гиза – это не только пирамиды, но и богатая история," 
            " древние традиции и культурное наследие, которые можно изучить," 
            " посетив этот город.",
            seasons="Осень",
            tour_type="Пляжный",
            image="https://yestravel.ru/countries/africa/giza/",
            rating=4.78,
        ),


        Tour(
            in_date=datetime(2024, 2, 25),
            out_date=datetime(2024, 2, 28),
            count_people=2,
            country="Франция",
            city="Париж",
            price=150000,
            description="Париж имеет репутацию лучшего города для романтической поездки." 
            " Однако на самом деле посетители теряют голову от самого города." 
            " Великолепные здания из камня и кованого железа," 
            " тротуары, уютные кафе," 
            " извилистые берега Сены — почувствуйте себя как в кино." 
            " Однако очарование города не ограничивается внешним видом." 
            " Местная кухня славится бесконечным разнообразием." 
            " Сочный и сытный петух в вине, золотистые масляные круассаны…" 
            " Здесь стоит также попробовать блюда современной кухни фьюжн и оригинальные международные блюда."
            " (Поверьте, в этом городе делают потрясающий фалафель.)" 
            " А дух Парижа так и манит прогуливаться по переулкам," 
            " заглядывать в многочисленные музеи и исследовать лабиринты магазинов." 
            " Ну а вечером отправляйтесь на Марсово поле," 
            " чтобы насладиться видом сверкающей Эйфелевой башни.",
            seasons="Зима",
            tour_type="Экскурсионный",
            image="https://ru.wikivoyage.org/wiki/%D0%9F%D0%B0%D1%80%D0%B8%D0%B6",
            rating=3.47
        ),


        Tour(
            in_date=datetime(2025, 8, 5),
            out_date=datetime(2025, 8, 12),
            count_people=3,
            country="Мексика",
            city="Канкун",
            price=110000,
            description="Популярный пляжный курорт в Мексике," 
            " расположенный на полуострове Юкатан," 
            " известный своими белоснежными пляжами," 
            " бирюзовым морем и развитой инфраструктурой." 
            " Это идеальное место для любителей морского отдыха," 
            " а также для тех," 
            " кто интересуется историей и культурой майя.",
            seasons="Лето",
            tour_type="Пляжный",
            image="https://blog.ostrovok.ru/desyat-veshhej-kotorye-ne-stoit-delat-v-kankune/",
            rating=4.89
        ),


        Tour(
            in_date=datetime(2025, 3, 25),
            out_date=datetime(2025, 4, 1),
            count_people=1,
            country="Япония",
            city="Киото",
            price=220000,
            description="Это город в Японии," 
            " который известен своей богатой историей," 
            " богатым культурным наследием и множеством достопримечательностей." 
            " Он был столицей Японии более 1000 лет," 
            " и этот факт отражается в его архитектуре," 
            " храмах, садах и традициях",
            seasons="Весна",
            tour_type="Экскурсионный",
            image="https://experience.tripster.ru/experience/50037/",
            rating=1.20
        ),


        Tour(
            in_date=datetime(2025, 2, 20),
            out_date=datetime(2025, 2, 27),
            count_people=1,
            country="Бразилия",
            city="Рио-де-Жанейро",
            price=130000,
            description="Город контрастов и незабываемых впечатлений," 
            " где жизнь кипит, а пляжи," 
            " горы и океан создают незабываемую атмосферу." 
            " Главные достопримечательности включают статую Христа Искупителя," 
            " гору Сахарная Голова, знаменитые пляжи Копакабана и Ипанема," 
            " а также яркий карнавал.",
            seasons="Зима",
            tour_type="Пляжный",
            image="https://blog.global-guide.org/top-28-dostoprimechatelnost-v-rio-de-zhanejro-chto-posmotret-i-kuda-shodit",
            rating=3.25
        ),


        Tour(
            in_date=datetime(2025, 10, 1),
            out_date=datetime(2025, 10, 8),
            count_people=3,
            country="Индия",
            city="Агра",
            price=80000,
            description="Исторический город в северной Индии," 
            " известнясь Тадж-Махалом." 
            " Это один из самых посещаемых городов Индии," 
            " благодаря великолепному Тадж-Махалу и другим историческим памятникам." 
            " Город расположен на берегу реки Ямуны и был столицей империи Великих Моголов в 1527-1627 годах.",
            seasons="Осень",
            tour_type="Экскурсионный",
            image="https://experience.tripster.ru/articles/agra/",
            rating=5.00
        ),


        Tour(
            in_date=datetime(2025, 7, 20),
            out_date=datetime(2025, 7, 27),
            count_people=5,
            country="США",
            city="Нью-Йорк",
            price=180000,
            description="Это не просто город," 
            " а эпицентр мировой культуры, финансов и бизнеса," 
            " где каждый уголок дышит историей и энергией." 
            " Город, который никогда не спит," 
            " предлагает невероятное разнообразие достопримечательностей," 
            " от небоскребов до парков, от музеев до театров Бродвея.",
            seasons="Лето",
            tour_type="Пляжный",
            image="https://experience.tripster.ru/articles/new-york/",
            rating=4.89
        ),


        Tour(
            in_date=datetime(2025, 7, 15),
            out_date=datetime(2025, 7, 22),
            count_people=3,
            country="Греция",
            city="Санторини",
            price=170000,
            description="Уникальный греческий остров," 
            " знаменитый своими сказочными видами," 
            " белоснежными домами на крутых скалах," 
            " захватывающими закатами и разноцветными пляжами." 
            " Остров сформировался в результате извержения вулкана," 
            " что придает ему неповторимый ландшафт с вулканическим песком и скалами." 
            " Это место идеально подходит для романтического отдыха," 
            " наслаждения красотой природы и погружения в греческую культуру. ",
            seasons="Лето",
            tour_type="Пляжный",
            image="https://guide.planetofhotels.com/ru/blog/chto-posmotret-na-santorini",
            rating=5.00
        ),

        Tour(
        in_date=datetime(2025, 5, 10),
        out_date=datetime(2025, 5, 20),
        count_people=2,
        country="Греция",
        city="Афины",
        price=135000,
        description="Колыбель западной цивилизации, где античные памятники соседствуют с современной жизнью. "
        "Акрополь с Парфеноном, древняя Агора и храм Зевса Олимпийского переносят в эпоху философов и героев. "
        "Узкие улочки Плаки с тавернами и сувенирными лавками создают неповторимую атмосферу.",
        seasons="Весна",
        tour_type="Экскурсионный",
        image="https://www.tournet.ru/wp-content/uploads/athens-likavitos.jpg",
        rating=4.85
    ),

    Tour(
        in_date=datetime(2024, 8, 3),
        out_date=datetime(2024, 8, 14),
        count_people=3,
        country="Турция",
        city="Анталия",
        price=95000,
        description="Жемчужина турецкой Ривьеры с лазурными бухтами и золотистыми пляжами. "
        "Старый город Калеичи с османской архитектурой, водопады Дюден и древние города Перге и Аспендос. "
        "Идеально сочетает пляжный отдых с экскурсиями к античным памятникам.",
        seasons="Лето",
        tour_type="Пляжный",
        image="https://viasun.ru/blog/otdyh-v-antalii/",
        rating=4.75
    ),

    Tour(
        in_date=datetime(2025, 1, 15),
        out_date=datetime(2025, 1, 22),
        count_people=4,
        country="Таиланд",
        city="Пхукет",
        price=110000,
        description="Тропический рай с бирюзовыми водами и пальмовыми пляжами. "
        "Остров Джеймса Бонда, смотровая площадка на мысе Промтеп, шоу Фантазия и оживленная Патонг. "
        "Возможность заняться дайвингом, сноркелингом и отведать изыски тайской кухни.",
        seasons="Зима",
        tour_type="Пляжный",
        image="https://cdn2.tu-tu.ru/image/pagetree_node_data/6/18a13ec0de276bae69b5da8676ce3d45/",
        rating=4.92
    ),

    Tour(
        in_date=datetime(2024, 9, 12),
        out_date=datetime(2024, 9, 19),
        count_people=2,
        country="Чехия",
        city="Прага",
        price=105000,
        description="Город ста башен с волшебной архитектурой и средневековыми улочками. "
        "Карлов мост, Пражский Град, Астрономические часы и золотые крыши храмов создают сказочную атмосферу. "
        "Знаменитое чешское пиво и традиционная кухня дополняют впечатления.",
        seasons="Осень",
        tour_type="Экскурсионный",
        image="https://lifetour.pl/wp-content/uploads/2023/10/praga_ng-1.jpg",
        rating=4.78
    ),

    Tour(
        in_date=datetime(2025, 6, 5),
        out_date=datetime(2025, 6, 15),
        count_people=2,
        country="Мальдивы",
        city="Мале",
        price=290000,
        description="Райский архипелаг с бирюзовыми лагунами и коралловыми рифами. "
        "Вилы на воде, идеальные условия для дайвинга, спа-процедуры с видом на океан. "
        "Уединенный отдых в окружении нетронутой природы и кристально чистых вод.",
        seasons="Лето",
        tour_type="Пляжный",
        image="https://tour-platform.ru/destinations/maldives/south-male-atoll/",
        rating=4.97
    ),

    Tour(
        in_date=datetime(2024, 11, 20),
        out_date=datetime(2024, 11, 27),
        count_people=1,
        country="Венгрия",
        city="Будапешт",
        price=98000,
        description="Жемчужина Дуная с роскошными купальнями и неоготической архитектурой. "
        "Замок Буда, Рыбацкий бастион, здание Парламента и мосты через Дунай. "
        "Знаменитые термальные источники и изысканная венгерская кухня с гуляшом.",
        seasons="Осень",
        tour_type="Экскурсионный",
        image="https://experience.tripster.ru/articles/budapesht/",
        rating=4.63
    ),

    Tour(
        in_date=datetime(2025, 4, 15),
        out_date=datetime(2025, 4, 22),
        count_people=3,
        country="Нидерланды",
        city="Амстердам",
        price=125000,
        description="Город каналов и тюльпанов с уникальной атмосферой свободы. "
        "Прогулки на лодке по каналам, Рейксмузей, квартал Йордан и цветочный рынок. "
        "Велосипедные экскурсии вдоль старинных домов с остроконечными фасадами.",
        seasons="Весна",
        tour_type="Экскурсионный",
        image="https://experience.tripster.ru/articles/amsterdam/",
        rating=4.55
    ),

    Tour(
        in_date=datetime(2024, 12, 5),
        out_date=datetime(2024, 12, 12),
        count_people=4,
        country="Финляндия",
        city="Рованиеми",
        price=145000,
        description="Официальная резиденция Санта-Клауса за Полярным кругом. "
        "Сафари на хаски, ночь в стеклянном иглу, северное сияние и арктический зоопарк. "
        "Посещение деревни Санта-Клауса и ледяного отеля.",
        seasons="Зима",
        tour_type="Экскурсионный",
        image="https://guide.planetofhotels.com/ru/finlyandiya/rovaniemi",
        rating=4.88
    ),

    Tour(
        in_date=datetime(2025, 3, 10),
        out_date=datetime(2025, 3, 17),
        count_people=2,
        country="ОАЭ",
        city="Дубай",
        price=155000,
        description="Город будущего с небоскребами и искусственными островами. "
        "Бурдж-Халифа, пальма Джумейра, аквапарки и роскошные торговые центры. "
        "Пустынное сафари, катание на верблюдах и традиционные восточные базары.",
        seasons="Весна",
        tour_type="Экскурсионный",
        image="https://oboitd.ru/images/goods/big/20200214041003_Gorod_p2067.jpg",
        rating=4.68
    ),

    Tour(
        in_date=datetime(2024, 10, 15),
        out_date=datetime(2024, 10, 22),
        count_people=1,
        country="Австрия",
        city="Вена",
        price=128000,
        description="Имперская столица с дворцами Габсбургов и вальсами Штрауса. "
        "Шенбрунн, Бельведер, собор Святого Стефана и Венская опера. "
        "Знаменитые кофейни с яблочным штруделем и атмосфера музыкальной столицы Европы.",
        seasons="Осень",
        tour_type="Экскурсионный",
        image="https://experience.tripster.ru/articles/vena/",
        rating=4.82
    ),

    Tour(
        in_date=datetime(2025, 2, 10),
        out_date=datetime(2025, 2, 17),
        count_people=2,
        country="Вьетнам",
        city="Нячанг",
        price=85000,
        description="Курорт с семью километрами золотистых пляжей в бухте Нячанга. "
        "Остров обезьян, грязелечебница Тхап Ба, пагода Лонг Шон. "
        "Идеальное место для любителей дайвинга и морской кухни.",
        seasons="Зима",
        tour_type="Пляжный",
        image="https://guide.planetofhotels.com/ru/vetnam/nyachang",
        rating=4.71
    ),

    Tour(
        in_date=datetime(2025, 7, 1),
        out_date=datetime(2025, 7, 10),
        count_people=3,
        country="Хорватия",
        city="Дубровник",
        price=142000,
        description="Жемчужина Адриатики с крепостными стенами и старинными улочками. "
        "Съемочная площадка Игры престолов, канатная дорога на гору Срдж, остров Локрум. "
        "Кристально чистое море и средиземноморская кухня.",
        seasons="Лето",
        tour_type="Пляжный",
        image="https://ru.wikivoyage.org/wiki/%D0%94%D1%83%D0%B1%D1%80%D0%BE%D0%B2%D0%BD%D0%B8%D0%BA",
        rating=4.93
    ),

    Tour(
        in_date=datetime(2024, 6, 20),
        out_date=datetime(2024, 6, 30),
        count_people=4,
        country="Португалия",
        city="Лиссабон",
        price=132000,
        description="Город на семи холмах с желтыми трамваями и фаду. "
        "Башня Белен, монастырь Жеронимуш, замок Святого Георгия. "
        "Поездка в Синтру с ее сказочными дворцами и мыс Рока.",
        seasons="Лето",
        tour_type="Экскурсионный",
        image="https://experience.tripster.ru/experience/16125/",
        rating=4.59
    ),

    Tour(
        in_date=datetime(2025, 1, 5),
        out_date=datetime(2025, 1, 12),
        count_people=2,
        country="Индонезия",
        city="Бали",
        price=175000,
        description="Остров богов с рисовыми террасами и вулканическими пляжами. "
        "Храмы Улувату и Танах Лот, водопады Тегенунган, культурный центр Убуд. "
        "Серфинг в Куте и спа-ритуалы.",
        seasons="Зима",
        tour_type="Пляжный",
        image="https://cdn.mybalitrips.com/common/blog_mbt/Ulu%20guide/uluwatu_compressed.jpg",
        rating=4.94
    ),

    Tour(
        in_date=datetime(2024, 4, 10),
        out_date=datetime(2024, 4, 17),
        count_people=1,
        country="Германия",
        city="Берлин",
        price=115000,
        description="Современная столица с богатой историей и бурной культурной жизнью. "
        "Бранденбургские ворота, Рейхстаг, Берлинская стена и Музейный остров. "
        "Легендарные клубы и гастрономические фестивали.",
        seasons="Весна",
        tour_type="Экскурсионный",
        image="https://experience.tripster.ru/articles/berlin/",
        rating=4.49
    ),

    Tour(
        in_date=datetime(2025, 9, 5),
        out_date=datetime(2025, 9, 15),
        count_people=2,
        country="Швейцария",
        city="Интерлакен",
        price=195000,
        description="Сердце швейцарских Альп между озерами Тун и Бриенц. "
        "Юнгфрауйох - вершина Европы, водопады Труммельбах, парк Хардер Кульм. "
        "Поездки на горных поездах и дегустация шоколада.",
        seasons="Осень",
        tour_type="Экскурсионный",
        image="https://guide.planetofhotels.com/ru/shveycariya/interlaken",
        rating=4.87
    ),
    Tour(
        in_date=datetime(2024, 7, 25),
        out_date=datetime(2024, 8, 5),
        count_people=3,
        country="Кипр",
        city="Айя-Напа",
        price=105000,
        description="Молодежная столица Кипра с золотыми пляжами и бирюзовым морем. "
        "Мыс Греко, аквапарк WaterWorld, морские пещеры и ночные клубы. "
        "Экскурсии в старый город Фамагусту и монастырь Айя-Напы.",
        seasons="Лето",
        tour_type="Пляжный",
        image="https://kidpassage.com/publications/ayya-napa-v-iyune-otdyh-pogoda",
        rating=4.53
    ),

    Tour(
        in_date=datetime(2025, 5, 20),
        out_date=datetime(2025, 5, 27),
        count_people=2,
        country="Норвегия",
        city="Берген",
        price=168000,
        description="Ворота в царство фьордов с цветными домиками набережной Брюгген. "
        "Фломская железная дорога, фьорды Согне-фьорд и Хардангер-фьорд. "
        "Рыбный рынок и горные походы на гору Флойен.",
        seasons="Весна",
        tour_type="Экскурсионный",
        image="https://style.rbc.ru/impressions/5b2909aa9a79476ab42710c0",
        rating=4.79
    ),

    Tour(
        in_date=datetime(2024, 8, 20),
        out_date=datetime(2024, 8, 27),
        count_people=4,
        country="Болгария",
        city="Солнечный Берег",
        price=75000,
        description="Крупнейший черноморский курорт с песчаными пляжами протяженностью 8 км. "
        "Аквапарк Action, ночные клубы, старинный Несебр и мыс Калиакра. "
        "Идеальное сочетание цен и качества для пляжного отдыха.",
        seasons="Лето",
        tour_type="Пляжный",
        image="https://kidpassage.com/images/resorts/solnechny-bereg/gallery/38c3388d791d7d3282426ad3a9626e6b.jpg",
        rating=4.35
    ),

    Tour(
        in_date=datetime(2025, 10, 20),
        out_date=datetime(2025, 10, 27),
        count_people=2,
        country="Аргентина",
        city="Буэнос-Айрес",
        price=145000,
        description="Париж Южной Америки с танго и колониальной архитектурой. "
        "Район Ла Бока, кладбище Реколета, театр Колон и Пуэрто-Мадеро. "
        "Гаучо-шоу в пампасах и дегустация мальбека.",
        seasons="Осень",
        tour_type="Экскурсионный",
        image="https://experience.tripster.ru/articles/buenos-ajres/",
        rating=4.61
    ),

    Tour(
        in_date=datetime(2025, 12, 20),
        out_date=datetime(2025, 12, 30),
        count_people=3,
        country="Швеция",
        city="Стокгольм",
        price=152000,
        description="Столица на 14 островах с разноцветными домами Гамла Стана. "
        "Музей Васа, Скансен, ратуша и дворец Дроттнингхольм. "
        "Рождественские ярмарки и арктический ресторан с северным сиянием.",
        seasons="Зима",
        tour_type="Экскурсионный",
        image="https://cdn.tripster.ru/thumbs2/1e67af6a-4161-11ee-bb67-368e28cf9d68.1220x600.jpeg",
        rating=4.67
    ),

    Tour(
        in_date=datetime(2025, 1, 5),
        out_date=datetime(2025, 1, 12),
        count_people=2,
        country="Австрия",
        city="Инсбрук",
        price=185000,
        description="Столица зимних видов спорта с 9 крупными горнолыжными регионами. "
        "Олимпийские трассы, современные подъемники и традиционные альпийские хижины. "
        "Возможность катания на ледниках и посещения рождественских базаров.",
        seasons="Зима",
        tour_type="Горнолыжный",
        image="https://kolllak.livejournal.com/78821.html",
        rating=4.88
    ),

    Tour(
        in_date=datetime(2025, 2, 15),
        out_date=datetime(2025, 2, 22),
        count_people=4,
        country="Франция",
        city="Шамони",
        price=210000,
        description="Легендарный курорт у подножия Монблана с самым длинным спуском Валле Бланш (22 км). "
        "Ледниковое катание, фрирайд-зоны и трассы для всех уровней подготовки. "
        "Панорамные канатные дороги с видом на Альпы.",
        seasons="Зима",
        tour_type="Горнолыжный",
        image="https://www.pac.ru/guide/france/haute-savoie/mont-blanc/chamonix/",
        rating=4.92
    ),

    Tour(
        in_date=datetime(2024, 12, 20),
        out_date=datetime(2024, 12, 27),
        count_people=3,
        country="Швейцария",
        city="Церматт",
        price=245000,
        description="Эксклюзивный курорт у подножия Маттерхорна с автомобильным запретом. "
        "365 дней катания на леднике, 360 км трасс и самые высокогорные рестораны Европы. "
        "Традиционные шале и спа-комплексы класса люкс.",
        seasons="Зима",
        tour_type="Горнолыжный",
        image="https://houseville.villas/magazine/ru/how-to-spend-one-day-in-zermatt/",
        rating=4.95
    ),

    Tour(
        in_date=datetime(2025, 1, 10),
        out_date=datetime(2025, 1, 17),
        count_people=2,
        country="Италия",
        city="Кортина-д'Ампеццо",
        price=195000,
        description="Жемчужина Доломитовых Альп, место проведения Олимпиады-2026. "
        "120 км трасс в зоне Dolomiti Superski, ледяные водопады для альпинистов. "
        "Бутики высокой моды и аперитивы в стильных барах.",
        seasons="Зима",
        tour_type="Горнолыжный",
        image="https://ru.wikipedia.org/wiki/%D0%9A%D0%BE%D1%80%D1%82%D0%B8%D0%BD%D0%B0-%D0%B4%E2%80%99%D0%90%D0%BC%D0%BF%D0%B5%D1%86%D1%86%D0%BE",
        rating=4.85
    ),

    Tour(
        in_date=datetime(2025, 3, 1),
        out_date=datetime(2025, 3, 8),
        count_people=1,
        country="Япония",
        city="Нисэко",
        price=220000,
        description="Мекка для ценителей пухлого снега (Japow) на острове Хоккайдо. "
        "Ежегодно более 15 метров снега, зоны для фрирайда и термальные источники онсэн. "
        "Ночное катание и культура апрес-ски.",
        seasons="Зима",
        tour_type="Горнолыжный",
        image="https://www.quinta.ru/upload/iblock/c5f/4ldb4rfl4qzazbb9hki71rcssjvasil3/HiltonNisekoVillage_HR.jpg",
        rating=4.89
    ),

    Tour(
        in_date=datetime(2024, 11, 25),
        out_date=datetime(2024, 12, 2),
        count_people=4,
        country="Россия",
        city="Роза Хутор",
        price=135000,
        description="Современный курорт в Красной Поляне с олимпийской инфраструктурой. "
        "102 км трасс всех уровней сложности, сноупарки и хафпайп. "
        "Канатные дороги с панорамой Кавказских гор и термальные бассейны.",
        seasons="Зима",
        tour_type="Горнолыжный",
        image="https://estosadok.sutochno.ru/doc/images/galleries/180/gkrosa1.jpg",
        rating=4.75
    ),

    Tour(
        in_date=datetime(2025, 2, 1),
        out_date=datetime(2025, 2, 8),
        count_people=2,
        country="Канада",
        city="Уистлер",
        price=230000,
        description="Крупнейший горнолыжный курорт Северной Америки с 200+ трассами. "
        "Зона фрирайда для экспертов, хели-ски и снегоступы. "
        "Пешеходная деревня с ресторанами мировой кухни.",
        seasons="Зима",
        tour_type="Горнолыжный",
        image="https://www.airbnb.ru/whistler-canada/stays",
        rating=4.91
    ),

    Tour(
        in_date=datetime(2025, 1, 20),
        out_date=datetime(2025, 1, 27),
        count_people=3,
        country="Болгария",
        city="Банско",
        price=115000,
        description="Лучшее соотношение цены и качества на Балканах. "
        "75 км ухоженных трасс, современные подъемники и традиционные механы. "
        "Старинный город с объектами ЮНЕСКО и минеральными источниками.",
        seasons="Зима",
        tour_type="Горнолыжный",
        image="https://kidpassage.com/publications/bansko-v-fevrale-otdyh-pogoda",
        rating=4.42
    ),

    Tour(
        in_date=datetime(2025, 3, 10),
        out_date=datetime(2025, 3, 17),
        count_people=2,
        country="Андорра",
        city="Грандвалира",
        price=155000,
        description="Крупнейшая зона катания в Пиренеях с 210 км трасс. "
        "Дьюти-фри шопинг, аквапарк Caldea и катание на снегоходах. "
        "Солнечная погода и снег до поздней весны.",
        seasons="Зима",
        tour_type="Горнолыжный",
        image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS3mT7JR-uUHEhtXHbkaSvLgmSNxRAFBkoTJQ&s",
        rating=4.58
    ),

    Tour(
        in_date=datetime(2024, 12, 10),
        out_date=datetime(2024, 12, 17),
        count_people=1,
        country="Финляндия",
        city="Леви",
        price=142000,
        description="Лучший курорт Финляндии за Полярным кругом. "
        "Лапландская природа, сафари на хаски и ночи в стеклянных иглу. "
        "Ухоженные трассы, сноупарк и возможность увидеть северное сияние.",
        seasons="Зима",
        tour_type="Горнолыжный",
        image="https://break-sokos-levi-hotel.nochi.com/data/Photos/OriginalPhoto/15372/1537268/1537268662/Break-Sokos-Hotel-Levi-Exterior.JPEG",
        rating=4.63
    ),

    Tour(
        in_date=datetime(2025, 2, 20),
        out_date=datetime(2025, 2, 27),
        count_people=4,
        country="США",
        city="Аспен",
        price=255000,
        description="Элитный курорт Колорадо с четырьмя зонами катания. "
        "Трассы для чемпионов, глубочайший снег и роскошные отели. "
        "Апре-ски в стильных лаунжах и галереи современного искусства.",
        seasons="Зима",
        tour_type="Горнолыжный",
        image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTe2jS1ikzN4Q54lsXoWgbKCWKk8bYZfWS8wQ&s",
        rating=4.93
    ),

    Tour(
        in_date=datetime(2025, 1, 15),
        out_date=datetime(2025, 1, 22),
        count_people=2,
        country="Норвегия",
        city="Хемседал",
        price=198000,
        description="Скандинавская Мекка фрирайда с лучшими внетрассовыми спусками. "
        "Современные подъемники, сноупарк и 50 км освещенных трасс. "
        "Традиционные кафе с коричными булочками и каминами.",
        seasons="Зима",
        tour_type="Горнолыжный",
        image="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/2a/aa/37/b6/caption.jpg?w=1200&h=-1&s=1&cx=1920&cy=1080&chk=v1_f1f80a41f1a77dd54eec",
        rating=4.79
    )
    ]
    
    async with session_maker() as session:
        for tour in tours:
            session.add(tour)
        await session.commit()

if __name__ == "__main__":
    asyncio.run(fill_db())