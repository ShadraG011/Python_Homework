# 2. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math

Xa = int(input("Введите координату X точки A: "))
Ya = int(input("Введите координату Y точки A: "))
Xb = int(input("\n" + "Введите координату X точки B: "))
Yb = int(input("Введите координату Y точки B: "))

distanse = math.sqrt(pow((Xb - Xa), 2) + pow((Yb - Ya), 2))

print(f"Расстояние между точкой A и точкой B: {round(distanse.real, 2)}")
