#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

height = 1.75
weight = 80.5
BMI = (weight / height ** 2)

if BMI < 18.5:
    print('过轻')
elif BMI < 25:
    print('正常')
elif BMI < 28:
    print('过重')
elif BMI < 32:
    print('肥胖')
else:
    print('严重肥胖')
