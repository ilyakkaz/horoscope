from datetime import datetime

import pytz
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import ContentTypes
from aiogram.utils.markdown import hlink

from data.config import pifagor_img
from states.states import Test, Pifagor
from utils.db_api import quick_commands as qc
import pandas as pd

from loader import dp
from utils.db_api.db_gino import db
from telegraph import Telegraph

telegraph = Telegraph()


@dp.message_handler(content_types=ContentTypes.TEXT, state=Pifagor.date)
async def def_name(message: types.Message, state: FSMContext):
    user = await qc.get_user(id=int(message.from_user.id))
    date = message.text
    date_save = date
    date_check_replace = 0
    try:
        date = date.replace(" ", "")
        date_check_replace += 1
    except:
        pass
    try:
        date = date.replace(".", "")
        date_check_replace += 1
    except:
        pass
    try:
        date = date.replace(",", "")
        date_check_replace += 1
    except:
        pass
    try:
        date = date.replace("/", "")
        date_check_replace += 1
    except:
        pass
    if date_check_replace == 0:
        if user.language == "ru":
            await message.answer(f"Вы неправильно указали дату вашего рождения, укажите ее в формате:\n"
                                 f"<b>дд.мм.гггг</b> или <b>дд,мм,гггг</b> или <b>дд/мм/гггг</b>")
        if user.language == "en":
            await message.answer(f"You have incorrectly indicated your date of birth, please enter it in the format:"
                                 f"<b>dd.mm.yyyy</b> or <b>dd,mm,yyyy</b> or <b>dd/mm/yyyy</b>")
        if user.language == "es":
            await message.answer(f"Ha indicado incorrectamente su fecha de nacimiento, introdúzcala en el formato:"
                                 f"<b>dd.mm.aaaa</b> o <b>dd,mm,aaaa</b> o <b>dd/mm/aaaa</b>")
        if user.language == "de":
            await message.answer(f"Sie haben Ihr Geburtsdatum falsch angegeben, bitte geben Sie es im Format ein:"
                                 f"<b>dd.mm.yyyy</b> oder <b>dd,mm,yyyy</b> oder <b>dd/mm/yyyy</b>")
    else:
        if (int(date[0]) == 0 and int(date[1]) == 0) or (int(date[2]) == 0 and int(date[3]) == 0):
            if user.language == "ru":
                await message.answer(f"Вы неправильно указали дату вашего рождения, укажите ее в формате:\n"
                                     f"<b>дд.мм.гггг</b> или <b>дд,мм,гггг</b> или <b>дд/мм/гггг</b>")
            elif user.language == "en":
                await message.answer(
                    f"You have incorrectly indicated your date of birth, please enter it in the format:"
                    f"<b>dd.mm.yyyy</b> or <b>dd,mm,yyyy</b> or <b>dd/mm/yyyy</b>")
            elif user.language == "es":
                await message.answer(f"Ha indicado incorrectamente su fecha de nacimiento, introdúzcala en el formato:"
                                     f"<b>dd.mm.aaaa</b> o <b>dd,mm,aaaa</b> o <b>dd/mm/aaaa</b>")
            elif user.language == "de":
                await message.answer(f"Sie haben Ihr Geburtsdatum falsch angegeben, bitte geben Sie es im Format ein:"
                                     f"<b>dd.mm.yyyy</b> oder <b>dd,mm,yyyy</b> oder <b>dd/mm/yyyy</b>")
        else:
            first = 0
            second = 0
            third = 0
            fourth = 0
            for i in date:
                first += int(i)
            print("1)", first)
            for i in str(first):
                second += int(i)
            print("2)", second)
            if int(date[0]) != 0:
                third = first - int(date[0]) * 2
                print("date[0] = ", date[0])
            if int(date[0]) == 0:
                third = first - int(date[1]) * 2
                print("date[1] = ", date[1])
            print("3)", third)
            if third in (10, 11, 12):
                fourth = int(third)
            else:
                for i in str(third):
                    fourth += int(i)
            print("4)", fourth)
            one = 0
            two = 0
            three = 0
            four = 0
            five = 0
            six = 0
            seven = 0
            eight = 0
            nine = 0
            for i in str(date):
                if int(i) == 1:
                    one += 1
                if int(i) == 2:
                    two += 1
                if int(i) == 3:
                    three += 1
                if int(i) == 4:
                    four += 1
                if int(i) == 5:
                    five += 1
                if int(i) == 6:
                    six += 1
                if int(i) == 7:
                    seven += 1
                if int(i) == 8:
                    eight += 1
                if int(i) == 9:
                    nine += 1
            for i in str(first):
                if int(i) == 1:
                    one += 1
                if int(i) == 2:
                    two += 1
                if int(i) == 3:
                    three += 1
                if int(i) == 4:
                    four += 1
                if int(i) == 5:
                    five += 1
                if int(i) == 6:
                    six += 1
                if int(i) == 7:
                    seven += 1
                if int(i) == 8:
                    eight += 1
                if int(i) == 9:
                    nine += 1
            for i in str(second):
                if int(i) == 1:
                    one += 1
                if int(i) == 2:
                    two += 1
                if int(i) == 3:
                    three += 1
                if int(i) == 4:
                    four += 1
                if int(i) == 5:
                    five += 1
                if int(i) == 6:
                    six += 1
                if int(i) == 7:
                    seven += 1
                if int(i) == 8:
                    eight += 1
                if int(i) == 9:
                    nine += 1
            for i in str(third):
                if int(i) == 1:
                    one += 1
                if int(i) == 2:
                    two += 1
                if int(i) == 3:
                    three += 1
                if int(i) == 4:
                    four += 1
                if int(i) == 5:
                    five += 1
                if int(i) == 6:
                    six += 1
                if int(i) == 7:
                    seven += 1
                if int(i) == 8:
                    eight += 1
                if int(i) == 9:
                    nine += 1
            for i in str(fourth):
                if int(i) == 1:
                    one += 1
                if int(i) == 2:
                    two += 1
                if int(i) == 3:
                    three += 1
                if int(i) == 4:
                    four += 1
                if int(i) == 5:
                    five += 1
                if int(i) == 6:
                    six += 1
                if int(i) == 7:
                    seven += 1
                if int(i) == 8:
                    eight += 1
                if int(i) == 9:
                    nine += 1
            print(f"1 - {one}\n"
                  f"2 - {two}\n"
                  f"3 - {three}\n"
                  f"4 - {four}\n"
                  f"5 - {five}\n"
                  f"6 - {six}\n"
                  f"7 - {seven}\n"
                  f"8 - {eight}\n"
                  f"9 - {nine}")
            if user.language == "ru":
                if one == 0:
                    text_one = f"Встречается только у людей, рожденных после 2000 года. Считает, что, мир крутится вокруг него и все ему чем-то обязаны. Важно еще в раннем детстве избавлять его от ощущения своей неповторимости и особенности, предпочтительнее воспитание в коллективе"
                if one == 1:
                    text_one = f"Утонченный эгоист. Он не обращает внимания на окружающих и стремится извлечь выгоду из всех ситуаций только для себя. Его мало интересуют другие люди и то, чем они живут. Главное, что живет и должен жить только он один."
                if one == 2:
                    text_one = f"Характер, очень близкий к эгоистичному. Вечно ищет одобрения окружающих, даже если для этого нет никаких предпосылок. Любит хвалить себя. Кажется себе самым умным и талантливым и удивлен, что окружающие этого не замечают."
                if one == 3:
                    text_one = f"«Золотая середина». Характер спокойный, покладистый. Человек коммуникабельный, не очень любит подчиняться, но и не рвется к руководству. Если с таким человеком поговорить по душам, всегда можно найти компромисс."
                if one == 4:
                    text_one = f"Человек сильного характера, волевой. Он не терпит лжи и подхалимажа, но иногда может пойти на это ради близких людей. Мужчины с таким характером избирают роль профессиональных военных, женщины обычно властно держат в руках семью."
                if one == 5:
                    text_one = f"Диктатор и самодур. Ради соей идеи или прихоти может пустить по ветру миллионы человеческих жизней. Для достижения цели идет, что называется, «по трупам». Если не хватает данных для большего, становится тираном в семье, отшельником, в противном случае получает психическое расстройство. Настойчив в намерениях, в мести, хорошо приспосабливается. Почти всегда обладает некой манией. Испытывает привязанность к детям (своим)"
                if one >= 6:
                    text_one = f"Редкая комбинация. Человек необычайно жестокий, но для близких или «ради человечества» способен совершить невозможное. Человек одной фанатичной идеи и очень тяжелый в общении."
                if two == 0:
                    text_two = "Биоэнергия на самом низком уровне; открыт канал для ее интенсивного набора. Эти люди любят антиквариат, старинные книги, хорошо относятся к окружающим, стараясь подпитаться от них; воспитанны и благородны. Исключения противоположного плана встречаются редко."
                if two == 1:
                    text_two = "Обычные в биоэнергетическом плане люди. Они избегают стрессовых ситуаций, сильных эмоций.Для них просто необходимы занятия физкультурой и спортом, а еще лучше йогой. Чувствительны к изменениям в атмосфере."
                if two == 2:
                    text_two = "Относительно большой запас биоэнергии. Люди, способные стать хорошими врачами, медсестрами, санитарами. Их призвание — медицина. В их семьях редки нервные стрессы."
                if two == 3:
                    text_two = "Знак экстрасенса. Возможно, он сам и не подозревает о таких способностях, но лечит своим биополем, даже своим присутствием. Такие люди долгие годы находятся в ожидании толчка, для того чтобы раскрыть свои способности."
                if two >= 4:
                    text_two = "Если встречается женщина, в которую все влюблены, или неотразимый мужчина, то это объясняется наличием у них избытка биоэнергии, которой они готовы со всеми поделиться. К сожалению, эти люди очень уязвимы для злых, энергетически голодных типов с «сатанинскими возможностями»."
                if three == 0:
                    text_three = "Чистоплотные и порядочные люди, отличные хозяева, но несколько навязчивые в своем постоянном стремлении к чистоте. Очень пунктуальны, любят смотреться в зеркало, объясняются витиевато. Кропотливый труд выполняют безукоризненно."
                if three == 1:
                    text_three = "Люди настроения. Не любят экономить, широкие натуры, нередко противоречивые. В доме беспорядочны, но иногда все сразу и неожиданно приводят в совершенное состояние."
                if three == 2:
                    text_three = "Люди, склонные к наукам. Имеют определенный аналитический склад ума."
                if three >= 3:
                    text_three = "Склонность к наукам. Реализация этой склонности порождает педантичность, отрешенность, скупость, наконец, постоянную потребность в справедливости."
                if four == 0:
                    text_four = "Здоровье очень слабое, человек с детства подвержен различным заболеваниям. Болеть такой человек будет тем дольше, чем больше в его математическом прогнозе двоек, потому что он отдает в мир свою энергию."
                if four == 1:
                    text_four = "Здоровье среднее, его нужно закалять, иначе к старости человек превратится в развалину. Главные виды спорта — плавание и бег."
                if four == 2:
                    text_four = "Здоровье крепкое. Такие люди не афишируют свою сексуальную потенцию, но могут быть символами сексуальной привлекательности."
                if four >= 3:
                    text_four = "Люди с очень крепким здоровьем, встречающиеся крайне редко. Сексуальный темперамент таких людей неимоверно притягателен."
                if five == 0:
                    text_five = "Канал связи с тонким миром, с Космосом, закрыт при рождении. Такой человек занят расчетами, экспериментами и доказательствами, напряженными размышлениями. Эти люди делают очень много ошибок."
                if five == 1:
                    text_five = "Канал связи открыт. Количество ошибок таких людей сокращено, жизненные ситуации находятся под контролем для извлечения из них максимальной пользы."
                if five == 2:
                    text_five = "Сильно развитая интуиция. Наличие «вещих снов», предчувствий событий. Откровения при наличии единственной детали. Умение предугадывать прошлое так же, как и будущее. Потребность в юридической и следственной работе."
                if five == 3:
                    text_five = "Почти ясновидящие. Без всяких знаний и подсказок такие люди знают, как действовать самому и своему окружению. В отдельных случаях точно предсказывают грядущие события, но не могут указать, как избежать неприятностей."
                if five >= 4:
                    text_five = "Ясновидящие. Им ясно и безразлично все происходящее вокруг. Они часто пребывают вне времени и пространства, будто включаясь в некую иную систему существования."
                if six == 0:
                    text_six = "Этот человек пришел на землю, чтобы приобрести ремесло. Для развития и продвижения по лестнице жизни ему необходим физический труд, который он не любит. Воображение, фантазия, художественный вкус — главные двигатели его развития. Однако, несмотря на отвлекающие потребности, способен на серьезные поступки."
                if six == 1:
                    text_six = "Заземленный человек, но способный по духовным качествам на гуманные поступки. Может запинаться творческими или точными науками, но для продления его существования обязателен физический труд. Бывают достаточно часто проявления в художественных областях."
                if six == 2:
                    text_six = "Заземленный чеповек. Стремится к физическому труду, который мешает его развитию. Умственная деятельность и занятие искусством — единственное, что может приподнять таких людей."
                if six == 3:
                    text_six = "«Знак сатаны», зловещий знак. Темпераментные люди, стремящиеся за счет своего обаяния быть всегда в центре общества. Человек ненадежный, ищущий, часто меняющий случайных партнеров."
                if six >= 4:
                    text_six = "Человек, перебравший в прежних воплощениях злонамеренности, зазем-ленности и пытающийся изгнать это через труд, занятия умственной деятельностью, совершенствующийся."
                if seven == 0:
                    text_seven = "Человек, рожденный, дабы понять, что такое талант. Его жизненный опыт и поступки помогают обрести талант, а страдания и религия подталкивают к его пониманию. Главное — уловить момент, когда талант будет послан свыше."
                if seven == 1:
                    text_seven = "Такие люди живут легко, но удача приходит к ним в результате творческого труда. Талант выражен не ярко."
                if seven == 2:
                    text_seven = "Одаренный человек с тонким художественным, музыкальным вкусом и склонностью к живописи. Эгоистическое начало в его творчестве имеет как плохие, так и хорошие стороны. Он удачлив в азартных играх и забывчив в добродетели."
                if seven == 3:
                    text_seven = "Особый знак людей, ненадолго посещающих землю. Если они задерживаются на этом пути, их ждут тяжелые болезни. Чувствительность губит их самих из-за обостренного чувства справедливости."
                if seven >= 4:
                    text_seven = "Знак ангела. Люди, постоянно заботящиеся об окружающих, но, как правило, не доживающие до старости."
                if eight == 0:
                    text_eight = "Человек, у которого полностью отсутствует чувство долга. Если, скажем, он берет взаймы, то не спешит отдавать и пропускает все сроки расчета."
                if eight == 1:
                    text_eight = "Эти люди наделены чувством долга и предельно добросовестны."
                if eight == 2:
                    text_eight = "Развитое чувство долга. Удивительная готовность помогать ближнему. Этот человек - прекрасный семьянин, но зависим от непорядочных людей."
                if eight == 3:
                    text_eight = "Знак долга перед народом, который воспитал его владельца. Символ избранных людей, возглавляющих народы. Люди, добивающиеся выдающихся результатов."
                if eight >= 4:
                    text_eight = "Знак несет парапсихологические способности и безмерную восприимчивость к точным наукам. Удивительный знак людей, идущих сверхъестественными путями."
                if nine == 0:
                    text_nine = "Отсутствие девятки может быть только у появившихся на свет после 2000 года. С самого рождения надо начинать развивать память и логику, чтобы уже к школе восполнить пустующий квадрат "
                if nine == 1:
                    text_nine = "Самый таинственный знак. Чтобы его постичь, человек должен трудиться всю жизнь."
                if nine == 2:
                    text_nine = "Умны от рождения. Не любят учиться, потому что привыкли легко получать знания. Главным препятствием в этом является чувство иронии. Независимость."
                if nine == 3:
                    text_nine = "Очень умные люди. Познание не представляет для них никаких затруднений. Прекрасные собеседники."
                if nine >= 4:
                    text_nine = "Люди, которым открывается истина. Если при этом у них развита интуиция, то существует полная гарантия от провала в любом начинании. Эти люди достаточно неприятны, грубы, немилосердны и жестоки. Их трудно, временами невозможно сделать адекватными в обществе."
                first_line = one + four + seven
                second_line = two + five + eight
                third_line = three + six + nine
                if first_line == 0:
                    text_1_line = "Значение Человек не ставит перед собой цели и задачи, надеясь на случай или других людей, его достаточно легко переубедить и заставить отказаться от своих планов. "
                if first_line == 1:
                    text_1_line = "Слабая целеустремленность; человек может включиться в спор, но это не означает, что он желает достичь результата, как правило — это только стремление победить другого в споре. Надеется на случай и друзей. "
                if first_line == 2:
                    text_1_line = "Нормальная целеустремленность. Можно сказать, что человек медленно «разбегается» по жизни. Он вначале узнает свои возможности и только после этого начинает ставить перед собой достойные цели. "
                if first_line == 3:
                    text_1_line = "Человек может менять свои цели совершенно непредсказуемо (экстренно, вдруг, внезапно). Часто его выбор ничем не оправдан и не объясним. "
                if first_line == 4:
                    text_1_line = "Сильная целеустремленность. Человек ставит перед собой цель, только после этого начинает соизмерять свои возможности и интерес к самой цели. Очень часто достигает тех целей, которые не соответствуют его интересам или возможностям. Выбрав нужное направление, не стоит занижать цели."
                if first_line == 5:
                    text_1_line = "Очень сильная целеустремленность. Это означает, что, поставив перед собой цель, человек может забыть о том, что рядом с ним люди, близкие, родные, -он может гораздо больше потерять, но цели достигнет. Необходим контроль за чувством меры в достижении поставленной задачи."
                if first_line >= 6:
                    text_1_line = "Перегрузка качества. Человек ставит перед собой завышенные цели или несколько целей одновременно, что тормозит его в продвижении вперед."
                if second_line == 0:
                    text_2_line = "Человек не семьянин.  Это означает, что семья за ним стоит на последнем месте.  Такие люди, как правило, не спешат создать семью (их больше интересует работа, карьера, друзья и др.).  "
                if second_line == 1 or second_line == 2:
                    text_2_line = "Человек помнит, что семью надо создать, но усилия в этом направлении не проявляет.  Ждет случая, когда все образуется само собой (ждет, когда предложат создать семью)."
                if second_line == 3:
                    text_2_line = "Человек мечется между сильнейшим желанием создать семью, во что бы то ни стало и нежеланием делать это вообще. Если такой человек решился на брак, то необходимо использовать случай, иначе все отложится на долгий срок. "
                if second_line == 4:
                    text_2_line = "Человек хочет создать семью и делает это, не затягивая.  Как правило, редко становится причиной распада семьи, так как стремится ее сохранить "
                if second_line == 5:
                    text_2_line = "Очень сильное качество семьянина.  Такие люди пытаются увидеть свою семью в идеале (по их мнению).  Единственное, что может их извинить, - это то, что они предъявляют такие же требования к себе.  Без семьи не могут существовать вообще.  "
                if second_line >= 6:
                    text_2_line = "Качество семьянина перегружено, что означает ослабление этого качества.  Объяснение простое - они очень долго ищут свой идеал, что приводит к торможению в создании семьи."
                if third_line == 0 or third_line == 1:
                    text_3_line = "Человек революционер духу. Он стремится все изменить вокруг себя, меняет окружение, место работы, оспаривает практически все, стремясь изменить всех и вся. "
                if third_line == 2:
                    text_3_line = "Человек легок на подъем, но уже может остановить свой революционный порыв (при желании). "
                if third_line == 3:
                    text_3_line = "Нестабильный в привычках человек. Может инициировать множество привычек и привязанностей, создавая стабильность, но также легко отказаться от них без видимой причины; через некоторое время может вновь реанимировать забытые привязанности. Все это происходит неожиданно. "
                if third_line == 4 or third_line == 5:
                    text_3_line = "Очень стабильные люди. Окружают себя различными привязанностями и привычками, создавая стабильное окружение. Могут быть немного занудными в своих привязанностях. Очень тяжелы на перемены. "
                if third_line >= 6:
                    text_3_line = "Перегрузка качества стабильности. Человек стремится окружить себя таким изобилием привычек, что начинает сам их отменять, так как они мешают ему. Можно сказать, что он сам борется со своей собственной стабильностью."
                first_col = one + two + three
                second_col = four + five + six
                third_col = seven + eight + nine
                if first_col in (0, 1, 2, 3):
                    text_1_col = "Можно говорить о том, что человек имеет заниженную самооценку, недооценивает свои возможности. "
                if first_col == 4:
                    text_1_col = "Хорошая самооценка. Человек стремится выделиться из общей массы и прикладывает для этого много усилий (другое дело, в нужном ли направлении?)."
                if first_col == 5:
                    text_1_col = "Очень сильная самооценка, она может быть завышенной, когда человек, не совершенствуясь, начинает оценивать себя только по потенциальным возможностям, преувеличивая их."
                if first_col >= 6:
                    text_1_col = "Перегрузка качества самооценки приводит к тому, что человек, увлекаясь показом себя, забывает об истинных своих способностях и занимается больше. внешней формой, чем внутренним содержанием. Такие люди, как правила, не достигают поставленных перед собой целей, истратив весь свой пыл на мелькание перед толпой, которая восхищается их внешним видом."
                if second_col in (0, 1):
                    text_2_col = "Человек не хочет обеспечивать себя сам,может позволить себе сесть на шею кому-либо (родителям, жене, мужу). Эта линия не представляет особой опасности при своей слабости для женщин, так как обеспечение семьи должно лежать на плечах мужа."
                if second_col == 2:
                    text_2_col = "Человек помнит о том, что надо кормить семью и, боясь этого в дальнейшем, начинает искать себе профессию по той оплате, которую предлагают. В результате человек может отказаться от своей мечты ради стабильного заработка, но если появится возможность не делать этого, то он не будет особо упираться, так как не очень жаждет кормить себя и семью."
                if second_col == 3:
                    text_2_col = "Такие люди могут работать импульсивно. Их принцип — быстро поработать, чтобы хватило на какой-то срок, а потом можно еще поработать."
                if second_col in (4, 5):
                    text_2_col = "Люди уделяют очень много времени и сил для обеспечения своей семьи. Очень часто это их единственная цель в жизни."
                if second_col >= 6:
                    text_2_col = "Перегрузка качества, человек, начиная интенсивно трудиться, быстро изнашивает себя и приходит к полному отстранению от труда (надорвался), он делает много разных дел, распыляет себя, создавая полную иллюзию работ"
                text_3_col = "Сила таланта определяется количеством цифр в столбце. Но шесть и более цифр приводят к перегрузу качества, что не есть хорошо. Раскроет ли человек талан - зависит только от него"
                telegraph.create_account(short_name='совместимость')
                response = telegraph.create_page(
                    f'Квадрат Пифагора {date_save}',
                    html_content=f"Ваш квадрат Пифагора<br>"
                                 f"{one} ░ {four} ░ {seven}<br>"
                                 f"{two} ░ {five} ░ {eight}<br>"
                                 f"{three} ░ {six} ░ {nine}<br>"
                                 f"<br>"
                                 f"1️⃣<i>Цифра 1 в психоматрице отвечает за характер человека, его волевые качества, силу стремления к власти, способность отстоять свои взгляды.</i><br>"
                                 f"<br>"
                                 f"У вас едениц - {one} шт: {text_one}<br>"
                                 f"___________________________________<br>"
                                 f"<br>"
                                 f"2️⃣<i>Цифра 2 в числовой системе Пифагора обозначает энергию человека. Нужно понять, что энергия в данном случае — это действия человека в семье, на работе, в обществе.</i><br>"
                                 f"<br>"
                                 f"У вас двоек - {two} шт: {text_two}<br>"
                                 f"___________________________________<br>"
                                 f"<br>"
                                 f"3️⃣<i>Цифра 3 в психоматрице отвечает за интерес к наукам и в первую очередь к точным наукам или технике.</i><br>"
                                 f"<br>"
                                 f"У вас троек - {three} шт: {text_three}<br>"
                                 f"___________________________________<br>"
                                 f"<br>"
                                 f"4️⃣<i>Цифра 4 в психоматрице отвечает за здоровье человека.</i><br>"
                                 f"<br>"
                                 f"У вас четверок - {four} шт: {text_four}<br>"
                                 f"___________________________________<br>"
                                 f"<br>"
                                 f"5️⃣<i>Цифра 5 в психоматрице отвечает за логику и интуицию человека, что в свою очередь определяет возможности человека строить планы и анализировать ситуацию, разбираться в точных науках и технике.</i><br>"
                                 f"<br>"
                                 f"У вас пятерок - {five} шт: {text_five}<br>"
                                 f"___________________________________<br>"
                                 f"<br>"
                                 f"6️⃣<i>Значение цифры 6 — это степень приземленности человека, склонность к физическому труду.</i><br>"
                                 f"<br>"
                                 f"У вас шестерок - {six} шт: {text_six}<br>"
                                 f"___________________________________<br>"
                                 f"<br>"
                                 f"7️⃣<i>Цифру 7 всегда связывали с понятием везения (удачи).</i><br>"
                                 f"<br>"
                                 f"У вас семерок - {seven} шт: {text_seven}<br>"
                                 f"___________________________________<br>"
                                 f"<br>"
                                 f"8️⃣<i>Цифра 8 отвечает за чувство долга к близким (родители, семья), чувство терпимости и доброты — качества, которые мы должны проявлять по отношения к родителям и близким людям.</i><br>"
                                 f"<br>"
                                 f"У вас восьмерок - {eight} шт: {text_eight}<br>"
                                 f"___________________________________<br>"
                                 f"<br>"
                                 f"9️⃣<i>Цифра 9 в психоматрице отвечает за ум, память и ясновидение человека.</i><br>"
                                 f"<br>"
                                 f"У вас девяток - {nine} шт: {text_nine}<br>"
                                 f"<br>"
                                 f"___________________________________<br>"
                                 f"<br>"
                                 f"⬇️<i>Сумма первой строки (целеустремленность): {first_line}</i><br>"
                                 f"{text_1_line}<br>"
                                 f"___________________________________<br>"
                                 f"<br>"
                                 f"⬇️<i>Сумма второй строки (семья): {second_line}</i><br>"
                                 f"{text_2_line}<br>"
                                 f"___________________________________<br>"
                                 f"<br>"
                                 f"⬇️<i>Сумма третьей строки (привычки): {third_line}</i><br>"
                                 f"{text_3_line}<br>"
                                 f"___________________________________<br>"
                                 f"<br>"
                                 f"➡️<i>Сумма первого столбца (самооценка): {first_col}</i><br>"
                                 f"{text_1_col}<br>"
                                 f"___________________________________<br>"
                                 f"<br>"
                                 f"➡️<i>Сумма второго столбца (отношение к работе): {second_col}</i><br>"
                                 f"{text_2_col}<br>"
                                 f"___________________________________<br>"
                                 f"<br>"
                                 f"➡️<i>Сумма третьего столбца (талант): {third_col}</i><br>"
                                 f"{text_3_col}<br>"
                )
                print(response)
                link = 'http://telegra.ph/{}'.format(response['path'])
                msg_text = hlink(" ", link)
                await message.answer(f"Результат{msg_text}расчета:")
            elif user.language == "en":
                if one == 0:
                    text_one = "Occurs only in people born after 2000. He believes that the world revolves around him and everyone owes him something. It is important in early childhood to relieve him of the feeling of his uniqueness and peculiarity, it is preferable to be brought up in a team."
                if one == 1:
                    text_one = "A refined egoist. He does not pay attention to those around him and seeks to benefit from all situations only for himself. He has little interest in other people and what they live by. The main thing is that only he lives and should live."
                if one == 2:
                    text_one = "A character very close to selfish. Always seeks the approval of others, even if there are no prerequisites for this. Likes to praise himself. It seems to himself the most intelligent and talented and is surprised that others do not notice it."
                if one == 3:
                    text_one = " The golden mean. The character is calm, docile. The person is sociable, does not really like to obey, but also does not rush to leadership. If you talk to such a person heart to heart, you can always find a compromise. "
                if one == 4:
                    text_one = "A person of strong character, strong-willed. He does not tolerate lies and toadying, but sometimes he can do it for the sake of loved ones. Men with this character choose the role of professional military men, women usually hold the family in their hands."
                if one == 5:
                    text_one = "A dictator and tyrant. For the sake of his idea or whim, he can blow millions of human lives down the wind. To achieve the goal, he goes, as they say, over corpses. If there is not enough data for more, he becomes a tyrant in the family, a hermit, otherwise case he gets a mental disorder. Persistent in intentions, in revenge, adapts well. Almost always has a kind of mania. Feels attachment to children (his) "
                if one >= 6:
                    text_one = "A rare combination. A man is unusually cruel, but for those close to him or for the sake of humanity he can do the impossible. A man of one fanatical idea and very difficult to communicate."
                if two == 0:
                    text_two = "Bioenergy is at the lowest level; a channel is open for its intensive recruitment. These people love antiques, old books, treat others well, trying to feed on them; well-mannered and noble. Exceptions of the opposite plan are rare."
                if two == 1:
                    text_two = "People are ordinary in bioenergetic terms. They avoid stressful situations, strong emotions. They just need physical education and sports, and even better yoga. Sensitive to changes in the atmosphere."
                if two == 2:
                    text_two = "A relatively large supply of bioenergy. People who can become good doctors, nurses, orderlies. Their vocation is medicine. Nervous stress is rare in their families."
                if two == 3:
                    text_two = "The sign of a psychic. Perhaps he himself is unaware of such abilities, but he heals with his biofield, even with his presence. Such people have been waiting for a push for many years in order to reveal their abilities."
                if two >= 4:
                    text_two = "If you meet a woman everyone is in love with, or an irresistible man, this is because they have an excess of bioenergy that they are ready to share with everyone. Unfortunately, these people are very vulnerable to evil, energetically hungry types with satanic capabilities."
                if three == 0:
                    text_three = "Clean and decent people, excellent owners, but somewhat obtrusive in their constant pursuit of cleanliness. Very punctual, like to look in the mirror, explain themselves floridly. Painstaking work is done impeccably."
                if three == 1:
                    text_three = "People of the mood. They do not like to save money , they are broad-minded, often contradictory. The house is messy, but sometimes everything is suddenly and unexpectedly brought to a perfect state."
                if three == 2:
                    text_three = " Science-minded people. They have a certain analytical mind."
                if three >= 3:
                    text_three = "Addiction to science. The realization of this inclination gives rise to pedantry, detachment, stinginess, and finally, a constant need for justice."
                if four == 0:
                    text_four = "Health is very weak, a person is susceptible to various diseases from childhood. Such a person will get sick the longer, the more twos in his mathematical forecast, because he gives his energy to the world."
                if four == 1:
                    text_four = "Health is average, it needs to be tempered, otherwise by old age a person will turn into a wreck. The main sports are swimming and running."
                if four == 2:
                    text_four = "Health is strong. Such people do not advertise their sexual potency, but can be symbols of sex appeal."
                if four >= 3:
                    text_four = "People with very good health, which are extremely rare. Their sexual temperament is incredibly attractive."
                if five == 0:
                    text_five = "The channel of communication with the subtle world, with the Cosmos, is closed at birth. Such a person is busy with calculations, experiments and proofs, intense reflections. These people make a lot of mistakes."
                if five == 1:
                    text_five = "The communication channel is open. The number of mistakes of such people has been reduced, life situations are under control to get the most out of them."
                if five == 2:
                    text_five = "Strongly developed intuition. Presence of prophetic dreams , premonitions of events. Revelations with a single detail. Ability to predict the past as well as the future. The need for legal and investigative work."
                if five == 3:
                    text_five = "Almost clairvoyants. Without any knowledge and tips, such people know how to act for themselves and their surroundings. In some cases, they accurately predict future events, but cannot indicate how to avoid trouble."
                if five >= 4:
                    text_five = "Clairvoyants. They are clear and indifferent to everything that happens around them. They often stay outside time and space, as if they are included in some other system of existence."
                if six == 0:
                    text_six = "This person came to earth to acquire a craft. To develop and climb the ladder of life, he needs physical labor, which he does not like. Imagination, fantasy, artistic taste are the main engines of his development. However, despite the distracting needs, he is able for serious deeds. "
                if six == 1:
                    text_six = "A grounded person, but capable of humane deeds by spiritual qualities. He may stumble over creative or exact sciences, but physical labor is required to prolong his existence. There are quite often manifestations in artistic fields."
                if six == 2:
                    text_six = "A grounded man. Seeks physical labor that interferes with his development. Mental activity and art is the only thing that can lift such people."
                if six == 3:
                    text_six = "The sign of Satan, an ominous sign. Temperamental people who strive to be always in the center of society due to their charm. He is an unreliable person, looking for, often changing casual partners."
                if six >= 4:
                    text_six = "A person who has sorted out malice, groundedness in previous incarnations and tries to expel it through work, mental activity, and improving."
                if seven == 0:
                    text_seven = "A person born to understand what talent is. His life experience and deeds help to gain talent, and suffering and religion push to understand it. The main thing is to catch the moment when the talent will be sent from above."
                if seven == 1:
                    text_seven = "Such people live easily, but luck comes to them as a result of creative work. Talent is not expressed clearly."
                if seven == 2:
                    text_seven = "A gifted person with a fine artistic, musical taste and a penchant for painting. Selfishness in his work has both good and bad sides. He is lucky in gambling and forgetful in virtue."
                if seven == 3:
                    text_seven = "A special sign of people who visit the earth for a short time. If they stay on this path, serious illnesses await them. Sensitivity ruins them because of a heightened sense of justice."
                if seven >= 4:
                    text_seven = "Sign of an angel. People who constantly care about others, but, as a rule, do not live to old age."
                if eight == 0:
                    text_eight = "A person who has no sense of duty at all. If, say, he borrows, then he is in no hurry to give back and misses all the calculation deadlines."
                if eight == 1:
                    text_eight = "These people have a sense of duty and are extremely conscientious."
                if eight == 2:
                    text_eight = "Developed sense of duty. Amazing willingness to help others. This person is a wonderful family man, but dependent on dishonest people."
                if eight == 3:
                    text_eight = "A symbol of duty to the people who raised its owner. The symbol of the chosen people who lead the people. People who achieve outstanding results."
                if eight >= 4:
                    text_eight = "The sign carries parapsychological abilities and an immense sensitivity to the exact sciences. An amazing sign of people who follow supernatural paths."
                if nine == 0:
                    text_nine = "Only those born after 2000 can have the absence of a nine. From the very birth, one must begin to develop memory and logic in order to fill the empty square by school."
                if nine == 1:
                    text_nine = "The most mysterious sign. To comprehend it, a person must work all his life."
                if nine == 2:
                    text_nine = "Smart from birth. They don't like to learn, because they are used to gaining knowledge easily. The main obstacle in this is a sense of irony. Independence."
                if nine == 3:
                    text_nine = " They are very smart people. Cognition presents no difficulties for them. Excellent conversationalists."
                if nine >= 4:
                    text_nine = "People to whom the truth is revealed. If at the same time they have developed intuition, then there is a complete guarantee against failure in any undertaking. These people are quite unpleasant, rude, merciless and cruel. It is difficult, sometimes impossible to make them adequate in society."
                first_line = one + four + seven
                second_line = two + five + eight
                third_line = three + six + nine
                if first_line == 0:
                    text_1_line = "Meaning A person does not set goals and objectives, hoping for a chance or other people, it is easy enough to convince him and force him to abandon his plans."
                if first_line == 1:
                    text_1_line = "Weak determination; a person can get involved in an argument, but this does not mean that he wants to achieve a result, as a rule, it is only a desire to defeat another in an argument. He hopes for a chance and friends."
                if first_line == 2:
                    text_1_line = "Normal purposefulness. We can say that a person slowly scatters through life. He first learns his capabilities and only after that begins to set himself worthy goals."
                if first_line == 3:
                    text_1_line = "A person can change his goals completely unpredictably (urgently, suddenly, suddenly). Often his choice is unjustified and inexplicable."
                if first_line == 4:
                    text_1_line = "Strong dedication. A person sets a goal, only after that he begins to measure his capabilities and interest in the goal itself. Very often he achieves goals that do not correspond to his interests or capabilities. Choosing the right direction, you should not underestimate the goals."
                if first_line == 5:
                    text_1_line = "A very strong sense of purpose. This means that, having set a goal, a person can forget that next to him people, close ones, relatives, - he can lose much more, but he will achieve the goal. It is necessary to control the sense of proportion in achievement of the task. "
                if first_line >= 6:
                    text_1_line = "Quality overload. A person sets high goals or several goals at the same time, which slows him down in moving forward."
                if second_line == 0:
                    text_2_line = "A person is not a family man. This means that his family is in last place. Such people, as a rule, are in no hurry to start a family (they are more interested in work, career, friends, etc.)."
                if second_line == 1 or second_line == 2:
                    text_2_line = "A person remembers that a family needs to be created, but does not show any efforts in this direction. He is waiting for a case when everything will be formed by itself (he is waiting for the offer to start a family)."
                if second_line == 3:
                    text_2_line = "A person rushes between a strong desire to start a family, at all costs, and a reluctance to do it at all. If such a person decides to marry, then it is necessary to use the case, otherwise everything will be postponed for a long time."
                if second_line == 4:
                    text_2_line = "A person wants to start a family and does it without delaying. As a rule, it rarely causes the family to break up, as he seeks to keep it."
                if second_line == 5:
                    text_2_line = "A very strong quality of a family man. Such people try to see their family ideally (in their opinion). The only thing that can excuse them is that they make the same demands on themselves. Without a family they cannot exist at all."
                if second_line >= 6:
                    text_2_line = "The quality of a family man is overwhelmed, which means weakening of this quality. The explanation is simple - they are looking for their ideal for a very long time, which leads to inhibition in creating a family."
                if third_line == 0 or third_line == 1:
                    text_3_line = "A person is a revolutionary in spirit. He seeks to change everything around him, changes the environment, the place of work, challenges almost everything, striving to change everyone and everything."
                if third_line == 2:
                    text_3_line = "A person is easy- going , but can already stop his revolutionary impulse (if desired)."
                if third_line == 3:
                    text_3_line = "A person who is unstable in habits. Can initiate many habits and attachments, creating stability, but also easily abandon them for no apparent reason; after a while, can reanimate forgotten attachments. All this happens unexpectedly."
                if third_line == 4 or third_line == 5:
                    text_3_line = "Very stable people. Surround themselves with different attachments and habits, creating a stable environment. May be a little boring in their attachments. Very difficult to change."
                if third_line >= 6:
                    text_3_line = "An overload of the quality of stability. A person tends to surround himself with such an abundance of habits that he begins to cancel them himself, since they interfere with him. You can say that he is struggling with his own stability."
                first_col = one + two + three
                second_col = four + five + six
                third_col = seven + eight + nine
                if first_col in (0, 1, 2, 3):
                    text_1_col = "We can say that a person has low self-esteem, underestimates his capabilities."
                if first_col == 4:
                    text_1_col = "Good self-esteem. A person seeks to stand out from the crowd and puts a lot of effort for this (another matter, is in the right direction?)."
                if first_col == 5:
                    text_1_col = "Very strong self-esteem, it can be overestimated when a person, without improving, begins to evaluate himself only by his potential, exaggerating them."
                if first_col >= 6:
                    text_1_col = "An overload of the quality of self-esteem leads to the fact that a person, carried away by showing himself, forgets about his true abilities and is occupied with more external form than internal content. Such people, as rules, do not achieve their goals, having spent all their ardor flashing in front of a crowd that admires their appearance. "
                if second_col in (0, 1):
                    text_2_col = "A person does not want to provide for himself, he can afford to sit on the neck of someone (parents, wife, husband). This line does not pose a particular danger, given its weakness for women, since the provision of the family must rest on the shoulders of the husband."
                if second_col == 2:
                    text_2_col = "A person remembers that he needs to feed his family and, fearing this in the future, begins to look for a profession for the pay that is offered. As a result, a person can give up his dream for a stable income, but if there is an opportunity not to do this, then he will not really bother, because he is not very eager to feed himself and his family. "
                if second_col == 3:
                    text_2_col = "Such people can work impulsively. Their principle is to work quickly, to last for a while, and then you can work more."
                if second_col in (4, 5):
                    text_2_col = "People devote a lot of time and energy to supporting their families. Very often this is their only goal in life."
                if second_col >= 6:
                    text_2_col = "Quality overload, a person, starting to work intensively, quickly wears out himself and comes to a complete removal from work (overstrained), he does many different things, spray himself, creating a complete illusion of work"
                text_3_col = "The strength of a talent is determined by the number of digits in a column. But six or more digits lead to an overload of quality, which is not good. Whether a person will reveal talent depends only on him."
                telegraph.create_account(short_name='совместимость')
                response = telegraph.create_page(
                    f'Pythagoras square {date_save}',
                    html_content=f"Your Pythagoras square<br>"
                                 f"{one} ░ {four} ░ {seven}<br>"
                                 f"{two} ░ {five} ░ {eight}<br>"
                                 f"{three} ░ {six} ░ {nine}<br>"
                                 f"<br>"
                                 f"1️⃣<i>Number 1 in the psychomatrix is responsible for a person's character, his volitional qualities, the strength of his desire for power, the ability to defend his views.</i><br>"
                                 f"<br>"
                                 f"You have units - {one} pcs: {text_one} <br>"
                                 f"___________________________________<br>"
                                 f"<br>"
                                 f"2️⃣<i>The number 2 in the Pythagorean numerical system denotes human energy. You need to understand that energy in this case is a person's actions in the family, at work, in society.</i><br>"
                                 f"<br>"
                                 f"You have two - {two} pieces: {text_two}<br>"
                                 f"___________________________________<br>"
                                 f"<br>"
                                 f"3️⃣<i>The number 3 in the psychomatrix is responsible for interest in sciences and, first of all, in exact sciences or technology.</i><br>"
                                 f"<br>"
                                 f"You have triples - {three} pcs: {text_three}<br>"
                                 f"___________________________________<br>"
                                 f"<br>"
                                 f"4️⃣<i>The number 4 in the psychomatrix is responsible for human health.</i><br>"
                                 f"<br>"
                                 f"You have fours - {four} pieces: {text_four}<br>"
                                 f"___________________________________<br>"
                                 f"<br>"
                                 f"5️⃣<i>The number 5 in the psychomatrix is responsible for the logic and intuition of a person, which in turn determines a person's ability to make plans and analyze a situation, to understand exact sciences and technology.</i><br>"
                                 f"<br>"
                                 f"You have fives - {five} pieces: {text_five}<br>"
                                 f"___________________________________<br>"
                                 f"<br>"
                                 f"6️⃣<i>The meaning of the number 6 is the degree of down-to-earthness of a person, a tendency to physical labor.</i><br>"
                                 f"<br>"
                                 f"You have sixes - {six} pieces: {text_six}<br>"
                                 f"___________________________________<br>"
                                 f"<br>"
                                 f"7️⃣<i>Number 7 has always been associated with the concept of luck (good luck).</i><br>"
                                 f"<br>"
                                 f"You have sevens - {seven} pcs: {text_seven}<br>"
                                 f"___________________________________<br>"
                                 f"<br>"
                                 f"8️⃣<i>Number 8 is responsible for a sense of duty towards loved ones (parents, family), a sense of tolerance and kindness - qualities that we should show in relation to parents and loved ones.</i><br>"
                                 f"<br>"
                                 f"You have eights - {eight} pcs: {text_eight}<br>"
                                 f"___________________________________<br>"
                                 f"<br>"
                                 f"9️⃣<i>The number 9 in the psychomatrix is responsible for the mind, memory and clairvoyance of a person.</i><br>"
                                 f"<br>"
                                 f"You have nines - {nine} pieces: {text_nine}<br>"
                                 f"<br>"
                                 f"___________________________________<br>"
                                 f"<br>"
                                 f"⬇️<i>Sum of the first line (purposefulness): {first_line}</i><br>"
                                 f"{text_1_line}<br>"
                                 f"___________________________________<br>"
                                 f"<br>"
                                 f"⬇️<i>Sum of second line (family): {second_line}</i><br>"
                                 f"{text_2_line}<br>"
                                 f"___________________________________<br>"
                                 f"<br>"
                                 f"⬇️<i>Sum of third line (habit): {third_line}</i><br>"
                                 f"{text_3_line}<br>"
                                 f"___________________________________<br>"
                                 f"<br>"
                                 f"➡️<i>Sum of the first column (self-reported): {first_col}</i><br>"
                                 f"{text_1_col}<br>"
                                 f"___________________________________<br>"
                                 f"<br>"
                                 f"➡️<i>Sum of the second column (related to work): {second_col}</i><br>"
                                 f"{text_2_col}<br>"
                                 f"___________________________________<br>"
                                 f"<br>"
                                 f"➡️<i>Third Column Sum (Talent): {third_col}</i><br>"
                                 f"{text_3_col}<br>"
                )
                print(response)
                link = 'http://telegra.ph/{}'.format(response['path'])
                msg_text = hlink(" ", link)
                await message.answer(f"Calculation{msg_text}result:")
            elif user.language == "es":
                if one == 0:
                    text_one = f"Se encuentra solo en personas nacidas después del 2000. Él cree que el mundo gira en torno a él y todos le deben algo. Es importante en la primera infancia aliviarlo del sentimiento de su unicidad y peculiaridad, es preferible estar criado en equipo "
                if one == 1:
                    text_one = f"Un egoísta refinado . No presta atención a quienes lo rodean y busca beneficiarse de todas las situaciones solo para él. Tiene poco interés en otras personas y en lo que viven. Lo principal es que solo él vive y debe En Vivo."
                if one == 2:
                    text_one = f"Un personaje muy cercano al egoísta. Siempre busca la aprobación de los demás, aunque no existan requisitos previos para ello. Le gusta elogiarse a sí mismo. Se parece a sí mismo el más inteligente y talentoso y se sorprende de que los demás no lo noten. "
                if one == 3:
                    text_one = f"La media dorada. El personaje es tranquilo, dócil. La persona es sociable, no le gusta obedecer, pero no se apresura al liderazgo. Si hablas con esa persona de corazón a corazón, siempre puedes encontrar un compromiso."
                if one == 4:
                    text_one = f"Un hombre de carácter fuerte, obstinado. No tolera las mentiras y los engaños, pero a veces puede hacerlo por el bien de sus seres queridos. Los hombres con este carácter eligen el papel de militares profesionales, las mujeres suelen mantener su familias en sus manos "
                if one == 5:
                    text_one = f"Un dictador y tirano. Por el bien de su idea o capricho, puede arrojar millones de vidas humanas por el viento. Para lograr el objetivo, camina sobre cadáveres, como dicen. desorden. Persistente en las intenciones, en venganza , se adapta bien. Casi siempre tiene una especie de manía. Siente apego a los niños (su) "
                if one >= 6:
                    text_one = f"Una combinación rara. Una persona es inusualmente cruel, pero para quienes están cerca de él o por el bien de la humanidad, es capaz de hacer lo imposible. Una persona con una idea fanática y muy difícil de comunicar"
                if two == 0:
                    text_two = "La bioenergía está en el nivel más bajo; un canal está abierto para su reclutamiento intensivo. Estas personas aman las antigüedades, los libros antiguos, tratan bien a los demás, tratan de alimentarse de ellos; educados y nobles. Las excepciones del plan opuesto son raras . "
                if two == 1:
                    text_two = "Las personas son ordinarias en términos bioenergéticos. Evitan situaciones estresantes, emociones fuertes. Solo necesitan educación física y deportes, e incluso mejor yoga. Sensibles a los cambios en la atmósfera."
                if two == 2:
                    text_two = "Un suministro relativamente grande de bioenergía. Personas que pueden convertirse en buenos médicos, enfermeras, enfermeras. Su vocación es la medicina. El estrés nervioso es raro en sus familias."
                if two == 3:
                    text_two = "Un signo de un psíquico. Quizás él mismo desconozca tales habilidades, pero se cura con su biocampo, incluso con su presencia. Estas personas han estado esperando un empujón durante muchos años para revelar sus habilidades."
                if two >= 4:
                    text_two = "Si conoces a una mujer de la que todos están enamorados, o un hombre irresistible, es porque tienen un exceso de bioenergía que están dispuestos a compartir con todos. Desafortunadamente, estas personas son muy vulnerables al mal, energéticamente tipos hambrientos con capacidades satánicas "
                if three == 0:
                    text_three = "Gente limpia y decente, excelentes dueños, pero algo entrometidos en su constante búsqueda de la limpieza. Muy puntuales, les gusta mirarse en el espejo, explicarse floridamente. El trabajo minucioso se hace impecablemente."
                if three == 1:
                    text_three = "Gente de buen humor. No les gusta ahorrar dinero , son de mente amplia, a menudo contradictorios. La casa está desordenada, pero a veces todo se lleva repentina e inesperadamente a un estado perfecto."
                if three == 2:
                    text_three = "ersonas con mentalidad científica . Tienen cierta mente analítica"
                if three >= 3:
                    text_three = "Adicción a la ciencia. La realización de esta inclinación da lugar a la pedantería, el desapego, la tacañería y, finalmente, una constante necesidad de justicia"
                if four == 0:
                    text_four = "La salud es muy débil, una persona es susceptible a diversas enfermedades desde la infancia. Tal persona estará enferma cuanto más tiempo, más de dos en su pronóstico matemático, porque da su energía al mundo"
                if four == 1:
                    text_four = "La salud es normal, hay que moderarla, de lo contrario, con la vejez una persona se convertirá en un naufragio. Los deportes principales son nadar y correr."
                if four == 2:
                    text_four = "La salud es fuerte. Estas personas no anuncian su potencia sexual, pero pueden ser símbolos de atractivo sexual"
                if four >= 3:
                    text_four = "Personas con muy buena salud, que son extremadamente raras. Su temperamento sexual es increíblemente atractivo"
                if five == 0:
                    text_five = "El canal de comunicación con el mundo sutil, con el Cosmos, está cerrado al nacer. Una persona así está ocupada con cálculos, experimentos y pruebas, reflexiones intensas. Estas personas cometen muchos errores"
                if five == 1:
                    text_five = "El canal de comunicación está abierto. Se reduce el número de errores de estas personas, las situaciones de la vida están bajo control para sacarles el máximo partido."
                if five == 2:
                    text_five = "Intuición fuertemente desarrollada. Presencia de sueños proféticos, premoniciones de eventos. Revelaciones con un solo detalle. Capacidad para predecir tanto el pasado como el futuro. La necesidad de un trabajo legal e investigativo."
                if five == 3:
                    text_five = "Casi clarividentes. Sin ningún conocimiento ni consejos, estas personas saben cómo actuar por sí mismas y por su entorno. En algunos casos, predicen con precisión eventos futuros, pero no pueden indicar cómo evitar problemas"
                if five >= 4:
                    text_five = "Clarividentes. Son claros e indiferentes a todo lo que sucede a su alrededor. A menudo se quedan fuera del tiempo y del espacio, como si estuvieran incluidos en algún otro sistema de existencia."
                if six == 0:
                    text_six = "Esta persona vino a la tierra para adquirir un oficio. Para desarrollarse y ascender en la escala de la vida, necesita trabajo físico, que no le gusta. La imaginación, la fantasía, el gusto artístico son los principales motores de su desarrollo. Sin embargo, a pesar de las necesidades que lo distraen, es capaz de realizar acciones serias "
                if six == 1:
                    text_six = "Una persona con los pies en la tierra , pero capaz de acciones humanas por cualidades espirituales. Puede tropezar con las ciencias creativas o exactas, pero se requiere trabajo físico para prolongar su existencia. Muy a menudo hay manifestaciones en los campos artísticos."
                if six == 2:
                    text_six = "Un hombre con los pies en la tierra. Busca trabajo físico que interfiera con su desarrollo. La actividad mental y el arte es lo único que puede levantar a esas personas"
                if six == 3:
                    text_six = "El signo de Satanás, un signo ominoso. Personas temperamentales que se esfuerzan por estar siempre en el centro de la sociedad debido a su encanto. Es una persona poco confiable, que busca, a menudo cambia de pareja casual."
                if six >= 4:
                    text_six = "Una persona que ha resuelto la malicia, la base en encarnaciones anteriores y trata de expulsarla a través del trabajo, la actividad mental y la mejora"
                if seven == 0:
                    text_seven = "Una persona nacida para entender qué es el talento. Su experiencia de vida y sus hechos ayudan a ganar talento, y el sufrimiento y la religión empujan a entenderlo. Lo principal es captar el momento en que el talento será enviado desde arriba"
                if seven == 1:
                    text_seven = "Estas personas viven con facilidad, pero la suerte les llega como resultado del trabajo creativo. El talento no se expresa con claridad."
                if seven == 2:
                    text_seven = "Una persona talentosa con un buen gusto artístico, musical y una inclinación por la pintura. El egoísmo en su trabajo tiene aspectos buenos y malos. Tiene suerte en el juego y olvidadizo en la virtud."
                if seven == 3:
                    text_seven = "Un signo especial de personas que visitan la tierra por poco tiempo. Si permanecen en este camino, les esperan graves enfermedades. La sensibilidad los arruina debido a un mayor sentido de la justicia."
                if seven >= 4:
                    text_seven = "Signo de ángel. Personas que se preocupan constantemente por los demás, pero que, por regla general, no viven hasta la vejez."
                if eight == 0:
                    text_eight = "Una persona que no tiene ningún sentido del deber. Si, por ejemplo, pide prestado, entonces no tiene prisa por devolver y no cumple con todos los plazos de cálculo"
                if eight == 1:
                    text_eight = "Estas personas tienen un sentido del deber y son extremadamente concienzudas"
                if eight == 2:
                    text_eight = "Desarrolló un sentido del deber. Increíble disposición para ayudar a los demás. Esta persona es un maravilloso hombre de familia, pero depende de personas deshonestas."
                if eight == 3:
                    text_eight = "Un símbolo de deber para con las personas que criaron a su dueño. El símbolo de las personas elegidas que lideran a las personas. Personas que logran resultados sobresalientes."
                if eight >= 4:
                    text_eight = "El signo tiene habilidades parapsicológicas y una inmensa sensibilidad a las ciencias exactas. Un signo asombroso de personas que siguen caminos sobrenaturales."
                if nine == 0:
                    text_nine = "Solo los nacidos después del 2000 pueden tener la ausencia de un nueve. Desde el mismo nacimiento, uno debe comenzar a desarrollar la memoria y la lógica para llenar el cuadrado vacío por escuela"
                if nine == 1:
                    text_nine = "El signo más misterioso. Para comprenderlo, una persona debe trabajar toda su vida"
                if nine == 2:
                    text_nine = "Inteligentes desde el nacimiento. No les gusta aprender, porque están acostumbrados a adquirir conocimientos fácilmente. El principal obstáculo en esto es el sentido de la ironía. Independencia."
                if nine == 3:
                    text_nine = "Son personas muy inteligentes. El conocimiento no les presenta ninguna dificultad. Excelentes conversadores."
                if nine >= 4:
                    text_nine = "Son personas muy inteligentes. El conocimiento no les presenta ninguna dificultad. Excelentes conversadores."
                first_line = one + four + seven
                second_line = two + five + eight
                third_line = three + six + nine
                if first_line == 0:
                    text_1_line = "Significado Una persona no se fija metas y objetivos, esperando una oportunidad u otras personas, es bastante fácil convencerlo y obligarlo a abandonar sus planes. "
                if first_line == 1:
                    text_1_line = "Determinación débil; una persona puede involucrarse en una discusión, pero esto no significa que quiera lograr un resultado, como regla, es solo un deseo de derrotar a otro en una discusión. Espera una oportunidad y amigos "
                if first_line == 2:
                    text_1_line = "Propósito normal. Podemos decir que una persona se dispersa lentamente a lo largo de la vida. Primero aprende sus capacidades y solo después de eso comienza a fijarse metas dignas para sí mismo. "
                if first_line == 3:
                    text_1_line = "Una persona puede cambiar sus metas de manera completamente impredecible (urgente, repentina, repentina). A menudo, su elección es injustificada e inexplicable."
                if first_line == 4:
                    text_1_line = "Fuerte dedicación. Una persona establece una meta, solo después de eso comienza a medir sus capacidades e interés en la meta en sí. Muy a menudo logra metas que no corresponden a sus intereses o capacidades. Al elegir la dirección correcta, debe No subestimes los goles "
                if first_line == 5:
                    text_1_line = "Un sentido de propósito muy fuerte. Esto significa que, habiendo fijado una meta, una persona puede olvidar que junto a él personas, seres cercanos, parientes, puede perder mucho más, pero logrará la meta. Es necesario para controlar el sentido de la proporción en el logro de la tarea "
                if first_line >= 6:
                    text_1_line = "Sobrecarga de calidad. Una persona establece metas altas o varias al mismo tiempo, lo que le ralentiza para avanzar"
                if second_line == 0:
                    text_2_line = "Una persona no es un hombre de familia. Esto significa que su familia está en el último lugar. Estas personas, por regla general, no tienen prisa por formar una familia (están más interesadas en el trabajo, la carrera, los amigos, etc.) "
                if second_line == 1 or second_line == 2:
                    text_2_line = "Una persona recuerda que se necesita crear una familia, pero no muestra ningún esfuerzo en esta dirección. Está esperando un caso en el que todo saldrá por sí solo (está esperando la propuesta para formar una familia) . "
                if second_line == 3:
                    text_2_line = "Una persona corre entre un fuerte deseo de formar una familia, a toda costa, y una renuencia a hacerlo. Si esa persona decide casarse, entonces es necesario usar el caso, de lo contrario todo se pospondrá por mucho tiempo."
                if second_line == 4:
                    text_2_line = "Una persona quiere formar una familia y lo hace sin demora. Como regla, rara vez causa la ruptura de la familia, ya que él busca mantenerla"
                if second_line == 5:
                    text_2_line = "Una cualidad muy fuerte de un hombre de familia. Estas personas tratan de ver a su familia de manera ideal (en su opinión). Lo único que puede excusarlos es que se exigen lo mismo a sí mismos. Sin una familia no pueden existir todas."
                if second_line >= 6:
                    text_2_line = "La calidad de un hombre de familia está abrumada, lo que significa un debilitamiento de esta cualidad. La explicación es simple: están buscando su ideal desde hace mucho tiempo, lo que conduce a la inhibición para crear una familia"
                if third_line == 0 or third_line == 1:
                    text_3_line = "Una persona es de espíritu revolucionario. Busca cambiar todo lo que le rodea, cambia el entorno, el lugar de trabajo, desafía casi todo, lucha por cambiar a todos y todo "
                if third_line == 2:
                    text_3_line = "Una persona es tranquila, pero ya puede detener su impulso revolucionario (si lo desea) "
                if third_line == 3:
                    text_3_line = "Una persona inestable. Puede iniciar muchos hábitos y apegos, creando estabilidad, pero también abandonarlos fácilmente sin razón aparente; después de un tiempo, puede reanimar los apegos olvidados. Todo esto sucede inesperadamente"
                if third_line == 4 or third_line == 5:
                    text_3_line = "Gente muy estable. Rodearse de diferentes apegos y hábitos, creando un ambiente estable. Puede ser un poco aburrido en sus apegos. Muy difícil de cambiar."
                if third_line >= 6:
                    text_3_line = "Una sobrecarga de la cualidad de la estabilidad. Una persona tiende a rodearse de tal abundancia de hábitos que comienza a anularlos él mismo, ya que le interfieren. Se puede decir que él mismo está luchando con su propia estabilidad."
                first_col = one + two + three
                second_col = four + five + six
                third_col = seven + eight + nine
                if first_col in (0, 1, 2, 3):
                    text_1_col = "Podemos decir que una persona tiene baja autoestima, subestima sus capacidades"
                if first_col == 4:
                    text_1_col = "Buena autoestima. Una persona se esfuerza por destacarse entre la multitud y pone mucho esfuerzo en esto (otro asunto, ¿va en la dirección correcta?)"
                if first_col == 5:
                    text_1_col = "Autoestima muy fuerte, se puede sobrestimar cuando una persona, sin mejorar, comienza a evaluarse a sí misma solo por sus potencialidades, exagerándolas."
                if first_col >= 6:
                    text_1_col = "Una sobrecarga de la calidad de la autoestima lleva a que una persona, dejándose llevar por mostrarse a sí mismo, se olvide de sus verdaderas habilidades y se ocupe más de la forma externa que del contenido interno. Tales personas, como reglas, hacen No lograr sus objetivos, habiendo gastado todo su ardor destellando frente a una multitud que admira su apariencia"
                if second_col in (0, 1):
                    text_2_col = "Una persona no quiere mantenerse a sí misma, puede permitirse sentarse en el cuello de alguien (padres, esposa, esposo). Esta línea no representa un peligro particular por su debilidad para las mujeres, ya que la provisión de la la familia debe descansar sobre los hombros del marido "
                if second_col == 2:
                    text_2_col = "Una persona recuerda que necesita alimentar a su familia y, temiendo esto en el futuro, comienza a buscar una profesión por el salario que se le ofrece. Como resultado, una persona puede renunciar a su sueño por un ingreso estable, pero si existe la oportunidad de no hacer esto, entonces realmente no se molestará, porque no está muy ansioso por alimentarse a sí mismo y a su familia "
                if second_col == 3:
                    text_2_col = "Estas personas pueden trabajar impulsivamente. Su principio es trabajar rápido, durar un tiempo, y luego puedes trabajar más"
                if second_col in (4, 5):
                    text_2_col = "Las personas dedican mucho tiempo y energía a mantener a sus familias. Muy a menudo, este es su único objetivo en la vida"
                if second_col >= 6:
                    text_2_col = "Sobrecarga de calidad, una persona, que comienza a trabajar intensamente, se desgasta rápidamente y se retira por completo del trabajo (sobrecargado), hace muchas cosas diferentes, se rocía, creando una completa ilusión de trabajo"
                text_3_col = "La fuerza de un talento está determinada por la cantidad de dígitos en una columna. Pero seis o más dígitos conducen a una sobrecarga de calidad, lo cual no es bueno. Que una persona revele talento depende solo de él"
                telegraph.create_account(short_name='совместимость')
                response = telegraph.create_page(
                    f'Tu plaza de Pitágoras {date_save}',
                    html_content=f"Tu plaza de Pitágoras<br>"
                                 f"{one} ░ {four} ░ {seven}<br>"
                                 f"{two} ░ {five} ░ {eight}<br>"
                                 f"{three} ░ {six} ░ {nine}<br>"
                                 f"<br>"
                                 f"1️⃣<i>El número 1 en la psicomatriz es responsable del carácter de una persona, sus cualidades volitivas, la fuerza de su deseo de poder, la capacidad de defender sus puntos de vista.</i><br>"
                                 f"<br>"
                                 f"Tiene unidades - {one} шт: {text_one} <br>"
                                 f"___________________________________<br>"
                                 f"<br>"
                                 f"2️⃣<i>El número 2 en el sistema numérico pitagórico denota la energía de una persona. Debe comprender que la energía en este caso son las acciones de una persona en la familia, en el trabajo, en la sociedad.</i><br>"
                                 f"<br>"
                                 f"Tienes dos - {two} шт: {text_two}<br>"
                                 f"___________________________________<br>"
                                 f"<br>"
                                 f"3️⃣<i>El número 3 de la psicomatriz es responsable del interés por las ciencias y, en primer lugar, por las ciencias exactas o la tecnología.</i><br>"
                                 f"<br>"
                                 f"Tienes triples - {three} шт: {text_three}<br>"
                                 f"___________________________________<br>"
                                 f"<br>"
                                 f"4️⃣<i>El número 4 de la psicomatriz es responsable de la salud humana.</i><br>"
                                 f"<br>"
                                 f"Tienes cuatro - {four} шт: {text_four}<br>"
                                 f"___________________________________<br>"
                                 f"<br>"
                                 f"5️⃣<i>El número 5 en la psicomatriz es responsable de la lógica y la intuición de una persona, que a su vez determina la capacidad de una persona para hacer planes y analizar una situación, para comprender las ciencias y la tecnología exactas.</i><br>"
                                 f"<br>"
                                 f"Tienes cinco - {five} шт: {text_five}<br>"
                                 f"___________________________________<br>"
                                 f"<br>"
                                 f"6️⃣<i>El significado del número 6 es el grado de terrenalidad de una persona, una tendencia al trabajo físico. </i><br>"
                                 f"<br>"
                                 f"Tienes seis - {six} шт: {text_six}<br>"
                                 f"___________________________________<br>"
                                 f"<br>"
                                 f"7️⃣<i>El número 7 siempre se ha asociado con el concepto de suerte (buena suerte).</i><br>"
                                 f"<br>"
                                 f"Tienes siete - {seven} шт: {text_seven}<br>"
                                 f"___________________________________<br>"
                                 f"<br>"
                                 f"8️⃣<i>El número 8 es responsable del sentido del deber hacia los seres queridos (padres, familia), un sentido de tolerancia y bondad, cualidades que debemos mostrar en relación con los padres y seres queridos.</i><br>"
                                 f"<br>"
                                 f"Tienes ocho - {eight} шт: {text_eight}<br>"
                                 f"___________________________________<br>"
                                 f"<br>"
                                 f"9️⃣<i>El número 9 en la psicomatriz es responsable de la mente, la memoria y la clarividencia de una persona.</i><br>"
                                 f"<br>"
                                 f"Tienes nueves - {nine} шт: {text_nine}<br>"
                                 f"<br>"
                                 f"___________________________________<br>"
                                 f"<br>"
                                 f"⬇️<i>Suma de la primera línea (propósito): {first_line}</i><br>"
                                 f"{text_1_line}<br>"
                                 f"___________________________________<br>"
                                 f"<br>"
                                 f"⬇️<i>Suma de la segunda línea (familia): {second_line}</i><br>"
                                 f"{text_2_line}<br>"
                                 f"___________________________________<br>"
                                 f"<br>"
                                 f"⬇️<i>Suma de la tercera línea (hábito): {third_line}</i><br>"
                                 f"{text_3_line}<br>"
                                 f"___________________________________<br>"
                                 f"<br>"
                                 f"➡️<i>Suma de la primera columna (autoinformada): {first_col}</i><br>"
                                 f"{text_1_col}<br>"
                                 f"___________________________________<br>"
                                 f"<br>"
                                 f"➡️<i>Suma de la segunda columna (relacionada con el trabajo): {second_col}</i><br>"
                                 f"{text_2_col}<br>"
                                 f"___________________________________<br>"
                                 f"<br>"
                                 f"➡️<i>Suma de la tercera columna (talento): {third_col}</i><br>"
                                 f"{text_3_col}<br>"
                )
                print(response)
                link = 'http://telegra.ph/{}'.format(response['path'])
                msg_text = hlink(" ", link)
                await message.answer(f"Resultado del{msg_text}cálculo:")
            elif user.language == "de":
                if one == 0:
                    text_one = "Es kommt nur bei Menschen vor, die nach 2000 geboren wurden. Er glaubt, dass sich die Welt um ihn dreht und jeder ihm etwas schuldet. Es ist wichtig, ihm in der frühen Kindheit das Gefühl seiner Einzigartigkeit und Eigenart zu nehmen, es ist vorzuziehen im Team aufgewachsen."
                if one == 1:
                    text_one = "Ein raffinierter Egoist. Er achtet nicht auf seine Umgebung und versucht aus allen Situationen nur für sich selbst zu profitieren. Er hat wenig Interesse an anderen Menschen und wovon sie leben. Hauptsache, nur er lebt und soll wohnen."
                if one == 2:
                    text_one = "Ein Charakter, der dem Egoismus sehr nahe kommt. Sucht immer die Anerkennung anderer, auch wenn es dafür keine Voraussetzungen gibt. Lobt sich gerne selbst. Er scheint sich am klügsten und talentiertesten zu sein und wundert sich, dass andere es nicht bemerken. "
                if one == 3:
                    text_one = "Die goldene Mitte. Der Charakter ist ruhig, gelehrig. Die Person ist gesellig, gehorcht nicht wirklich gerne, eilt aber nicht zur Führung. Wenn man mit so einer Person von Herzen spricht, findet man immer eine Kompromiss."
                if one == 4:
                    text_one = "Ein Mann mit starkem Charakter, starkem Willen. Er duldet keine Lügen und Hetze, aber manchmal kann er es um seiner Lieben willen tun. Männer mit diesem Charakter wählen die Rolle von professionellen Militärs, Frauen halten normalerweise ihre Familien in ihren Händen."
                if one == 5:
                    text_one = "Ein Diktator und Tyrann. Um seiner Idee oder Laune willen kann er Millionen von Menschenleben in den Wind werfen. Um das Ziel zu erreichen, geht er über Leichen, wie sie sagen. Unordnung. Beharrlich in Absichten, in Rache Sie passt sich gut an. Hat fast immer eine Art Manie. Fühlt Verbundenheit zu Kindern (seinen) "
                if one >= 6:
                    text_one = "Eine seltene Kombination. Ein Mensch ist ungewöhnlich grausam, aber für die Menschen, die ihm nahe stehen oder um der Menschheit willen, ist er in der Lage, das Unmögliche zu tun. Ein Mensch mit einer fanatischen Idee und sehr schwer zu kommunizieren."
                if two == 0:
                    text_two = "Bioenergie ist auf der untersten Ebene; ein Kanal ist offen für seine intensive Rekrutierung. Diese Leute lieben Antiquitäten, alte Bücher, behandeln andere gut, versuchen sich davon zu ernähren; wohlerzogen und edel. Ausnahmen vom gegenteiligen Plan sind selten ."
                if two == 1:
                    text_two = "Menschen sind bioenergetisch gewöhnlich. Sie vermeiden Stresssituationen, starke Emotionen. Sie brauchen nur Sport und Sport und noch besser Yoga. Sensibel für Veränderungen in der Atmosphäre."
                if two == 2:
                    text_two = "Ein relativ großer Vorrat an Bioenergie. Menschen, die gute Ärzte, Krankenschwestern, Pfleger werden können. Ihre Berufung ist die Medizin. Nervöser Stress ist in ihren Familien selten."
                if two == 3:
                    text_two = "Ein Zeichen eines Hellsehers . Vielleicht ist er sich solcher Fähigkeiten nicht bewusst, aber er heilt mit seinem Biofeld, sogar mit seiner Anwesenheit. Solche Leute warten seit vielen Jahren auf einen Schubs, um ihre Fähigkeiten zu offenbaren."
                if two >= 4:
                    text_two = "Wenn du eine Frau triffst , in die alle verliebt sind, oder einen unwiderstehlichen Mann, dann liegt das daran, dass sie einen Überschuss an Bioenergie haben, den sie bereit sind, mit allen zu teilen. Leider sind diese Menschen energetisch sehr anfällig für das Böse hungrige Typen mit satanischen Fähigkeiten."
                if three == 0:
                    text_three = "Saubere und anständige Leute, ausgezeichnete Besitzer, aber etwas aufdringlich in ihrem ständigen Streben nach Sauberkeit. Sehr pünktlich, schaut gerne in den Spiegel, erklärt sich schwungvoll."
                if three == 1:
                    text_three = "Leute mit Laune. Sie sparen nicht gerne, sie sind aufgeschlossen, oft widersprüchlich. Das Haus ist unordentlich, aber manchmal wird alles plötzlich und unerwartet in einen perfekten Zustand gebracht."
                if three == 2:
                    text_three = " Wissenschaftsorientierte Menschen. Sie haben einen gewissen analytischen Verstand."
                if three >= 3:
                    text_three = "Sucht nach Wissenschaft. Die Erkenntnis dieser Neigung führt zu Pedanterie, Distanz, Geiz und schließlich zu einem ständigen Bedürfnis nach Gerechtigkeit."
                if four == 0:
                    text_four = "Die Gesundheit ist sehr schwach, ein Mensch ist von Kindheit an anfällig für verschiedene Krankheiten. Ein solcher Mensch wird umso länger krank sein, je mehr zwei in seiner mathematischen Vorhersage, weil er seine Energie der Welt gibt."
                if four == 1:
                    text_four = "Gesundheit ist durchschnittlich, sie muss ausgeglichen werden, sonst wird ein Mensch im Alter zum Wrack. Die Hauptsportarten sind Schwimmen und Laufen."
                if four == 2:
                    text_four = "Gesundheit ist stark. Solche Leute machen keine Werbung für ihre sexuelle Potenz, können aber Symbole für Sexappeal sein."
                if four >= 3:
                    text_four = "Menschen mit sehr guter Gesundheit, die extrem selten sind. Ihr sexuelles Temperament ist unglaublich attraktiv."
                if five == 0:
                    text_five = "Der Kommunikationskanal mit der feinstofflichen Welt, mit dem Kosmos, ist bei der Geburt geschlossen. Solch ein Mensch ist mit Berechnungen, Experimenten und Beweisen, intensiven Überlegungen beschäftigt. Diese Menschen machen viele Fehler."
                if five == 1:
                    text_five = "Der Kommunikationskanal ist offen. Die Anzahl der Fehler solcher Menschen wird reduziert, Lebenssituationen werden unter Kontrolle, um das Beste aus ihnen herauszuholen."
                if five == 2:
                    text_five = "Stark entwickelte Intuition. Präsenz prophetischer Träume, Vorahnungen von Ereignissen. Offenbarungen mit einem einzigen Detail. Fähigkeit, sowohl die Vergangenheit als auch die Zukunft vorherzusagen. Die Notwendigkeit von Rechts- und Ermittlungsarbeit."
                if five == 3:
                    text_five = "Fast Hellseher. Ohne Wissen und Tipps wissen solche Menschen, wie sie für sich und ihre Umgebung handeln müssen. In einigen Fällen können sie zukünftige Ereignisse genau vorhersagen, aber keine Hinweise geben, wie sie Schwierigkeiten vermeiden können."
                if five >= 4:
                    text_five = "Hellseher. Sie sind klar und gleichgültig gegenüber allem, was um sie herum passiert. Sie bleiben oft außerhalb von Zeit und Raum, als ob sie in ein anderes Existenzsystem eingebunden wären."
                if six == 0:
                    text_six = "Dieser Mensch ist auf die Erde gekommen, um ein Handwerk zu erwerben. Um sich zu entwickeln und auf der Leiter des Lebens aufzusteigen, braucht er körperliche Arbeit, die er nicht mag. Fantasie, Fantasie, künstlerischer Geschmack sind die Hauptmotoren seiner Entwicklung. trotz der ablenkenden Bedürfnisse ist er zu ernsthaften Taten fähig."
                if six == 1:
                    text_six = "Ein geerdeter Mensch, aber aufgrund seiner spirituellen Qualitäten zu humanen Taten fähig. Er mag über kreative oder exakte Wissenschaften stolpern, aber körperliche Arbeit ist erforderlich, um seine Existenz zu verlängern. Es gibt ziemlich oft Manifestationen in künstlerischen Bereichen."
                if six == 2:
                    text_six = "Ein geerdeter Mann. Sucht nach körperlicher Arbeit, die seine Entwicklung behindert . Geistige Aktivität und Kunst sind das Einzige, was solche Menschen heben kann."
                if six == 3:
                    text_six = "Das Zeichen Satans, ein unheilvolles Zeichen. Temperamentvolle Menschen, die aufgrund ihres Charmes danach streben, immer im Mittelpunkt der Gesellschaft zu stehen."
                if six >= 4:
                    text_six = "Eine Person, die in früheren Inkarnationen Bosheit und Bodenständigkeit aussortiert hat und versucht, sie durch Arbeit, geistige Aktivität und Verbesserung zu vertreiben."
                if seven == 0:
                    text_seven = "Eine Person, die geboren wurde, um zu verstehen, was Talent ist. Seine Lebenserfahrung und Taten helfen, Talente zu gewinnen, und Leiden und Religion drängen darauf, es zu verstehen. Die Hauptsache ist, den Moment zu erwischen, in dem das Talent von oben gesendet wird."
                if seven == 1:
                    text_seven = "Solche Menschen leben leicht, aber das Glück kommt durch kreative Arbeit zu ihnen. Talent kommt nicht klar zum Ausdruck."
                if seven == 2:
                    text_seven = "Ein begabter Mensch mit einem feinen künstlerischen, musikalischen Geschmack und einer Vorliebe für Malerei. Egoismus in seiner Arbeit hat sowohl gute als auch schlechte Seiten. Er hat Glück im Glücksspiel und vergesslich in Tugend."
                if seven == 3:
                    text_seven = "Ein besonderes Zeichen für Menschen, die die Erde für kurze Zeit besuchen. Wenn sie auf diesem Weg bleiben, erwarten sie schwere Krankheiten. Sensibilität ruiniert sie wegen eines erhöhten Gerechtigkeitsempfindens."
                if seven >= 4:
                    text_seven = " Engelszeichen . Menschen, die sich ständig um andere kümmern, aber in der Regel nicht alt werden."
                if eight == 0:
                    text_eight = "Ein Mensch, der überhaupt kein Pflichtgefühl hat. Wenn er beispielsweise Kredite leiht, dann hat er es nicht eilig, zurückzugeben und verpasst alle Berechnungsfristen."
                if eight == 1:
                    text_eight = "Diese Leute haben ein Pflichtbewusstsein und sind äußerst gewissenhaft."
                if eight == 2:
                    text_eight = "Entwickeltes Pflichtbewusstsein. Erstaunliche Hilfsbereitschaft. Diese Person ist ein wunderbarer Familienvater, aber abhängig von unehrlichen Menschen."
                if eight == 3:
                    text_eight = "Ein Symbol der Pflicht gegenüber dem Volk, das seinen Besitzer großgezogen hat. Das Symbol des auserwählten Volkes, das das Volk führt. Menschen, die herausragende Ergebnisse erzielen."
                if eight >= 4:
                    text_eight = "Das Zeichen trägt parapsychologische Fähigkeiten und eine immense Sensibilität für die exakten Wissenschaften. Ein erstaunliches Zeichen für Menschen, die übernatürlichen Pfaden folgen."
                if nine == 0:
                    text_nine = "Nur diejenigen, die nach 2000 geboren wurden, können die Abwesenheit einer Neun haben. Von Geburt an muss man anfangen, Gedächtnis und Logik zu entwickeln, um das leere Quadrat in der Schule zu füllen."
                if nine == 1:
                    text_nine = "Das mysteriöseste Zeichen. Um es zu verstehen, muss ein Mensch sein ganzes Leben lang arbeiten."
                if nine == 2:
                    text_nine = " Schlau von Geburt an. Sie lernen nicht gerne, weil sie es gewohnt sind, sich leicht Wissen anzueignen. Das Haupthindernis dabei ist ein Gefühl der Ironie. Unabhängigkeit."
                if nine == 3:
                    text_nine = " Sie sind sehr kluge Leute. Wissen bereitet ihnen keine Schwierigkeiten. Ausgezeichnete Gesprächspartner."
                if nine >= 4:
                    text_nine = "Menschen, denen die Wahrheit offenbart wird. Wenn sie gleichzeitig Intuition entwickelt haben, dann gibt es eine vollständige Garantie gegen das Scheitern in jedem Unternehmen. Diese Menschen sind ziemlich unangenehm, unhöflich, gnadenlos und grausam unmöglich, sie in der Gesellschaft angemessen zu machen."
                first_line = one + four + seven
                second_line = two + five + eight
                third_line = three + six + nine
                if first_line == 0:
                    text_1_line = "Bedeutung Eine Person setzt sich keine Ziele und Ziele, hofft auf eine Chance oder andere Menschen, es ist einfach genug, sie zu überzeugen und sie zu zwingen, ihre Pläne aufzugeben."
                if first_line == 1:
                    text_1_line = "Schwache Entschlossenheit; ein Mensch kann sich auf einen Streit einlassen , aber das bedeutet nicht, dass er ein Ergebnis erzielen will, in der Regel ist es nur der Wunsch, einen anderen in einem Streit zu besiegen. Er hofft auf eine Chance und Freunde."
                if first_line == 2:
                    text_1_line = "Normale Zielstrebigkeit. Wir können sagen, dass ein Mensch langsam durch das Leben zerstreut. Er lernt zuerst seine Fähigkeiten und beginnt erst danach, sich würdige Ziele zu setzen."
                if first_line == 3:
                    text_1_line = "Ein Mensch kann seine Ziele völlig unvorhersehbar ändern (dringend, plötzlich, plötzlich). Oft ist seine Wahl ungerechtfertigt und unerklärlich."
                if first_line == 4:
                    text_1_line = "Starkes Engagement. Ein Mensch setzt sich ein Ziel, erst danach beginnt er, seine Fähigkeiten und sein Interesse am Ziel selbst zu messen. Sehr oft erreicht er Ziele, die nicht seinen Interessen oder Fähigkeiten entsprechen. Die richtige Richtung wählen, sollten Sie die Ziele nicht unterschätzen."
                if first_line == 5:
                    text_1_line = "Eine sehr starke Zielstrebigkeit . Dies bedeutet, dass eine Person, nachdem sie sich ein Ziel gesetzt hat, vergessen kann, dass neben ihnen Menschen, nahestehende, Verwandte, - sie viel mehr verlieren können, aber sie werden das Ziel erreichen. Es ist notwendig, um das Augenmaß bei der Erfüllung der Aufgabe zu kontrollieren."
                if first_line >= 6:
                    text_1_line = "Qualitätsüberlastung. Ein Mensch setzt sich hohe Ziele oder mehrere Ziele gleichzeitig, was ihn in seinem Vorwärtskommen verlangsamt."
                if second_line == 0:
                    text_2_line = "Ein Mensch ist kein Familienvater. Das bedeutet, dass seine Familie an letzter Stelle steht. Solche Menschen haben es in der Regel nicht eilig, eine Familie zu gründen (sie interessieren sich mehr für Arbeit, Karriere, Freunde usw.). )."
                if second_line == 1 or second_line == 2:
                    text_2_line = "Eine Person erinnert sich daran, dass eine Familie gegründet werden muss, zeigt aber keine Bemühungen in diese Richtung. Er wartet auf einen Fall, in dem sich alles von selbst ergibt (er wartet auf den Vorschlag, eine Familie zu gründen) ."
                if second_line == 3:
                    text_2_line = "Eine Person eilt zwischen dem starken Wunsch, um jeden Preis eine Familie zu gründen, und der Zurückhaltung, es überhaupt zu tun. Wenn eine solche Person sich entscheidet zu heiraten, muss der Fall verwendet werden, sonst wird alles verschoben Für eine lange Zeit."
                if second_line == 4:
                    text_2_line = "Ein Mensch möchte eine Familie gründen und tut dies ohne Zögern. In der Regel führt dies selten dazu, dass die Familie zerbricht , da er sie behalten will."
                if second_line == 5:
                    text_2_line = "Eine sehr starke Eigenschaft eines Familienmenschen. Solche Menschen versuchen, ihre Familie (aus ihrer Sicht) ideal zu sehen. Das einzige, was sie entschuldigen kann, ist, dass sie die gleichen Ansprüche an sich selbst stellen. Ohne eine Familie können sie nicht existieren exist alle."
                if second_line >= 6:
                    text_2_line = "Die Qualität eines Familienvaters ist überfordert, was eine Schwächung dieser Eigenschaft bedeutet. Die Erklärung ist einfach - sie suchen sehr lange nach ihrem Ideal, was zu Hemmungen bei der Familiengründung führt."
                if third_line == 0 or third_line == 1:
                    text_3_line = "Ein Mensch ist ein Revolutionär im Geiste. Er versucht, alles um sich herum zu verändern, verändert die Umgebung, den Arbeitsplatz, fordert fast alles heraus und strebt danach, alles und jeden zu verändern."
                if third_line == 2:
                    text_3_line = "Ein Mensch ist locker, kann aber schon seinen revolutionären Impuls stoppen (falls gewünscht)."
                if third_line == 3:
                    text_3_line = "Eine instabile Person. Kann viele Gewohnheiten und Eigensinne initiieren, Stabilität schaffen, aber auch ohne ersichtlichen Grund leicht aufgeben; kann nach einer Weile vergessene Eigensinne wiederbeleben. All dies geschieht unerwartet."
                if third_line == 4 or third_line == 5:
                    text_3_line = "Sehr stabile Menschen. Umgeben Sie sich mit unterschiedlichen Eigensinnen und Gewohnheiten und schaffen Sie so eine stabile Umgebung. Kann in ihren Eigensinnen etwas langweilig sein. Sehr schwer zu ändern."
                if third_line >= 6:
                    text_3_line = "Eine Überlastung der Stabilitätsqualität. Ein Mensch neigt dazu, sich mit einer solchen Fülle von Gewohnheiten zu umgeben, dass er beginnt, diese selbst aufzulösen , da sie ihn stören. Man kann sagen, dass er selbst mit seiner eigenen Stabilität zu kämpfen hat. "
                first_col = one + two + three
                second_col = four + five + six
                third_col = seven + eight + nine
                if first_col in (0, 1, 2, 3):
                    text_1_col = "Wir können sagen, dass eine Person ein geringes Selbstwertgefühl hat und ihre Fähigkeiten unterschätzt."
                if first_col == 4:
                    text_1_col = "Gutes Selbstwertgefühl. Eine Person strebt danach, sich von der Masse abzuheben und gibt sich viel Mühe (eine andere Sache, geht in die richtige Richtung?)."
                if first_col == 5:
                    text_1_col = "Sehr starkes Selbstwertgefühl, es kann überschätzt werden, wenn eine Person, ohne sich zu verbessern, beginnt, sich selbst nur nach ihrem Potenzial zu bewerten und es zu übertreiben."
                if first_col >= 6:
                    text_1_col = "Eine Überlastung der Qualität des Selbstwertgefühls führt dazu, dass ein Mensch, der sich davon mitreißen lässt , seine wahren Fähigkeiten vergisst und sich mehr mit äußerer Form als mit innerem Inhalt beschäftigt. Solche Menschen tun es als Regeln ihre Ziele nicht erreichen, nachdem sie ihre ganze Begeisterung vor einer Menge aufgeblitzt haben, die ihr Aussehen bewundert."
                if second_col in (0, 1):
                    text_2_col = "Eine Person will nicht für sich selbst sorgen, sie kann es sich leisten, jemandem (Eltern, Ehefrau, Ehemann) auf den Hals zu sitzen. Diese Linie stellt keine besondere Gefahr für ihre Schwäche für Frauen dar, da die Bereitstellung der Familie muss auf den Schultern des Ehemannes ruhen."
                if second_col == 2:
                    text_2_col = "Eine Person erinnert sich daran, dass sie ihre Familie ernähren muss und beginnt aus Angst vor der Zukunft nach einem Beruf für das angebotene Gehalt zu suchen. Infolgedessen kann eine Person ihren Traum für ein stabiles Einkommen aufgeben, aber wenn es eine Gelegenheit gibt, dies nicht zu tun, wird er sich nicht wirklich darum kümmern, weil er nicht sehr darauf bedacht ist, sich und seine Familie zu ernähren."
                if second_col == 3:
                    text_2_col = "Solche Leute können impulsiv arbeiten. Ihr Prinzip ist, schnell zu arbeiten, eine Weile durchzuhalten und dann kann man mehr arbeiten."
                if second_col in (4, 5):
                    text_2_col = "Menschen widmen viel Zeit und Energie, um ihre Familien zu unterstützen. Sehr oft ist dies ihr einziges Ziel im Leben."
                if second_col >= 6:
                    text_2_col = "Qualitätsüberlastung, ein Mensch, der intensiv zu arbeiten beginnt, ermüdet sich schnell und kommt zu einer vollständigen Entfernung von der Arbeit (überfordert), er macht viele verschiedene Dinge, sprüht sich selbst ein, schafft eine vollständige Illusion von Arbeit"
                text_3_col = "Die Stärke eines Talents wird durch die Anzahl der Ziffern in einer Spalte bestimmt. Aber sechs oder mehr Ziffern führen zu einer Überfrachtung der Qualität, was nicht gut ist. Ob ein Mensch Talent zeigt, hängt nur von ihm ab."
                telegraph.create_account(short_name='совместимость')
                response = telegraph.create_page(
                    f'Pythagoras-Platz {date_save}',
                    html_content=f"Dein Pythagoras-Platz<br>"
                                 f"{one} ░ {four} ░ {seven}<br>"
                                 f"{two} ░ {five} ░ {eight}<br>"
                                 f"{three} ░ {six} ░ {nine}<br>"
                                 f"<br>"
                                 f"1️⃣<i>Nummer 1 in der Psychomatrix ist verantwortlich für den Charakter einer Person, ihre Willensqualitäten, die Stärke ihres Machtwillens, die Fähigkeit, ihre Ansichten zu verteidigen.</i><br>"
                                 f"<br>"
                                 f"Sie haben Einheiten - {one} pcs : {text_one}<br>"
                                 f"___________________________________<br>"
                                 f"<br>"
                                 f"2️⃣<i>Die Zahl 2 im pythagoräischen Zahlensystem bezeichnet die Energie einer Person. Sie müssen verstehen, dass Energie in diesem Fall die Handlungen einer Person in der Familie, bei der Arbeit, in der Gesellschaft ist.</i><br>"
                                 f"<br>"
                                 f"Du hast zwei - {two} Teile: {text_two}<br>"
                                 f"___________________________________<br>"
                                 f"<br>"
                                 f"3️⃣<i>Die Zahl 3 in der Psychomatrix ist verantwortlich für das Interesse an Naturwissenschaften und vor allem an exakten Wissenschaften oder Technik.</i><br>"
                                 f"<br>"
                                 f"Du hast Tripel - {four} Stk.: {text_three}<br>"
                                 f"___________________________________<br>"
                                 f"<br>"
                                 f"4️⃣<i>Die Zahl 4 in der Psychomatrix ist für die menschliche Gesundheit verantwortlich. </i><br>"
                                 f"<br>"
                                 f"Du hast Vieren - {five} Stücke: {text_four}<br>"
                                 f"___________________________________<br>"
                                 f"<br>"
                                 f"5️⃣<i>Die Zahl 5 in der Psychomatrix ist für die Logik und Intuition einer Person verantwortlich, die wiederum die Fähigkeit einer Person bestimmt, Pläne zu schmieden und eine Situation zu analysieren, exakte Wissenschaften und Technologien zu verstehen.</i><br>"
                                 f"<br>"
                                 f"Du hast Fünfer - {five} pieces: {text_five}<br>"
                                 f"___________________________________<br>"
                                 f"<br>"
                                 f"6️⃣<i>Die Bedeutung der Zahl 6 ist der Grad der Erdigkeit einer Person, eine Neigung zu körperlicher Arbeit.</i><br>"
                                 f"<br>"
                                 f"Du hast Sechsen - {six} Teile: {text_six}<br>"
                                 f"___________________________________<br>"
                                 f"<br>"
                                 f"7️⃣<i>Nummer 7 wurde schon immer mit dem Konzept des Glücks (Glück) in Verbindung gebracht.</i><br>"
                                 f"<br>"
                                 f"Du hast sieben - {seven} Stk.: {text_seven}<br>"
                                 f"___________________________________<br>"
                                 f"<br>"
                                 f"8️⃣<i>Nummer 8 ist verantwortlich für ein Pflichtbewusstsein gegenüber unseren Lieben (Eltern, Familie), ein Gefühl von Toleranz und Freundlichkeit - Eigenschaften, die wir in Bezug auf Eltern und geliebte Menschen zeigen sollten.</i><br>"
                                 f"<br>"
                                 f"Du hast Achter - {eight} Teile: {text_eight}<br>"
                                 f"___________________________________<br>"
                                 f"<br>"
                                 f"9️⃣<i>Die Zahl 9 in der Psychomatrix ist verantwortlich für den Geist, das Gedächtnis und das Hellsehen einer Person.</i><br>"
                                 f"<br>"
                                 f"Du hast Neunen - {nine} Stücke: {text_nine}<br>"
                                 f"<br>"
                                 f"___________________________________<br>"
                                 f"<br>"
                                 f"⬇️<i>Betrag in der ersten Zeile (Zweckmäßigkeit): {first_line}</i><br>"
                                 f"{text_1_line}<br>"
                                 f"___________________________________<br>"
                                 f"<br>"
                                 f"⬇️<i>Zweite Zeilensumme (Familie): {second_line}</i><br>"
                                 f"{text_2_line}<br>"
                                 f"___________________________________<br>"
                                 f"<br>"
                                 f"⬇️<i>Summe der dritten Zeile (Gewohnheiten): {third_line}</i><br>"
                                 f"{text_3_line}<br>"
                                 f"___________________________________<br>"
                                 f"<br>"
                                 f"➡️<i>Erste Spalte Summe (Selbstauskunft): {first_col}</i><br>"
                                 f"{text_1_col}<br>"
                                 f"___________________________________<br>"
                                 f"<br>"
                                 f"➡️<i>Die Summe der zweiten Spalte (Einstellung zur Arbeit): {second_col}</i><br>"
                                 f"{text_2_col}<br>"
                                 f"___________________________________<br>"
                                 f"<br>"
                                 f"➡️<i>Summe der dritten Spalte (Talent): {third_col}</i><br>"
                                 f"{text_3_col}<br>"
                )
                print(response)
                link = 'http://telegra.ph/{}'.format(response['path'])
                msg_text = hlink(":", link)
                await message.answer(f"Berechnungsergebnis{msg_text}")
            await state.finish()


@dp.message_handler(text="test_time")
async def def_name(message: types.Message, state: FSMContext):
    now_moscow = datetime.now(pytz.timezone("europe/moscow"))
    date_moscow = now_moscow.strftime("%Y-%m-%d %H:%M:%S")
    now = datetime.now()
    date = now.strftime("%Y-%m-%d %H:%M:%S")
    await message.answer(f"now_moscow - {now_moscow}\n"
                         f"date_moscow - {date_moscow}\n"
                         f"\n"
                         f"now_server- {now}\n"
                         f"date_server - {date}\n")


@dp.message_handler(text="111")
async def def_name(message: types.Message, state: FSMContext):
    await message.answer(f"Отправь др партнера")
    await Test.date.set()


@dp.message_handler(state=Test.date)
async def def_name(message: types.Message, state: FSMContext):
    date = message.text
    date_copy = date
    user = await qc.get_user(id=int(message.from_user.id))
    try:
        date = date.replace(",", " ")
    except:
        print("нет такого символа для замены")
    try:
        date = date.replace(".", " ")
    except:
        print("нет такого символа для замены")
    try:
        date = date.replace("/", " ")
    except:
        print("нет такого символа для замены")
    date_split = date.split()
    date = date.replace(" ", "")
    summa = 0
    summa1 = 0
    summa2 = 0
    summa3 = 0
    summa4 = 0
    summa5 = 0
    summa_user = 0
    summa_user1 = 0
    summa_user2 = 0
    summa_user3 = 0
    summa_user4 = 0
    summa_user5 = 0
    summa_recipient = 0
    summa_recipient1 = 0
    summa_recipient2 = 0
    summa_recipient3 = 0
    summa_recipient4 = 0
    summa_recipient5 = 0
    for i in user.birthday.replace(' ', ''):
        summa_user += int(i)
    for i in str(summa_user):
        summa_user1 += int(i)
    for i in str(summa_user1):
        summa_user2 += int(i)
    for i in str(summa_user2):
        summa_user3 += int(i)
    for i in str(summa_user3):
        summa_user4 += int(i)
    for i in str(summa_user4):
        summa_user5 += int(i)
    for i in date:
        summa_recipient += int(i)
    for i in str(summa_recipient):
        summa_recipient1 += int(i)
    for i in str(summa_recipient1):
        summa_recipient2 += int(i)
    for i in str(summa_recipient2):
        summa_recipient3 += int(i)
    for i in str(summa_recipient3):
        summa_recipient4 += int(i)
    for i in str(summa_recipient4):
        summa_recipient5 += int(i)
    for i in user.birthday.replace(' ', ''):
        summa1 += int(i)
        print(f"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! summa = {summa}")
    for i in date:
        summa1 += int(i)
        print(f"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! summa1 = {summa1}")
    for i in str(summa1):
        summa2 += int(i)
    for i in str(summa2):
        summa3 += int(i)
    for i in str(summa3):
        summa4 += int(i)
    for i in str(summa4):
        summa5 += int(i)
    if summa5 == 1:
        text = f"Главное для такого союза – действовать вместе. Здесь выявляется внутренний потенциал друг друга. " \
               f"Такие отношения помогают общему развитию. Нельзя забывать, единица – это число лидера, поэтому могут " \
               f"быть недоразумения из-за деления власти в отношениях. Могут появиться ссоры и выяснения отношений, " \
               f"поэтому одному из партнёров просто необходимо научиться подчиняться другому, тогда и семейная жизнь, " \
               f"и бизнес будут более гармоничными."
    if summa5 == 2:
        text = "Такая пара держится на материальной основе. Людям очень нравится общаться друг с другом, но они в " \
               "основном это делают из-за прибыли, потому что вместе им везёт. Нельзя отрицать и того, что со временем " \
               "может получиться семья с хорошим достатком. Здесь тоже всё будет стабильно. Но даже если Вы просто ведёте" \
               " бизнес, Ваша фирма будет процветать. Надо помнить, что двойка является земной цифрой, поэтому ей не " \
               "свойственны яркие чувства. Могут даже появиться конфликты на почве денег. Такой союз не любит перемен и романтики."
    if summa5 == 3:
        text = "Основные составляющие этого союза – умение общаться и быть непостоянными. Скучно здесь не будет. Хочется" \
               " заметить, что уместнее в данном случае будут дружеские отношения, так как в семье с этой цифрой возникает " \
               "холодность. Даются друг другу обещания и не выполняются. Могут быть измены с обеих сторон. Это, пожалуй, " \
               "самое сложное число для совместимости."
    if summa5 == 4:
        text = "Организованность, размеренность, постоянство, комфорт – составляющие данного союза. Семья будет " \
               "излучать тепло и благополучие. Теплота в отношениях делает их искренними. Чрезмерная энергия может" \
               " мешать деловой жизни пары. Здесь главное – это духовное обогащение, получение новых впечатлений, " \
               "но неспособность увеличения капитала."
    if summa5 == 5:
        text = "Один из самых сексуальных союзов, где кипят страсти. Партнёры доставляют друг другу много приятных " \
               "моментов. Всё основано только на любви. Но это пара эгоистов. Надо научиться не только слушать, но и" \
               " слышать друг друга, тогда всё будет хорошо и в семье появятся счастливые дети. Избыток энергии может " \
               "быть направлен на любую отрасль в бизнесе и достаточно успешно."
    if summa5 == 6:
        text = "Взаимопомощь и партнёрство – вот главные звенья этой пары. Это тоже земное число, поэтому и отношения " \
               "бывают длительными. Для ведения бизнеса просто идеальный вариант. В семье – спокойствие, дружба, очень" \
               " редко – выяснение отношений. Чувства могут угаснуть, а поддержка друг друга останется."
    if summa5 == 7:
        text = "Основа этого союза – гармония. Партнёры умеют договариваться. Нельзя не заметить, что здесь могут" \
               "забывать о выполнении договорных обязательств. Хотя скандалы практически не наблюдаются, помогает " \
               "чувство такта, которое не доводит до разрыва отношения. Такие союзы довольно успешны. Совместно решаются " \
               "все проблемы, как семейные, так и материальные."
    if summa5 == 8:
        text = "В этой паре наблюдается некоторая странность, даже можно сказать – нестандартность. Людей сильно тянет " \
               "друг к другу. Один партнёр, благодаря такому влечению, может подталкивать другого, тем самым помогая ему" \
               " реализоваться в бизнесе. Но здесь может появиться внутреннее неудовлетворение, если первый поймёт, " \
               "что его в чём-либо использует из чувства корысти второй. Если возникнет ссора, она может перерасти в " \
               "грандиозный скандал. Надо научиться поднимать самооценку. В паре возможна ревность. Необходимо быть " \
               "гибкими в данном союзе, тогда всё получится."
    if summa5 == 9:
        text = "Самая философская пара. Если в материальном плане здесь всё будет благополучно – перед нами идеальная " \
               "пара. Ну а при слабом финансовом положении отношения дают трещину. Поэтому здесь лучше дружить, а не " \
               "создавать семейный союз, так как быт может поглотить обоих и развести в разные стороны. Если же всё-таки " \
               "брак имеет место, то обязательно кто-то из партнёров должен брать на себя многие бытовые проблемы. " \
               "Тогда союз будет гармоничным."
    if int(summa_user5) == 1:
        text_for_user = "Люди с числом 1 привыкли быть лидером во всех отношениях,  считают, что их мнение – самое " \
                        "верное и решения, которые они принимают – самые правильные. Это может негативно отразиться на" \
                        " отношениях. Все должно быть, как они хотят, не принимают точку зрения другого партнера. Их идеальный " \
                        "партнер с числом судьбы 3 или 5. Это те люди, которые применяют правильный подход к такой властной натуре," \
                        " как вы. Партнер с числом судьбы 3 – простая и беззаботная натура. Он не любит ничего решать, поэтому будет " \
                        "только рад, если все важные решения принимать будут не они. А человек с числом судьбы 5 – очень гибкая натура." \
                        " Он умеет находить компромиссы, добавляет некую динамичность и позитивную энергию в отношения, и серьезная «единица», " \
                        "попадая под его чары, становится беззаботнее и веселее. Также Людям с числом 1 подойдет партнер с числом судьбы 6." \
                        " Но он подходит всем числам судьбы, потому что это самая гармоничная натура, которая привнесет в любые отношения доброту, уют и счастье.\n" \
                        "Людям с числом 1 не стоит встречаться с «восьмерками» и другими «единицами». Оба числа любят авторитет, поэтому их ожидают частые споры и " \
                        "конфликты на тему «кто главный», ибо двух капитанов на одном корабле быть не может."
    if int(summa_user5) == 2:
        text_for_user = "Человек с числом 2— очень хрупкая эмоциональная натура, которая тем не менее использует искусные манипуляции в отношениях." \
                        " Самые гармоничные отношения ожидаются с человеком, число судьбы которого 8 или 9. Решительная и авторитетная «восьмерка» " \
                        "отлично сойдется с мягким характером «двойки». Партнер с числом судьбы 9 – это любящий защитник.Человеку с числом 2 подойдет" \
                        " именно такой человек.\n" \
                        "Приземленная и эмоционально-зависимая «четверка» или серьезный интроверт «семерка» могут стать Человеку с числом 2 хорошей парой," \
                        " но ненадолго, потому что ему это быстро наскучат такие отношения\n" \
                        "Если человек с числом 2 будет встречаться с человеком, число судьбы которого 1, будут гармоничные отношения только в том случае," \
                        " если их роли четко распределены. Придется принять то, что за единицей останется последнее слово, но двойка, как великий манипулятор, " \
                        "определит, каким это последнее слово будет."
    if int(summa_user5) == 3:
        text_for_user = "Для людей с числом судьбы 3 идеальный партнер – это 5 или 7.\n" \
                        "Смелая «пятерка», любящая приключения и яркие события, очень подходит для непредсказуемости и хаоса" \
                        " тройки. Тихий интроверт 7, любящий мистику и загадочность, добавит глубину и осознанность отношениям." \
                        " Это та совместимость, когда партнеры будут не только хорошо ладить, но и дополнять и понимать друг друга.\n" \
                        "Людям  с числом судьбы 3 стоит избегать практичную «четверку». Такая пара будет видеть друг в друге только " \
                        "плохие качества. Тройка может заинтересоваться привлекательной и властной «восьмеркой», но, в конце концов, " \
                        "не сможет справиться с критикой в свой адрес и отношениям быстро придет конец."
    if int(summa_user5) == 4:
        text_for_user = "Четверка нуждаются в крепких длительных отношениях, как никто другой. Это все потому, что они натура" \
                        " практичная и устойчивая. Спокойно относится к быту и рутине в отношениях. Именно поэтому им не подойдет " \
                        "непредсказуемая «тройка» и динамичная неутомимая «пятерка». Стоит также избегать мечтателя-идеалиста с " \
                        "числом 9, так как «четверку» будет раздражать его легкомысленность, потому что они натура практичная и " \
                        "приземленная. Зато отлично подойдет серьезная, сфокусированная на важном «единица» и целеустремленная «восьмерка». " \
                        "А если «четверка» сойдется с заботливой, доброй «шестеркой», у них точно будет крепкая многодетная семья. " \
                        "В этой паре удастся построить счастливое семейное будущее. Очень динамичные и сбалансированные отношения " \
                        "«четверку» ждут с «семеркой». Она добавит приземленной натуре духовность, мечтательность и некую загадку."
    if int(summa_user5) == 5:
        text_for_user = "«Пятерка»– тот человек, которому нужно разнообразие и перемены, поэтому им нужно избегать предсказуемых людей," \
                        " с которыми им будет просто скучно. Отлично подойдет смелая, авторитетная «единица» и оптимистичная веселая «тройка»." \
                        " С «семеркой» будут просто идеальные отношения. Динамичная, нетерпеливая «пятерка» и молчаливая загадочная «семерка» " \
                        "будут балансировать друг друга.\n" \
                        "4, 8 и 9 – нежелательные партнеры для в«пятерки». С 4 вам будет скучно, чрезмерная ответственность " \
                        "9 будет раздражать, а целеустремленная 8 будет раздражать своими бесконечными планами и целями."
    if int(summa_user5) == 6:
        text_for_user = "Людям  с числом судьбы 6  повезло, все черты характера идеально подойдут для любого другого числа судьбы." \
                        " Они могут с легкостью построить длительные, крепкие отношения. Умеют чем-то жертвовать ради любви," \
                        " подстраиваться под нужды партнера, они – заботливая и любящая натура. Если они будут встречаться с" \
                        " двойкой, которая является эмоциональной нежной натурой, их ждут просто идеальные отношения. Они будут " \
                        "любить и радовать друг друга постоянно. С остальными числами они также построят гармоничные отношения " \
                        "благодаря любви, ласке и заботе."
    if int(summa_user5) == 7:
        text_for_user = "У «семерок» очень завышенные ожидания, из-за этого им может быть сложно выбрать подходящего партнера." \
                        " «Единица» и «восьмерка» будут доминировать. «Двойка» слишком эмоциональна и чувствительна, а «девятка» " \
                        "уж слишком любит уединение. Тем не менее, «семерки» не зациклены на любви и отношениях, они умеют радоваться " \
                        "жизни и без партнера, им комфортно и хорошо. Им будет интересно с тем партнером, который просто поразит их" \
                        " своим интеллектом и чувством юмора, и будет понимать, что им нужно личное пространство, когда они хотят побыть " \
                        "наедине с собой.  Самым подходящим партнером для «семерок» может стать 3 или 5. Креативная и светлая «тройка»," \
                        " так же, как и интеллигентная непредсказуемая «пятерка» будут всегда мотивировать. А «семеркам» именно это и нужно в отношениях."
    if int(summa_user5) == 8:
        text_for_user = "«Восьмеркам» важно, чтобы все было под их контролем, в том числе и отношения. Они привыкли быть лидером и " \
                        "авторитетом. Они не умеют искать компромиссы, из-за этого часто возникают проблемы в личной жизни." \
                        " Им подойдет мягкая и нежная «двойка», так же, как любящая и жертвующая «шестерка».\n" \
                        "Независимая сильная «единица» – неподходящий «восьмеркам» партнер, они будут соревноваться за лидерство в" \
                        " отношениях, их ждут постоянные споры и конфликты. Свободолюбивая 5 также не подходит, «восьмерка» будете " \
                        "ее ограничивать, и в итоге потеряет.\n" \
                        "Лучший вариант – это «четверка». Они оба достаточно приземленные практичные натуры, дисциплинированные и " \
                        "целеустремленные личности, которые руководствуются логикой. У них очень много общего, их ждет успех не только" \
                        " в личной жизни, но и в бизнесе, так что смело можно открывать семейное дело!\n"
    if int(summa_user5) == 9:
        text_for_user = "«Девятки»– самая загадочная и сложная натура из всех вышеперечисленных. Они – натура довольно скрытная," \
                        " любит быть в одиночестве, избегает много говорить о своих чувствах и переживаниях. Они сходятся с теми" \
                        " людьми, которые уважают их личное пространство и всегда точно знают, когда они хотят побыть в одиночестве.\n" \
                        "«Девяткам» очень подойдет чувствительная «двойка» и любящая «шестерка». Удивительно, но тройка им тоже близка, " \
                        "они оба креативные и артистичные натуры, у них богатое воображение, необычное чувство юмора. Им точно будет, " \
                        "о чем поговорить друг с другом."
    if int(summa_recipient5) == 1:
        text_for_recipient = "Люди с числом 1 привыкли быть лидером во всех отношениях,  считают, что их мнение – самое " \
                             "верное и решения, которые они принимают – самые правильные. Это может негативно отразиться на" \
                             " отношениях. Все должно быть, как они хотят, не принимают точку зрения другого партнера. Их идеальный " \
                             "партнер с числом судьбы 3 или 5. Это те люди, которые применяют правильный подход к такой властной натуре," \
                             " как вы. Партнер с числом судьбы 3 – простая и беззаботная натура. Он не любит ничего решать, поэтому будет " \
                             "только рад, если все важные решения принимать будут не они. А человек с числом судьбы 5 – очень гибкая натура." \
                             " Он умеет находить компромиссы, добавляет некую динамичность и позитивную энергию в отношения, и серьезная «единица», " \
                             "попадая под его чары, становится беззаботнее и веселее. Также Людям с числом 1 подойдет партнер с числом судьбы 6." \
                             " Но он подходит всем числам судьбы, потому что это самая гармоничная натура, которая привнесет в любые отношения доброту, уют и счастье.\n" \
                             "Людям с числом 1 не стоит встречаться с «восьмерками» и другими «единицами». Оба числа любят авторитет, поэтому их ожидают частые споры и " \
                             "конфликты на тему «кто главный», ибо двух капитанов на одном корабле быть не может."
    if int(summa_recipient5) == 2:
        text_for_recipient = "Человек с числом 2— очень хрупкая эмоциональная натура, которая тем не менее использует искусные манипуляции в отношениях." \
                             " Самые гармоничные отношения ожидаются с человеком, число судьбы которого 8 или 9. Решительная и авторитетная «восьмерка» " \
                             "отлично сойдется с мягким характером «двойки». Партнер с числом судьбы 9 – это любящий защитник.Человеку с числом 2 подойдет" \
                             " именно такой человек.\n" \
                             "Приземленная и эмоционально-зависимая «четверка» или серьезный интроверт «семерка» могут стать Человеку с числом 2 хорошей парой," \
                             " но ненадолго, потому что ему это быстро наскучат такие отношения\n" \
                             "Если человек с числом 2 будет встречаться с человеком, число судьбы которого 1, будут гармоничные отношения только в том случае," \
                             " если их роли четко распределены. Придется принять то, что за единицей останется последнее слово, но двойка, как великий манипулятор, " \
                             "определит, каким это последнее слово будет."
    if int(summa_recipient5) == 3:
        text_for_recipient = "Для людей с числом судьбы 3 идеальный партнер – это 5 или 7.\n" \
                             "Смелая «пятерка», любящая приключения и яркие события, очень подходит для непредсказуемости и хаоса" \
                             " тройки. Тихий интроверт 7, любящий мистику и загадочность, добавит глубину и осознанность отношениям." \
                             " Это та совместимость, когда партнеры будут не только хорошо ладить, но и дополнять и понимать друг друга.\n" \
                             "Людям  с числом судьбы 3 стоит избегать практичную «четверку». Такая пара будет видеть друг в друге только " \
                             "плохие качества. Тройка может заинтересоваться привлекательной и властной «восьмеркой», но, в конце концов, " \
                             "не сможет справиться с критикой в свой адрес и отношениям быстро придет конец."
    if int(summa_recipient5) == 4:
        text_for_recipient = "Четверка нуждаются в крепких длительных отношениях, как никто другой. Это все потому, что они натура" \
                             " практичная и устойчивая. Спокойно относится к быту и рутине в отношениях. Именно поэтому им не подойдет " \
                             "непредсказуемая «тройка» и динамичная неутомимая «пятерка». Стоит также избегать мечтателя-идеалиста с " \
                             "числом 9, так как «четверку» будет раздражать его легкомысленность, потому что они натура практичная и " \
                             "приземленная. Зато отлично подойдет серьезная, сфокусированная на важном «единица» и целеустремленная «восьмерка». " \
                             "А если «четверка» сойдется с заботливой, доброй «шестеркой», у них точно будет крепкая многодетная семья. " \
                             "В этой паре удастся построить счастливое семейное будущее. Очень динамичные и сбалансированные отношения " \
                             "«четверку» ждут с «семеркой». Она добавит приземленной натуре духовность, мечтательность и некую загадку."
    if int(summa_recipient5) == 5:
        text_for_recipient = "«Пятерка»– тот человек, которому нужно разнообразие и перемены, поэтому им нужно избегать предсказуемых людей," \
                             " с которыми им будет просто скучно. Отлично подойдет смелая, авторитетная «единица» и оптимистичная веселая «тройка»." \
                             " С «семеркой» будут просто идеальные отношения. Динамичная, нетерпеливая «пятерка» и молчаливая загадочная «семерка» " \
                             "будут балансировать друг друга.\n" \
                             "4, 8 и 9 – нежелательные партнеры для в«пятерки». С 4 вам будет скучно, чрезмерная ответственность " \
                             "9 будет раздражать, а целеустремленная 8 будет раздражать своими бесконечными планами и целями."
    if int(summa_recipient5) == 6:
        text_for_recipient = "Людям  с числом судьбы 6  повезло, все черты характера идеально подойдут для любого другого числа судьбы." \
                             " Они могут с легкостью построить длительные, крепкие отношения. Умеют чем-то жертвовать ради любви," \
                             " подстраиваться под нужды партнера, они – заботливая и любящая натура. Если они будут встречаться с" \
                             " двойкой, которая является эмоциональной нежной натурой, их ждут просто идеальные отношения. Они будут " \
                             "любить и радовать друг друга постоянно. С остальными числами они также построят гармоничные отношения " \
                             "благодаря любви, ласке и заботе."
    if int(summa_recipient5) == 7:
        text_for_recipient = "У «семерок» очень завышенные ожидания, из-за этого им может быть сложно выбрать подходящего партнера." \
                             " «Единица» и «восьмерка» будут доминировать. «Двойка» слишком эмоциональна и чувствительна, а «девятка» " \
                             "уж слишком любит уединение. Тем не менее, «семерки» не зациклены на любви и отношениях, они умеют радоваться " \
                             "жизни и без партнера, им комфортно и хорошо. Им будет интересно с тем партнером, который просто поразит их" \
                             " своим интеллектом и чувством юмора, и будет понимать, что им нужно личное пространство, когда они хотят побыть " \
                             "наедине с собой.  Самым подходящим партнером для «семерок» может стать 3 или 5. Креативная и светлая «тройка»," \
                             " так же, как и интеллигентная непредсказуемая «пятерка» будут всегда мотивировать. А «семеркам» именно это и нужно в отношениях."
    if int(summa_recipient5) == 8:
        text_for_recipient = "«Восьмеркам» важно, чтобы все было под их контролем, в том числе и отношения. Они привыкли быть лидером и " \
                             "авторитетом. Они не умеют искать компромиссы, из-за этого часто возникают проблемы в личной жизни." \
                             " Им подойдет мягкая и нежная «двойка», так же, как любящая и жертвующая «шестерка».\n" \
                             "Независимая сильная «единица» – неподходящий «восьмеркам» партнер, они будут соревноваться за лидерство в" \
                             " отношениях, их ждут постоянные споры и конфликты. Свободолюбивая 5 также не подходит, «восьмерка» будете " \
                             "ее ограничивать, и в итоге потеряет.\n" \
                             "Лучший вариант – это «четверка». Они оба достаточно приземленные практичные натуры, дисциплинированные и " \
                             "целеустремленные личности, которые руководствуются логикой. У них очень много общего, их ждет успех не только" \
                             " в личной жизни, но и в бизнесе, так что смело можно открывать семейное дело!\n"
    if int(summa_recipient5) == 9:
        text_for_recipient = "«Девятки»– самая загадочная и сложная натура из всех вышеперечисленных. Они – натура довольно скрытная," \
                             " любит быть в одиночестве, избегает много говорить о своих чувствах и переживаниях. Они сходятся с теми" \
                             " людьми, которые уважают их личное пространство и всегда точно знают, когда они хотят побыть в одиночестве.\n" \
                             "«Девяткам» очень подойдет чувствительная «двойка» и любящая «шестерка». Удивительно, но тройка им тоже близка, " \
                             "они оба креативные и артистичные натуры, у них богатое воображение, необычное чувство юмора. Им точно будет, " \
                             "о чем поговорить друг с другом."
    await message.answer(f"Ваша дата рождения: {user.birthday.replace(' ', '.')}\n"
                         f"Дата рождения партнера: {date_copy}\n"
                         f"\n"
                         f"Общее число судьбы: {summa5}\n"
                         f"{text}\n"
                         f"\n"
                         f"Ваше число судьбы: {summa_user5}\n"
                         f"{text_for_user}\n"
                         f"\n"
                         f"Число судьбы партнера: {summa_recipient5}\n"
                         f"{text_for_recipient}\n")
    await state.finish()


@dp.message_handler(text="upd_horoscope")
async def main_command(message: types.Message):
    now = datetime.now(pytz.timezone("europe/moscow"))
    # await bot.send_message(chat_id=chat_id_group, text="Тестовое сообщение")
    # считываем всю таблиу
    await qc.drop_horoscope()
    x = pd.read_csv(
        f"https://docs.google.com/spreadsheets/d/1ayt5NzGPTE31uO9KNMhvg290bBNkLAP_lbjN0A4_PgU/export?format=csv&id=1ayt5NzGPTE31uO9KNMhvg290bBNkLAP_lbjN0A4_PgU&gid=0")
    now_date = now.strftime("%d,%m,%Y")
    # print(x)
    # print("date: ", now_date)
    # получаем данные на сегодня и дальше работаем с ними
    data_index = x.index
    for i in data_index:
        selected_row = x.loc[i]
        date = selected_row['Дата']
        language = selected_row['Язык']
        type = selected_row['Тип гороскопа']
        Aries = selected_row['Овен']
        Taurus = selected_row['Телец']
        Gemini = selected_row['Близены']
        Cancer = selected_row['Рак']
        Leo = selected_row['Лев']
        Virgo = selected_row['Дева']
        Libra = selected_row['Весы']
        Scorpio = selected_row['Скорпион']
        Sagittarius = selected_row['Стрелец']
        Capricorn = selected_row['Козерог']
        Aquarius = selected_row['Водолей']
        Pisces = selected_row['Рыбы']
        await qc.add_horoscope(date=date, language=language, type=type, Aries=Aries, Taurus=Taurus, Gemini=Gemini,
                               Cancer=Cancer, Leo=Leo, Virgo=Virgo
                               , Libra=Libra, Scorpio=Scorpio, Sagittarius=Sagittarius, Capricorn=Capricorn,
                               Aquarius=Aquarius, Pisces=Pisces)
        # print(f"Строка: {date}, {type}, {Aries}, {Taurus}, {Gemini}, {Cancer}, {Leo}, {Virgo}, {Libra}, {Scorpio}, {Sagittarius}, {Capricorn},"
        #       f"{Aquarius}, {Pisces}")
    await message.answer("Гороскоп обновлен")


@dp.message_handler(text="upd_prediction")
async def main_command(message: types.Message):
    # now = datetime.now(pytz.timezone("europe/moscow"))
    # await bot.send_message(chat_id=chat_id_group, text="Тестовое сообщение")
    # считываем всю таблиу
    await qc.drop_prediction()
    x = pd.read_csv(
        f"https://docs.google.com/spreadsheets/d/1Klfv5Yzrb1eZpXn8CQC5T6CVMfHE-Ngiy1WyaL8asms/export?format=csv&id=1Klfv5Yzrb1eZpXn8CQC5T6CVMfHE-Ngiy1WyaL8asms&gid=0")
    # now_date = now.strftime("%d,%m,%Y")
    print(x)
    # print("date: ", now_date)
    # получаем данные на сегодня и дальше работаем с ними
    data_index = x.index
    for i in data_index:
        selected_row = x.loc[i]
        id = selected_row['Номер']
        ru = selected_row['ru']
        en = selected_row['en']
        es = selected_row['es']
        de = selected_row['de']
        await qc.add_prediction(id=id, ru=ru, en=en, es=es, de=de)
    await message.answer("Предсказания обновлены")
