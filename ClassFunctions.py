class SubfieldsInAI():
    def listing():
        lists=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        print (lists[0])
        print (lists[1])
        print (lists[2])
        print (lists[3])
        print (lists[4])
    
    def oddeven():
        num = int(input("Enter a number : "))
        if ((num%2)==1):
            print ("odd number")
            message= "odd number"
        else:
            print (num,"is Even Number")
            message= "Even Number"
        return message
    
    def marriage():
        Gender = input("Your Gender : ")
        Gender_Age = int(input("Enter the age : "))
        if(Gender=="M"):
            if(Gender_Age <21):
                print("NOT ELIGIBLE")
            else:
                print("ELIGIBLE")
        elif(Gender=="F"):
            if(Gender_Age <18):
                print("NOT ELIGIBLE")
            else:
                print("ELIGIBLE")
                
       ####4.calculate the percentage of your 10th mark####
    def marks():
        Subject1= int(input("Subject1 = ")) #98
        Subject2= int(input("Subject2 = ")) #87
        Subject3= int(input("Subject3 = ")) #95
        Subject4= int(input("Subject4 = ")) #95
        Subject5= int(input("Subject5 = ")) #93
        Total = int(500)
        Obtained = Subject1+Subject2+Subject3+Subject4+Subject5
        print("Obtained = ",Obtained)
        percentage = int(Obtained)/int(Total)*100
        print("percentage :",percentage)
        
        ####5.print area and perimeter of triangle using class and functions####
    def triangle():
        Height= int(input("Height1:")) #32
        Breadth= int(input("Breadth:")) #34
        Area_formula= (Height*Breadth)/2
        print ("Area_formula= (Height*Breadth)/2")
        print ("Area of Triangle : ",Area_formula)
        Height1 = int(input("Height1:")) #2
        Height2 = int(input("Height2:")) #4
        Breadth = int(input("Breadth:")) #4
        Perimeter_formula = Height1+Height2+Breadth
        print ("Perimeter_formula = Height1+Height2+Breadth")
        print ("Perimeter of Triangle : ",Perimeter_formula)