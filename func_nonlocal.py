#!usr/bin/python

def func_outer():
	x = 2
	print('x is', x)
	def func_inner():
		nonlocal x
		#global x
		x = 5
	func_inner()
	print('Change x to ',x)
func_outer()

def say(message , time = 2):
	print(message * time)
say('hello,')
say('word,',5)