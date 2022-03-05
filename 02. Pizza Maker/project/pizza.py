from .dough import Dough
from .topping import Topping


class Pizza:
    def __init__(self, name, dough: Dough, toppings_capacity, toppings={}):
        self.name = name
        self.dough = dough
        self.toppings_capacity = toppings_capacity
        self.toppings = toppings

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError("The flour type cannot be an empty string")
        self.__name = value

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value):
        if value == None:
            raise ValueError("You should add dough to the pizza")
        self.__dough = value

    @property
    def toppings_capacity(self):
        return self.__toppings_capacity

    @toppings_capacity.setter
    def toppings_capacity(self, value):
        if value <= 0:
            raise ValueError("The topping's capacity cannot be less or equal to zero")
        self.__toppings_capacity = value

    def add_topping(self, topping: Topping):
        if self.__toppings_capacity == len(self.toppings):
            raise ValueError("Not enough space for another topping")
        if topping.topping_type in self.toppings.keys():
            self.toppings[topping.topping_type] += topping.weight
            return
        self.toppings[topping.topping_type] = topping.weight

    def calculate_total_weight(self):
        sum_weight = 0
        for topping in self.toppings:
            sum_weight += self.toppings[topping]
        sum_weight += self.dough.weight
        return sum_weight
