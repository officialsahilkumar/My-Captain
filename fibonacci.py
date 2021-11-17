num = int(input("Enter any number : "))
n1 , n2 = 0,1
count = 0
if num<=0:
    print("Enter number greater than zero")

else:
    for i in range (0,num):
        print(count,end=" ")
        n1 = n2
        n2 = count
        count = n1 + n2