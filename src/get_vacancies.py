from abc import ABC, abstractmethod


class GetVacanciesAPI(ABC):
    """Абстрактный класс для получения вакансии с hh.ru"""

    @abstractmethod
    def get_vacancies(self, keyword):
        pass
