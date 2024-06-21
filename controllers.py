import models
import views
from main import main


def sort_athletes_by_name(athletes):
    athletes.sort(key=lambda x: x.name)
    views.display_athletes_by_country(athletes)

def calculate_average_age(athletes):
    total_age = sum(athlete.age for athlete in athletes)
    average_age = total_age / len(athletes)
    print(f"Средний возраст спортсменов: {average_age}")

def find_max_height(athletes):
    max_height = max(athlete.height for athlete in athletes)
    print(f"Максимальный рост среди спортсменов: {max_height}")

def add_athlete(country_name):
    name = input("Введите имя спортсмена: ")
    age = int(input("Введите возраст спортсмена: "))
    weight = float(input("Введите вес спортсмена: "))
    height = float(input("Введите рост спортсмена: "))
    models.add_athlete(name, age, weight, height, country_name)

def delete_athlete(athletes):
    athlete_choice = int(input("Введите номер спортсмена для удаления: "))
    athlete = athletes[athlete_choice-1]
    models.delete_athlete(athlete.id)

def update_athlete(athletes):
    athlete_choice = int(input("Введите номер спортсмена для изменения: "))
    athlete = athletes[athlete_choice-1]
    name = input("Введите новое имя спортсмена: ")
    age = int(input("Введите новый возраст спортсмена: "))
    weight = float(input("Введите новый вес спортсмена: "))
    height = float(input("Введите новый рост спортсмена: "))
    models.update_athlete(athlete.id, name, age, weight, height)

def return_to_countries():
    countries = models.get_unique_countries()
    views.display_unique_countries(countries)
    country_choice = int(input("Введите номер страны: "))
    country_name = countries[country_choice-1]
    controllers.handle_country_choice(country_name)

def return_to_categories():
    main()

def exit_app():
    return

def find_youngest_and_oldest(athletes):
    youngest = min(athletes, key=lambda x: x.age)
    oldest = max(athletes, key=lambda x: x.age)
    print(f"Самый молодой спортсмен: {youngest.name}, возраст: {youngest.age}")
    print(f"Самый старший спортсмен: {oldest.name}, возраст: {oldest.age}")

def add_new_athlete():
    name = input("Введите имя спортсмена: ")
    age = int(input("Введите возраст спортсмена: "))
    weight = float(input("Введите вес спортсмена: "))
    height = float(input("Введите рост спортсмена: "))
    country_name = input("Введите национальность спортсмена: ")
    sport_name = input("Введите вид спорта спортсмена: ")
    models.add_athlete(name, age, weight, height, country_name, sport_name)

def delete_athlete(athletes):
    athlete_choice = int(input("Введите номер спортсмена для удаления: "))
    athlete = athletes[athlete_choice-1]
    models.delete_athlete(athlete.id)

def search_by_name(athletes):
    name = input("Введите имя спортсмена для поиска: ")
    found_athletes = [athlete for athlete in athletes if athlete.name == name]
    views.display_athletes_by_country(found_athletes)

def filter_athletes():
    countries = input("Введите страны для фильтрации (через запятую): ").split(',')
    sports = input("Введите виды спорта для фильтрации (через запятую): ").split(',')
    filtered_athletes = models.filter_athletes(countries, sports)
    views.display_filtered_athletes(filtered_athletes)

def handle_country_choice(country_name):
    athletes = models.get_athletes_by_country(country_name)
    views.display_athletes_by_country(athletes)
    while True:
        print("Выберите действие:")
        print("1. Отсортировать Фамилии участников от A до Z и от Z до A")
        print("2. Рассчитать средний возраст спортсменов")
        print("3. Определить максимальный рост среди спортсменов")
        print("4. Добавить спортсмена")
        print("5. Удалить запись")
        print("6. Изменить данные")
        print("7. Вернуться к списку национальностей")
        print("8. Вернуться к категориям")
        print("9. Выйти из приложения")
        action = input("Введите номер действия: ")
        if action == "1":
            sort_athletes_by_name(athletes)
        elif action == "2":
            calculate_average_age(athletes)
        elif action == "3":
            find_max_height(athletes)
        elif action == "4":
            add_athlete(country_name)
        elif action == "5":
            delete_athlete(athletes)
        elif action == "6":
            update_athlete(athletes)
        elif action == "7":
            break
        elif action == "8":
            break
        elif action == "9":
            return

def handle_sport_choice(sport_name):
    athletes = models.get_athletes_by_sport(sport_name)
    views.display_athletes_by_sport(athletes)
    while True:
        print("Выберите действие:")
        print("1. Отсортировать Фамилии участников от A до Z и от Z до A")
        print("2. Рассчитать средний возраст спортсменов")
        print("3. Определить максимальный рост среди спортсменов")
        print("4. Добавить спортсмена")
        print("5. Удалить запись")
        print("6. Изменить данные")
        print("7. Вернуться к списку видов спорта")
        print("8. Вернуться к категориям")
        print("9. Выйти из приложения")
        action = input("Введите номер действия: ")
        if action == "1":
            sort_athletes_by_name(athletes)
        elif action == "2":
            calculate_average_age(athletes)
        elif action == "3":
            find_max_height(athletes)
        elif action == "4":
            add_athlete(sport_name)
        elif action == "5":
            delete_athlete(athletes)
        elif action == "6":
            update_athlete(athletes)
        elif action == "7":
            break
        elif action == "8":
            break
        elif action == "9":
            return

def handle_all_athletes_choice():
    athletes = models.get_all_athletes()
    views.display_all_athletes(athletes)
    while True:
        print("Выберите действие:")
        print("1. Найти самых молодых и самых старших спортсменов")
        print("2. Добавить новую запись")
        print("3. Удалить запись")
        print("4. Поиск записей по Имени")
        print("5. Динамический фильтр по странам и видам спорта")
        print("6. Вернуться к категориям")
        print("7. Выйти из приложения")
        action = input("Введите номер действия: ")
        if action == "1":
            find_youngest_and_oldest(athletes)
        elif action == "2":
            add_new_athlete()
        elif action == "3":
            delete_athlete(athletes)
        elif action == "4":
            search_by_name(athletes)
        elif action == "5":
            filter_athletes()
        elif action == "6":
            break
        elif action == "7":
            return