"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def hello_user():
  user_say = input('Как дела? ')
  while user_say == 'Хорошо':
    try:
      user_say = input('Как дела? ')
    except KeyboardInterrupt:
      print('Пока')
      break

hello_user()
