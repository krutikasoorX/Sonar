def check():
    while(True):
        s1= str(input("If you want to continue get datatype, enter yes or no: "))
        s1.lower()
        #if user provides consent then continue
        if(s1=="yes"):
            s=input("Enter your input: ")
            s1=int(input("Which data type do you want? 1.int 2.boolean 3. string"))
            #st=(input("What is the data type ? "))
            if(s1==1):
                try:
                    s=int(s)
                    print(isinstance(s,int))
                except ValueError:
                    print("This is not a integer!!")
                
            elif(s1==2):
                try:
                    s=bool(s)
                    print(isinstance(s,bool))
                except bool:
                    print('this is not boolean!')
            elif(s1==3):
                s=str(s)
                print(isinstance(s,str))
            else:
                print("Wrong data type predicted")
        #if user doen't want to proceed then break
        elif(s1=="no"):
            break
        #if user enters something other then yes or no then go back to the function
        else:
            check()
#call check function.
check()