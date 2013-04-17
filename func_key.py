#!usr/bin/python
#Filename: func_key.py

def func(a, b=5, c=10):
	print('a is', a, 'and b is ', b,' and c is', c)
func(3, 7)
func(c=50, a=100)

def total(initial=5, *numbers, **keywords):
    count = initial
    for number in numbers:
        count += number
        print(count, number, numbers)
    for key in keywords:
        count += keywords[key]
        print(count, key, keywords[key], keywords)
    return count
print(total(10, 1, 2, 3, vegetables=50, fruits=100))
#print(total(10, 1, 2, 3, vegetables=50))