def solution01():
    x =1
    while x <= 10:
        print(x)
        x += 1

    print(x)


solution01()


def solution02():
    HELP = """
    help - напечатать справку о программе
    add - добавить задачу в список (название задачи запрашиваем у пользователя)ю
    show - напечатать все добавленные задачи.
    """

    tasks = []
    run = True

    while(run):
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

solution02()
