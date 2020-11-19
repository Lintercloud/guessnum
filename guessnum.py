# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 16:09:02 2020

@author: Linter
"""

import random
pwd = random.randint(1,100)
count = 0
while True:
    count = count + 1
    guess = int(input("請猜一個數字1~100: "))
    if guess == pwd:
        print("恭喜你答對了")
        print("你猜了", count, "次")
        break
    elif guess > pwd:
        print("要再小一點")
    elif guess < pwd:
        print("要再大一點")
    print("你猜了", count, "次")
        