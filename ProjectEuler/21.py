
def divisores(num):
    ldiv = []
    for div in range(1,1+num//2):
        if num%div == 0:ldiv.append(div)
    return ldiv

somatorio = 0

resultados = [0]

for i in range(1,10001):
    amicae1 = sum(divisores(i))
    amicae2 = sum(divisores(amicae1))
    if amicae1 != amicae2 and amicae2 == i:
        somatorio += i


print(somatorio)

