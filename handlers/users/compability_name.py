from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.utils.markdown import hlink
from telegraph import Telegraph

from keyboards.inline.compatibility_kb import comp_ru, comp_en, back_compatibility_ru, back_compatibility_en, comp_es, \
    back_compatibility_es, comp_de, back_compatibility_de
from loader import dp
from states.states import Compatibility
from utils.db_api import quick_commands as qc


telegraph = Telegraph()


@dp.callback_query_handler(text="compatibility_name")
async def compatibility_name(call: types.CallbackQuery):
    await call.message.delete()
    user = await qc.get_user(id=int(call.from_user.id))
    referrals = await qc.select_referrals(id=call.from_user.id)
    x = 0
    for referral in referrals:
        x += 1
    if user.language == "ru":
        if x < 3:
            await call.message.answer(f"Для активации функции пригласите минимум 3 людей.\n"
                                      f"Ваша ссылка для приглашения: ")
            await call.message.answer(f"https://t.me/horo_server_temp_bot?start={call.from_user.id}",
                                      reply_markup=comp_ru)
        else:
            await call.message.answer(f"Введите имена: ваше и партнера\n"
                                      f"\n"
                                      f"<i>Например: Анастасия Дмитрий</i>\n"
                                      f"\n"
                                      f"Советуем вводить полные имена (например: <s>Настя</s> Анастасия).\n",
                                      reply_markup=back_compatibility_ru)
    if user.language == "en":
        if x < 3:
            await call.message.answer(f"To activate the function, invite at least 3 people.\n"
                                      f"Your invitation link: ")
            await call.message.answer(f"https://t.me/horo_server_temp_bot?start={call.from_user.id}",
                                      reply_markup=comp_en)
        else:
            await call.message.answer(f"Enter your partner's name\n", reply_markup=back_compatibility_en)
    if user.language == "es":
        if x < 3:
            await call.message.answer(f"Para activar la función, invite al menos a 3 personas.\n"
                                      f"Su enlace de invitación: ")
            await call.message.answer(f"https://t.me/horo_server_temp_bot?start={call.from_user.id}",
                                      reply_markup=comp_es)
        else:
            await call.message.answer(f"Ingrese el nombre de su socio\n", reply_markup=back_compatibility_es)
    if user.language == "de":
        if x < 3:
            await call.message.answer(f"Um die Funktion zu aktivieren, laden Sie mindestens 3 Personen ein.\n"
                                      f"Ihr Einladungslink: ")
            await call.message.answer(f"https://t.me/horo_server_temp_bot?start={call.from_user.id}",
                                      reply_markup=comp_de)
        else:
            await call.message.answer(f"Geben Sie den Namen Ihres Partners ein\n", reply_markup=back_compatibility_de)
    await Compatibility.name.set()


@dp.message_handler(state=Compatibility.name)
async def birthday(message: types.Message, state: FSMContext):
    names = message.text
    user = await qc.get_user(id=int(message.from_user.id))
    if user.language == "ru":
        names_split = names.split()
        x = 0
        for i in names_split:
            x += 1
        if x == 2:
            summ1 = 0
            summ2 = 0
            for y in names_split[0]:
                for z in y:
                    if z in ("а", "и", "с", "ъ", "А", "И", "С", "Ъ"):
                        summ1 += 1
                    if z in ("б", "й", "т", "ы", "Б", "Й", "Т", "Ы"):
                        summ1 += 2
                    if z in ("в", "к", "у", "ь", "В", "К", "У", "Ь"):
                        summ1 += 3
                    if z in ("г", "л", "ф", "э", "Г", "Л", "Ф", "Э"):
                        summ1 += 4
                    if z in ("д", "м", "х", "ю", "Д", "М", "Х", "Ю"):
                        summ1 += 5
                    if z in ("е", "н", "ц", "я", "Е", "Н", "Ц", "Я"):
                        summ1 += 6
                    if z in ("ё", "о", "ч", "Ё", "О", "Ч"):
                        summ1 += 7
                    if z in ("ж", "п", "ш", "Ж", "П", "Ш"):
                        summ1 += 8
                    if z in ("з", "р", "щ", "З", "Р", "Щ"):
                        summ1 += 9
            for y in names_split[1]:
                for z in y:
                    if z in ("а", "и", "с", "ъ", "А", "И", "С", "Ъ"):
                        summ2 += 1
                    if z in ("б", "й", "т", "ы", "Б", "Й", "Т", "Ы"):
                        summ2 += 2
                    if z in ("в", "к", "у", "ь", "В", "К", "У", "Ь"):
                        summ2 += 3
                    if z in ("г", "л", "ф", "э", "Г", "Л", "Ф", "Э"):
                        summ2 += 4
                    if z in ("д", "м", "х", "ю", "Д", "М", "Х", "Ю"):
                        summ2 += 5
                    if z in ("е", "н", "ц", "я", "Е", "Н", "Ц", "Я"):
                        summ2 += 6
                    if z in ("ё", "о", "ч", "Ё", "О", "Ч"):
                        summ2 += 7
                    if z in ("ж", "п", "ш", "Ж", "П", "Ш"):
                        summ2 += 8
                    if z in ("з", "р", "щ", "З", "Р", "Щ"):
                        summ2 += 9
            summa_u_1 = 0
            summa_r_1 = 0
            summa_u_2 = 0
            summa_r_2 = 0
            summa_u_3 = 0
            summa_r_3 = 0
            summa_u_4 = 0
            summa_r_4 = 0
            summa_u_5 = 0
            summa_r_5 = 0
            for f in str(summ1):
                print("summ1 = ", summ1)
                summa_u_1 += int(f)
            for f in str(summa_u_1):
                summa_u_2 += int(f)
            for f in str(summa_u_2):
                summa_u_3 += int(f)
            for f in str(summa_u_3):
                summa_u_4 += int(f)
            for f in str(summa_u_4):
                summa_u_5 += int(f)
            for f in str(summ2):
                print("summ2 = ", summ2)
                summa_r_1 += int(f)
            for f in str(summa_r_1):
                summa_r_2 += int(f)
            for f in str(summa_r_2):
                summa_r_3 += int(f)
            for f in str(summa_r_3):
                summa_r_4 += int(f)
            for f in str(summa_r_4):
                summa_r_5 += int(f)
            if summa_u_5 == 1:
                u_text = "Единицы свободолюбивы, часто эгоистичны. Такие люди стремятся к независимости, вкладывают силы в саморазвитие и реализацию себя. Способность направлять неуемную энергию в нужное русло поможет единицам добиться больших успехов в жизни. Среди них много творческих натур, активных и нуждающихся в постоянном движении вперед.\n" \
                         "\n" \
                         "Совет: развивайте честолюбие, решительность, дипломатичность, учитесь быстро реагировать на меняющуюся ситуацию. Вы можете реализовать себя на государственной службе, в политике, в медицине, научно-исследовательской деятельности, в авиации и космонавтике, машиностроении и горном деле, в авангардном искусстве."
            if summa_u_5 == 2:
                u_text = "Спокойствие и уравновешенность, присущие двойкам, позволяют им объективно мыслить и принимать обдуманные решения. Они стараются руководствоваться логикой и здравым смыслом. Прекрасные дипломаты, любой конфликт они способны уладить мирным путем. Им присущи доброта, тактичность в деликатных вопросах и мягкий характер.\n" \
                         "\n" \
                         "Совет: воспитывайте в себе терпение, трудолюбие, упорство, настойчивость. Вы можете проявить себя в роли финансиста, работника архива, музея, библиотеки, в сферах торговли, моды, сельского хозяйства, диетологии и производства продуктов питания."
            if summa_u_5 == 3:
                u_text = "Тройки удачливы, как никто другой. По натуре своей обычно это оптимистичные люди, не опускающие руки даже при столкновении с самыми сложными жизненными испытаниями. Часто они талантливы, легко обучаются любому ремеслу, общительны и нравятся людям, имеют много друзей.\n" \
                         "\n" \
                         "Совет: вам следует налаживать контакты, руководить людьми, стать ядром коллектива, развивать дипломатические способности, преодолевать недоверие к миру и людям. Вы можете избрать для себя путь поэта, живописца, литератора, дипломата, бизнесмена, журналиста, режиссера, музыканта, танцора, путешественника или ремесленника."
            if summa_u_5 == 4:
                u_text = "Ценят порядок и практичность, стабильность и спокойствие. Материалисты «до мозга костей», четверки не любят шумные сборища и острые ощущения. Их главная забота – благополучие в финансовом плане, постоянство комфорта. Это люди с принципами, им можно доверить свои тайны и не волноваться за их сохранность. Друзей у таких людей немного, но те, что есть – преданные и проверенные годами товарищи.\n" \
                         "\n" \
                         "Совет: найти себя и укрепить свой внутренний стержень, опираться на традиции, учиться отвечать не только за себя и свое дело, но и за окружающих. Вы можете проявить себя наиболее полно в изучении истории или археологии, заняться гостиничным или ресторанным бизнесом, музейным делом, реставрацией, архитектурой, химией или производством продуктов."
            if summa_u_5 == 5:
                u_text = "Любители приключений, пятерки ценят острые ощущения и перемены в жизни. Эти люди не терпят однообразия, быстро теряя интерес к любой монотонной деятельности. Часто они непредсказуемы, способны быстро изменить свое мнение, а потому не отличаются надежностью.\n" \
                         "\n" \
                         "Совет: учитесь принимать нестандартные решения и не бойтесь поставить все на карту. Искать себя надо там, где необходимо выполнять тонкую работу. Вы можете проявить себя в ювелирном и оружейном деле, стать пластическим и кардиохирургом, стоматологом и реставратором. Можно пойти в кино или на телевидение, стать руководителем."
            if summa_u_5 == 6:
                u_text = "Люди с числом имени 6 любят быть в центре внимания, часто высокомерны и эгоистичны. Проявляют заботу об окружающих обычно только если она принесет им моральное удовлетворение от своего поступка. Людей этого числа много в шоу-бизнесе, иных публичных профессиях.\n" \
                         "\n" \
                         "Совет: оставайтесь внутренне свободным, подчиняйтесь обстоятельствам, но не превращайтесь в их раба. Учитесь делать трудные дела привычными, привычные — легкими, легкие — красивыми. Вы можете проявить себя там, где требуются дисциплина, трудолюбие, выдержка, аккуратность и выносливость. Для вас больше всего подойдут профессии аналитиков, философов, исследователей, экономистов, физиков, биологов, математиков, чиновников, военных и политиков, даже аптекарей."
            if summa_u_5 == 7:
                u_text = "Загадочная личность. Проводя много времени в поисках себя многие семерки сталкиваются с непониманием окружающих и так и остаются одиноки. Они всерьез задумываются о своем предназначении и смысле человеческой жизни. Это одаренные личности, часто обладающие экстрасенсорной чувствительностью, например, способные предсказывать будущее.\n" \
                         "\n" \
                         "Совет: учитесь находить общий язык со всеми, с кем свела вас судьба, не стремитесь подчинять себе всех, победить врагов и недругов любой ценой, избавляйтесь от эгоцентризма. Работа от такого человека требует честолюбия, дипломатичности, умения вести переговоры, судебные процессы, связанные с защитой."
            if summa_u_5 == 8:
                u_text = "Лидеры по натуре, восьмерки невероятно трудолюбивы и выносливы. Природные организаторские способности, целеустремленность и незаурядный ум позволяют им достигать поставленных целей.\n" \
                         "\n" \
                         "Совет: учитесь ориентироваться в постоянно меняющихся ситуациях, делать правильный выбор и нести за него ответственность. Характерные виды деятельности для такого человека: рисковые специальности — шофер, альпинист, испытатель, пожарный, спасатель, психиатр, врач «скорой помощи», сотрудник секретной службы, цензор."
            if summa_u_5 == 9:
                u_text = "Девятки ленивы, у них много желаний и катастрофически мало энергии для их реализации. Поэтому они продолжают мечтать о чем-то и ничего для этого не делать годами. Надеясь, что все сбудется само собой, эти люди просто плывут по течению. При этом девятки отличаются душевной добротой и мягкостью.\n" \
                         "\n" \
                         "Совет: надо избавиться от стереотипов, способствовать созданию нового мировоззрения, построенного на глубоком изучении различных культур, научных и религиозных традиций. Лучшие сферы применения своих талантов: философия, культурология, социология, пропаганда, преподавание, религиозная и общественная деятельность."
            if summa_r_5 == 1:
                r_text = "Единицы свободолюбивы, часто эгоистичны. Такие люди стремятся к независимости, вкладывают силы в саморазвитие и реализацию себя. Способность направлять неуемную энергию в нужное русло поможет единицам добиться больших успехов в жизни. Среди них много творческих натур, активных и нуждающихся в постоянном движении вперед.\n"
            if summa_r_5 == 2:
                r_text = "Спокойствие и уравновешенность, присущие двойкам, позволяют им объективно мыслить и принимать обдуманные решения. Они стараются руководствоваться логикой и здравым смыслом. Прекрасные дипломаты, любой конфликт они способны уладить мирным путем. Им присущи доброта, тактичность в деликатных вопросах и мягкий характер.\n"
            if summa_r_5 == 3:
                r_text = "Тройки удачливы, как никто другой. По натуре своей обычно это оптимистичные люди, не опускающие руки даже при столкновении с самыми сложными жизненными испытаниями. Часто они талантливы, легко обучаются любому ремеслу, общительны и нравятся людям, имеют много друзей.\n"
            if summa_r_5 == 4:
                r_text = "Ценят порядок и практичность, стабильность и спокойствие. Материалисты «до мозга костей», четверки не любят шумные сборища и острые ощущения. Их главная забота – благополучие в финансовом плане, постоянство комфорта. Это люди с принципами, им можно доверить свои тайны и не волноваться за их сохранность. Друзей у таких людей немного, но те, что есть – преданные и проверенные годами товарищи.\n"
            if summa_r_5 == 5:
                r_text = "Любители приключений, пятерки ценят острые ощущения и перемены в жизни. Эти люди не терпят однообразия, быстро теряя интерес к любой монотонной деятельности. Часто они непредсказуемы, способны быстро изменить свое мнение, а потому не отличаются надежностью.\n"
            if summa_r_5 == 6:
                r_text = "Люди с числом имени 6 любят быть в центре внимания, часто высокомерны и эгоистичны. Проявляют заботу об окружающих обычно только если она принесет им моральное удовлетворение от своего поступка. Людей этого числа много в шоу-бизнесе, иных публичных профессиях.\n"
            if summa_r_5 == 7:
                r_text = "Загадочная личность. Проводя много времени в поисках себя многие семерки сталкиваются с непониманием окружающих и так и остаются одиноки. Они всерьез задумываются о своем предназначении и смысле человеческой жизни. Это одаренные личности, часто обладающие экстрасенсорной чувствительностью, например, способные предсказывать будущее.\n"
            if summa_r_5 == 8:
                r_text = "Лидеры по натуре, восьмерки невероятно трудолюбивы и выносливы. Природные организаторские способности, целеустремленность и незаурядный ум позволяют им достигать поставленных целей.\n"
            if summa_r_5 == 9:
                r_text = "Девятки ленивы, у них много желаний и катастрофически мало энергии для их реализации. Поэтому они продолжают мечтать о чем-то и ничего для этого не делать годами. Надеясь, что все сбудется само собой, эти люди просто плывут по течению. При этом девятки отличаются душевной добротой и мягкостью.\n"
            if (summa_u_5 == 1 and summa_r_5 == 1) or (summa_u_5 == 1 and summa_r_5 == 1):
                total_text = "1 и 1: Две свободолюбивые сильные личности, не умеющие уступать друг другу. Если это порождает конфликты, учитесь сдерживать негативные эмоции и рассуждать здраво."
            if (summa_u_5 == 1 and summa_r_5 == 2) or (summa_u_5 == 2 and summa_r_5 == 1):
                total_text = "1 и 2: Единицы действуют, а двойки – вдохновляют их. Продолжайте в том же духе – мотивируйте друг друга на новые свершения и личностный рост."
            if (summa_u_5 == 1 and summa_r_5 == 3) or (summa_u_5 == 3 and summa_r_5 == 1):
                total_text = "1 и 3: Идеи и намерения тройки могут подавляться единицей. Наладить отношения поможет четкое распределение обязанностей и порядка принятия решений в паре."
            if (summa_u_5 == 1 and summa_r_5 == 4) or (summa_u_5 == 4 and summa_r_5 == 1):
                total_text = "1 и 4: Сочетание несочетаемого – две противоположности, энергичность и сдержанность вполне могут быть вместе дополняя друг друга, если научатся прислушиваться к партнеру."
            if (summa_u_5 == 1 and summa_r_5 == 5) or (summa_u_5 == 5 and summa_r_5 == 1):
                total_text = "1 и 5: Отношения основаны на страсти и чувственности. Проявления пылкой любви могут быстро приесться и даже утомить, поэтому регулярно отдыхайте от этого."
            if (summa_u_5 == 1 and summa_r_5 == 6) or (summa_u_5 == 6 and summa_r_5 == 1):
                total_text = "1 и 6: Идеальное сочетание. Эмоциональная и свободолюбивая единица находит понимание шестерки. Забота друг о друге и любовь помогут сохранить и развить ваш союз."
            if (summa_u_5 == 1 and summa_r_5 == 7) or (summa_u_5 == 7 and summa_r_5 == 1):
                total_text = "1 и 7: Сочетание экстраверсии единицы и интроверсии семерки при условии взаимоуважения позволит партнерам удачно дополнить друг друга."
            if (summa_u_5 == 1 and summa_r_5 == 8) or (summa_u_5 == 8 and summa_r_5 == 1):
                total_text = "1 и 8: Хорошая нумерологическая совместимость, основанная на ласковом и теплом отношении партнеров друг к другу."
            if (summa_u_5 == 1 and summa_r_5 == 9) or (summa_u_5 == 9 and summa_r_5 == 1):
                total_text = "1 и 9: Инициативная и увлекающаяся единица найдет поддержку в девятке. Способность к самоконтролю лишь улучшит атмосферу в паре."
            if (summa_u_5 == 2 and summa_r_5 == 2) or (summa_u_5 == 2 and summa_r_5 == 2):
                total_text = "2 и 2: Идеальный дружеский союз. В любовных отношениях опасайтесь негативного влияния быта на разнообразие в отношениях."
            if (summa_u_5 == 2 and summa_r_5 == 3) or (summa_u_5 == 3 and summa_r_5 == 2):
                total_text = "2 и 3: Двойка дарит ощущение надежности и стабилизирует, а тройка внушает оптимизм и делится инициативностью. Такой союз вполне гармоничен."
            if (summa_u_5 == 2 and summa_r_5 == 4) or (summa_u_5 == 4 and summa_r_5 == 2):
                total_text = "2 и 4: Прекрасная совместимость за счет заботы и ласки партеров по отношению друг к другу. Ссоры в таком союзе – редкие гости."
            if (summa_u_5 == 2 and summa_r_5 == 5) or (summa_u_5 == 5 and summa_r_5 == 2):
                total_text = "2 и 5: Свободолюбивые люди, которых тянет друг к другу. Учитесь контролировать свои эмоции во время ссор и семейных неурядиц."
            if (summa_u_5 == 2 and summa_r_5 == 6) or (summa_u_5 == 6 and summa_r_5 == 2):
                total_text = "2 и 6: Хорошая пара, отношения в которой основаны на нежности, взаимном уважении и чувстве ответственности за партнера. Искренность чувств делает отношения абсолютно гармоничными."
            if (summa_u_5 == 2 and summa_r_5 == 7) or (summa_u_5 == 7 and summa_r_5 == 2):
                total_text = "2 и 7: В этой паре царит постоянство, спокойствие и надежность. Впрочем, порой двойку раздражает медлительность семерки и ее подверженность дурному влиянию со стороны"
            if (summa_u_5 == 2 and summa_r_5 == 8) or (summa_u_5 == 8 and summa_r_5 == 2):
                total_text = "2 и 8: Восьмерка пытается подавить инициативность двойки. Научитесь идти на уступки друг другу, договоритесь о справедливом разделении домашних хлопот и в отношениях будет царить мир."
            if (summa_u_5 == 2 and summa_r_5 == 9) or (summa_u_5 == 9 and summa_r_5 == 2):
                total_text = "2 и 9: Разные взгляды на жизнь не мешают вам быть вместе. Любовь девятки выходить в люди противопоставляется домоседству двойки. Принятие друг друга такими, какие вы есть, сохранит союз на долгие годы."
            if (summa_u_5 == 3 and summa_r_5 == 3) or (summa_u_5 == 3 and summa_r_5 == 3):
                total_text = "3 и 3: Дружеские отношения двух троек базируются на максимальном доверии друг другу. Любовь в таком союзе может оказаться недолговечной."
            if (summa_u_5 == 3 and summa_r_5 == 4) or (summa_u_5 == 4 and summa_r_5 == 3):
                total_text = "3 и 4: Это прочный союз, основанный на удачном дополнении темпераментности тройки уравновешенностью четверки. Понимание потребностей партнера в интимной и эмоциональной сферах сделает счастливыми обоих."
            if (summa_u_5 == 3 and summa_r_5 == 5) or (summa_u_5 == 5 and summa_r_5 == 3):
                total_text = "3 и 5: Общие интересы – путешествия, развлечение – объединяют тройку и пятерку. Конфликты могут возникать на фоне финансовых затруднений, обратите на это пристальное внимание."
            if (summa_u_5 == 3 and summa_r_5 == 6) or (summa_u_5 == 6 and summa_r_5 == 3):
                total_text = "3 и 6: оба партнера добродушные, отзывчивые люди. В таких отношениях царят гармония и теплота."
            if (summa_u_5 == 3 and summa_r_5 == 7) or (summa_u_5 == 7 and summa_r_5 == 3):
                total_text = "3 и 7: Интеллектуальная близость тройки и семерки не компенсирует разность их темпераментов. Учитесь уступать второй половине."
            if (summa_u_5 == 3 and summa_r_5 == 8) or (summa_u_5 == 8 and summa_r_5 == 3):
                total_text = "3 и 8: Энергичность и независимость партнеров позволяет им быть на одной волне, опасаться следует излишнего стремления к лидерству обоих."
            if (summa_u_5 == 3 and summa_r_5 == 9) or (summa_u_5 == 9 and summa_r_5 == 3):
                total_text = "3 и 9: Отношения гармоничны, партнеры подходят друг другу. Конфликты редки и недолгосрочны."
            if (summa_u_5 == 4 and summa_r_5 == 4) or (summa_u_5 == 4 and summa_r_5 == 4):
                total_text = "4 и 4: В целом отношения стабильны, но склонность обоих к упрямству может привести к затяжным ссорам. Учитесь решать такие ситуации мирно."
            if (summa_u_5 == 4 and summa_r_5 == 5) or (summa_u_5 == 5 and summa_r_5 == 4):
                total_text = "4 и 5: Этой паре свойственно сильное влечение в сочетании с разными характерами. То, что заводит одного, другому может быстро надоесть. Учитесь открыто высказывать свои желания и договариваться."
            if (summa_u_5 == 4 and summa_r_5 == 6) or (summa_u_5 == 6 and summa_r_5 == 4):
                total_text = "4 и 6: Этой паре можно позавидовать в плане совместимости. Общие цели, привычки, схожие взгляды на жизнь. Такие отношения наполнены теплом и уважением."
            if (summa_u_5 == 4 and summa_r_5 == 7) or (summa_u_5 == 7 and summa_r_5 == 4):
                total_text = "4 и 7: Боязнь проявления чувств может слегка охладить такие отношения. Не стесняйтесь быть ласковым и заботливым с любимым человеком."
            if (summa_u_5 == 4 and summa_r_5 == 8) or (summa_u_5 == 8 and summa_r_5 == 4):
                total_text = "4 и 8: Стремление к созданию семьи объединяет этих партнеров, однако повышенное внимание обоих к материальному благополучию может отвлечь их от чувственной стороны отношений."
            if (summa_u_5 == 4 and summa_r_5 == 9) or (summa_u_5 == 9 and summa_r_5 == 4):
                total_text = "4 и 9: Физическое влечение нивелирует все интеллектуальные противоречия в паре, в случае конфликтов партнерам надо стараться сглаживать разногласия."
            if (summa_u_5 == 5 and summa_r_5 == 5) or (summa_u_5 == 5 and summa_r_5 == 5):
                total_text = "5 и 5: Две пятерки часто влюбляются друг в друга с первого взгляда. Слабое место в отношениях - стремление к переменам."
            if (summa_u_5 == 5 and summa_r_5 == 6) or (summa_u_5 == 6 and summa_r_5 == 5):
                total_text = "5 и 6: Пятерке нравятся перемены, а шестерке — постоянство. Учитесь мириться с особенностями характера партнера."
            if (summa_u_5 == 5 and summa_r_5 == 7) or (summa_u_5 == 7 and summa_r_5 == 5):
                total_text = "5 и 7: Экстраверт и интроверт – эти люди должны беречь друг друга и учитывать такие особенности, тогда союз будет долгим."
            if (summa_u_5 == 5 and summa_r_5 == 8) or (summa_u_5 == 8 and summa_r_5 == 5):
                total_text = "5 и 8: Пятерке нравятся стабильность и успешность восьмерки, а восьмерку, в свою очередь, притягивают непосредственность и жизнерадостность пятерки. Принятие недостатков партнера позволит построить крепкие отношения."
            if (summa_u_5 == 5 and summa_r_5 == 9) or (summa_u_5 == 9 and summa_r_5 == 5):
                total_text = "5 и 9: Оба мечтательны и любят строить планы на будущее. Не сдавайтесь при столкновении с неудачами, учитесь упорству и ваш союз будет долговечным."
            if (summa_u_5 == 6 and summa_r_5 == 6) or (summa_u_5 == 6 and summa_r_5 == 6):
                total_text = "6 и 6: Схожие жизненные приоритеты помогут паре понять друг друга, но стоит опасаться финансовых затруднений. Учитесь преодолевать такие потрясения и стремитесь твердо стоять на ногах."
            if (summa_u_5 == 6 and summa_r_5 == 7) or (summa_u_5 == 7 and summa_r_5 == 6):
                total_text = "6 и 7: В целом партнеры подходят друг другу, но сложности могут возникать ввиду несдержанности и нетерпимости к манерам поведения партнера."
            if (summa_u_5 == 6 and summa_r_5 == 8) or (summa_u_5 == 8 and summa_r_5 == 6):
                total_text = "6 и 8: Сохранение баланса между духовным и материальным, позволит избежать разочарования в погоне за комфортом."
            if (summa_u_5 == 6 and summa_r_5 == 9) or (summa_u_5 == 9 and summa_r_5 == 6):
                total_text = "6 и 9: Оба склонны к мечтаниям, в паре вполне способны достигать поставленных целей. Отношения гармоничны как в физическом, так и в духовном аспектах."
            if (summa_u_5 == 7 and summa_r_5 == 7) or (summa_u_5 == 7 and summa_r_5 == 7):
                total_text = "7 и 7: Оба интровертивны, ценят спокойствие и размеренность в жизни. Прекрасная пара, совместимая во всех сферах, они могут рассчитывать на долгосрочные отношения, основанные на любви и взаимоуважении."
            if (summa_u_5 == 7 and summa_r_5 == 8) or (summa_u_5 == 8 and summa_r_5 == 7):
                total_text = "7 и 8: Семерка ценит духовное, восьмерка — материальное. Такой подход идеален для делового партнерства."
            if (summa_u_5 == 7 and summa_r_5 == 9) or (summa_u_5 == 9 and summa_r_5 == 7):
                total_text = "7 и 9: Способность мечтательных идеалистов поддержать друг друга в сложной ситуации может сделать такой союз счастливым."
            if (summa_u_5 == 8 and summa_r_5 == 8) or (summa_u_5 == 8 and summa_r_5 == 8):
                total_text = "8 и 8: Их связывает сильное влечение друг к другу, но ввиду нетерпеливости и амбициозности партнеров в такой паре могут часто случаться ссоры. Учитесь уступать и не зацикливайтесь на мелочах."
            if (summa_u_5 == 8 and summa_r_5 == 9) or (summa_u_5 == 9 and summa_r_5 == 8):
                total_text = "8 и 9: Эти люди прекрасно дополняют друг друга в деловых отношениях. Восьмерки темпераментны, а девяткам это нравится и сподвигает их осуществлять задуманное. Хорошая совместимость по именам для деловых отношений."
            if (summa_u_5 == 9 and summa_r_5 == 9) or (summa_u_5 == 9 and summa_r_5 == 9):
                total_text = "9 и 9: В таких отношениях царит взаимопонимание, нежность и верность. Оба партнера ценят друг в друге личность, поддерживая стремление второй половины к саморазвитию и внутреннему росту."

            try:
                telegraph.create_account(short_name='совместимость')
                response = telegraph.create_page(
                    f'Совместимость имен {names_split[0]} и {names_split[1]}',
                    html_content=f'🔮<b>Вашему имени ({names_split[0]}) соответствует число {summa_u_5}</b><br>'
                                 f'{u_text}<br>'
                                 f'<br>'
                                 f'🔮<b>Имени партнера ({names_split[1]}) соответствует число {summa_r_5}</b><br>'
                                 f'{r_text}<br>'
                                 f'<br>'
                                 f'👫<b>Совместимость</b> {total_text}'
                )
                print(response)
                link = 'http://telegra.ph/{}'.format(response['path'])
                msg_text = hlink(" ", link)
                await message.answer(f"Результат{msg_text}расчета:", reply_markup=back_compatibility_ru)
                await state.finish()
            except:
                await message.answer(f"Вы неправильно ввели имена\n"
                                     f"\n"
                                     f"<i>Введите их в формате: Анастасия Дмитрий</i>",
                                     reply_markup=back_compatibility_ru)
        else:
            await message.answer(f"Вы неправильно ввели имена\n"
                                 f"\n"
                                 f"<i>Введите их в формате: Анастасия Дмитрий</i>", reply_markup=back_compatibility_ru)
    if user.language == "en":
        names_split = names.split()
        x = 0
        for i in names_split:
            x += 1
        if x == 2:
            summ1 = 0
            summ2 = 0
            for y in names_split[0]:
                for z in y:
                    if z in ("a", "j", "s", "A", "J", "S"):
                        summ1 += 1
                    if z in ("b", "k", "t", "B", "K", "T"):
                        summ1 += 2
                    if z in ("c", "l", "u", "C", "L", "U"):
                        summ1 += 3
                    if z in ("d", "m", "v", "D", "M", "V"):
                        summ1 += 4
                    if z in ("e", "n", "w", "E", "N", "W"):
                        summ1 += 5
                    if z in ("f", "o", "x", "F", "O", "X"):
                        summ1 += 6
                    if z in ("g", "p", "y", "G", "P", "Y"):
                        summ1 += 7
                    if z in ("h", "q", "z", "H", "Q", "Z"):
                        summ1 += 8
                    if z in ("i", "r", "I", "R"):
                        summ1 += 9
            for y in names_split[1]:
                for z in y:
                    if z in ("a", "j", "s", "A", "J", "S"):
                        summ2 += 1
                    if z in ("b", "k", "t", "B", "K", "T"):
                        summ2 += 2
                    if z in ("c", "l", "u", "C", "L", "U"):
                        summ2 += 3
                    if z in ("d", "m", "v", "D", "M", "V"):
                        summ2 += 4
                    if z in ("e", "n", "w", "E", "N", "W"):
                        summ2 += 5
                    if z in ("f", "o", "x", "F", "O", "X"):
                        summ2 += 6
                    if z in ("g", "p", "y", "G", "P", "Y"):
                        summ2 += 7
                    if z in ("h", "q", "z", "H", "Q", "Z"):
                        summ2 += 8
                    if z in ("i", "r", "I", "R"):
                        summ2 += 9
            summa_u_1 = 0
            summa_r_1 = 0
            summa_u_2 = 0
            summa_r_2 = 0
            summa_u_3 = 0
            summa_r_3 = 0
            summa_u_4 = 0
            summa_r_4 = 0
            summa_u_5 = 0
            summa_r_5 = 0
            for f in str(summ1):
                print("summ1 = ", summ1)
                summa_u_1 += int(f)
            for f in str(summa_u_1):
                summa_u_2 += int(f)
            for f in str(summa_u_2):
                summa_u_3 += int(f)
            for f in str(summa_u_3):
                summa_u_4 += int(f)
            for f in str(summa_u_4):
                summa_u_5 += int(f)
            for f in str(summ2):
                print("summ2 = ", summ2)
                summa_r_1 += int(f)
            for f in str(summa_r_1):
                summa_r_2 += int(f)
            for f in str(summa_r_2):
                summa_r_3 += int(f)
            for f in str(summa_r_3):
                summa_r_4 += int(f)
            for f in str(summa_r_4):
                summa_r_5 += int(f)
            if summa_u_5 == 1:
                u_text = "Units are freedom-loving, often selfish. Such people strive for independence, invest strength in self-development and self-realization. The ability to direct irrepressible energy in the right direction will help units to achieve great success in life. Among them there are many creative natures, active and in need of constant movement forward. \n " \
                         " \n " \
                         "💡Advice: develop ambition, determination, diplomacy, learn to react quickly to a changing situation. You can realize yourself in public service, in politics, in medicine, research activities, in aviation and astronautics, mechanical engineering and mining, in the avant-garde art. "

            if summa_u_5 == 2:
                u_text = "The calmness and balance inherent in twos allow them to think objectively and make deliberate decisions. They try to be guided by logic and common sense. Excellent diplomats, they are able to settle any conflict peacefully. They are characterized by kindness, tact in delicate matters and a gentle character. \n " \
                         " \n " \
                         "💡Advice: cultivate patience, hard work, perseverance, perseverance. You can prove yourself as a financier, archive worker, museum, library, trade, fashion, agriculture, nutrition and food production."

            if summa_u_5 == 3:
                u_text = " Threes are lucky like no other. By their nature, they are usually optimistic people who do not give up even when faced with the most difficult challenges in life. They are often talented, easily learn any craft, are sociable and like people, have many friends. \n " \
                         " \n " \
                         "💡Advice: you should establish contacts, lead people, become the core of a team, develop diplomatic skills, overcome distrust of the world and people. You can choose for yourself the path of a poet, painter, writer, diplomat, businessman, journalist, director, musician, dancer, traveler or artisan. "

            if summa_u_5 == 4:
                u_text = "They value order and practicality, stability and tranquility. Materialists to the marrow, fours do not like noisy gatherings and thrills. Their main concern is financial well-being, the constancy of comfort. These are people with principles, they can be entrusted with their secrets and not Worry about their safety. Such people have few friends, but those that do exist are devoted and proven comrades over the years. \n " \
                         " \n " \
                         "💡Advice: find yourself and strengthen your inner core, rely on traditions, learn to be responsible not only for yourself and your business, but also for those around you. You can express yourself most fully in the study of history or archeology, engage in hotel or restaurant business, museum business , restoration, architecture, chemistry or product manufacturing. "

            if summa_u_5 == 5:
                u_text = "Adventurers, fives appreciate the thrill and change in life. These people do not tolerate monotony, quickly losing interest in any monotonous activity. They are often unpredictable, can quickly change their minds, and therefore are not reliable. \n " \
                         " \n " \
                         "💡Advice: learn to make non-standard decisions and do not be afraid to put everything at stake. You need to look for yourself where you need to do fine work. You can prove yourself in jewelry and weapons, become a plastic and cardiac surgeon, dentist and restorer. You can go to the cinema or on television, become a leader. "

            if summa_u_5 == 6:
                u_text = "People with the name number 6 love to be in the spotlight, are often arrogant and selfish. They usually take care of others only if it brings them moral satisfaction from their actions. There are many people of this number in show business and other public professions. \n " \
                         " \n " \
                         "💡Advice: stay inwardly free, obey circumstances, but do not turn into their slave. Learn to make difficult things familiar, familiar - easy, easy - beautiful. You can prove yourself where discipline, hard work, endurance, accuracy and endurance are required. For the professions of analysts, philosophers, researchers, economists, physicists, biologists, mathematicians, officials, military and politicians, even pharmacists will suit you best. "

            if summa_u_5 == 7:
                u_text = "Mysterious personality. Spending a lot of time in search of themselves, many sevens are faced with a lack of understanding of others and remain alone. They seriously think about their purpose and the meaning of human life. These are gifted individuals, often with extrasensory sensitivity, for example, able to predict the future. \n " \
                         " \n " \
                         "💡Advice: learn to find a common language with everyone with whom fate has brought you, do not seek to subjugate everyone, defeat enemies and foes at any cost, get rid of egocentrism. Working from such a person requires ambition, diplomacy, the ability to negotiate, litigation related with protection. "

            if summa_u_5 == 8:
                u_text = "Leaders by nature, the Eights are incredibly hardworking and resilient . Their natural organizational skills, dedication and extraordinary intelligence allow them to achieve their goals. \n " \
                         " \n " \
                         "💡Advice: learn to navigate constantly changing situations, make the right choice and take responsibility for it. Typical activities for such a person: risky specialties - driver, climber, tester, firefighter, rescuer, psychiatrist, ambulance doctor, secret service employee, censor . "

            if summa_u_5 == 9:
                u_text = "Nines are lazy, they have a lot of desires and catastrophically little energy to realize them. Therefore, they continue to dream about something and do nothing for this for years. Hoping that everything will come true by itself, these people just go with the flow. this nines are distinguished by their kindness and gentleness. \n " \
                         " \n " \
                         "💡Advice: we need to get rid of stereotypes, contribute to the creation of a new worldview, built on a deep study of various cultures, scientific and religious traditions. The best areas of application of their talents: philosophy, cultural studies, sociology, propaganda, teaching, religious and social activities."

            if summa_r_5 == 1:
                r_text = "Units are freedom-loving, often selfish. Such people strive for independence, invest in self-development and self-realization. The ability to direct irrepressible energy in the right direction will help units to achieve great success in life. Among them there are many creative natures, active and in need of constant movement. forward. \n "

            if summa_r_5 == 2:
                r_text = "The calmness and balance inherent in deuces allow them to think objectively and make deliberate decisions. They try to be guided by logic and common sense. Excellent diplomats, they are able to settle any conflict peacefully. They are characterized by kindness, tact in delicate matters and a gentle character. \n "

            if summa_r_5 == 3:
                r_text = " Threes are lucky like no other. By their nature, they are usually optimistic people who do not give up even when faced with the most difficult challenges in life. They are often talented, easily learn any craft, are sociable and like people, have many friends. \n "

            if summa_r_5 == 4:
                r_text = "They value order and practicality, stability and tranquility. Materialists to the core, fours do not like noisy gatherings and thrills. Their main concern is financial well-being, the constancy of comfort. These are people with principles, they can be entrusted with their secrets and not worry about their safety. Such people have few friends, but those that do exist are devoted and proven comrades over the years. \n "

            if summa_r_5 == 5:
                r_text = "Adventurers, fives appreciate the thrill and change in life. These people do not tolerate monotony, quickly losing interest in any monotonous activity. They are often unpredictable, can quickly change their minds, and therefore are not reliable. \n "

            if summa_r_5 == 6:
                r_text = "People with the name number 6 love to be in the spotlight, are often arrogant and selfish. They usually take care of others only if it brings them moral satisfaction from their actions. There are many people of this number in show business and other public professions. \n "

            if summa_r_5 == 7:
                r_text = "Mysterious person. Spending a lot of time in search of themselves, many sevens are faced with a lack of understanding of others and remain alone. They seriously think about their purpose and the meaning of human life. These are gifted individuals, often with extrasensory sensitivity, for example, able to predict the future. \n "

            if summa_r_5 == 8:
                r_text = "Leaders by nature, the Eights are incredibly hardworking and resilient . Their natural organizational skills, dedication and extraordinary intelligence allow them to achieve their goals. \n "

            if summa_r_5 == 9:
                r_text = "Nines are lazy, they have a lot of desires and catastrophically little energy to realize them. Therefore, they continue to dream about something and do nothing for this for years. Hoping that everything will come true by itself, these people just go with the flow. this nines are distinguished by their kindness and gentleness. \n "

            if (summa_u_5 == 1 and summa_r_5 == 1) or (summa_u_5 == 1 and summa_r_5 == 1):
                total_text = "1 and 1: Two freedom-loving strong personalities who cannot give in to each other. If this creates conflicts, learn to restrain negative emotions and reason sanely."

            if (summa_u_5 == 1 and summa_r_5 == 2) or (summa_u_5 == 2 and summa_r_5 == 1):
                total_text = "1 and 2: The ones work, and the twos inspire them. Keep up the good work - motivate each other for new achievements and personal growth."

            if (summa_u_5 == 1 and summa_r_5 == 3) or (summa_u_5 == 3 and summa_r_5 == 1):
                total_text = "1 and 3: The ideas and intentions of the trio can be suppressed by 1. The clear distribution of responsibilities and the order of decision-making in the couple will help to establish relationships."

            if (summa_u_5 == 1 and summa_r_5 == 4) or (summa_u_5 == 4 and summa_r_5 == 1):
                total_text = "1 and 4: The combination of the incompatible - two opposites, energy and restraint may well complement each other together, if you learn to listen to your partner."

            if (summa_u_5 == 1 and summa_r_5 == 5) or (summa_u_5 == 5 and summa_r_5 == 1):
                total_text = "1 & 5: Relationships are based on passion and sensuality. Expressions of passionate love can quickly become boring and even tiresome, so take a break from it regularly."

            if (summa_u_5 == 1 and summa_r_5 == 6) or (summa_u_5 == 6 and summa_r_5 == 1):
                total_text = "1 and 6: The perfect combination. Emotional and freedom-loving unit finds understanding 6. Caring for each other and love will help maintain and develop your union."

            if (summa_u_5 == 1 and summa_r_5 == 7) or (summa_u_5 == 7 and summa_r_5 == 1):
                total_text = "1 and 7: The combination of the extraversion of one and the introversion of the seven, subject to mutual respect, will allow partners to successfully complement each other."

            if (summa_u_5 == 1 and summa_r_5 == 8) or (summa_u_5 == 8 and summa_r_5 == 1):
                total_text = "1 and 8: Good numerological compatibility, based on the affectionate and warm relationship of partners to each other."

            if (summa_u_5 == 1 and summa_r_5 == 9) or (summa_u_5 == 9 and summa_r_5 == 1):
                total_text = "1 and 9: An enterprising and enthusiastic unit will find support in the nine. Self-control will only improve the atmosphere in a couple."

            if (summa_u_5 == 2 and summa_r_5 == 2) or (summa_u_5 == 2 and summa_r_5 == 2):
                total_text = "2 and 2: Perfect companionship. In romantic relationships, beware of the negative impact of everyday life on diversity in relationships."

            if (summa_u_5 == 2 and summa_r_5 == 3) or (summa_u_5 == 3 and summa_r_5 == 2):
                total_text = "2 and 3: The deuce gives a sense of security and stabilizes, while the troika inspires optimism and shares initiative. Such a union is quite harmonious."

            if (summa_u_5 == 2 and summa_r_5 == 4) or (summa_u_5 == 4 and summa_r_5 == 2):
                total_text = "2 and 4: Excellent compatibility due to the care and affection of the partners towards each other. Quarrels in such an alliance are rare guests."

            if (summa_u_5 == 2 and summa_r_5 == 5) or (summa_u_5 == 5 and summa_r_5 == 2):
                total_text = "2 and 5: Freedom-loving people who are drawn to each other. Learn to control your emotions during quarrels and family troubles."

            if (summa_u_5 == 2 and summa_r_5 == 6) or (summa_u_5 == 6 and summa_r_5 == 2):
                total_text = "2 and 6: A good couple, the relationship in which is based on tenderness, mutual respect and a sense of responsibility for the partner. Sincerity makes the relationship absolutely harmonious."

            if (summa_u_5 == 2 and summa_r_5 == 7) or (summa_u_5 == 7 and summa_r_5 == 2):
                total_text = "2 and 7: Constancy, calmness and reliability reign in this pair. However, sometimes the deuce is irritated by the slowness of the seven and its susceptibility to bad influence from the outside."

            if (summa_u_5 == 2 and summa_r_5 == 8) or (summa_u_5 == 8 and summa_r_5 == 2):
                total_text = "2 and 8: The 8 is trying to suppress the initiative of the 2. Learn to make concessions to each other, agree on a fair sharing of household chores and peace will reign in the relationship."

            if (summa_u_5 == 2 and summa_r_5 == 9) or (summa_u_5 == 9 and summa_r_5 == 2):
                total_text = "2 and 9: Different outlooks on life do not prevent you from being together. The love of a nine to go out is opposed to the home of two. Acceptance of each other as you are will keep the union for many years."

            if (summa_u_5 == 3 and summa_r_5 == 3) or (summa_u_5 == 3 and summa_r_5 == 3):
                total_text = "3 and 3: The friendship of two triplets is based on maximum trust in each other. Love in such a union can be short-lived."

            if (summa_u_5 == 3 and summa_r_5 == 4) or (summa_u_5 == 4 and summa_r_5 == 3):
                total_text = "3 and 4: This is a strong union based on the successful addition of the temperament of the 3 with the poise of the 4. Understanding the partner's intimate and emotional needs will make both happy."

            if (summa_u_5 == 3 and summa_r_5 == 5) or (summa_u_5 == 5 and summa_r_5 == 3):
                total_text = "3 and 5: Common interests - travel, entertainment - combine three and five. Conflicts can arise against the background of financial difficulties, pay close attention to this."

            if (summa_u_5 == 3 and summa_r_5 == 6) or (summa_u_5 == 6 and summa_r_5 == 3):
                total_text = "3 and 6: both partners are good-natured, sympathetic people. In such a relationship, harmony and warmth reign."

            if (summa_u_5 == 3 and summa_r_5 == 7) or (summa_u_5 == 7 and summa_r_5 == 3):
                total_text = "3 and 7: The intellectual proximity of a 3 and a 7 does not compensate for the difference in temperament. Learn to yield to the other half."

            if (summa_u_5 == 3 and summa_r_5 == 8) or (summa_u_5 == 8 and summa_r_5 == 3):
                total_text = "3 and 8: The energy and independence of partners allows them to be on the same wavelength, one should be wary of an excessive desire for leadership of both."

            if (summa_u_5 == 3 and summa_r_5 == 9) or (summa_u_5 == 9 and summa_r_5 == 3):
                total_text = "3 and 9: Relationships are harmonious, partners fit together. Conflicts are rare and short-lived."

            if (summa_u_5 == 4 and summa_r_5 == 4) or (summa_u_5 == 4 and summa_r_5 == 4):
                total_text = "4 and 4: In general, the relationship is stable, but the tendency of both to be stubborn can lead to protracted fights. Learn to deal with such situations peacefully."

            if (summa_u_5 == 4 and summa_r_5 == 5) or (summa_u_5 == 5 and summa_r_5 == 4):
                total_text = "4 and 5: This couple has a strong attraction combined with different personalities. What turns one on can quickly get bored with another. Learn to openly express your desires and negotiate."

            if (summa_u_5 == 4 and summa_r_5 == 6) or (summa_u_5 == 6 and summa_r_5 == 4):
                total_text = "4 and 6: This pair is enviable in terms of compatibility. Common goals, habits, similar outlook on life. Such a relationship is filled with warmth and respect."

            if (summa_u_5 == 4 and summa_r_5 == 7) or (summa_u_5 == 7 and summa_r_5 == 4):
                total_text = "4 and 7: Fear of expressing feelings can slightly cool this relationship. Feel free to be affectionate and caring with your loved one."

            if (summa_u_5 == 4 and summa_r_5 == 8) or (summa_u_5 == 8 and summa_r_5 == 4):
                total_text = "4 and 8: The desire to create a family brings these partners together, but the increased attention of both to material well-being can distract them from the sensual side of the relationship."

            if (summa_u_5 == 4 and summa_r_5 == 9) or (summa_u_5 == 9 and summa_r_5 == 4):
                total_text = "4 and 9: Physical attraction eliminates all intellectual contradictions in a couple, in case of conflicts, partners should try to smooth out the differences."

            if (summa_u_5 == 5 and summa_r_5 == 5) or (summa_u_5 == 5 and summa_r_5 == 5):
                total_text = "5 and 5: Two fives often fall in love at first sight. The weak point in a relationship is the desire for change."

            if (summa_u_5 == 5 and summa_r_5 == 6) or (summa_u_5 == 6 and summa_r_5 == 5):
                total_text = "5 and 6: 5 love change, 6 love consistency. Learn to accept your partner's personality traits."

            if (summa_u_5 == 5 and summa_r_5 == 7) or (summa_u_5 == 7 and summa_r_5 == 5):
                total_text = "5 and 7: Extrovert and introvert - these people should take care of each other and take into account such peculiarities, then the union will be long."

            if (summa_u_5 == 5 and summa_r_5 == 8) or (summa_u_5 == 8 and summa_r_5 == 5):
                total_text = "5 and 8: The 5 likes the stability and success of the 8, and the 8, in turn, attracts the spontaneity and cheerfulness of the 5. Accepting a partner's flaws will build strong relationships."

            if (summa_u_5 == 5 and summa_r_5 == 9) or (summa_u_5 == 9 and summa_r_5 == 5):
                total_text = "5 and 9: Both are dreamy and love to make plans for the future. Do not give up when faced with setbacks, learn perseverance and your union will last."

            if (summa_u_5 == 6 and summa_r_5 == 6) or (summa_u_5 == 6 and summa_r_5 == 6):
                total_text = "6 and 6: Having similar life priorities will help a couple understand each other, but fear financial hardship. Learn to cope with such turmoil and strive to stay on your feet."

            if (summa_u_5 == 6 and summa_r_5 == 7) or (summa_u_5 == 7 and summa_r_5 == 6):
                total_text = "6 and 7: In general, partners suit each other, but difficulties can arise due to intemperance and intolerance to the partner's demeanor."

            if (summa_u_5 == 6 and summa_r_5 == 8) or (summa_u_5 == 8 and summa_r_5 == 6):
                total_text = "6 and 8: Maintaining a balance between the spiritual and the material will avoid the frustration of pursuing comfort."

            if (summa_u_5 == 6 and summa_r_5 == 9) or (summa_u_5 == 9 and summa_r_5 == 6):
                total_text = "6 and 9: Both are inclined to daydreaming, couples are quite capable of achieving their goals. Relationships are harmonious both physically and spiritually."

            if (summa_u_5 == 7 and summa_r_5 == 7) or (summa_u_5 == 7 and summa_r_5 == 7):
                total_text = "7 and 7: Both are introverted, value calmness and regularity in life. A wonderful couple, compatible in all areas, they can count on a long-term relationship based on love and mutual respect."

            if (summa_u_5 == 7 and summa_r_5 == 8) or (summa_u_5 == 8 and summa_r_5 == 7):
                total_text = "7 and 8: 7 values ​​spiritual, 8 - material. This approach is ideal for business partnerships."

            if (summa_u_5 == 7 and summa_r_5 == 9) or (summa_u_5 == 9 and summa_r_5 == 7):
                total_text = "7 and 9: The ability of dreamy idealists to support each other in a difficult situation can make such a union happy."

            if (summa_u_5 == 8 and summa_r_5 == 8) or (summa_u_5 == 8 and summa_r_5 == 8):
                total_text = "8 and 8: They have a strong attraction to each other, but due to the impatience and ambition of the partners, quarrels can often occur in such a pair. Learn to give in and do not get hung up on trifles."

            if (summa_u_5 == 8 and summa_r_5 == 9) or (summa_u_5 == 9 and summa_r_5 == 8):
                total_text = "8 and 9: These people complement each other perfectly in business relationships. Eights are temperamental, and nines like it and encourages them to carry out their plans. Good name compatibility for business relationships."

            if (summa_u_5 == 9 and summa_r_5 == 9) or (summa_u_5 == 9 and summa_r_5 == 9):
                total_text = "9 and 9: In such a relationship, mutual understanding, tenderness and loyalty reign. Both partners value each other's personality, supporting the desire of the other half for self-development and inner growth."

            try:
                telegraph.create_account(short_name='совместимость')
                response = telegraph.create_page(
                    f'Name compatibility {names_split[0]} and {names_split[1]}',
                    html_content=f'🔮<b>Your name ({names_split[0]}) matches the number {summa_u_5}</b><br>'
                                 f'{u_text}<br>'
                                 f'<br>'
                                 f'🔮<b>Partner name ({names_split[1]}) matches the number {summa_r_5}</b><br>'
                                 f'{r_text}<br>'
                                 f'<br>'
                                 f'👫<b>Compatibility</b> {total_text}'
                )
                link = 'http://telegra.ph/{}'.format(response['path'])
                msg_text = hlink(" ", link)
                await message.answer(f"Calculation{msg_text}result:", reply_markup=back_compatibility_en)
                await state.finish()
            except:
                await message.answer(f"You entered the wrong names\n"
                                     f"\n"
                                     f"<i>Enter them in the format: Michelle John</i>",
                                     reply_markup=back_compatibility_en)
        else:
            await message.answer(f"You entered the wrong names\n"
                                 f"\n"
                                 f"<i>Enter them in the format: Michelle John</i>", reply_markup=back_compatibility_en)
    if user.language == "es":
        names_split = names.split()
        x = 0
        for i in names_split:
            x += 1
        if x == 2:
            summ1 = 0
            summ2 = 0
            for y in names_split[0]:
                for z in y:
                    if z in ("a", "j", "s", "A", "J", "S"):
                        summ1 += 1
                    if z in ("b", "k", "t", "B", "K", "T"):
                        summ1 += 2
                    if z in ("c", "l", "u", "C", "L", "U"):
                        summ1 += 3
                    if z in ("d", "m", "v", "D", "M", "V"):
                        summ1 += 4
                    if z in ("e", "n", "w", "E", "N", "W"):
                        summ1 += 5
                    if z in ("f", "o", "x", "F", "O", "X"):
                        summ1 += 6
                    if z in ("g", "p", "y", "G", "P", "Y"):
                        summ1 += 7
                    if z in ("h", "q", "z", "H", "Q", "Z"):
                        summ1 += 8
                    if z in ("i", "r", "I", "R"):
                        summ1 += 9
            for y in names_split[1]:
                for z in y:
                    if z in ("a", "j", "s", "A", "J", "S"):
                        summ2 += 1
                    if z in ("b", "k", "t", "B", "K", "T"):
                        summ2 += 2
                    if z in ("c", "l", "u", "C", "L", "U"):
                        summ2 += 3
                    if z in ("d", "m", "v", "D", "M", "V"):
                        summ2 += 4
                    if z in ("e", "n", "w", "E", "N", "W"):
                        summ2 += 5
                    if z in ("f", "o", "x", "F", "O", "X"):
                        summ2 += 6
                    if z in ("g", "p", "y", "G", "P", "Y"):
                        summ2 += 7
                    if z in ("h", "q", "z", "H", "Q", "Z"):
                        summ2 += 8
                    if z in ("i", "r", "I", "R"):
                        summ2 += 9
            summa_u_1 = 0
            summa_r_1 = 0
            summa_u_2 = 0
            summa_r_2 = 0
            summa_u_3 = 0
            summa_r_3 = 0
            summa_u_4 = 0
            summa_r_4 = 0
            summa_u_5 = 0
            summa_r_5 = 0
            for f in str(summ1):
                print("summ1 = ", summ1)
                summa_u_1 += int(f)
            for f in str(summa_u_1):
                summa_u_2 += int(f)
            for f in str(summa_u_2):
                summa_u_3 += int(f)
            for f in str(summa_u_3):
                summa_u_4 += int(f)
            for f in str(summa_u_4):
                summa_u_5 += int(f)
            for f in str(summ2):
                print("summ2 = ", summ2)
                summa_r_1 += int(f)
            for f in str(summa_r_1):
                summa_r_2 += int(f)
            for f in str(summa_r_2):
                summa_r_3 += int(f)
            for f in str(summa_r_3):
                summa_r_4 += int(f)
            for f in str(summa_r_4):
                summa_r_5 += int(f)
            if summa_u_5 == 1:
                u_text = "Las unidades son amantes de la libertad, a menudo egoístas. Estas personas luchan por la independencia, invierten fuerza en el desarrollo y la autorrealización. La capacidad de dirigir energía incontenible en la dirección correcta ayudará a las unidades a lograr un gran éxito en la vida. Entre para ellos hay muchas naturalezas creativas, activas y que necesitan un movimiento constante hacia adelante. \n " \
                         " \n " \
                         "Asesoramiento: desarrolla ambición, determinación, diplomacia, aprende a reaccionar rápidamente ante una situación cambiante. Puedes realizarte en el servicio público, en política, en medicina, actividades de investigación, en aviación y astronáutica, ingeniería mecánica y minería, en la vanguardia garde art "
            if summa_u_5 == 2:
                u_text = "La calma y el equilibrio inherentes a la pareja les permite pensar con objetividad y tomar decisiones deliberadas. Intentan guiarse por la lógica y el sentido común. Excelentes diplomáticos, son capaces de resolver cualquier conflicto de manera pacífica. Se caracterizan por la amabilidad, el tacto en asuntos delicados y un carácter amable. \n " \
                         " \n " \
                         "Consejo: cultive la paciencia, el trabajo duro, la perseverancia, la perseverancia. Puede demostrar su valía como financiero, trabajador de archivos, museo, biblioteca, comercio, moda, agricultura, nutrición y producción de alimentos"
            if summa_u_5 == 3:
                u_text = "Los tres son afortunados como ningún otro. Por su naturaleza, suelen ser personas optimistas que no se rinden incluso cuando se enfrentan a los desafíos más difíciles de la vida. A menudo son talentosos, aprenden fácilmente cualquier oficio, son sociables y les gustan las personas. , tengo muchos amigos. \n " \
                         " \n " \
                         "Consejo: debes establecer contactos, liderar personas, convertirte en el núcleo de un equipo, desarrollar habilidades diplomáticas, superar la desconfianza en el mundo y las personas. Puedes elegir por ti mismo el camino de poeta, pintor, escritor, diplomático, empresario, periodista , director, músico, bailarín, viajero o artesano "
            if summa_u_5 == 4:
                u_text = " Valoran el orden y la practicidad, la estabilidad y la tranquilidad. Materialistas hasta la médula, a los cuatro no les gustan las reuniones ruidosas y las emociones fuertes. Su principal preocupación es el bienestar financiero, la constancia de la comodidad. Son personas con principios, pueden ser confiados con sus secretos y no preocuparse por su seguridad. Estas personas tienen pocos amigos, pero los que existen son camaradas devotos y probados a lo largo de los años. \n " \
                         " \n " \
                         "Consejo: encuéntrese y fortalezca su núcleo interno, confíe en las tradiciones, aprenda a ser responsable no solo de usted y su negocio, sino también de quienes lo rodean. Puede expresarse más plenamente en el estudio de la historia o la arqueología, participar en hotel o restaurante, museo, restauración, arquitectura, química o fabricación de productos "
            if summa_u_5 == 5:
                u_text = "Aventureros, los cinco aprecian la emoción y el cambio en la vida. Estas personas no toleran la monotonía y pierden rápidamente el interés en cualquier actividad monótona. A menudo son impredecibles, pueden cambiar de opinión rápidamente y, por lo tanto, no son confiables. \n " \
                         " \n " \
                         "Consejo: aprenda a tomar decisiones atípicas y no tenga miedo de poner todo en juego. Debe buscar por sí mismo donde necesita hacer un buen trabajo. Puede demostrar su valía en el negocio de la joyería y las armas, convertirse en un plástico y un cardíaco cirujano, dentista y restaurador. Puedes ir al cine o en la televisión, convertirte en un líder "
            if summa_u_5 == 6:
                u_text = "A las personas con el nombre número 6 les encanta estar en el centro de atención, a menudo son arrogantes y egoístas. Por lo general, cuidan a los demás solo si les brinda satisfacción moral de sus acciones. Hay muchas personas de este número en el mundo del espectáculo y otras profesiones públicas. \n " \
                         " \n " \
                         "Consejo: manténgase libre interiormente, obedezca las circunstancias, pero no se convierta en su esclavo. Aprenda a hacer que las cosas difíciles sean familiares, familiares, fáciles, fáciles, hermosas. Puede demostrar su valía donde se requiere disciplina, trabajo duro, perseverancia, precisión y resistencia. . Para las profesiones de analistas, filósofos, investigadores, economistas, físicos, biólogos, matemáticos, funcionarios, militares y políticos, incluso los farmacéuticos serán los más adecuados para usted "
            if summa_u_5 == 7:
                u_text = "Personalidad misteriosa. Pasando mucho tiempo buscándose a sí mismos, muchos sietes se enfrentan a la falta de comprensión de los demás y permanecen solos. Piensan seriamente en su propósito y el significado de la vida humana. Estos son individuos dotados, a menudo con sensibilidad extrasensorial, por ejemplo, capaz de predecir el futuro. \n " \
                         " \n " \
                         "Consejo: aprende a encontrar un lenguaje común con todos los que te ha traído el destino, no busques subyugar a todos, derrota a enemigos y enemigos a toda costa, deshazte del egocentrismo. Trabajar desde una persona así requiere ambición, diplomacia, la habilidad para negociar, litigios relacionados con la protección "
            if summa_u_5 == 8:
                u_text = "Líderes por naturaleza, los Ocho son increíblemente trabajadores y resistentes . Sus habilidades organizativas naturales, determinación e inteligencia extraordinaria les permiten alcanzar sus objetivos. \n " \
                         " \n " \
                         "Consejo: aprenda a navegar en situaciones en constante cambio, tome la decisión correcta y asuma la responsabilidad. Actividades típicas de una persona así: especialidades de riesgo: conductor, escalador, examinador, bombero, rescatista, psiquiatra, médico de ambulancia, empleado del servicio secreto, censor . "
            if summa_u_5 == 9:
                u_text = "Los Nueve son vagos, tienen muchos deseos y catastróficamente poca energía para realizarlos. Por lo tanto, continúan soñando con algo y no hacen nada por esto durante años. Con la esperanza de que todo se haga realidad por sí solo, estas personas simplemente se van con la corriente. Estos nueves se distinguen por su amabilidad y dulzura. \n " \
                         " \n " \
                         "Consejo: necesitamos deshacernos de los estereotipos, contribuir a la creación de una nueva cosmovisión, construida sobre un estudio profundo de diversas culturas, tradiciones científicas y religiosas. Las mejores áreas de aplicación de sus talentos: filosofía, estudios culturales, sociología, propaganda, docencia, actividades religiosas y sociales "
            if summa_r_5 == 1:
                r_text = "Las unidades son amantes de la libertad, a menudo egoístas. Estas personas luchan por la independencia, invierten en el desarrollo y la autorrealización. La capacidad de dirigir energía incontenible en la dirección correcta ayudará a las unidades a lograr un gran éxito en la vida. Entre ellas hay muchas naturalezas creativas, activas y que necesitan un movimiento constante hacia adelante. \n "
            if summa_r_5 == 2:
                r_text = "La calma y el equilibrio inherentes a los deuces les permiten pensar con objetividad y tomar decisiones deliberadas. Intentan guiarse por la lógica y el sentido común. Excelentes diplomáticos, son capaces de resolver cualquier conflicto de forma pacífica. Se caracterizan por la amabilidad, el tacto en asuntos delicados y un carácter amable. \n "
            if summa_r_5 == 3:
                r_text = "Los tres son afortunados como ningún otro. Por su naturaleza, suelen ser personas optimistas que no se rinden incluso cuando se enfrentan a los desafíos más difíciles de la vida. A menudo son talentosos, aprenden fácilmente cualquier oficio, son sociables y les gustan las personas. , tengo muchos amigos. \n "
            if summa_r_5 == 4:
                r_text = " Valoran el orden y la practicidad, la estabilidad y la tranquilidad. Materialistas hasta la médula, a los cuatro no les gustan las reuniones ruidosas y las emociones fuertes. Su principal preocupación es el bienestar financiero, la constancia de la comodidad. Son personas con principios, pueden ser confiados con sus secretos y no preocuparse por su seguridad. Estas personas tienen pocos amigos, pero los que existen son camaradas devotos y probados a lo largo de los años. \n "
            if summa_r_5 == 5:
                r_text = "Aventureros, los cinco aprecian la emoción y el cambio en la vida. Estas personas no toleran la monotonía y pierden rápidamente el interés en cualquier actividad monótona. A menudo son impredecibles, pueden cambiar de opinión rápidamente y, por lo tanto, no son confiables. \n "
            if summa_r_5 == 6:
                r_text = "A las personas con el nombre número 6 les encanta estar en el centro de atención, a menudo son arrogantes y egoístas. Por lo general, cuidan de los demás solo si les brinda satisfacción moral de sus acciones. Hay muchas personas de este número en el mundo del espectáculo y otras profesiones públicas. \n "
            if summa_r_5 == 7:
                r_text = "Personalidad misteriosa. Pasando mucho tiempo buscándose a sí mismos, muchos sietes se enfrentan a la falta de comprensión de los demás y permanecen solos. Piensan seriamente en su propósito y el significado de la vida humana. Estos son individuos dotados, a menudo con sensibilidad extrasensorial, por ejemplo, capaz de predecir el futuro. \n "
            if summa_r_5 == 8:
                r_text = "Líderes por naturaleza, los Ocho son increíblemente trabajadores y resistentes . Sus habilidades organizativas naturales, dedicación e inteligencia poco común les permiten alcanzar sus objetivos. \n "
            if summa_r_5 == 9:
                r_text = "Los Nueve son vagos, tienen muchos deseos y catastróficamente poca energía para realizarlos. Por lo tanto, continúan soñando con algo y no hacen nada por esto durante años. Con la esperanza de que todo se haga realidad por sí solo, estas personas simplemente se van con la corriente. Estos nueves se distinguen por su amabilidad y dulzura. \n "
            if (summa_u_5 == 1 and summa_r_5 == 1) or (summa_u_5 == 1 and summa_r_5 == 1):
                total_text = "1 y 1: Dos personalidades fuertes amantes de la libertad que no pueden ceder el uno al otro. Si esto crea conflictos, aprenda a contener las emociones negativas y razone con sensatez"
            if (summa_u_5 == 1 and summa_r_5 == 2) or (summa_u_5 == 2 and summa_r_5 == 1):
                total_text = "1 y 2: Los unos funcionan y los dos los inspiran. Sigan con el buen trabajo, motívense mutuamente para lograr nuevos logros y crecimiento personal"
            if (summa_u_5 == 1 and summa_r_5 == 3) or (summa_u_5 == 3 and summa_r_5 == 1):
                total_text = "1 y 3: Las ideas e intenciones del trío pueden ser suprimidas por 1. La clara distribución de responsabilidades y el orden de toma de decisiones en la pareja ayudará a establecer relaciones."
            if (summa_u_5 == 1 and summa_r_5 == 4) or (summa_u_5 == 4 and summa_r_5 == 1):
                total_text = "1 y 4: La combinación de lo incompatible: dos opuestos, energía y moderación pueden complementarse entre sí, si aprendes a escuchar a tu pareja"
            if (summa_u_5 == 1 and summa_r_5 == 5) or (summa_u_5 == 5 and summa_r_5 == 1):
                total_text = "1 y 5: Las relaciones se basan en la pasión y la sensualidad. Las expresiones de amor apasionado pueden volverse rápidamente aburridas e incluso aburridas, así que tómate un descanso con regularidad"
            if (summa_u_5 == 1 and summa_r_5 == 6) or (summa_u_5 == 6 and summa_r_5 == 1):
                total_text = "1 y 6: combinación perfecta. La unidad emocional y amante de la libertad encuentra comprensión del 6. Cuidarse y amar el uno al otro ayudará a mantener y desarrollar su unión"
            if (summa_u_5 == 1 and summa_r_5 == 7) or (summa_u_5 == 7 and summa_r_5 == 1):
                total_text = "1 y 7: La combinación de la extraversión de uno y la introversión de los siete, sujeta al respeto mutuo, permitirá que los socios se complementen exitosamente"
            if (summa_u_5 == 1 and summa_r_5 == 8) or (summa_u_5 == 8 and summa_r_5 == 1):
                total_text = "1 y 8: Buena compatibilidad numerológica, basada en la relación afectuosa y cálida de los socios entre sí"
            if (summa_u_5 == 1 and summa_r_5 == 9) or (summa_u_5 == 9 and summa_r_5 == 1):
                total_text = "1 y 9: Una unidad emprendedora y entusiasta encontrará apoyo en los nueve. El autocontrol solo mejorará el ambiente en una pareja"
            if (summa_u_5 == 2 and summa_r_5 == 2) or (summa_u_5 == 2 and summa_r_5 == 2):
                total_text = "2 y 2: Compañerismo perfecto. En las relaciones románticas, tenga cuidado con el impacto negativo de la vida cotidiana en la diversidad de las relaciones"
            if (summa_u_5 == 2 and summa_r_5 == 3) or (summa_u_5 == 3 and summa_r_5 == 2):
                total_text = "2 y 3: El deuce da una sensación de seguridad y estabilización, mientras que la troika inspira optimismo y comparte iniciativa. Esta unión es bastante armoniosa"
            if (summa_u_5 == 2 and summa_r_5 == 4) or (summa_u_5 == 4 and summa_r_5 == 2):
                total_text = "2 y 4: Excelente compatibilidad debido al cuidado y afecto de los socios entre sí. Las disputas en tal alianza son invitados raros."
            if (summa_u_5 == 2 and summa_r_5 == 5) or (summa_u_5 == 5 and summa_r_5 == 2):
                total_text = "2 y 5: Personas amantes de la libertad que se sienten atraídas entre sí. Aprenda a controlar sus emociones durante las peleas y los problemas familiares"
            if (summa_u_5 == 2 and summa_r_5 == 6) or (summa_u_5 == 6 and summa_r_5 == 2):
                total_text = "2 y 6: Una buena pareja, cuya relación se basa en la ternura, el respeto mutuo y el sentido de responsabilidad hacia la pareja. La sinceridad hace que la relación sea absolutamente armoniosa"
            if (summa_u_5 == 2 and summa_r_5 == 7) or (summa_u_5 == 7 and summa_r_5 == 2):
                total_text = "2 y 7: En esta pareja reinan la constancia, la tranquilidad y la seriedad. Sin embargo, a veces al deuce le molesta la lentitud del siete y su susceptibilidad a la mala influencia del exterior"
            if (summa_u_5 == 2 and summa_r_5 == 8) or (summa_u_5 == 8 and summa_r_5 == 2):
                total_text = "2 y 8: El 8 está tratando de reprimir la iniciativa del 2. Aprenda a hacer concesiones entre sí, acuerde compartir las tareas del hogar de manera justa y la paz reinará en la relación"
            if (summa_u_5 == 2 and summa_r_5 == 9) or (summa_u_5 == 9 and summa_r_5 == 2):
                total_text = "2 y 9: Diferentes visiones de la vida no les impiden estar juntos. El amor de un nueve por salir se opone al hogar de dos. Aceptarse el uno al otro como está mantendrá la unión por muchos años. "
            if (summa_u_5 == 3 and summa_r_5 == 3) or (summa_u_5 == 3 and summa_r_5 == 3):
                total_text = "3 y 3: La amistad de dos trillizos se basa en la máxima confianza el uno en el otro. El amor en una unión así puede durar poco."
            if (summa_u_5 == 3 and summa_r_5 == 4) or (summa_u_5 == 4 and summa_r_5 == 3):
                total_text = "3 y 4: Esta es una unión fuerte basada en la adición exitosa del temperamento del 3 con el equilibrio del 4. Comprender las necesidades íntimas y emocionales de la pareja hará felices a ambos"
            if (summa_u_5 == 3 and summa_r_5 == 5) or (summa_u_5 == 5 and summa_r_5 == 3):
                total_text = "3 y 5: Los intereses comunes - viajes, entretenimiento - combinan tres y cinco. Pueden surgir conflictos en el contexto de dificultades financieras, preste mucha atención a esto."
            if (summa_u_5 == 3 and summa_r_5 == 6) or (summa_u_5 == 6 and summa_r_5 == 3):
                total_text = "3 y 6: ambos socios son personas bondadosas y comprensivas. En tal relación, reinan la armonía y la calidez"
            if (summa_u_5 == 3 and summa_r_5 == 7) or (summa_u_5 == 7 and summa_r_5 == 3):
                total_text = "3 y 7: La proximidad intelectual de un 3 y un 7 no compensa la diferencia de temperamento. Aprende a ceder a la otra mitad."
            if (summa_u_5 == 3 and summa_r_5 == 8) or (summa_u_5 == 8 and summa_r_5 == 3):
                total_text = "3 y 8: La energía y la independencia de los socios les permite estar en la misma longitud de onda, uno debe tener cuidado con un deseo excesivo de liderazgo de ambos"
            if (summa_u_5 == 3 and summa_r_5 == 9) or (summa_u_5 == 9 and summa_r_5 == 3):
                total_text = "3 y 9: Las relaciones son armoniosas, los socios encajan. Los conflictos son raros y de corta duración."
            if (summa_u_5 == 4 and summa_r_5 == 4) or (summa_u_5 == 4 and summa_r_5 == 4):
                total_text = "4 y 4: En general, la relación es estable, pero la tendencia de ambos a ser tercos puede llevar a peleas prolongadas. Aprende a lidiar con estas situaciones de manera pacífica"
            if (summa_u_5 == 4 and summa_r_5 == 5) or (summa_u_5 == 5 and summa_r_5 == 4):
                total_text = "4 y 5: Esta pareja tiene una fuerte atracción combinada con diferentes personalidades. Lo que enciende a uno puede aburrirse rápidamente con otro. Aprenda a expresar abiertamente sus deseos y a negociar"
            if (summa_u_5 == 4 and summa_r_5 == 6) or (summa_u_5 == 6 and summa_r_5 == 4):
                total_text = "4 y 6: esta pareja es envidiable en términos de compatibilidad. Objetivos comunes, hábitos, una visión similar de la vida. Esta relación está llena de calidez y respeto"
            if (summa_u_5 == 4 and summa_r_5 == 7) or (summa_u_5 == 7 and summa_r_5 == 4):
                total_text = "4 y 7: El miedo a expresar sentimientos puede enfriar un poco esta relación. Siéntete libre de ser cariñoso y cariñoso con tu ser querido"
            if (summa_u_5 == 4 and summa_r_5 == 8) or (summa_u_5 == 8 and summa_r_5 == 4):
                total_text = "4 y 8: El deseo de crear una familia une a estos socios, pero la mayor atención de ambos al bienestar material puede distraerlos del lado sensual de la relación"
            if (summa_u_5 == 4 and summa_r_5 == 9) or (summa_u_5 == 9 and summa_r_5 == 4):
                total_text = "4 y 9: La atracción física elimina todas las contradicciones intelectuales en una pareja, en caso de conflictos, los socios deben tratar de suavizar las diferencias"
            if (summa_u_5 == 5 and summa_r_5 == 5) or (summa_u_5 == 5 and summa_r_5 == 5):
                total_text = "5 y 5: Dos cinco a menudo se enamoran a primera vista. El punto débil de una relación es el deseo de cambio"
            if (summa_u_5 == 5 and summa_r_5 == 6) or (summa_u_5 == 6 and summa_r_5 == 5):
                total_text = "5 y 6: 5 aman el cambio, 6 aman la coherencia. Aprenda a aceptar los rasgos de personalidad de su pareja"
            if (summa_u_5 == 5 and summa_r_5 == 7) or (summa_u_5 == 7 and summa_r_5 == 5):
                total_text = "5 y 7: Extrovertido e introvertido: estas personas deben cuidarse entre sí y tener en cuenta esas peculiaridades, entonces la unión será larga"
            if (summa_u_5 == 5 and summa_r_5 == 8) or (summa_u_5 == 8 and summa_r_5 == 5):
                total_text = "5 y 8: Al 5 le gusta la estabilidad y el éxito del 8, y el 8, a su vez, atrae la espontaneidad y la alegría del 5. Aceptar los defectos de la pareja construirá relaciones sólidas"
            if (summa_u_5 == 5 and summa_r_5 == 9) or (summa_u_5 == 9 and summa_r_5 == 5):
                total_text = "5 y 9: Ambos son soñadores y les encanta hacer planes para el futuro. No te rindas ante los contratiempos, aprende perseverancia y tu unión perdurará."
            if (summa_u_5 == 6 and summa_r_5 == 6) or (summa_u_5 == 6 and summa_r_5 == 6):
                total_text = "6 y 6: Tener prioridades similares en la vida ayudará a una pareja a entenderse, pero temerá las dificultades económicas. Aprenda a sobrellevar tal confusión y esfuércese por mantenerse en pie"
            if (summa_u_5 == 6 and summa_r_5 == 7) or (summa_u_5 == 7 and summa_r_5 == 6):
                total_text = "6 y 7: En general, los socios se adaptan entre sí, pero pueden surgir dificultades debido a la intemperancia y la intolerancia al comportamiento del socio"
            if (summa_u_5 == 6 and summa_r_5 == 8) or (summa_u_5 == 8 and summa_r_5 == 6):
                total_text = "6 y 8: Mantener un equilibrio entre lo espiritual y lo material evitará la frustración de buscar la comodidad."
            if (summa_u_5 == 6 and summa_r_5 == 9) or (summa_u_5 == 9 and summa_r_5 == 6):
                total_text = "6 y 9: Ambos se inclinan a soñar despiertos, las parejas son bastante capaces de lograr sus objetivos. Las relaciones son armoniosas tanto física como espiritualmente."
            if (summa_u_5 == 7 and summa_r_5 == 7) or (summa_u_5 == 7 and summa_r_5 == 7):
                total_text = "7 y 7: Ambos son introvertidos, aprecian la tranquilidad y la regularidad en la vida. Una pareja maravillosa, compatible en todos los ámbitos, pueden contar con una relación a largo plazo basada en el amor y el respeto mutuo"
            if (summa_u_5 == 7 and summa_r_5 == 8) or (summa_u_5 == 8 and summa_r_5 == 7):
                total_text = "7 y 8: 7 valores espirituales, 8 - material. Este enfoque es ideal para asociaciones comerciales"
            if (summa_u_5 == 7 and summa_r_5 == 9) or (summa_u_5 == 9 and summa_r_5 == 7):
                total_text = "7 y 9: La capacidad de los idealistas soñadores para apoyarse mutuamente en situaciones difíciles puede hacer feliz a esa unión"
            if (summa_u_5 == 8 and summa_r_5 == 8) or (summa_u_5 == 8 and summa_r_5 == 8):
                total_text = "8 y 8: Tienen una fuerte atracción el uno por el otro, pero debido a la impaciencia y la ambición de los socios, a menudo pueden ocurrir peleas en una pareja así. Aprenda a ceder y no se obsesione con las nimiedades."
            if (summa_u_5 == 8 and summa_r_5 == 9) or (summa_u_5 == 9 and summa_r_5 == 8):
                total_text = "8 y 9: Estas personas se complementan perfectamente en las relaciones comerciales. Los ocho son temperamentales, y a los nueves les gusta y les anima a llevar a cabo sus planes. Compatibilidad de buen nombre para las relaciones comerciales."
            if (summa_u_5 == 9 and summa_r_5 == 9) or (summa_u_5 == 9 and summa_r_5 == 9):
                total_text = "9 y 9: En tal relación, reinan el entendimiento mutuo, la ternura y la lealtad. Ambos socios valoran la personalidad del otro, apoyando el deseo de la otra mitad de autodesarrollo y crecimiento interior"
            try:
                telegraph.create_account(short_name='совместимость')
                response = telegraph.create_page(
                    f'Compatibilidad de nombres {names_split[0]} y {names_split[1]}',
                    html_content=f'🔮<b>Tu nombre ({names_split[0]}) coincide con el número {summa_u_5}</b><br>'
                                 f'{u_text}<br>'
                                 f'<br>'
                                 f'🔮<b>Nombre del socio ({names_split[1]}) coincide con el número {summa_r_5}</b><br>'
                                 f'{r_text}<br>'
                                 f'<br>'
                                 f'👫<b>Compatibilidad</b> {total_text}'
                )
                link = 'http://telegra.ph/{}'.format(response['path'])
                msg_text = hlink(" ", link)
                await message.answer(f"Resultado del{msg_text}cálculo", reply_markup=back_compatibility_es)
                await state.finish()
            except:
                await message.answer(f"Ingresaste los nombres incorrectos\n"
                                     f"\n"
                                     f"<i>Ingréselos en el formato: Michelle John (en inglés)</i>",
                                     reply_markup=back_compatibility_es)
        else:
            await message.answer(f"Ingresaste los nombres incorrectos\n"
                                 f"\n"
                                 f"<i>Ingréselos en el formato: Michelle John (en inglés)</i>",
                                 reply_markup=back_compatibility_es)
    if user.language == "de":
        names_split = names.split()
        x = 0
        for i in names_split:
            x += 1
        if x == 2:
            summ1 = 0
            summ2 = 0
            for y in names_split[0]:
                for z in y:
                    if z in ("a", "j", "s", "A", "J", "S"):
                        summ1 += 1
                    if z in ("b", "k", "t", "B", "K", "T"):
                        summ1 += 2
                    if z in ("c", "l", "u", "C", "L", "U"):
                        summ1 += 3
                    if z in ("d", "m", "v", "D", "M", "V"):
                        summ1 += 4
                    if z in ("e", "n", "w", "E", "N", "W"):
                        summ1 += 5
                    if z in ("f", "o", "x", "F", "O", "X"):
                        summ1 += 6
                    if z in ("g", "p", "y", "G", "P", "Y"):
                        summ1 += 7
                    if z in ("h", "q", "z", "H", "Q", "Z"):
                        summ1 += 8
                    if z in ("i", "r", "I", "R"):
                        summ1 += 9
            for y in names_split[1]:
                for z in y:
                    if z in ("a", "j", "s", "A", "J", "S"):
                        summ2 += 1
                    if z in ("b", "k", "t", "B", "K", "T"):
                        summ2 += 2
                    if z in ("c", "l", "u", "C", "L", "U"):
                        summ2 += 3
                    if z in ("d", "m", "v", "D", "M", "V"):
                        summ2 += 4
                    if z in ("e", "n", "w", "E", "N", "W"):
                        summ2 += 5
                    if z in ("f", "o", "x", "F", "O", "X"):
                        summ2 += 6
                    if z in ("g", "p", "y", "G", "P", "Y"):
                        summ2 += 7
                    if z in ("h", "q", "z", "H", "Q", "Z"):
                        summ2 += 8
                    if z in ("i", "r", "I", "R"):
                        summ2 += 9
            summa_u_1 = 0
            summa_r_1 = 0
            summa_u_2 = 0
            summa_r_2 = 0
            summa_u_3 = 0
            summa_r_3 = 0
            summa_u_4 = 0
            summa_r_4 = 0
            summa_u_5 = 0
            summa_r_5 = 0
            for f in str(summ1):
                print("summ1 = ", summ1)
                summa_u_1 += int(f)
            for f in str(summa_u_1):
                summa_u_2 += int(f)
            for f in str(summa_u_2):
                summa_u_3 += int(f)
            for f in str(summa_u_3):
                summa_u_4 += int(f)
            for f in str(summa_u_4):
                summa_u_5 += int(f)
            for f in str(summ2):
                print("summ2 = ", summ2)
                summa_r_1 += int(f)
            for f in str(summa_r_1):
                summa_r_2 += int(f)
            for f in str(summa_r_2):
                summa_r_3 += int(f)
            for f in str(summa_r_3):
                summa_r_4 += int(f)
            for f in str(summa_r_4):
                summa_r_5 += int(f)
            if summa_u_5 == 1:
                u_text = "Einheiten sind freiheitsliebend, oft egoistisch. Solche Menschen streben nach Unabhängigkeit, investieren Kraft in die Selbstentwicklung und Selbstverwirklichung. Die Fähigkeit, unbändige Energie in die richtige Richtung zu lenken, wird Einheiten zu großem Erfolg im Leben verhelfen es gibt viele kreative Naturen, die aktiv sind und ständiger Bewegung bedürfen. \n " \
                         " \n " \
                         "Beratung: Entwickeln Sie Ehrgeiz, Zielstrebigkeit, Diplomatie, lernen Sie, schnell auf eine sich ändernde Situation zu reagieren. Sie können sich im öffentlichen Dienst, in der Politik, in der Medizin, in der Forschung, in der Luft- und Raumfahrt, im Maschinenbau und im Bergbau, in der Avantgarde verwirklichen. Garde-Kunst."
            if summa_u_5 == 2:
                u_text = "Die Ruhe und Ausgeglichenheit von Zweien ermöglichen es ihnen, objektiv zu denken und bewusste Entscheidungen zu treffen. Sie versuchen, sich von Logik und gesundem Menschenverstand leiten zu lassen. Ausgezeichnete Diplomaten, sie sind in der Lage, jeden Konflikt friedlich zu lösen. Sie zeichnen sich durch Freundlichkeit und Taktgefühl aus in zarten Dingen und einem sanften Charakter. \n " \
                         " \n " \
                         "Ratschlag: kultiviere Geduld, Fleiß, Ausdauer, Ausdauer. Du kannst dich als Finanzier, Archivar, Museum, Bibliothek, Handel, Mode, Landwirtschaft, Ernährung und Lebensmittelproduktion beweisen."
            if summa_u_5 == 3:
                u_text = " Dreier haben Glück wie kein Zweiter . Von Natur aus sind sie meist optimistische Menschen, die auch bei den schwierigsten Herausforderungen des Lebens nicht aufgeben. Sie sind oft talentiert, lernen leicht jedes Handwerk, sind kontaktfreudig und menschenähnlich , viele Freunde haben. \n " \
                         " \n " \
                         "Ratschlag: Sie sollten Kontakte knüpfen, Menschen führen, zum Kern eines Teams werden, diplomatische Fähigkeiten entwickeln, das Misstrauen gegenüber der Welt und den Menschen überwinden. Sie können den Weg eines Dichters, Malers, Schriftstellers, Diplomaten, Kaufmanns, Journalisten wählen , Regisseur, Musiker, Tänzer, Reisender oder Handwerker."
            if summa_u_5 == 4:
                u_text = "Sie legen Wert auf Ordnung und Zweckmäßigkeit, Stabilität und Ruhe. Materialisten bis ins Mark, Vierer mögen keine lauten Versammlungen und Nervenkitzel. Ihr Hauptanliegen ist das finanzielle Wohlergehen, die Beständigkeit des Komforts. Dies sind Menschen mit Prinzipien, sie können sein betraut mit ihren Geheimnissen und nicht Sorge um ihre Sicherheit. Solche Leute haben wenige Freunde, aber diejenigen , die existieren gewidmet sind und bewährten Kameraden im Laufe der Jahre. \n " \
                         " \n " \
                         "Rat: Finden Sie sich selbst und stärken Sie Ihren inneren Kern, setzen Sie auf Traditionen, lernen Sie, nicht nur für sich und Ihr Geschäft, sondern auch für Ihre Umgebung verantwortlich zu sein. Am besten können Sie sich im Studium der Geschichte oder Archäologie ausdrücken, sich engagieren Hotel- oder Restaurantbetrieb, Museumsbetrieb, Restaurierung, Architektur, Chemie oder Produktherstellung."
            if summa_u_5 == 5:
                u_text = "Abenteurer, Fünfer schätzen den Nervenkitzel und die Veränderung im Leben. Diese Menschen tolerieren keine Monotonie und verlieren schnell das Interesse an monotonen Aktivitäten. Sie sind oft unberechenbar, können ihre Meinung schnell ändern und sind daher nicht zuverlässig. \n " \
                         " \n " \
                         "Ratschlag: Lernen Sie, ungewöhnliche Entscheidungen zu treffen und haben Sie keine Angst, alles aufs Spiel zu setzen. Sie müssen selbst suchen, wo Sie gute Arbeit leisten müssen. Sie können sich im Schmuck- und Waffengeschäft beweisen, ein Plastik- und Herzschlager werden Chirurg, Zahnarzt und Restaurator. Sie können ins Kino oder ins Fernsehen gehen, eine Führungspersönlichkeit werden."
            if summa_u_5 == 6:
                u_text = "Menschen mit dem Namen Nummer 6 stehen gerne im Rampenlicht, sind oft arrogant und egoistisch. Sie kümmern sich normalerweise nur um andere, wenn es ihnen moralische Befriedigung durch ihr Handeln bringt. Es gibt viele Menschen dieser Nummer im Showbusiness und andere öffentliche Berufe. \n " \
                         " \n " \
                         "Ratschlag: bleib innerlich frei, gehorche den Umständen, aber verwandle dich nicht in ihre Sklavin. Lerne, schwierige Dinge vertraut, vertraut - leicht, leicht - schön zu machen. Du kannst dich dort beweisen, wo Disziplin, Fleiß, Ausdauer, Genauigkeit und Ausdauer gefragt sind . Für die Berufe Analytiker, Philosophen, Forscher, Ökonomen, Physiker, Biologen, Mathematiker, Beamte, Militärs und Politiker passen sogar Apotheker am besten zu Ihnen."
            if summa_u_5 == 7:
                u_text = "Mysteriöse Persönlichkeit. Viele Siebener verbringen viel Zeit auf der Suche nach sich selbst und sind mit einem Mangel an Verständnis für andere konfrontiert und bleiben allein. Sie denken ernsthaft über ihren Zweck und den Sinn des menschlichen Lebens nach. Dies sind oft begabte Individuen mit übersinnlicher Sensibilität, zum Beispiel in der Lage, die Zukunft vorherzusagen. \n " \
                         " \n " \
                         "Ratschlag: Lerne, mit allen, mit denen dich das Schicksal gebracht hat, eine gemeinsame Sprache zu finden, versuche nicht, alle zu unterwerfen, besiege Feinde und Feinde um jeden Preis, befreie dich vom Egozentrismus. Von einer solchen Person zu arbeiten erfordert Ehrgeiz, Diplomatie, die Fähigkeit zu verhandeln, Rechtsstreitigkeiten im Zusammenhang mit dem Schutz."
            if summa_u_5 == 8:
                u_text = "Die Eights sind von Natur aus Führungskräfte, die unglaublich fleißig und belastbar sind . Ihre natürlichen Organisationsfähigkeiten, Entschlossenheit und außergewöhnliche Intelligenz ermöglichen es ihnen, ihre Ziele zu erreichen. \n " \
                         " \n " \
                         "Tipp: lernen, sich in ständig wechselnden Situationen zurechtzufinden, die richtige Wahl zu treffen und Verantwortung dafür zu übernehmen. Typische Tätigkeiten für eine solche Person: riskante Spezialitäten - Fahrer, Bergsteiger, Tester, Feuerwehrmann, Retter, Psychiater, Rettungsarzt, Geheimdienstmitarbeiter, Zensor . "
            if summa_u_5 == 9:
                u_text = "Neunen sind faul, sie haben viele Wünsche und katastrophal wenig Energie, um sie zu verwirklichen. Deshalb träumen sie weiter von etwas und tun jahrelang nichts dafür. In der Hoffnung, dass sich alles von selbst erfüllt, gehen diese Leute einfach hin mit dem Fluss. Diese Neunen zeichnen sich durch ihre Freundlichkeit und Sanftmut aus. \n " \
                         " \n " \
                         "Ratschlag: Wir müssen Stereotype loswerden, zur Schaffung einer neuen Weltanschauung beitragen, die auf einem tiefen Studium verschiedener Kulturen, wissenschaftlicher und religiöser Traditionen basiert. Die besten Anwendungsgebiete ihrer Talente: Philosophie, Kulturwissenschaften, Soziologie, Propaganda, Lehre, religiöse und soziale Aktivitäten."
            if summa_r_5 == 1:
                r_text = "Einheiten sind freiheitsliebend, oft egoistisch. Solche Menschen streben nach Unabhängigkeit, investieren in Selbstentwicklung und Selbstverwirklichung. Die Fähigkeit, unbändige Energie in die richtige Richtung zu lenken, wird Einheiten zu großem Erfolg im Leben verhelfen. Unter ihnen es gibt viele kreativen Naturen, aktiv und in der Notwendigkeit der ständigen Bewegung nach vorn. \n "
            if summa_r_5 == 2:
                r_text = "Die Ruhe und Ausgeglichenheit, die Zweien innewohnen, ermöglichen es ihnen, objektiv zu denken und bewusste Entscheidungen zu treffen. Sie versuchen, sich von Logik und gesundem Menschenverstand leiten zu lassen. Ausgezeichnete Diplomaten, sie sind in der Lage, jeden Konflikt friedlich beizulegen. Sie zeichnen sich durch Freundlichkeit und Taktgefühl aus in zarten Dingen und einem sanften Charakter. \n "
            if summa_r_5 == 3:
                r_text = " Drei haben Glück wie kein Zweiter . Von Natur aus sind sie meist optimistische Menschen, die auch bei den schwierigsten Herausforderungen des Lebens nicht aufgeben. Sie sind oft talentiert, erlernen jedes HandwFerk leicht, sind kontaktfreudig und menschenähnlich , habe viele Freunde. \n "
            if summa_r_5 == 4:
                r_text = "Sie legen Wert auf Ordnung und Zweckmäßigkeit, Stabilität und Ruhe. Materialisten durch und durch, Vierer mögen keine lauten Versammlungen und Nervenkitzel. Ihr Hauptanliegen ist das finanzielle Wohlergehen, die Beständigkeit des Komforts. Dies sind Menschen mit Prinzipien, sie können sein mit ihren Geheimnissen anvertraut und sich keine Sorgen um ihre Sicherheit machen müssen. Solche Leute haben nur wenige Freunde, aber die, die es gibt, sind treue und bewährte Kameraden über die Jahre. \n "
            if summa_r_5 == 5:
                r_text = "Abenteurer, Fünfer schätzen den Nervenkitzel und die Veränderung im Leben. Diese Menschen tolerieren keine Monotonie und verlieren schnell das Interesse an monotonen Aktivitäten. Sie sind oft unberechenbar, können ihre Meinung schnell ändern und sind daher nicht zuverlässig. \n "
            if summa_r_5 == 6:
                r_text = "Menschen mit dem Namen Nummer 6 stehen gerne im Rampenlicht, sind oft arrogant und egoistisch. Sie kümmern sich normalerweise nur um andere, wenn es ihnen moralische Befriedigung durch ihr Handeln bringt. Es gibt viele Menschen dieser Nummer im Showbusiness und show andere öffentliche Berufe. \n "
            if summa_r_5 == 7:
                r_text = "Mysteriöse Persönlichkeit. Viele Siebener, die viel Zeit auf der Suche nach sich selbst verbringen, werden mit einem Mangel an Verständnis für andere konfrontiert und bleiben allein. Sie denken ernsthaft über ihren Zweck und den Sinn des menschlichen Lebens nach. Dies sind oft begabte Individuen mit extrasensory Empfindlichkeit, zum Beispiel, in der Lage , die Zukunft vorherzusagen. \n "
            if summa_r_5 == 8:
                r_text = "Die Eights sind von Natur aus Führungskräfte, die unglaublich fleißig und belastbar sind . Ihre natürlichen Organisationsfähigkeiten, ihr Engagement und ihre ungewöhnliche Intelligenz ermöglichen es ihnen, ihre Ziele zu erreichen. \n "
            if summa_r_5 == 9:
                r_text = "Neunen sind faul, sie haben viele Wünsche und katastrophal wenig Energie, um sie zu verwirklichen. Deshalb träumen sie weiter von etwas und tun jahrelang nichts dafür. In der Hoffnung, dass sich alles von selbst erfüllt, gehen diese Leute einfach hin mit dem Fluss. Diese Neunen zeichnen sich durch ihre Freundlichkeit und Sanftmut aus. \n "
            if (summa_u_5 == 1 and summa_r_5 == 1) or (summa_u_5 == 1 and summa_r_5 == 1):
                total_text = "1 und 1: Zwei freiheitsliebende starke Persönlichkeiten, die einander nicht nachgeben können. Wenn dies zu Konflikten führt, lerne, negative Emotionen zurückzuhalten und vernünftig zu argumentieren."
            if (summa_u_5 == 1 and summa_r_5 == 2) or (summa_u_5 == 2 and summa_r_5 == 1):
                total_text = "1 und 2: Die einen funktionieren und die beiden inspirieren sie. Mach weiter so - motiviere dich gegenseitig für neue Leistungen und persönliches Wachstum."
            if (summa_u_5 == 1 and summa_r_5 == 3) or (summa_u_5 == 3 and summa_r_5 == 1):
                total_text = "1 und 3: Die Ideen und Absichten des Trios können durch 1 unterdrückt werden. Die klare Verteilung der Verantwortlichkeiten und die Reihenfolge der Entscheidungsfindung im Paar hilft, Beziehungen aufzubauen."
            if (summa_u_5 == 1 and summa_r_5 == 4) or (summa_u_5 == 4 and summa_r_5 == 1):
                total_text = "1 und 4: Die Kombination des Unvereinbaren - zwei Gegensätze, Energie und Zurückhaltung können sich durchaus ergänzen, wenn Sie lernen, Ihrem Partner zuzuhören."
            if (summa_u_5 == 1 and summa_r_5 == 5) or (summa_u_5 == 5 and summa_r_5 == 1):
                total_text = "1 und 5: Beziehungen basieren auf Leidenschaft und Sinnlichkeit. Ausdrücke leidenschaftlicher Liebe können schnell langweilig und sogar ermüdend werden, also mach regelmäßig eine Pause."
            if (summa_u_5 == 1 and summa_r_5 == 6) or (summa_u_5 == 6 and summa_r_5 == 1):
                total_text = "1 und 6: Perfekte Kombination. Emotionale und freiheitsliebende Einheit findet Verständnis für 6. Sich umeinander zu kümmern und zu lieben wird helfen, Ihre Einheit zu erhalten und zu entwickeln."
            if (summa_u_5 == 1 and summa_r_5 == 7) or (summa_u_5 == 7 and summa_r_5 == 1):
                total_text = "1 und 7: Die Kombination aus der Extraversion der einen und der Introversion der Sieben unter gegenseitigem Respekt ermöglicht es den Partnern, sich erfolgreich zu ergänzen."
            if (summa_u_5 == 1 and summa_r_5 == 8) or (summa_u_5 == 8 and summa_r_5 == 1):
                total_text = "1 und 8: Gute numerologische Kompatibilität, basierend auf der liebevollen und herzlichen Beziehung der Partner zueinander."
            if (summa_u_5 == 1 and summa_r_5 == 9) or (summa_u_5 == 9 and summa_r_5 == 1):
                total_text = "1 und 9: Eine unternehmungslustige und enthusiastische Einheit wird in den Neun Unterstützung finden. Selbstbeherrschung verbessert nur die Atmosphäre in einem Paar."
            if (summa_u_5 == 2 and summa_r_5 == 2) or (summa_u_5 == 2 and summa_r_5 == 2):
                total_text = "2 und 2: Perfekte Kameradschaft. Hüten Sie sich in romantischen Beziehungen vor den negativen Auswirkungen des täglichen Lebens auf die Vielfalt in Beziehungen."
            if (summa_u_5 == 2 and summa_r_5 == 3) or (summa_u_5 == 3 and summa_r_5 == 2):
                total_text = "2 und 3: Der Zweier vermittelt ein Gefühl von Sicherheit und Stabilisierung, während die Troika Optimismus und Eigeninitiative weckt . Eine solche Union ist sehr harmonisch."
            if (summa_u_5 == 2 and summa_r_5 == 4) or (summa_u_5 == 4 and summa_r_5 == 2):
                total_text = "2 und 4: Hervorragende Verträglichkeit durch die Fürsorge und Zuneigung der Partner zueinander. Streitereien in einer solchen Allianz sind seltene Gäste."
            if (summa_u_5 == 2 and summa_r_5 == 5) or (summa_u_5 == 5 and summa_r_5 == 2):
                total_text = "2 und 5: Freiheitsliebende Menschen, die sich zueinander hingezogen fühlen . Lernen Sie, Ihre Emotionen bei Streitigkeiten und Familienproblemen zu kontrollieren."
            if (summa_u_5 == 2 and summa_r_5 == 6) or (summa_u_5 == 6 and summa_r_5 == 2):
                total_text = "2 und 6: Ein gutes Paar, dessen Beziehung auf Zärtlichkeit, gegenseitigem Respekt und Verantwortungsbewusstsein für den Partner basiert. Aufrichtigkeit macht die Beziehung absolut harmonisch."
            if (summa_u_5 == 2 and summa_r_5 == 7) or (summa_u_5 == 7 and summa_r_5 == 2):
                total_text = "2 und 7: Konstanz, Ruhe und Verlässlichkeit herrschen in diesem Paar. Manchmal ärgert sich die Zwei jedoch über die Langsamkeit der Sieben und ihre Anfälligkeit für schlechten Einfluss von außen."
            if (summa_u_5 == 2 and summa_r_5 == 8) or (summa_u_5 == 8 and summa_r_5 == 2):
                total_text = "2 und 8: Die 8 versucht, die Initiative der 2 zu unterdrücken. Lernen Sie, einander Zugeständnisse zu machen, einigen Sie sich auf eine faire Aufteilung der Hausarbeit und Frieden wird in der Beziehung herrschen."
            if (summa_u_5 == 2 and summa_r_5 == 9) or (summa_u_5 == 9 and summa_r_5 == 2):
                total_text = "2 und 9: Unterschiedliche Lebensauffassungen hindern euch nicht daran, zusammen zu sein. Die Liebe einer Neun zum Ausgehen steht dem Zuhause von zwei entgegen. Die gegenseitige Akzeptanz, so wie ihr seid, wird die Verbindung für viele Jahre halten. "
            if (summa_u_5 == 3 and summa_r_5 == 3) or (summa_u_5 == 3 and summa_r_5 == 3):
                total_text = "3 und 3: Die Freundschaft zweier Drillinge basiert auf maximalem Vertrauen zueinander. Liebe in einer solchen Verbindung kann nur von kurzer Dauer sein."
            if (summa_u_5 == 3 and summa_r_5 == 4) or (summa_u_5 == 4 and summa_r_5 == 3):
                total_text = "3 und 4: Dies ist eine starke Vereinigung, die auf der erfolgreichen Addition des Temperaments der 3 mit der Gelassenheit der 4 basiert. Das Verständnis der intimen und emotionalen Bedürfnisse des Partners wird beide glücklich machen."
            if (summa_u_5 == 3 and summa_r_5 == 5) or (summa_u_5 == 5 and summa_r_5 == 3):
                total_text = "3 und 5: Gemeinsame Interessen - Reisen, Unterhaltung - kombinieren Sie drei und fünf. Konflikte können vor dem Hintergrund finanzieller Schwierigkeiten entstehen, achten Sie genau darauf."
            if (summa_u_5 == 3 and summa_r_5 == 6) or (summa_u_5 == 6 and summa_r_5 == 3):
                total_text = "3 und 6: Beide Partner sind gutmütige, sympathische Menschen. In einer solchen Beziehung herrschen Harmonie und Wärme."
            if (summa_u_5 == 3 and summa_r_5 == 7) or (summa_u_5 == 7 and summa_r_5 == 3):
                total_text = "3 und 7: Die intellektuelle Nähe einer 3 und einer 7 gleicht den Temperamentunterschied nicht aus. Lerne, der anderen Hälfte nachzugeben."
            if (summa_u_5 == 3 and summa_r_5 == 8) or (summa_u_5 == 8 and summa_r_5 == 3):
                total_text = "3 und 8: Die Energie und Unabhängigkeit der Partner ermöglicht es ihnen, auf einer Wellenlänge zu sein, man sollte sich vor einem übermäßigen Wunsch nach Führung beider hüten ."
            if (summa_u_5 == 3 and summa_r_5 == 9) or (summa_u_5 == 9 and summa_r_5 == 3):
                total_text = "3 und 9: Beziehungen sind harmonisch, Partner passen zusammen. Konflikte sind selten und von kurzer Dauer."
            if (summa_u_5 == 4 and summa_r_5 == 4) or (summa_u_5 == 4 and summa_r_5 == 4):
                total_text = "4 und 4: Im Allgemeinen ist die Beziehung stabil, aber die Neigung beider, stur zu sein, kann zu langwierigen Kämpfen führen. Lerne, mit solchen Situationen friedlich umzugehen."
            if (summa_u_5 == 4 and summa_r_5 == 5) or (summa_u_5 == 5 and summa_r_5 == 4):
                total_text = "4 und 5: Dieses Paar hat eine starke Anziehungskraft, kombiniert mit unterschiedlichen Persönlichkeiten. Was einen anmacht, kann einem anderen schnell langweilig werden. Lerne, deine Wünsche offen zu äußern und zu verhandeln."
            if (summa_u_5 == 4 and summa_r_5 == 6) or (summa_u_5 == 6 and summa_r_5 == 4):
                total_text = "4 und 6: Dieses Paar ist beneidenswert in Bezug auf die Kompatibilität. Gemeinsame Ziele, Gewohnheiten, ähnliche Lebenseinstellung. Eine solche Beziehung ist voller Wärme und Respekt."
            if (summa_u_5 == 4 and summa_r_5 == 7) or (summa_u_5 == 7 and summa_r_5 == 4):
                total_text = "4 und 7: Angst, Gefühle auszudrücken, kann diese Beziehung etwas abkühlen. Seien Sie ruhig und fürsorglich mit Ihrem geliebten Menschen."
            if (summa_u_5 == 4 and summa_r_5 == 8) or (summa_u_5 == 8 and summa_r_5 == 4):
                total_text = "4 und 8: Der Wunsch, eine Familie zu gründen, bringt diese Partner zusammen, aber die erhöhte Aufmerksamkeit beider auf das materielle Wohlergehen kann sie von der sinnlichen Seite der Beziehung ablenken."
            if (summa_u_5 == 4 and summa_r_5 == 9) or (summa_u_5 == 9 and summa_r_5 == 4):
                total_text = "4 und 9: Körperliche Anziehung beseitigt alle intellektuellen Widersprüche bei einem Paar, bei Konflikten sollten die Partner versuchen, die Unterschiede auszugleichen ."
            if (summa_u_5 == 5 and summa_r_5 == 5) or (summa_u_5 == 5 and summa_r_5 == 5):
                total_text = "5 und 5: Zwei Fünfer verlieben sich oft auf den ersten Blick. Die Schwachstelle in einer Beziehung ist der Wunsch nach Veränderung."
            if (summa_u_5 == 5 and summa_r_5 == 6) or (summa_u_5 == 6 and summa_r_5 == 5):
                total_text = "5 und 6: 5 Liebesveränderung, 6 Liebeskonsistenz. Lerne, die Persönlichkeitsmerkmale deines Partners zu akzeptieren."
            if (summa_u_5 == 5 and summa_r_5 == 7) or (summa_u_5 == 7 and summa_r_5 == 5):
                total_text = "5 und 7: Extrovertiert und introvertiert - diese Leute sollten aufeinander aufpassen und solche Besonderheiten berücksichtigen, dann wird die Vereinigung lang."
            if (summa_u_5 == 5 and summa_r_5 == 8) or (summa_u_5 == 8 and summa_r_5 == 5):
                total_text = "5 und 8: Die 5 mag die Stabilität und den Erfolg der 8 und die 8 wiederum zieht die Spontaneität und Fröhlichkeit der 5 an. Die Fehler eines Partners zu akzeptieren wird starke Beziehungen aufbauen."
            if (summa_u_5 == 5 and summa_r_5 == 9) or (summa_u_5 == 9 and summa_r_5 == 5):
                total_text = "5 und 9: Beide sind verträumt und schmieden gerne Pläne für die Zukunft. Gib bei Rückschlägen nicht auf, lerne Durchhaltevermögen und deine Verbindung wird halten."
            if (summa_u_5 == 6 and summa_r_5 == 6) or (summa_u_5 == 6 and summa_r_5 == 6):
                total_text = "6 und 6: Ähnliche Prioritäten im Leben zu haben wird einem Paar helfen, sich zu verstehen, aber finanzielle Not fürchten. Lerne, mit solchen Turbulenzen umzugehen und strebe danach, auf den Beinen zu bleiben."
            if (summa_u_5 == 6 and summa_r_5 == 7) or (summa_u_5 == 7 and summa_r_5 == 6):
                total_text = "6 und 7: Im Allgemeinen passen Partner zueinander, aber aufgrund von Unmäßigkeit und Intoleranz gegenüber dem Verhalten des Partners können Schwierigkeiten auftreten."
            if (summa_u_5 == 6 and summa_r_5 == 8) or (summa_u_5 == 8 and summa_r_5 == 6):
                total_text = "6 und 8: Die Aufrechterhaltung eines Gleichgewichts zwischen dem Spirituellen und dem Materiellen wird die Frustration beim Streben nach Komfort vermeiden."
            if (summa_u_5 == 6 and summa_r_5 == 9) or (summa_u_5 == 9 and summa_r_5 == 6):
                total_text = "6 und 9: Beide neigen zum Tagträumen, Paare sind durchaus in der Lage, ihre Ziele zu erreichen. Beziehungen sind sowohl physisch als auch spirituell harmonisch."
            if (summa_u_5 == 7 and summa_r_5 == 7) or (summa_u_5 == 7 and summa_r_5 == 7):
                total_text = "7 und 7: Beide sind introvertiert, schätzen Ruhe und Regelmäßigkeit im Leben. Ein wunderbares Paar, in allen Bereichen vereinbar, sie können auf eine langfristige Beziehung bauen, die auf Liebe und gegenseitigem Respekt basiert."
            if (summa_u_5 == 7 and summa_r_5 == 8) or (summa_u_5 == 8 and summa_r_5 == 7):
                total_text = "7 und 8: 7 Werte spirituell, 8 - materiell. Dieser Ansatz ist ideal für geschäftliche Partnerschaften."
            if (summa_u_5 == 7 and summa_r_5 == 9) or (summa_u_5 == 9 and summa_r_5 == 7):
                total_text = "7 und 9: Die Fähigkeit verträumter Idealisten, sich in schwierigen Situationen gegenseitig zu unterstützen, kann eine solche Vereinigung glücklich machen."
            if (summa_u_5 == 8 and summa_r_5 == 8) or (summa_u_5 == 8 and summa_r_5 == 8):
                total_text = "8 und 8: Sie haben eine starke Anziehungskraft zueinander, aber aufgrund der Ungeduld und des Ehrgeizes der Partner kann es in einem solchen Paar oft zu Streitigkeiten kommen. Lernen Sie nachzugeben und hängen Sie sich nicht an Kleinigkeiten auf."
            if (summa_u_5 == 8 and summa_r_5 == 9) or (summa_u_5 == 9 and summa_r_5 == 8):
                total_text = "8 und 9: Diese Menschen ergänzen sich perfekt in Geschäftsbeziehungen. Achter sind temperamentvoll, und Neuner mögen es und ermutigt sie, ihre Pläne umzusetzen . Gute Namenskompatibilität für Geschäftsbeziehungen."
            if (summa_u_5 == 9 and summa_r_5 == 9) or (summa_u_5 == 9 and summa_r_5 == 9):
                total_text = "9 und 9: In einer solchen Beziehung herrschen gegenseitiges Verständnis, Zärtlichkeit und Loyalität. Beide Partner schätzen die Persönlichkeit des anderen und unterstützen den Wunsch der anderen Hälfte nach Selbstentwicklung und innerem Wachstum."
            try:
                telegraph.create_account(short_name='совместимость')
                response = telegraph.create_page(
                    f'Namenskompatibilität {names_split[0]} und {names_split[1]}',
                    html_content=f'🔮<b>Dein Name ({names_split[0]}) stimmt mit der Zahl überein {summa_u_5}</b><br>'
                                 f'{u_text}<br>'
                                 f'<br>'
                                 f'🔮<b>Partnername ({names_split[1]}) stimmt mit der Zahl überein {summa_r_5}</b><br>'
                                 f'{r_text}<br>'
                                 f'<br>'
                                 f'👫<b>Kompatibilität</b> {total_text}'
                )
                link = 'http://telegra.ph/{}'.format(response['path'])
                msg_text = hlink(":", link)
                await message.answer(f"Berechnungsergebnis{msg_text}:", reply_markup=back_compatibility_de)
                await state.finish()
            except:
                await message.answer(f"Du hast die falschen Namen eingegeben\n"
                                     f"\n"
                                     f"<i>Geben Sie sie im Format ein: Michelle John (auf Englisch)</i>",
                                     reply_markup=back_compatibility_de)
        else:
            await message.answer(f"Du hast die falschen Namen eingegeben\n"
                                 f"\n"
                                 f"<i>Geben Sie sie im Format ein: Michelle John (auf Englisch)</i>",
                                 reply_markup=back_compatibility_de)
