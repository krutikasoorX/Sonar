def strToUp():
        #run till user does't want to stop
    while(True):
        #get consent of user
        s1= str(input("If you want to continue to generate, enter yes or no: "))
        s1.lower()
        #if user provides consent then continue
        if(s1=="yes"):
            st=str(input("Enter the string - "))
            print(st.upper())
        #if user doen't want to proceed then break
        elif(s1=="no"):
            break
        #if user enters something other then yes or no then go back to the function
        else:
            strToUp()
#call check function.
strToUp()