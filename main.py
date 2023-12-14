from enum import Enum


# Список возможных состояний бота
class BotState(Enum):
    GREET = 1
    RECOMMEND_GENRE = 2
    RECOMMEND_MOVIE = 3
    THANK = 4
    BYE = 5


# Класс, представляющий чатбота
class MovieBot:
    def __init__(self):
        self.current_state = BotState.GREET

    # Метод для обработки входящего сообщения
    def process_message(self, message):
        if self.current_state == BotState.GREET:
            if message.lower() == "привет":
                print("Привет! Я могу порекомендовать тебе фильм на новогоднюю или рождественскую тематику.")
                print("Какой фильм вы смотрели последним?")
                self.current_state = BotState.RECOMMEND_GENRE
            else:
                print("Прости, я не понимаю. Попробуй сказать 'привет'")

        elif self.current_state == BotState.RECOMMEND_GENRE:
            print("Отлично!")
            print("Могу порекомендовать тебе фильмы следующих жанров:")
            print("- Комедия")
            print("- Мультфильм")
            print("- Романтика")
            print("- Фэнтези")
            print("Какой жанр тебя интересует?")
            self.current_state = BotState.RECOMMEND_MOVIE

        elif self.current_state == BotState.RECOMMEND_MOVIE:
            genre = message.lower()
            print("Понятно, ты ищешь фильм в жанре", genre)
            print("Вот несколько рекомендаций:")
            if genre == "комедия":
                print("- Один дома")
                print("- Гринч — похититель Рождества")
            elif genre == "мультфильм":
                print("- Рождественская история")
                print("- Головоломка")
            elif genre == "романтика":
                print("- Любовь на Рождество")
                print("- Рождественская песня")
            elif genre == "фэнтези":
                print("- Как гринч украл Рождество")
                print("- Однажды в Рождественской сказке")
            else:
                print("Извини, я не знаю фильмов в жанре", genre)
                print("Может, выберешь что-то другое?")
                return
            print("Наслаждайся просмотром!")
            self.current_state = BotState.THANK

        elif self.current_state == BotState.THANK:
            print("Понравился ли тебе выбранный фильм?")
            self.current_state = BotState.BYE

        elif self.current_state == BotState.BYE:
            if message.lower() == "да":
                print("Отлично! Рад, что смог помочь.")
            else:
                print("Жаль, что фильм не понравился. Может, попробуем что-то другое?")
            print("Спасибо за общение! Удачного просмотра!")
            self.current_state = BotState.GREET


# Создаем экземпляр чатбота
movie_bot = MovieBot()

# Основной цикл программы
while True:
    message = input("Ваше сообщение: ")
    movie_bot.process_message(message)