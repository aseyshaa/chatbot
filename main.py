# Функция для отображения главного меню
def show_main_menu():
    print("Выберите действие:")
    print("1. Режим приветствия")
    print("2. Режим разговора")
    print("3. Режим прощания")
    print("4. Выйти")


# Функция для обработки выбранного действия в главном меню
def process_main_menu_choice(choice):
    if choice == "1":
        greet_mode()
    elif choice == "2":
        talk_mode()
    elif choice == "3":
        bye_mode()
    elif choice == "4":
        exit_mode()
    else:
        print("Неверный выбор. Пожалуйста, выберите число от 1 до 4.")


# Функция для режима приветствия
def greet_mode():
    print("Привет! Как я могу тебе помочь?")
    while True:
        # Читаем сообщение пользователя
        message = input("Ваше сообщение: ")
        # Если пользователь говорит "пока", переходим в режим прощания
        if message.lower() == "пока":
            bye_mode()
            break


# Функция для режима разговора
def talk_mode():
    print("В какую тему тебя интересует общение?")
    while True:
        # Читаем сообщение пользователя
        topic = input("Тема: ")
        # Если пользователь говорит "пока", переходим в режим прощания
        if topic.lower() == "пока":
            bye_mode()
            break
        else:
            print(f"Разговор на тему {topic}...")
            # Здесь можно добавить логику для разговора на конкретную тему


# Функция для режима прощания
def bye_mode():
    print("Пока! Буду ждать тебя снова.")


# Функция для режима выхода из программы
def exit_mode():
    print("До встречи!")
    exit()


# Основной цикл программы
while True:
    show_main_menu()
    choice = input("Ваш выбор: ")
    process_main_menu_choice(choice)
