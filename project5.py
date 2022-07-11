class Game:
############## Constructor For Main Game
    def __init__(self):
        print('WelCome To The Main Game ,If You Wanna Close The Main Game Press[x]')
        print("There are Four Games Here...,Choose your Game From Our collection ")
        print('Press[1]: This Game Print Number Is Even Or Odd')
        print("Press[2]: This Game Give Groups Number And Print Groups Even Numbers , Print Groups Odd Numbers  ")
        print("press[3]: This Game Print Any Character ")
        print("press[4]: This Game Print Multiplication Table To This Number ")
        self.choices()
############ Choices
    def choices(self):
        while True:
          choose=input("Enter You Choice 1,2,3,4 :")
          if choose.lower()=='x':
             print("Closing All Games, Thanks For every Thing !!!!")
             break
          try:
              choose=int(choose)
              if choose==1:
                  self.game1()
              elif choose==2:
                  self.game2()
              elif choose==3:
                  self.game3()
              elif choose==4:
                  self.game4()
              else:  print("Please Choose Between 1,2 Or 3 ! ")
          except ValueError:
              print("Please Enter A Valid Number")
######################### (Game 1)
    def game1(self):
      print("\"WelCome To Even_Odd_Game,Will Be Print This Number Odd Or Even \"")
      print("If You Wanna To Close This Game Press[x]")
      while True:
        n1=input("Enter The Number : ")
        if n1.lower()=='x':
           print("Now Will Be Closing Game ,Thanks....")
           break
        n1=int(n1)
        if n1%2==0:print("Even Number !")
        else:print("Odd Number ! ")
###################### (Game 2  )
    def game2(self):
     print("\t\t\'Welcome To Game Numbers Group,Will Be Print The All Even Number And All Odd Number\' ")
     print("\t\t\'If You Wanna Eixting Game Press [x]\'")
     even=0
     odd=0
     while True:
        num=input('Enter The Number :')
        if num.lower()=='x':
          print('Closing Game,Thanks...')
          break
        try:
          num=int(num)
          if num %2==0:
             print('\"',num,'\"','Is Even Number !')
             even+=1
          else:
           print('\"',num,'\"','Is Odd Number !')
           odd+=1
        except ValueError:
         print("You Entered An Invalid Number")
     print("The All Numbers Even Are : ", even)
     print('The All Numbers Odd Are : ', odd)


#####################(Game 3)
    def game3(self):
     print("WelCome To This Game, will Be Print Any  Character ")
     print("If you Wnnna Close The Game Press[x]")
     while True:
       char=input("Enter The Character : ")
       if char.lower()=='x':
         print("Closing Game, Sorry")
         break
       for b in range(1,8):
         for n in range(b,8):
           print(char,end='\t')
         print('\n')
#####################(Game 4)
    def game4(self):
     print('\"WelCome IN Multiplication Table, Will Be Print Multiplication To This Number \" ')
     n1=int(input("Enter Integer Number : "))
     for b in range(2,n1+1):#2,7
       print()
       for d in range(1,11):#1,10
         print(b ,'X' , d, '= ',b*d, end=' \t ')
     print()


x=Game()




