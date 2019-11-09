Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Nama = 'Muhammad Iqbal Rachmad Anwar'
>>> NIM = 'L200194074'
>>> X = '1' + NIM[7:]
>>> a = int(X)
>>> b = len(Nama)
>>> type(a)
<class 'int'>
>>> #Because data 'X' has been changed to integer data type
>>> type(b)
<class 'int'>
>>> #Because data 'Nama' has a 'len' instruction
>>> a / b
38.357142857142854
>>> #Because the result of 1074 divided by 28 is 38.357142857142854
>>> a // b
38
>>> #Because the sign '//' means division by rownding
>>> 10 * (a - 999)
750
>>> #Because the value of 'a' reduced by 999 is 75. After that multiplied by 10
>>> b ** 2
784
>>> #Because the value of 'b' squared is 784
>>> a % b
10
>>> #Because the remainder resulting from division 'a' by 'b' is 10
>>> c = 12.5
>>> type(c)
<class 'float'>
>>> #Because the 'c' data is a float
>>> a / c
85.92
>>> #Because the result of 1074 divided by 12.5 is 85.92
>>> a // c
85.0
>>> #Because the rounding result of 1074 divided by 12.5 is 85.0
>>> a % c
11.5
>>> #Because the remainder resulting from division 'a' by 'c' is 11.5
>>> c > b
False
>>> #Because the value of 'c' is smaller than the value of 'b'
>>> type(c > b)
<class 'bool'>
>>> #Because the 'c > b' data had changed to boolean data type
>>> a > b and b > c
True
>>> #Because the 'a > b' and 'b > c' data is true
>>> a > 1100 or b < 10
False
>>> #Because the 'a > 1100' and 'b < 10' data is false
