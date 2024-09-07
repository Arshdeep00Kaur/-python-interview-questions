""" find smallest and second smallest no. in list """
list1=[1,2,3,2,6,8,4,0,2]
sn=float('inf')
ssn=float('inf')
for num in list1:
    if num <= sn:
        sn,ssn = num,sn
    elif num < ssn:
        ssn = num
print(sn,ssn) 