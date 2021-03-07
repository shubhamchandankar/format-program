Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Nadeem>Deepak
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    Nadeem>Deepak
NameError: name 'Nadeem' is not defined
>>> 10 > 9
True
>>> True
True
>>> 10 >= 10
True
>>> "Nadeem" > "nadeem"
False
>>> "Nadeem" > "Deepak"
True
>>> 
>>> 
>>> "nadeem" > "NADEEM"
True
>>> "NADEEM" > "nadeem"
False
>>> 
>>> 
>>> 
>>> 10 and 10
10
>>> 1 and 1
1
>>> 1 and 0
0
>>>  0 and 0
 
SyntaxError: unexpected indent
>>> 10 and 10
10
>>> 
>>> 1 or 1
1
>>> 1 or 0
1
>>> 0 or 0
0
>>> 10 and 10
10
>>> 10 or 0
10
>>> 0 or 0
0
>>> 0 or 1
1
>>> "nadeem" and "khan"
'khan'
>>> "nadeem " abd "Khan"
SyntaxError: invalid syntax
>>> "nadeem " and "Khan"
'Khan'
>>> 
>>> 
>>> "Nadeem" and "Khan"
'Khan'
>>> 
>>> 
>>> 0 or 0
0
>>> "Nadeem" and "khan"
'khan'
>>> "nadeem" and "khan"
'khan'
>>> 
>>> 
>>> "nadeem" and "Khan"
'Khan'
>>> 'Khan'
'Khan'
>>> "nadeem" and "NADEEM"
'NADEEM'
>>> 10 or 0
10
>>> "Gun" and "Hen"
'Hen'
>>> 
>>> 
>>> "shubham " and "Shubham"
'Shubham'
>>> 
>>> 
>>> x=10
>>> if x==10:
	print("shubham")

	
shubham
>>> shubham
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    shubham
NameError: name 'shubham' is not defined
>>> 
>>> 
>>> x=10
>>> if x==10:
	print("shubham")
else:
	print("subhi")

shubham
>>> x=10
>>> if x==11:
	print("shubham")
else:
	print("subhi")
	
SyntaxError: multiple statements found while compiling a single statement
>>> x=10
>>> if x==1:
	print("shubham")
else:
	print("subhi")
	
SyntaxError: multiple statements found while compiling a single statement
>>> x=10
>>> if x==10:
	print("shubham")
else:
	print("subhi")

    

