anos = {365:{1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31},
        366:{1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}}

diasTotais = 0
domingos = 0

for ano in range(1900,2001):
    if ano%4 == 0 and ano%100 != 0:meses = anos[366]
    else:meses = anos[365]

    for i in meses.values():
        diasTotais += i
        if (diasTotais+1)%7 == 0 and ano > 1900:domingos +=1

print(domingos-1)