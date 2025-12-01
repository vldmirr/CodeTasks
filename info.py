#перевернуть строку
s="hello"
print(s[::-1])

#классы с наследованием
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Привет, меня зовут {self.name} и мне {self.age} лет."

class Mentor(Student):
    def __init__(self, name, age, speciality):
        super().__init__(name, age) 
        self.speciality = speciality

    def introduce(self):
       
        return f"Name: {self.name}, my {self.age} age, i am {self.speciality}."

o=Mentor("Oleg",32,"svarhik")
print(o.introduce())

#Дан список чисел. Найти уникальные элементы / убрать дубликаты python
#1
my_list = [1, 2, 2, 3, 4, 4, 5]
new_list = list(set(my_list))
print(new_list)  # Вывод: [1, 2, 3, 4, 5]

#2
my_list = [1, 2, 2, 3, 4, 4, 5]
new_list = []
for item in my_list:
    if item not in new_list:
        new_list.append(item)
print(new_list) # Вывод: [1, 2, 3, 4, 5]

#Пример генератора списка
# Генерация списков  — это способ создания списков с использованием лаконичного синтаксиса. Он позволяет 
# генерировать новые списки, применяя выражение  к  каждому элементу существующего  
# итерируемого  объекта (например,  списка  или  диапазона ). Это помогает писать более чистый и читаемый код по сравнению с традиционными методами циклов.

# Например , если у нас есть список целых чисел и мы хотим создать новый список, 
# содержащий квадрат каждого элемента, мы можем легко добиться этого, используя включение списков.

a = [2,3,4,5]
res = [val ** 2 for val in a]
print(res)

#Пример использования lambda
s1 = 'GeeksforGeeks'

s2 = lambda func: func.upper()
print(s2(s1))

#Сортировака списка
my_list = [100, 50, 65, 82, 23]
my_list.sort()
print(my_list) # Вывод: [23, 50, 65, 82, 100]