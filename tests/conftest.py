import pytest

from src.vacancy import Vacancy


@pytest.fixture
def vacancy():
    return Vacancy("Менеджер по работе с клиентами", "https://hh.ru/vacancy/101709979",
                   50000, "Ташкент", "Опыт работы в продажах обязателен")
