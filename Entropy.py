import sys
import configparser

print('\033[92m'+'    Entropy (v 0.1)'+'\033[0m')
input('    Чтобы продолжить, нажмите Enter...')

def main_menu():
    answer_menu = True
    while answer_menu:
        print("""
    1.Начать игру
    2.Настройки
    3.Создатели
    
    4.Выход
        """)
        answer_menu = input('')    
        if answer_menu == ('1'): 
            game_mode()
            break
        elif answer_menu == ('2'):
            settings()
            break
        elif answer_menu == ('3'):
            print("""
                        Directed by
                        Pavel Karasev

                        Written by
                        Pavel Karasev

                        Producer
                        Pavel Karasev

                        Game Design
                        Pavel Karasev

                        Planning
                        Pavel Karasev

                        Lead Programmer
                        Pavel Karasev



                        See you space cowboy...
                """) 
        elif answer_menu == ('4'):
            print('\033[91m'+'Теперь питание компьютера можно отключить'+'\033[0m')
            sys.exit(0)
        elif answer_menu != (''):
            print("\n Нет такой опции. Пожалуйста, введите снова") 

def settings():
    END = '\033[0m' # переменная содержить дефолтные настройки
    answer_settings = True
    while answer_settings:
        print("""
    1.Цвет текста
    2.Стиль текста
    3.Сброс настроек
    
    4.Назад в меню
            """)
        answer_settings = input('')    
        if answer_settings == ('1'): 
            color_text()
            break
        elif answer_settings == ('2'):
            style_text()
            break
        elif answer_settings == ('3'):
            print(END + 'Возвращены стандартные настройки')
        elif answer_settings == ('4'):
            main_menu()
            break
        elif answer_settings != (''):
            print("\n Нет такой опции. Пожалуйста, введите снова")
    
def color_text():
    Red = '\033[91m'
    Green = '\033[92m'
    Yellow = '\033[93m'
    Blue = '\033[94m'
    White = '\033[97m'
    Grey = '\033[90m'
    answer_color = True
    while answer_color:
        print("""
    1.Выберите цвет текста:
            
    1.Красный
    2.Зеленый
    3.Желтый
    4.Голубой
    5.Белый
    6.Серый

    7.Назад в меню
            """)
        answer_color = input('')    
        if answer_color == ('1'): 
            print(Red + 'Выбран красный цвет')
        elif answer_color == ('2'):
            print(Green + 'Выбран зеленый цвет')
        elif answer_color == ('3'):
            print(Yellow + 'Выбран желтый цвет')
        elif answer_color == ('4'):
            print(Blue + 'Выбран голубой цвет')
        elif answer_color == ('5'):
            print(White + 'Выбран белый цвет')
        elif answer_color == ('6'):
            print(Grey + 'Выбран серый цвет')
        elif answer_color == ('7'):
            settings()
            break
        elif answer_color != (''):
            print("\n Такого цвета нет. Пожалуйста, введите снова")

def style_text():
    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    answer_style = True
    while answer_style:
        print("""
    1.Выберите цвет текста:
            
    1.Жирный
    2.Курсив
    3.Подчеркнутый текст
    
    4.Назад в меню
            """)
        answer_style = input('')    
        if answer_style == ('1'): 
            print(BOLD + 'Выбран жирный шрифт')
        elif answer_style== ('2'):
            print(ITALIC + 'Выбран курсив')
        elif answer_style == ('3'):
            print(UNDERLINE + 'Выбрано нижнее подчеркивание')
        elif answer_style == ('4'):
            settings()
            break
        elif answer_style != (''):
            print("\n Такого стиля нет. Пожалуйста, введите снова")

def load_save():

    config = configparser.ConfigParser()  
    config.read("save.ini")

    if config['Player']['Act0'] == ('End'):
        act_one()
    # elif config['Player']['Act1'] == ('End'):
    #     act_two()
    # elif config['Player']['Act2'] == ('End'):
    #     act_three()
    # elif config['Player']['Act4'] == ('End'):
    #     end()
    else:
        print('    Сохранение отсутствует. Начните новую игру')
        
def game_mode():
    answer_mode = True
    while answer_mode:
        print("""
    Выберите режим игры:

    1.Режим истории
    2.Режим ответов
    3.Загрузить сохранение
    
    4.Назад в меню
        """)
        answer_mode = input('')
        if answer_mode == ('1'):
            character_info()
            break
        elif answer_mode == ('2'):
            puzzle_mode()
            break
        elif answer_mode == ('3'):
            load_save()
        elif answer_mode == ('4'):
            main_menu()
            break
        elif answer_mode != (''):
            print("\n Нет такой опции. Пожалуйста, введите снова") 

def character_info():
    
    def character_info_name():
        print("""
    В Entropy используется система создания персонажа. Характеристики созданного аватара, будут влиять на исходы некоторых событий. 
            """)
        answer_name = input('    Введите имя персонажа:' )
        save_file = open("save.ini", "w")
        save_file.write('[Player]')
        save_file.write('\nName=' + answer_name)
        save_file.close()
        character_info_gender()
        
    def character_info_gender():
        answer_gender = True
        while answer_gender:
            print("""
    Выберите пол персонажа:

    1.Мужской
    2.Женский
    3.Другой
            """)
            answer_gender = input('')
            save_file = open("save.ini", "a") 
            if answer_gender == ('1'): 
                save_file.write('\nGender=' + 'Мужской')
                save_file.close()  
                character_info_specialization()
                break
            elif answer_gender == ('2'):
                save_file.write('\nGender=' + 'Женский')
                save_file.close()  
                character_info_specialization()
                break
            elif answer_gender == ('3'):
                print('\n Такого пола еще нет в игре. Новые гендеры будут добавлены с выходом платного DLC в будущем. Выберите снова')
            elif answer_gender != (''):
                print("\n Нет такой опции. Пожалуйста, введите снова")
    
    def character_info_specialization():
        answer_specialization = True
        while answer_specialization:
            print("""
    Выберите специализацию персонажа:

    1.Медик
    2.Инженер
    3.Сотрудник охраны
    4.Научный сотрудник
            """)
            answer_specialization = input('')
            save_file = open("save.ini", "a")   
            if answer_specialization == ('1'): 
                save_file.write('\nSpec=' + 'Медик')
                save_file.close()  
                character_info_blood()
                break
            elif answer_specialization == ('2'):
                save_file.write('\nSpec=' + 'Инженер')
                save_file.close()  
                character_info_blood()
                break
            elif answer_specialization == ('3'):
                save_file.write('\nSpec=' + 'Сотрудник охраны')
                save_file.close()  
                character_info_blood()
                break
            elif answer_specialization == ('4'):
                save_file.write('\nSpec=' + 'Научный сотрудник')
                save_file.close()  
                character_info_blood()
                break
            elif answer_specialization != (''):
                print("\n Такой специализации нет. Пожалуйста, выберите снова")    

    def character_info_blood():
        answer_blood = True
        while answer_blood:
            print("""
    Выберите тип крови персонажа:

    1.0 (первая группа крови)
    2.A (вторая группа крови)
    3.B (третья группа крови)
    4.AB (четвертая группа крови)
            """)
            answer_blood = input('')
            save_file = open("save.ini", "a")
            if answer_blood == ('1'): 
                save_file.write('\nBlood=' + '0')
                save_file.close() 
                character_info_short()
                break
            elif answer_blood == ('2'):
                save_file.write('\nBlood=' + 'A')
                save_file.close() 
                character_info_short()
                break
            elif answer_blood == ('3'):
                save_file.write('\nBlood=' + 'B')
                save_file.close() 
                character_info_short()
                break
            elif answer_blood == ('4'):
                save_file.write('\nBlood=' + 'AB')
                save_file.close() 
                character_info_short()
                break
            elif answer_blood != (''):
                print("\n Нет такой опции. Пожалуйста, введите снова")
    
    def character_info_short():
        config = configparser.ConfigParser()  
        config.read("save.ini")
        print("""
    From: jane.hr@projectentropy.com
    To: jhon.research@projectentropy.com
    
    Привет, Джон. Мы сделали отбор из нескольких кандидатов для твоего отдела. Один из них прошел все наши проверки. Вот его анкета. 
    В скором времени, он прибудет к тебе. Пожалуйста, дай нам знать подходит он тебе или нет.
            """)
        print('    Имя: ' + config['Player']['Name'])
        print('    Пол: ' + config['Player']['Gender'])
        print('    Дата рождения: Засекречено')
        print('    Место рождения: Детройт')
        print('    Профессия: ' + config['Player']['Spec'])
        print("""
    С раннего детства наблюдается повышенная эмоциональная восприимчивость. Судимости и привлечения полицией - отсутствуют. 
    Окончен университет Уэйна по вышеуказанной специальности. Имеется очень хорошая рекомендация с предыдущего места работы.
    Изъявляет сильное желание развиваться в нашей компании. О проекте 'Э' ничего не знает.
    Мне кажется, это идеальный кандидат.
            """)
        answer_final = True
        while answer_final:
            print("""
    1.Принять нового сотрудника
    2.Продолжить поиск кандидатов
    3.Закончить поиск
            """)
            answer_final= input('')
            if answer_final == ('1'): 
                print("""
    From: jhon.research@projectentropy.com
    To: jane.hr@projectentropy.com
    
    Привет, Джейн. Он нам подходит. Можете оформлять все нужные бумаги. Новый сотрудник выступает на работу уже завтра.
    Спасибо.
            """)
                input('    Чтобы начать, нажмите Enter...')
                introduction()
                break
            elif answer_final == ('2'):
                print("""
    From: jhon.research@projectentropy.com
    To: jane.hr@projectentropy.com
    
    Привет, Джейн. Ты нашла интересного человека, но у него есть качества, которые не подходят для нашего проекта. 
    Я уверен, что у него будет нестабильное состояние. Пожалуйста, продолжай поиски. 
    Спасибо.
                """)
                input('    Чтобы найти нового кандидата, нажмите Enter...')
                character_info()
                break
            elif answer_final == ('3'):
                print("""
    From: jhon.research@projectentropy.com
    To: jane.hr@projectentropy.com
    
    Привет, Джейн. Больше не ищи кандидатов для моего проекта. Я принял решение свернуть его. 
    Новые участники не способствуют улучшению качества проводимых исследований. 
    У многих из них, не такой стабильный эмоциональный фон, как нам хотелось бы. В последнее время, прибавилось проблем сверх нормы.
    Видимо, есть вещи, которым лучше оставаться загадкой.
            """)
                input('    Чтобы закончить, нажмите Enter...')
                print("""
                        Directed by
                        Pavel Karasev

                        Written by
                        Pavel Karasev

                        Producer
                        Pavel Karasev

                        Game Design
                        Pavel Karasev

                        Planning
                        Pavel Karasev

                        Lead Programmer
                        Pavel Karasev



                        See you space cowboy...
                """)
                main_menu()
            elif answer_final != (''):
                print("\n Пытаешься играть по другим правилам? Все уже давно предначертано")

        
        
    character_info_name()

def introduction():
    config = configparser.ConfigParser()  
    config.read("save.ini")
    print("""
    "Люди охотно верят тому, чему желают верить" 
		
		                ------- Гай Юлий Цезарь (4)


    Все в этом мире подчиняется определенным законам. С давних времен, люди пытались найти ответы о структуре мироздания и определить последовательности, которые помогли бы объяснить многие вещи. 
    Проект “Энтропия” - новая попытка в изучении структуры мироздания. Проект создан в 1992 году. За 6 лет существования, он позволил сильно продвинуться в изучении феномена Кларца-Штайнера. 
    В основе феномена и проекта, лежит идея иллюзорности окружающего мира, который можно изменять с помощью эмоционально-психического воздействия.
    Джон Салистер - основатель проекта “Энтропия”. О нем известно, не так много, но ходят слухи, что он связан с модернизацией нейрофона Патрика Фланагана. 
    Обновленную версию использовали во время Вьетнамской войны. Говорят, что модернизированный  нейрофон позволял читать мысли людей и переписывать их на сторонние. 
    Была лишь одна проблема, нейрофон нужно было вшивать субдермальным путем и прокладывать контакты напрямую к мозгу. Проект не давал ощутимых эффектов, да и был сложен в обслуживании. 
    Проект был заморожен до лучших времен, данные о нем засекречены, а Джон был переброшен на другие проекты.
        """) 
    print('    Сейчас на дворе 1998 год. Вас зовут '+ config["Player"]["Name"] + '. Вы прошли нелегкий путь, чтобы попасть в проект "Энтропия", который курируется компанией "Протосити". Добро пожаловать в команду, '+ config["Player"]["Name"] + '!')
    input('    Чтобы закончить вступление и сохранить прогресс, нажмите Enter...')
    save_file = open("save.ini", "a")
    save_file.write('\nAct0=' + 'End')
    save_file.close()
    act_one()

def act_one():
    print('    День 1. Блаженное неведение')
    print("""
    21 мая 1998 год.
    Вы проснулись, умылись, позавтракали, собрались и пошли на свой первый рабочий день. 
    Время позволяет вдоволь насладиться весенней прогулкой, на которую воодушевляет и полученная должность в крупной компании. 
    Вы еще мало знаете о том, что вас ожидает. Но…. не стоит забегать вперед раньше времени.
        """)
    answer_first = True
    while answer_first:
        print("""
    1.Вызвать такси
    2.Прогуляться
        """)
        answer_first = input('')    
        if answer_first == ('1'): 
            act_one_taxi()
            break
        elif answer_first == ('2'):
            act_one_walk()
            break
        elif answer_first == (''):
            print('Неужели тебе не нравится наша игра?')

def act_one_walk():
    print("""
    Вы решили прогулятся и поднять себе настроение. Свежая зеленая листва, приятный теплый ветерок, ласковое солнце. Все это очень хорошо улучшает вам настроение. 
    В момент, когда вы идете по парку, вам на встречу выбегает из кустов грязный мужчина пожилого возраста и начинает клянчить у вас один доллар на питание. 
    Вы в хорошем расположении духа и решаете дать ему этот доллар. Для вас он не такая большая сумма, а для него это еще один день жизни.
        """)
    input('    Чтобы продолжить, нажмите Enter...')
    act_one_workplace()
    
def act_one_taxi():
    print("""
    Вы добираетесь до своего места работы без проишествий.
        """)
    input('    Чтобы продолжить, нажмите Enter...')
    act_one_workplace()

def act_one_workplace():
    config = configparser.ConfigParser()  
    config.read("save.ini")
    
    print('Джексон - начальник охраны')
    print('Джексон: Привет, ' + config["Player"]["Name"] + '!')
    
    input('    Чтобы поприветствовать и поговорить, нажмите Enter...')
    print(config["Player"]["Name"] + ': ' + 'Рад видеть тебя, Джексон!')
    print('Джексон: Как настроение?')
    print(config["Player"]["Name"] + ': ' + 'Пока не жалуюсь.')
    print('Джексон: Придется тебе его испортить. Тебя вызывают в кабинет 110.')
    print(config["Player"]["Name"] + ': ' + 'Ты так говоришь, как будто это что-то страшное. У меня первый рабочий день. Скорее всего, какие нибудь формальности.')
    print('Джексон: Я поэтому и говорю в таком писсимистичном тоне, потому что никто не любит возиться с бумажками. Иди уже давай, не заставляй меня оправдываться.')
    print(config["Player"]["Name"] + ': ' + 'Еще свидимся.')
    
    input('    Чтобы войти в кабинет 110, нажмите Enter...')
    print('Клариса - личная помощница Джони Салистера')
    if config["Player"]["Gender"] == 'Мужской':
        print('Клариса: А ты симпотичнее, чем на фотографии.')
    elif config["Player"]["Gender"] == 'Женский':
        print('Клариса: Привет, дорогуша. Как настроение?')

    input('    Чтобы ответить, нажмите Enter...')
    print(config["Player"]["Name"] + ': ' + 'Доброе утро. Я...')
    
    print('Клариса: Давай без лишней болтовни. Ты ведь знаешь о феномене Кларца-Штайнера?')
    if config["Player"]["Spec"] == 'Научный сотрудник':
        print(config["Player"]["Name"] + ': Психо-эмоциональное воздействие на материальный мир? Вы шутите что-ли? Я думал вы меня позвали по более серьезным вещам.')
    elif config["Player"]["Spec"] == 'Медик' or 'Сотрудник охраны' or 'Инженер':
        print(config["Player"]["Name"] + ': Не слышал о таком')
    
    print('Клариса: Все нужные бумаги уже были подписаны, так что ты узнаешь очень много интересного. Мне придется тебе вколоть тебе вещество для усиленья психоспособностей. И давай без вопросов. Больше дела')

    answer_second = True
    while answer_second:
        print("""
    1.Согласиться
    2.отказаться
        """)
        answer_second = input('')    
        if answer_second == ('1'): 
            print('Клариса: *говорит по интеркому* Джексон, веди своих людей, нужно немного подержать буйного')
        elif answer_second == ('2'):
            print('Клариса: Сразу видно делового человека, живущего ради науки')
        elif answer_second == (''):
            print('Пытаешься избежать неизбежного?')
    
    print('    Вам вкололи сильнодействующий препарат неизвестного происхождения')
    input('    Чтобы уйти в царство Морфея, нажмите Enter... Не сопротивляйся.')
    
    save_file = open("save.ini", "a")
    save_file.write('\nAct1=' + 'End')
    save_file.close()  

def act_two():
    print('Временной парадокс. Эта часть событий еще не произошла')

def act_three():
    print('Временной парадокс. Эта часть событий еще не произошла')

def end():
    print('Временной парадокс. Эта часть событий еще не произошла')

def puzzle_mode():
    print("""
    "Путь в тысячу ли начинается с первого шага" 
		
		                        ------- Лао-Цзы 
    
    Фикмр ёянзиц ё ечзчэир зтутпсисмм
        """)

main_menu()