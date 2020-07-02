
# Euler project question 1:
Sum = 0
for i in range(1,1000):
    if ((i % 3 == 0) or (i % 5 == 0)):
        Sum += i

print(Sum)


# Euler project question 16:
big_num = 2 ** 1000
Sum = 0
str_big_num = str(big_num)
for i in range(0,len(str_big_num)):
    Sum += int(str_big_num[i])
print(Sum)


# Euler project question 48:
Sum = 0
for i in range(1,1001):
    Sum += i ** i
print(Sum)

