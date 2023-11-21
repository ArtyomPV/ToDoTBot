# hello = 'Hello world'
# print(hello)
def learnNumber():
    # NUMBERS
    print(2 + 2)
    print(15 - 2)
    print(3 * 7)
    print(2 ** 8)
    print(7 % 2)


def learnString():
    # STRINGS

    s1 = "hello"
    s2 = 'hello'
    s3 = """hello"""

    print(s1)
    print(s2)
    print(s3)

    greeting = "hello " + "world"
    print(greeting)

    len_word = len(greeting)
    print(len_word)

    print(len(s1))


def learnList():
    # LIST
    strings = ["hello", "world"]
    numbers = [1, 2, 3, 4, 5]
    data = ["hello", 1]

    print(strings)
    print(numbers)
    print(data)

    summa = numbers + data
    print(summa)

    numbers.append(6)
    print(numbers)

    first = strings[0]
    second = strings[1]
    print(first)
    print(second)
    strings_length = len(strings)
    print(strings_length)

    s = sum(numbers)
    print(s)


def learnDict():
    # DICTIONARY
    # key: vaLUE
    # dictionary = {
    #     "cat": "кошка",
    #     "bat": "летучая мышь",
    # }
    # print(dictionary)
    # cat = dictionary["cat"]
    # print(cat)

    countries = {
        'Африка': ['Египет', 'Конго', 'ЮАР'],
        'Азия': ['Китай', 'Тайланд', 'Индонезия']
    }

    africa = countries['Африка']
    print(africa)
    africa_key = "Африка"
    print(countries[africa_key])

    # add new key:value
    countries['Европа'] = ['Австрия', 'Испания', 'Италия']

    print(countries)

    # countries[0] = 'Hello'
    # print(countries)

    africa.append('Эфиопия')
    print(africa)
    print(countries)
    print(len(countries['Африка']))


def input_data():
    name = input("Введите имя: ")
    print(name)

    print('Привет', name)
