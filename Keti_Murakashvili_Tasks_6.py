#1
from abc import ABC, abstractmethod

class Country(ABC):
    @abstractmethod
    def get_population(self):
        pass

    @abstractmethod
    def get_gdp(self):
        pass

    @abstractmethod
    def get_capital(self):
        pass

#2
class Georgia(Country):
    def __init__(self):

        self.population = 3.7
        self._budget = 15
        self.__capital = "Tbilisi"

    def get_population(self):
        return f"{self.population} million"

    def get_gdp(self):
        return "$17 billion"

    def get_capital(self):
        return self.__capital
    def get_budget(self):
        return f"${self._budget} billion"

    def _get_private_capital(self):
        return self.__capital

#3
georgia = Georgia()
print(georgia.get_population())
print(georgia.get_gdp())
print(georgia.get_capital())
print(georgia.get_budget())

print(georgia.population)
print(georgia._budget)
print(georgia._Georgia__capital)

#3





