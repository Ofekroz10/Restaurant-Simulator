import abc
from abc import ABC, abstractmethod
from enum import IntEnum


class Status(IntEnum):
    WAIT = 0
    INPRODUCE = 1
    DELIVERY = 2
    FINISH = 3


class Meal(ABC):
    @property
    def all_ing_map(self):
        try:
            return self._all_ing_map
        except:
            raise NotImplementedError

    @property
    def ing_map(self):
        try:
            return self._ing_map
        except:
            raise NotImplementedError

    @property
    def name(self):
        try:
            return self._name
        except:
            raise NotImplementedError

    @property
    def price(self):
        try:
            return self._price
        except:
            raise NotImplementedError

    @property
    def seconds(self):
        try:
            return self._seconds
        except:
            raise NotImplementedError

    @property
    def status(self):
        try:
            return  self._status
        except:
            raise NotImplementedError

    def status_plus(self):
        self._status = self.status+1

    def add_ingredient(self, ingredient):
        print(self.ing_map.keys())
        if self.ing_map.get(ingredient) is not None:
            self.ing_map[ingredient] = self.ing_map[ingredient] + 1
            self._price += (self.all_ing_map[ingredient]).price
            self._seconds += (self.all_ing_map[ingredient]).seconds
        else:
            raise KeyError

    def minus_ingredient(self, ingredient):
        if self.ing_map.get(ingredient) is not None:
            if self.ing_map[ingredient] > 0:
                self.ing_map[ingredient] = self.ing_map[ingredient] - 1
                self._price -= (self.all_ing_map[ingredient]).price
                self._seconds -= (self.all_ing_map[ingredient]).seconds
        else:
            raise KeyError

    def calc_price(self):
        """ ing_map is a map: <ING,AMOUNT> """
        for ing in self.ing_map.keys():
            self._price += self.ing_map[ing] * (self.all_ing_map[ing]).price
        print('total price ', self._price)

    def calc_seconds(self):
        """ ing_map is a map: <ING,AMOUNT> """
        for ing in self.ing_list:
            self._price += self.ing_map[ing] * (self.all_ing_map[ing]).seconds
        print('total seconds ', self._seconds)

    def read_ing(self, file_name):
        ZERO_AMOUNT = 0
        with open(file_name, 'r') as file:
            for i in file.readlines():
                i = i.replace('\n', '')
                self._ing_map[i] = ZERO_AMOUNT

    def make_ing_amount_zero(self, ingredient):
        ZERO_AMOUNT = 0
        if self.ing_map.get(ingredient) is not None:
            prev_amount = self.ing_map[ingredient]
            self._price -= (self.all_ing_map[ingredient]).price * prev_amount
            self._seconds -= (self.all_ing_map[ingredient]).seconds * prev_amount
            self.ing_map[ingredient] = ZERO_AMOUNT
        else:
            raise KeyError

    def get_ingredients(self):
        return self.ing_map.keys()


class Burger(Meal):
    def __init__(self, all_ing_map):
        self._all_ing_map = all_ing_map
        self._ing_map = {}
        self._name = 'Burger'
        self._price = 0
        self._seconds = 0
        self.read_ing('burger.txt')


class Salad(Meal):
    def __init__(self, ing_map):
        self._all_ing_map = ing_map
        self._ing_map = {}
        self._name = 'Salad'
        self._price = 0
        self._seconds = 0
        self.read_ing('salad.txt')
