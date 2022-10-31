mterm = float(input("mid-Term Exam: "))
fterm = float(input("Final-Term Exam: "))

grade = mterm*0.4 + fterm*0.6

if(grade>=85 and grade<= 100):
    print(grade , "Grade : AA")
elif(grade>=75 and grade<85):
    print(grade, "Grade: AB")
elif(grade>=60 and grade<75):
    print(grade, "Grade : BB")
elif (grade >= 50 and grade < 60):
    print(grade, "Grade: CC")
else :
    print(grade , "failed ")

g = [89,32,45,12,34]
numbers = len(g)
su = 0
for n in g:
    su+=n
    avg = su/numbers
print("average" .format(numbers,avg))



i=0
while(i!=len(g)):
    print(g[i])
    i+=1

def factorialOfNumber(num):
    f = 1
    for n in range(1,num+1):
       f = f * n
    return f

print("factorial is : ",factorialOfNumber(6))


n = int(input("Enter a Number:"))
number = []
for i in range(0,n):
    E = int(input("Enter Element numer: "+ str(i+1))+"  \n")
    number.append(E)
avg = sum(number)/n
print("Hers is the average of all entered numbers : " ,avg)
