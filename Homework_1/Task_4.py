# 1. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

quarter = int(input("Введите номер четверти (от 1 до 4): "))

if quarter >= 1 and quarter <= 4:
    if quarter == 1: print("Диапозон возможных точек в четверти I: x > 0 и y > 0")
    if quarter == 2: print("Диапозон возможных точек в четверти II: x < 0 и y > 0")
    if quarter == 3: print("Диапозон возможных точек в четверти III: x < 0 и y < 0")
    if quarter == 4: print("Диапозон возможных точек в четверти IV: x > 0 и y < 0")
else: print("Такой четверти не существует.")