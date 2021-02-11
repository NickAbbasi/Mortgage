import pandas as pd

def calc_reg_payment(rate, amount, years):


    n = years * 12
    r = rate/12
    #test = (((1+0.0025)*84) - 1) / (0.0025*(1+0.0025)*84)
    d = (((1+r)**n) - 1) / (r*(1+r)**n)
    p = (amount/d)
    #print(n,r,d,p)
    return(p)


def calcing_payment_schedule(rate, total,years):

    dict = {'month':[],'payment':[],'principal':[],'interest':[], 'remaining':[]}
    months = years * 12

    p = calc_reg_payment(rate, total   , years)
    #print(p, p*84)
    remaining = total
    monthly_rate = rate/12
    x=1
    while x <= months:

        dict['month'].append(x)
        dict['payment'].append(p)
        dict['principal'].append(p - (remaining*(monthly_rate)))
        dict['interest'].append((remaining*(monthly_rate)))
        remaining = remaining*(1 + monthly_rate) - p
        dict['remaining'].append(remaining)
        #print(x,remaining)
        x+=1
    return(dict)


rate = .02875
years = 30
total = 315400

dict = calcing_payment_schedule(rate, total, years)

df = pd.DataFrame(dict)

df.to_excel('..\mort.xlsx', 'data')

print(df)
