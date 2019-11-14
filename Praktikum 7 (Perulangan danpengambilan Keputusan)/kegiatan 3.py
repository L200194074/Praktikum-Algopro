x = input('please input your name: ')
y = float(input('what time it is: '))
if 04.00 < y < 10.00:
    print('good morning',x)
if 10.01 < y < 14.00:
    print('its hot out there right?',x)
if 14.01 < y < 18.00:
    print('good afternoon',x)
if 18.00 < y < 24.00:
    print('go to bed please',x)
