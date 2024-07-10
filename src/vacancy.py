class Vacancy:
    """ Класс для работы с вакансиями """

    __slots__ = ("name", "alternate_url", "salary_from", "salary_to", "area_name", "requirement", "responsibility")

    def __init__(self, name, alternate_url, salary_from, salary_to, area_name, requirement, responsibility):
        self.name = name
        self.alternate_url = alternate_url
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.area_name = area_name
        self.requirement = requirement
        self.responsibility = responsibility

    def __str__(self):
        return (f"Наименование вакансии: {self.name}, Ссылка на вакансию: {self.alternate_url},"
                f" Зарплата: от {self.salary_from} до {self.salary_to}, Место работы: {self.area_name},"
                f" Краткое описание: {self.requirement}, {self.responsibility}")

    def __lt__(self, other):
        if type(other) is Vacancy:
            return self.salary_from, self.salary_to < other.salary_from, other.salary_to
        else:
            raise ValueError


# if __name__ in "__main__":
#     vacancy = Vacancy("Менеджер по работе с клиентами", "https://hh.ru/vacancy/101709979",
#                       4_000_000, 7_000_000, "Ташкент",
#                       "Опыт работы в продажах обязателен", "Консультирование клиентов")
#     print(vacancy.name)
#     print(vacancy.alternate_url)
#     print(vacancy.salary_from)
#     print(vacancy.salary_to)
#     print(vacancy.area_name)
#     print(vacancy.requirement)
#     print(vacancy.responsibility)
#
#     print(str(vacancy))
