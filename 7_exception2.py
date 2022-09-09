"""

Домашнее задание №1

Исключения: приведение типов

* Перепишите функцию discounted(price, discount, max_discount=20)
  из урока про функции так, чтобы она перехватывала исключения,
  когда переданы некорректные аргументы.
* Первые два нужно приводить к вещественному числу при помощи float(),
  а третий - к целому при помощи int() и перехватывать исключения
  ValueError и TypeError, если приведение типов не сработало.
    
"""

def discounted(price, discount, max_discount=20):
  try:
    price = abs(float(price))
    discount = abs(float(discount))
    max_discount = abs(float(max_discount))
    if max_discount >= 100:
      raise ValueError('Скидка не может быть больше 100%')
    if discount > max_discount:
      discount = max_discount
      price_with_discount = price - (price * discount / 100)
      print(int(price_with_discount))
    else:
      price_with_discount = price - (price * discount / 100)
      print(int(price_with_discount))
  except ValueError:
    print('Неверная величина')
  except TypeError:
    print('Неверный тип данных')

    


discounted(100, 2)
discounted(100, "3")
discounted("100", "4.5")
discounted("five", 5)
discounted("сто", "десять")
discounted(100.0, 5, "10")