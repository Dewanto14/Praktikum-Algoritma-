# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 12:08:09 2023

@author: Huawei
"""

import math

print("=====Selamat Datang di Program Mencari Akar Persamaan Kuadrat dan Determinan=====")

a = int(input("Masukkan nilai A : ")) 
b = int(input("Masukkan nilai B : "))
c = int(input("Masukkan nilai C : "))



determinan = b**2 - 4*a*c  


if a !=0:
    print(f"Persamaan kuadrat {a}x² + {b}x + {c}")
    print("Determinanya =", determinan)
    if determinan > 0: 
        akar1 = (-b + math.sqrt(determinan)) / (2*a)
        akar2 = (-b - math.sqrt(determinan)) / (2*a) 
        print("Memiliki Akar Berbeda")
        print("Akar x1 =", akar1)
        print("Akar x2 =", akar2)
        akar1, akar2
    elif determinan == 0:
        akar1 = -b / (2*a)
        print("Merupakan Akar Kembar")
        print("Akar =", akar1)
        akar1
    else:
        print("Merupakan Akar Imaginer")
        print(f"Akar x1 = -{b} + √{determinan} / 2*{a}")
        print(f"Akar x2 = -{b} - √{determinan} / 2*{a}")
else:
    print("Bukan merupakan persamaan kuadrat, karena nilai A = 0")    





