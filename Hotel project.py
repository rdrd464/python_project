class vacation:
    def __init__(self):

        print("WelCome To This Program For Calculate your Vacation Costs")
        print("There are three or four things to calculate the cost")
        self.trip_cost()
        '''
        print("The First One Is Hotel Cost ")
        self.hotel_cost()
        print("\t\t------------------------\t\t")
        print("The Second One Is Plane Ride Cost ")
        self.plane_ride_cost()
        print("\t\t------------------------\t\t")
        print("The Third One Is Rental Car Cost ")
        self.rental_car_cost()
        print("\t\t------------------------\t\t")
        print("Finally Print Trip Cost : ")
        t4=self.trip_cost()
        '''
    def hotel_cost(self):
        print("The First One Is Hotel Cost ")
        nights=int(input('How Many nights Stay :'))
        return 140*nights
    def plane_ride_cost(self):
      print("\t\t------------------------\t\t")
      print("The Second One Is Plane Ride Cost ")
      while True:
       city=input("What The City :")
       if city=="Charlotte":
         return 183
         break
       elif city=="Tampa":
         return 220
         break
       elif city=="Pittsburgh":
         return 222
         break
       elif city=="Los Angeles":
         return 475
         break
       else:
           print("Your Enter City Don,t Found Please Write {\"Charlotte\",\"Pittsburgh\",\"Los Angeles\"} ")
    def rental_car_cost(self):
      print("\t\t------------------------\t\t")
      print("The Third One Is Rental Car Cost ")
      while True:
        days=int(input("Enter The Days :"))
        costEveryday= 40 * days
        if days>=7:
         costEveryday-=50
         break
        elif  days>=3:
         costEveryday-=20
         break
        else:
          print("Sorry Try Agine")
        return costEveryday
    def trip_cost(self):
        spendingMoney = int(input("What Else Did You Spend Money?"))
        return  print(spendingMoney)
b=vacation()





