Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s="Iam going to LPU"
s.split
<built-in method split of str object at 0x0000016F69AAA5B0>
s.split()
['Iam', 'going', 'to', 'LPU']
s.alnum()
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    s.alnum()
AttributeError: 'str' object has no attribute 'alnum'. Did you mean: 'isalnum'?
s.isalnum()
False
s.isalpha()
False
s.isdigit()
False
s.islower()
False
s.isupper()
False
s.isspace()
False
s="Pythonprogramming"
s.endswith("programming")
True
s.endswith("java"-+)
SyntaxError: invalid syntax
s.endswith("java")
False
s.find("prog")
6
s.find("java")
-1
s.find("o")
4
s.count("m")
2
s="hello how are you")
SyntaxError: unmatched ')'
s="hello how are you"
s.capatalize()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    s.capatalize()
AttributeError: 'str' object has no attribute 'capatalize'. Did you mean: 'capitalize'?
s.capitalize()
'Hello how are you'
s.lower()
'hello how are you'
s.upper()
'HELLO HOW ARE YOU'
s.title()
'Hello How Are You'
s="HelloWorld"
s.swapcase()
'hELLOwORLD'
s="hello""world"
s.replace
<built-in method replace of str object at 0x0000016F69B53170>
s.replace()
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    s.replace()
TypeError: replace expected at least 2 arguments, got 0
s="abcde"
s.r:3
s.r(:3)
SyntaxError: invalid syntax
s.r(3)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    s.r(3)
AttributeError: 'str' object has no attribute 'r'
