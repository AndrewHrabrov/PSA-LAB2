enter = " ".join(input().split())

result_list = []
for i in enter.split():
    result_list.append(int(i, 2))

print(" ".join(str(x) for x in result_list)) # Объединение списка строк в одну строку по пробелу