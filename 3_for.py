"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

list=[
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]




summa = 0
srednee = 0
for j in range(len(list)):
  summa += sum(list[j]['items_sold']) 
  print('Суммарное количество продаж', list[j]['product'], 'равно', sum(list[j]['items_sold']))
for k in range(len(list)):
  srednee += (sum(list[k]['items_sold']))/len(list[k]['items_sold'])
  print('Среднее количество продаж для', list[k]['product'], 'равно', (sum(list[k]['items_sold']))/len(list[k]['items_sold']))

print('Суммарное количество продаж всех товаров равно', summa)
print('Среднее количество продаж всех товаров равно', srednee/len(list))