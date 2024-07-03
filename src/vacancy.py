class Vacancy:
    """ Класс для работы с вакансиями """

    __slots__ = ("name", "alternate_url", "salary", "area", "snippet")

    def __init__(self, name, alternate_url, salary, area, snippet):
        self.name = name
        self.alternate_url = alternate_url
        self.salary = self.get_information(salary)
        self.area = self.get_information(area)
        self.snippet = self.get_information(snippet)

    def __str__(self):
        return (f"Наименование вакансии: {self.name}, Ссылка на вакансию: {self.alternate_url},"
                f" Зарплата: {self.salary}, Место работы: {self.area}, Краткое описание: {self.snippet}")

    def __lt__(self, other):
        if type(other) is Vacancy:
            return self.salary < other.salary
        else:
            ValueError("")

    @staticmethod
    def get_information(data):
        return data if data else "Нет информаций"


# if __name__ in "__main__":
#     vacancy = Vacancy("Менеджер по работе с клиентами", "https://hh.ru/vacancy/101709979",
#                       None, "Ташкент", "Опыт работы в продажах обязателен")
#     print(vacancy.name)
#     print(vacancy.salary)
#     print(vacancy.alternate_url)
#     print(vacancy.area)
#     print(vacancy.snippet)
#
#     print(str(vacancy))
