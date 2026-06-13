#1.BMI Calculator
height=float(input("enter height in meters:"))
weight=float(input("enter weight in kilograms:"))
BMI=(weight/(height**2))
print("BMI is",BMI)
if BMI>=30:
    print("Obesity")
elif BMI>=25:
    print("Overweight")
elif BMI>=18.5:
    print("Normal weight")
else:
    print("Underweight")
#2.which country a city belongs to
Australia=["Sydney","Melbourne","Brisbane","Perth"]
UAE=["Dubai","Abu Dhabi","Sharjah","Ajman"]
India=["Mumbai","Bangalore","Chennai","Delhi"]
city=input("enter the name of the city:")
if city in Australia:
    print(city,"is in Australia")
elif city in UAE:
    print(city,"is in UAE")
elif city in India:
    print(city,"is in India")
else:
    print("City not found")
#3.check whether 2 cities belong to the same country or not
Australia=["Sydney","Melbourne","Brisbane","Perth"]
UAE=["Dubai","Abu Dhabi","Sharjah","Ajman"]
India=["Mumbai","Bangalore","Chennai","Delhi"]
city1=input("enter the name of the first city:")
city2=input("enter the name of the second city:") 
if (city1 in Australia and city2 in Australia):
    print(city1,"and",city2,"belong to the same country: Australia")    
elif (city1 in UAE and city2 in UAE):
    print(city1,"and",city2,"belong to the same country: UAE") 
elif (city1 in India and city2 in India):
    print(city1,"and",city2,"belong to the same country: India")
else:
    print("The cities belong to different countries")
