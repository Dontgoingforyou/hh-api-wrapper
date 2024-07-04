import json

from config import VACANCIES_PATH
from src.saver import Saver
from src.vacancy import Vacancy


class JSONSaver(Saver):

    def __init__(self):
        self.filename = VACANCIES_PATH

    def write_data(self, data):
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=5)

    def get_data(self):
        with open(self.filename, encoding="utf-8") as file:
            data = json.load(file)
            vacancies = []
            for vacancy in data:
                vacancies.append(Vacancy(
                    name=vacancy.get("name"),
                    alternate_url=vacancy.get("alternate_url"),
                    salary_from=vacancy.get("salary").get("from"),
                    salary_to=vacancy.get("salary").get("to"),
                    area_name=vacancy.get("area").get("name"),
                    requirement=vacancy.get("snippet").get("requirement"),
                    responsibility=vacancy.get("snippet").get("responsibility")
                ))
            return vacancies

    def del_data(self):
        pass
