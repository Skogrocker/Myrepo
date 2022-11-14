Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> todos = dict() # todos = {}
... todos = list() # todos = []
... 
... 
... 
... HELP = '''
... Список доступных команд:
... * print/show  - напечать все задачи на заданную дату
... * todo - добавить задачу
... * help - Напечатать help
... '''
... 
... stop = False 
... while not stop: 
...     command = input('Введите команду: ')
...     if command == 'help':
...         print(HELP)
...     elif command == 'todo':
...         task = input('Введите задачу: ')
...         todos.append(task)
...         # Про синтаксис f-строк можно прочитать, например, тут:
...         # https://pythonru.com/osnovy/formatirovanie-v-python-s-pomoshhju-f-strok
...         # Альтернативный вариант:
...         # print('Задача ' + task + ' добавлена')
...         print(f'Задача {task} добавлена')
...     elif (command == 'print') or (command == 'show'):
...         print(todos)
...     elif command == 'exit':
...       print('Спасибо за использование! До свидания!')
...       stop = True
...     else:
...       print('Неизвестная команда!')
...       print(HELP)
