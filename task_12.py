from task_11 import Dessert


class JellyBean(Dessert):
    def __init__(self, name='Undefined', calories=0, flavor='Undefined'):
        super().__init__(name, calories)
        self.flavor = flavor

    @property
    def flavor(self):
        return self.__flavor

    @flavor.setter
    def flavor(self, value):
        self.__flavor = value

    def is_delicious(self):
        if self.flavor == 'black licorice':
            return False
        return True


des = Dessert('myata', 400)
gru = JellyBean('grusha', 20, 'black licorice')

print(gru.is_healthy())