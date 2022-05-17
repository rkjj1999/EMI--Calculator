#!/usr/bin/env python
# coding: utf-8

# In[ ]:


principal_amount= float(input("Enter the Principal: \n"))
interest_rate = float(input("Enter the Interest rate: \n"))
time_period = int(input("Enter the Time period in years: \n"))
rate_of_interest = interest_rate/(12*100)
EMI= principal_amount * rate_of_interest (1+ rate_of_interest* time_period)/(1+ rate_of_interest * time_period-1)
print(EMI)


# In[ ]:


p = float(input("Enter principal amount: "))
R = float(input("Enter annual interest rate: "))
n = int(input("Enter number of months: " ))

# Calculating interest rate per month
r = R/(12*100)

# Calculating Equated Monthly Installment (EMI)
emi = p * r * ((1+r, n))/((1+r,n) - 1)

print("Monthly EMI = ", emi)


# In[ ]:


def emi(p,r,t):
    r=r/(12*100)
    t=t*12
    emi= (p*r*pow(1+r,t))/(pow(1+r,t)-1)
    return emi

pa= float(input("Enter Principal amount: \n"));
ra= float(input("Enter the Interest rate: \n"));
time= int(input("Enter the Time period in years: \n"));
emi= emi(pa, ra, time);
print(emi)


# In[ ]:


P_A= float(input("Enter the Principal: \n"))
I_R = float(input("Enter the Interest rate: \n"))
T_P= int(input("Enter the Time period in Months \n"))
ROI = I_R/(12*100)
EMI= P_A * ROI * (1+ROI** T_P)/((1+ROI** T_P)-1) 
print(EMI)


# In[ ]:





# In[ ]:




