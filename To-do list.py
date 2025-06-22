tasks = []

while True:
    print("=== To-Do List ===")
    print("Нажми 1 чтобы посмотреть список задач")
    print("Нажми 2 чтобы добавить задачу")
    print("Нажми 3 чтобы удалить задачу")
    print("Нажми 4 чтобы выйти")

    try:
        a = int(input("Введите номер действия: "))
        if a == 1:
            if not tasks:
                print("Нет задач")
            else:
                print("Твои задачи:")
                for index, task in enumerate(tasks):
                    print(index + 1, task) #чтобы показывало задачи не с нулевой позиции
        elif a == 2:
            task = input("Введите задачу: ")
            if task.strip():
                tasks.append(task)
                print("Твои задачи:", tasks)
            else:
                print("Ошибка: задача не может быть пустой!")
        elif a == 3:
            if not tasks:
                print("Удалять нечего")
            else:
                print(tasks)
                print("Какую задачу вы хотите удалить?")
                try:
                    number = int(input("Введите номер задачи: "))
                    if 1 <= number <= len(tasks):
                        del tasks[number - 1]
                        print("Твои задачи:", tasks)
                    else:
                        print("Ошибка: такого номера задачи нет!")
                except ValueError:
                    print("Ошибка: введи число!")
        elif a == 4:
            print("Пока!")
            break  
        else:
            print("Ошибка: выбери от 1 до 4!")
    except ValueError:
        print("Ошибка: введи число!")
