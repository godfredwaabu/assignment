#6949521
#WAABU GODFRED
#COMPUTER APPLICATION ASSIGNMENT 3
#https://github.com/godfredwaabu/assignment.git
Car =["Ford Mustang","Audi A5","Chevrolet Corvette","Honda Civic",\
      "Toyota Corolla","Toyota Yaris","Toyota Camry","Toyota Rav4",
      "Toyota Highlander","Toyota Fortuner","Ford Mini","Toyota LandCruiser Prado",
      "Toyota Hilux","Toyota Tundra","Toyota Tacoma","Benz C300","Toyota Matrix",\
      "Nissan Pathfinder","Nissan Sentra","Nissan Maxima","Nissan Rogue",\
      "Nissan Patrol","Benz 4matic","Benz SUV",
      "Hyundai Accent","Hyundai Elantra","Hyundai Sonata","Honda Accord","Honda Odyssey",
      "BMW M8","Audi R8","Ford Fiesta","KIA Rio","Dodge Charger","Ford Bronco"]
Models=["2010","2013","2015","2017","2019","2020","2022","2023"]
Price=[18790,20000,33000,57990,150000,252000,308000,599000]
CarModelPrice=[]
print("Welcome to THE CAR MAN SHOP!")

order=input("State the car you would like to buy: ")
if order in Car:
   model=input("Please enter the model of the car you would like to buy: ")
   if model in Models:
     if model=="2010":
      print("The price of the vehicle model selected is GHS",Price[0])
     elif model=="2013":
      print("The price of the vehicle model selected is GHS",Price[1])
     elif model=="2015":
      print("The price of the vehicle model selected is GHS",Price[2])
     elif model=="2017":
      print("The price of the vehicle model selected is GHS",Price[3])
     elif model=="2019":
      print("The price of the vehicle model selected is GHS",Price[4])
     elif model=="2020":
      print("The price of the vehicle model selected is GHS",Price[5])
     elif model=="2022":
      print("The price of the vehicle model selected is GHS",Price[6])
     elif model=="2023":
      print("The price of the vehicle model selected is GHS",Price[7])
   else:
     print("This model of the specified car is currently not available")
else:
 print("This vehicle is not available,please see the receptionist for further assistance")
 
      
    