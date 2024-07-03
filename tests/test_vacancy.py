

def test_vacancy_init(vacancy):
    """ Тесты конструктора класса """

    assert vacancy.name == "Менеджер по работе с клиентами"
    assert vacancy.alternate_url == "https://hh.ru/vacancy/101709979"
    assert vacancy.salary == 50000
    assert vacancy.area == "Ташкент"
    assert vacancy.snippet == "Опыт работы в продажах обязателен"


def test_vacancy_str(vacancy):
    """ Тест строкового представления вакансии """

    assert str(vacancy) == ("Наименование вакансии: Менеджер по работе с клиентами, "
                            "Ссылка на вакансию: https://hh.ru/vacancy/101709979, Зарплата: 50000, "
                            "Место работы: Ташкент, Краткое описание: Опыт работы в продажах обязателен")
