class Dessert:
    def __init__(self, name='Undefined', calories=0):
        self.__name = name
        self.__calories = calories

    @staticmethod
    def is_delicious():
        return True

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def calories(self):
        return self.__calories

    @calories.setter
    def calories(self, value):
        self.__calories = value

    def is_healthy(self):
        if self.calories < 200:
            return True
        return False
