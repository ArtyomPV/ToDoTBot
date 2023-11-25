def solution01():
    x = 1
    while x <= 10:
        print(x)
        x += 1

    print(x)


# solution01()


def solution02():
    HELP = """
    help - напечатать справку о программе
    add - добавить задачу в список (название задачи запрашиваем у пользователя)ю
    show - напечатать все добавленные задачи.
    """

    tasks = []
    run = True

    while (run):
        command = input("Type command: ")
        if command == 'help':
            print(HELP)
        elif command == 'show':
            print(tasks)
        elif command == 'add':
            task = input("Enter a task: ")
            tasks.append(task)
            print('Task is added')
        else:
            print("Unknown command!")
            # run = False
            break

    print('GoodBay!')


# solution02()

def advansed_solution02():
    import random
    # Сегодня, завтра, 31.12.23
    # [Задача1, Задача2, Задача3, ....]
    # Дата -> [Задача1, Задача2, Задача3, ...]
    HELP = """
        help - напечатать справку о программе
        add - добавить задачу в список (название задачи запрашиваем у пользователя)ю
        show - напечатать все добавленные задачи.
        random - добавить случайную задачу на дату сегодня
        """

    tasks = {}
    run = True
    RANDOM_TASK = 'изучать создание телеграмм бота на Python'
    RANDOM_TASKS = ['Clean car', 'wash dishes', 'draw a picture', 'write letter', 'feed the dog']

    def show():
        date = input("Enter date: ")
        if date in tasks:
            for task in tasks[date]:
                print('-', task)
        else:
            print('no any task for', date)

    def add_task(date, task):
        if date in tasks:
            tasks[date].append(task)
        else:
            tasks[date] = []
            tasks[date].append(task)
            return f'{task} added to date: {date}'

    while (run):
        command = input("Type command: ")
        if command == 'help':
            print(HELP)
        elif command == 'show':
            show()
            # print(tasks)
        elif command == 'add':
            date = input("Enter date for adding a task: ")
            task = input("Enter a task: ")
            print(add_task(date, task))

            # print('Task ', task, 'is added at ', date)
        elif command == 'random':
            task = random.choice(RANDOM_TASKS)
            print(add_task('today', task))
            # if 'today' in tasks:
            #     tasks['today'].append(RANDOM_TASK)
            # else:
            #     tasks['today'] = []
            #     tasks['today'].append(RANDOM_TASK)
        else:
            print("Unknown command!")
            # run = False
            break

    print('GoodBay!')


advansed_solution02()


def solution04():
    for i in [4, 5, 6]:
        if i % 2 == 0:
            print(i)


solution04()
