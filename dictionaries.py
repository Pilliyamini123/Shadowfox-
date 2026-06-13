#1.list of friends    
friends=["yamini","lalitha","varshitha","ammulu","sreeja"]
#list of friends and their length
friends_length=[]
for name in friends:
    friends_length.append((name,len(name)))
print("friends list:")
print(friends)
print("name and length of friends:");
print(friends_length)
#This program creates a list of my friends' names and then creates a list of tuples. 
# Each tuple contains a friend's name and the length of that name. 
# The len() function is used to calculate the number of characters in each name, and the result is displayed in the format (name, length).   
#2.trip expenses
your_expenses={
 "Hotel":1200,
 "Food":800,
 "Transportation":500,
 "Attractions":300,
"Miscellaneous":200
} 
your_partner={ 
"Hotel":1000,
"Food":900,
"Transportation":600,
"Attractions":400,
"Miscellaneous":150
}
#total expenses
total_your_expenses=sum(your_expenses.values())
total_partner_expenses=sum(your_partner.values())
print("total your expenses:",total_your_expenses)
print("total your partner expenses:",total_partner_expenses)
#who spend more
if(total_your_expenses>total_your_expenses):
    print("you spend more money than your partner")
else:
    print("your partner spend more money than you")
#find maximum difference
max_diff=0
max_category=""
for category in your_expenses:
    diff=abs(your_expenses[category]-your_partner[category])
    if diff>max_diff:
        max_diff=diff
        max_category=category
print("maximum difference category:",max_category)
print("max difference amount:",max_diff)
#In a dictionary, category is the key obtained from the loop. 
# #To access its corresponding amount, we use dictionary[key], so your_expenses[category] returns the value associated with that category.
