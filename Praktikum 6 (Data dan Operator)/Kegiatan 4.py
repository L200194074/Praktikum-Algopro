Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Nama = 'Muhammad Iqbal Rachmad Anwar'
>>> NIM = 1074
>>> Tinggi = 1.72
>>> Berat = 57
>>> TahunLahir = 2000
>>> Aku = (TahunLahir, Berat, Tinggi, NIM, Nama)
>>> Data = [TahunLahir, Berat, Tinggi, NIM, Nama]
>>> type(Aku)
<class 'tuple'>
>>> #Because data 'Aku' is written in parentheses
>>> Aku[0]
2000
>>> #Because the first object or the 0th index of data 'Aku' is 2000
>>> a = NIM % 4; Aku[a]
1.72
>>> #Because the remaining result of 1074 divided by 4 is 2, so the result of Aku[2] is 1.72
>>> type(Aku[a])
<class 'float'>
>>> #Because 1.72 is a float data type
>>> Aku[a:4]
(1.72, 1074)
>>> #Because the object in 'Aku' start from 'Tnggi, NIM'
>>> Aku[0] = 'ok'
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    Aku[0] = 'ok'
TypeError: 'tuple' object does not support item assignment
>>> #Because 'Aku' data type is tuple, so can't changed with another data
>>> type(Data)
<class 'list'>
>>> #Because the 'Data' data is written in brackets
>>> type(Data[4])
<class 'str'>
>>> #Because the value of 'Data[4]' data is string
>>> Data[4][5]
'm'
>>> #Because in value 'Data[4]' object in the value start in 5, and this is 'm'
>>> Data[4][a:6]
'hamm'
>>> #Because in value 'Data[4]' object in the value start from 'a' until '5' is 'hamm'
>>> Data[0] = 'ok' ; Data
['ok', 57, 1.72, 1074, 'Muhammad Iqbal Rachmad Anwar']
>>> #Because the first object has changed by 'ok', and it call all list in 'Data'
>>> Data[-a]
1074
>>> #Because it is call from rear list
>>> range(a)
range(0, 2)
>>> #Because range of 2 is (0, 2)
