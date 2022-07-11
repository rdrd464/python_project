class Game:
    #####################################################
    #### Constructor For Main Game
    def __init__(self):
       print("Welcome In Full Game.....")
       print("Choose your Game From Our collection ")
       print('Press[1] : Play  Even_Odd_Game ')
       print('Press[2] : Play Sum_Average_Game')
       print('Press[3] : Play Multiplication_Table_Game')
       print("If You Wanna Close The All Game Enter \"X\"")
       self.Choices()
     #####################################################
     #### Available Choices
    def Choices(self):
        while True:
         user_choice=input("Enter Your Choice : ")
         if user_choice=='x' or 'X':
             print("Closing All Game...")
             print("Thanks.........")
             break
         try:
          user_choice=int(user_choice)
          if user_choice==1:
            self.Even_Odd_Game()
          elif user_choice==2:
            self.Sum_Average_Game()
          elif user_choice==3:
            self.Multiplication_Table_Game()
          else:
            print("Please Choose Between 1,2 Or 3 ! ")
         except ValueError:
           print('Please Enter A Valid Number ')

   #########################################################
    #### Evan-Odd-Game Code
    def Even_Odd_Game(self):
     print("Welcome In The Even-Odd Game")
     print("Please Enter A number....and I Will Tell You If it Odd Or Even")
     print("If You Wanna Close The Game Enter \"X\"")

     while True:
        number=input("Enter The Number :")
        if number=='x' or 'X':
            print("Closing Game ! ")
            print("Thanks....")
            break
        try:
          number=int(number)
          if number % 2==0:
             print("Even Number ! ")
          else:
            print("Odd Number ! ")
        except ValueError:
            print("Please Enter A Valid Number ")
     ###########################################################
     ### Sum Average Gam Code
    def Sum_Average_Game(self):
        print("This Game Will Take Several Numbers And Print The Average Of Them ")
        count = int(input("How Many Numbers Would You Like To sum : "))
        count_loop=0
        summ=0
        while count_loop<count:
           number=int(input("Enter The Number : "))
           summ+=number
           count_loop+=1

        print("Sum Of All Numbers = ",summ)
        print("Average Of All Numbers = ",summ/count)
     ###########################################################
     ### Multiplication_Table_Game Code
    def Multiplication_Table_Game(self):
        print("\t\tWelcome In Multiplication App ")
        print("\t\t------------------------------")
        print("Please enter The First Number And Last Number Of The Multiplication Table ! ")
        start=int(input("Enter The First Number Of The Multiplication Table : "))
        end=int(input("Enter The Last  Number Of The Multiplication Table : "))
        for x in range(start,end+1):
            for y in range(1,11):
                print(x , ' X ' ,y ,'=' ,x*y)
            print("--------------------------")
### Create Object  From The Class
game1=Game()

'''
Steps For Write Project:

1-Create Class
2-Methods-pass
3-Create Object From The Class
4-Copy and Write past projects
5-Add Code Constructor
6-Create Choices Method 
7-Handing Exception (! Character ,! 1 2 3)
8-Connect Methods ----------Choices

'''