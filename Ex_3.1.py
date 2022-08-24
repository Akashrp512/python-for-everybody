hrs = input("Enter Hours: ")
rate= input("enter rate per hour: ")
h=float(hrs)
if h<=40:
    pay=h*float(rate)
else :
    hnew=h-40
    pay=(40*float(rate))+(float(hnew)*(float(rate)*1.5))
print(pay)    
