#Initialize the list of Justice League members
justice_league=["Superman","Batman","Wonder Women","Flash","Aquaman","Green Lantern"]
#1.calculate the length of the list
print("The length of the list is:",len(justice_league))
#2.Add a new members to the list
justice_league.append("Batgirl")
print("The updated list is:",justice_league)
justice_league.append("Nightwing")
print("The updated list is:",justice_league)
#3.move Wonder Women to the beginning of the list
justice_league.remove("Wonder Women")
justice_league.insert(0, "Wonder Women")
print("The updated list is:",justice_league)
#4.move green lantern between aquaman and flash
justice_league.remove("Green Lantern")
justice_league.insert(justice_league.index("Aquaman")+1, "Green Lantern")
print("The updated list is:",justice_league)
#5.replace entire list with new members
justice_league=["Cyborg","Shazam","Hawkgirl","Martian Manhunter","Green Arrow"]
print("The updated list is:",justice_league)
#6.sort the list in alphabetical order
justice_league.sort()
print("The sorted list is:",justice_league)
#Bonus:leader of the Justice League
print("The leader of the Justice League is:",justice_league[0])