fat = 100
result = 1
for i in range(1,fat+1):
    result *= i
soma = 0
for x in str(result):
    soma += int(x)
print(soma)