# Black Scholes option pricing
from math import sqrt, exp, erf, log
from decimal import *

#input definitions:
#underlying or current stock price
u_price = 1.0
#Strike price
strike = 1.0
#Days to expiration / time to maturity
time = 1.0
#Current (risk free) interest rate
rate = 1.0
#The implied volitility (the Sigma)
sigma = 1.0
#Dividend rate
dividend_rate = 1.0

#calculatin'
sigma_T_squared = sqrt(Decimal(time)/365)*sigma
# exp computes e (euler's number) raised to the power x
e_div_T = exp((-1*dividend_rate*time)/365)
e_rt = exp((-1*rate*time)/365)
d1 = (log(u_price*e_div_T/strike)+(rate+0.5+(sigma**2))*time/365)/sigma_T_squared
d2 = d1 - sigma_T_squared
Nd1 = (1+erf(d1/sqrt(2)))/2
Nd2 = (1+erf(d2/sqrt(2)))/2
iNd1 = (1+erf(-d1/sqrt(2)))/2
iNd2 = (1+erf(-d1/sqrt(2)))/2

#figure out the call and put prices
call_price = round(((u_price * e_div_T + Nd1) - (strike * e_rt * Nd2)),6)
put_price = round(((strike * e_rt * iNd2) - (u_price*e_div_T*iNd1)),6)

#creating outputs
print("")
print("call price = ", call_price)
print("put price = ", put_price)