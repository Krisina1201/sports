import models
import views
import controllers

def main():
    while True:
        print("Выберите категорию:")
        print("1. Национальность")
        print("2. Вид спорта")
        print("3. Все участники")
        choice = input("Введите номер категории: ")
        if choice == "1":
            countries = models.get_unique_countries()
            views.display_unique_countries(countries)
            country_choice = int(input("Введите номер страны: "))
            country_name = countries[country_choice-1]
            controllers.handle_country_choice(country_name)
        elif choice == "2":
            sports = models.get_unique_sports()
            views.display_unique_sports(sports)
            sport_choice = int(input("Введите номер вида спорта: "))
            sport_name = sports[sport_choice-1]
            controllers.handle_sport_choice(sport_name)
        elif choice == "3":
            controllers.handle_all_athletes_choice()
        else:
            print("Такой цифры не существует")

if __name__ == "__main__":
    main()