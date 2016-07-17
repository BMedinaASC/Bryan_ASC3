from random import *

nameString = input ("What is your name?")
print("Hello", nameString, ", I want to play a game.")

houseString = input("What kind of house would you like to live in?")
countryString = input("What country would you like to live in?")
jobString = input ("What job would you liek to have?")
carString = input("What car would you like to own?")
moneyString = input("How much money do you want to make in a year?")
soString = input("what quality would you like your significant other to have?")
childString = input("How many childern would you like to have?")

houseList = ["Mansion","Apartment","Shack","House"]
moneyList = ["$10,000","$50,000","$100,000","$1,000,000","$600,000",
            "$1,000,000,000"]
jobList = [jobString,"Sanitation Engineer", "Software Engineer", "Stripper", "Electrical Engineer", "Computer Scientist", "Bar Tender", "CEO", "Cashier", "Failed Writer", "Struggling Artist", "Stunt Person", "Prostitute"]
carList = [carString, "Honda Civic","Bugatti Veyron","Mclaren P1","Audi R8",
            "Toyota Corolla","Ferrari 488", "Lamborghini Huracan","Nissan Altima",
            "Saleen S7","Mitsubishi Lancer Evo","Toyota Camry"]
soList = [soString, "Beautiful", "Smart", "Funny", "Quirky", "Weird", "Crazy"]
countryList = [countryString, "France", "Belgium","Latvia","America","Italy",
                "Scandinavia","Mother Russia","England","Japan","China",
                "El Salvador","Brazil","Argentina"]
childList = [childString, "1","2","3"]

house = randrange(len(houseList))
money = randrange(len(moneyList))
job = randrange(len(jobList))
car = randrange(len(carList))
so = randrange(len(soList))
country = randrange(len(countryList))
child = randrange(len(childList))

print("You will live in a", houseList[house])
print("You will make", moneyList[money], "per year!")
print("You will work as a", jobList[job])
print("You will own a", carList[car])
print("Your significant other will be", soList[so])
print("You will live in", countryList[country])
print("You will have", childList[child], "offspring!")

