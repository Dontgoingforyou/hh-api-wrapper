from src.hh_api import HeadHunterAPI

def user_choice():
    keyword = input("Какую профессию ищите?\n").lower()
    per_page = int(input("Сколько профессии вывести?\n"))
    hh_api = HeadHunterAPI(keyword, per_page)
    from_hh = hh_api.get_filter_vacancies(keyword, per_page=per_page)
    print("Список вакансии с 'HeadHunter': \n")
    for i in from_hh:
        print(i)

