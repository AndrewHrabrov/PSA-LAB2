s = {1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7:'семь',
     8: 'восемь', 9: 'девять', 10: 'десять', 11: 'одиннадцать', 12: 'двенадцать',
     13: 'тренадцать', 14: 'четырнадцать'
    ,15: 'пятнадцать', 16: 'шестнадцать', 17: 'семнадцать', 18: 'восемнадцать', 19:'девятнадцать',
     20: 'двадцать', 30: 'тридцать', 40: 'сорок', 50: 'пятьдесят', 60: 'шестьдесят',
     70: 'семьдесят', 80: 'восемьдесят', 90: 'девяносто'}

def to_word(number):
    if (number < 1): return None
    elif (number > 99): return 'много'
    elif (number >= 1 and number <= 20): return s[number]
    elif (number % 10 != 0): return s[number // 10 * 10] + ' ' + s[number % 10]
    else: return s[number // 10 * 10] + ' ' + ''

for i in range(1, 100):
    print(to_word(i))