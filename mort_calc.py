def calc_reg_payment(rate, amount, years):
    import pandas as pd

    n = years * 12
    r = rate/12
    #test = (((1+0.0025)*84) - 1) / (0.0025*(1+0.0025)*84)
    d = (((1+r)**n) - 1) / (r*(1+r)**n)
    p = (amount/d)
    #print(n,r,d,p)
    return(p)



rate = .03
total = 10000
years = 7
months = years * 12

p = calc_reg_payment(rate, total   , years)
#print(p, p*84)
remaining = total
monthly_rate = rate/12
x=1
while x <= months:
    remaining = remaining*(1 + monthly_rate) - p
    print(x,remaining)
    x+=1
