def sumd():#Input the size of list
 try:
    n=int(input("Enter size of list: "))
#create empty list
    lis=[]
#loop in to append element
    for i in range(n):
        lis.append(float(input("Enter list element: ")))


    sum=0

#loop through list and add to sum
    for i in lis:   
        sum+=round(i,2)

    print("sum of list is: {:0.2f}".format(sum))
 except ValueError:
    print("You've to enter float values: ")

#create check function to take consent of user to continue
def check():
    while(True):
        s1= str(input("If you want to continue to calculate sum, enter yes or no: "))
        s1.lower()
        #if user provides consent then continue
        if(s1=="yes"):
            sumd()
        #if user doen't want to proceed then break
        elif(s1=="no"):
            break
        #if user enters something other then yes or no then go back to the function
        else:
            check()
#call check function.
check()
   
