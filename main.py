#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8

tickets = int(input('Сколько билетов будете покупать?\n'))
L = []
L1 = []

L = [int(input('Сколько лет посетителю?\n')) for i in range(1, tickets+1)]
#print(L)
for i in L:
    if i < 18:
        L1.append(0)
    elif 18 <= i < 25:
        L1.append(990)
    else:
        L1.append(1390)
#print(L1)
#print(sum(L1))
if tickets <= 3:
    print ('Сумма к оплате', sum(L1))
else: 
    print ('Сумма к оплате', (sum(L1)-sum(L1)*0.1))
