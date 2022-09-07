#!/usr/bin/python3
import time
from decimal import *
   
print('Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.')
   
start_time = time.perf_counter()

getcontext().prec = 30001 
limit = 10000
dmax = 0
dmax2 = 0
fmax = 0
for fr in range(2,limit):
    val = Decimal(1000) / Decimal(float(fr))
    test = str(val).replace('.','')           # convert to string - substring-find is verry efficient                        
    tsub = test[5:55]                         # teststring 20 digits
    tcheck = test.find(tsub,56)               # find first reoccurance of teststring
    if tcheck > 0:           
        tcheck2 = test.find(tsub,tcheck+1)    # find secod occurance
        if tcheck > dmax:
            dmax = tcheck
            dmax2 = tcheck2
            fmax = fr         
            print('Denominator ', fmax, ' contains the longest recurring cycle - length = ', dmax2 - dmax )

print("--- %s seconds ---" % (time.perf_counter() - start_time))