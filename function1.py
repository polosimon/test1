#!/usr/bin/python

def printMax(a, b):
	if a > b:
		print(a, 'is max')
	elif a == b:
		print(a, 'is equal to ', b)
	else:
		print(b, 'is max')

#printMax(3,4)
a = int(input('a:'))
b = int(input('b:'))
printMax(a, b)

x = 50
def func():
	global x
	print('x is',x)
	x = 2
	print('Change x to',x)
func()
print('x is still', x)