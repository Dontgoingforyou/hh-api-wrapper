from src.hh_api import HeadHunterAPI
from src.vacancy import Vacancy


def user_choice():
    keyword = input("Какую профессию ищите?\n").lower()
    per_page = int(input("Сколько профессии вывести?\n"))
    hh_api = HeadHunterAPI(keyword, per_page)
    from_hh = hh_api.get_filter_vacancies(keyword, per_page=per_page)
    sorted_vacancies = sorted(from_hh, reverse=True)
    print("Список вакансии с 'HeadHunter' по зарплате по убывающей: \n")
    for i in sorted_vacancies:
        print(i)
