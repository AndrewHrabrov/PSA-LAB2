now = '2022-09-18 12:41:18-03:00'
date = now.split()[0].split('-')
time = now.split()[1].split('+')[0].split('-')[0].split(':')

try:
    tz = ( ['+'] + now.split()[1].split('+')[1].split(':') ) # Если возникает ошибка то
                                                             # выполняется блок except
except:
    tz = ( ['-'] + now.split()[1].split('-')[1].split(':') )

print(date)
print(time)
print(tz)
