from pprint import pprint
class Product:
    def __init__(self,name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        fr = file.read()
        file.close()
        return fr

    def add(self, *products):
        """Метод подходящий под вывод как в примере"""
        for j in products:
            if str(j) in self.get_products():  # здесь условие по продукту в целом и с весом и категорией
                print(f'Продукт {j} уже есть в магазине')

            else:
                file = open(self.__file_name, 'a')
                file.write(f'\n {j}')
                file.close()

    def add2(self, *products):
        """Метод по условию из задания: Добавляет в файл __file_name каждый продукт из products, если его ещё нет в файле (по НАЗВАНИЮ).
        Если такой продукт уже есть, то не добавляет и выводит строку 'Продукт <НАЗВАНИЕ> уже есть в магазине' """
        for j in products:
            if j.name in self.get_products():   # Здесь условие именно проверки по НАЗВАНИЮ продукта
                print(f'Продукт {j.name} уже есть в магазине')

            else:
                file = open(self.__file_name, 'a')
                file.write(f'\n {j}')
                file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())



