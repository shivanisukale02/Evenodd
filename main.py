''''
try:
    a= 10
    b=0
    c=a/b
    print(c)
'''
try:
    age=10
    if age<10:
        raise ValueError("Not eligiblefor vote")
    else:
        print("Eligible for vote")
except ZeroDivisionError as e:
    print("Exception occured =>"+str(e) )

except ValueError as e:
    print("Exception =>" +str(e))

except():
    print("Exception occured")

else:
    print()

finally:
    print("Harman LTd")

