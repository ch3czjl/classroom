list_1 = []

for i in range(1,101):
    list_1.append(i)

print list_1

list_2 = [i for i in list_1 if (i % 2 == 0)or(i % 5 == 0)or(i % 3 == 0)]

print list_2

