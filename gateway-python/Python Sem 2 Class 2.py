#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 13:24:00 2025

@author: vena
"""

hours = int(input("Please enter the number of hours worked: "))
pay_rate = int(input("Please enter the hourly pay rate: "))

# Computing gross weekly pay
gross_weekly_pay = hours*pay_rate

# Computing net pay
net_pay = gross_weekly_pay - (3.50*5) - (0.16*gross_weekly_pay)

print(gross_weekly_pay)
print(net_pay)
