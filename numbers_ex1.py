#!/usr/bin/env python
from __future__ import print_function

num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter a number: "))

sum = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / float(num2)
rem = num1 % float(num2)

print("sum is:  {:>30}".format(sum))
print("subtraction is:{:>30}".format(sub))
print("multiplication is:  {:>30}".format(mul))
print("division is:  {:>30}".format(div))
print("remainder is:  {:>30}".format(rem))
