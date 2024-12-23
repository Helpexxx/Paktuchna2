name = "Roman"
surname = "Tkachuk"
age = 17  #
count_int = 0
count_str = 0
count_bool = 0
count_set = 0
count_list = 0
count_tuple = 0
count_float = 0
lst_notnull = []  # Список для збереження ненульових значень
max_value = -1  # Початкове значення для пошуку максимального числа
types_count = {str, int, bool, set, list, tuple, float}  # Множина всіх можливих типів
lst_count_types = [count_set, count_float, count_tuple, count_list, count_bool, count_str, count_int]  # Лічильники типів
lst_name_type = ['set', 'float', 'tuple', 'list', 'bool', str, int]  # назви типів
lst = [name, surname, age]  # Список, який аналізується

# Перебір елементів у списку lst для підрахунку типів
for iteml in lst:
    if type(iteml) == int:
        lst_count_types[-1] += 1  # Збільшується лічильник цілих чисел
    elif type(iteml) == str:
        lst_count_types[-2] += 1  # Збільшується лічильник рядків

# Перебір лічильників
for itemc in lst_count_types:
    if itemc != 0:
        lst_notnull.append(itemc)  # ненульові значення до lst_notnull
    if len(lst_notnull) == 0:  # Якщо у списку немає ненульових значень
        print('Good')
    else:
        if itemc == max_value:
            print('Not')  # Виводимо "Not" і припиняємо виконання
            break
        elif itemc > max_value:  # Якщо значення більше за поточний максимум
            max_value = itemc  # Оновлюємо max_value

# Знаходимо індекс максимального значення в списку лічильників
inn = lst_count_types.index(max_value)

# Виводимо назву типу, який має найбільшу кількість елементів
print(lst_name_type[inn])

# Видаляємо елементи з lst, які не відповідають типу з найбільшим значенням
for iteml in lst:
    if type(iteml) != lst_name_type[inn]:  # Якщо тип елемента не збігається з основним
        lst.remove(iteml)  # Видаляємо цей елемент