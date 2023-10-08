# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 19:20:05 2023

@author: Huawei
"""
print("=========Selamat Datang di Segitiga Detektor==========")
a = float(input("Isi sisi a: "))
b = float(input("Isi sisi b: "))
c = float(input("Isi sisi c: "))

def j_segitiga (a,b,c):
    
    if a + b > c and a + c > b and b + c > a:
        if a == b and b == c:
            return "Segitiga Sama Sisi"
        elif a == b or a == c or b == c:
            return "Segitiga Sama Kaki"
        elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            return "Segitiga Siku-Siku"
        else:
            return "Segitiga Sembarang"
    else:
        return "Ini bukan merupakan segitiga"

jenis = j_segitiga(a,b,c)
print("Jenis segitiga:", jenis)
print("========Terimakasih=========")