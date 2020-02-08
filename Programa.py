Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def fib(n):
	a=0
	b=1
	for k in range(n):
		c=a+b
		a=b
		b=c
		return b
	for x in range(20):
		print(fib(x))

		
>>> #Forma recursiva
>>> def fibo_rec(n):
	if n<2:
		return n
	return fibo_rec(n-1)+fibo_rec(n-2)
for x in range(20):
	
SyntaxError: invalid syntax
>>> for x in range(20):
	print(fibo_rec(x))

	
Traceback (most recent call last):
  File "<pyshell#19>", line 2, in <module>
    print(fibo_rec(x))
NameError: name 'fibo_rec' is not defined
>>> 
>>> 