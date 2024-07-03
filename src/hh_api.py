import requests
from src.get_vacancies import GetVacanciesAPI


class HeadHunterAPI(GetVacanciesAPI):
    """ Класс для подключения к hh.ru """

    def __init__(self):
        self.url = "https://api.hh.ru/vacancies"
        self.headers = {"User-Agent": "HH-User-Agent"}
        self.params = {"text": "", "page": 0, "per_page": 100}
        self.vacancies = []

    def get_vacancies(self, keyword):

        self.params["text"] = keyword

        while self.params.get("page") != 1:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()["items"]
            vacancies.extend(vacancies)
            self.params["page"] += 1

