number=float(input("Input score1:"))
number2=float(input("Input score2:"))
number3=float(input("Input score3:"))
total=number+number2+number3
print(f"The total is:{total}")
avg=total/3
print(f"The average is:{avg}")
if(avg>=0 and avg<=49):
    grade='F'
elif(avg>50 and avg<=65):
    grade='E'
elif(avg>66 and avg<=75):
    grade='D'
elif(avg>76 and avg<=85):
    grade='C'
elif(avg>86 and avg<=95):
    grade='B'
else :
    grade='A'
print(f"Grade of student is:{grade}")