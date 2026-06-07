#rolling a sixsided die multiple times(atleast 20)
import random
count_6=0
count_1=0
two_6_in_row=0
previous=0
for i in range(20):
    roll=random.randint(1,6)
    print("roll",i+1,":",roll)
    if roll==6:
        count_6+=1
    if roll==6 and previous==6:
        two_6_in_row+=1
        previous=roll 
    if roll==1:
        count_1+=1
print("Number of 6s rolled:", count_6)
print("Number of 1s rolled:", count_1)
print("Number of times two 6s appeared in a row:", two_6_in_row)
#"I used a for loop to simulate rolling a die multiple times. I counted the occurrences of 1 and 6, and also checked whether two consecutive rolls were both 6."
#2.to complete 100 jumping jacks
total_jumping_jacks=100
for completed in range(10,101,10):
    print("\nyor completed",completed,"jumping jacks")
    remaining=total_jumping_jacks-completed
    print("remaining jumping jacks are:",remaining)
    if(completed==100):
        print("congratulations you finished 100 jumping jacks!")
        break
    tired=input("are you tired:yes/no?")
    if tired.lower()=="yes" or tired.lower()== "y":
        skip=input("do you want to skip remaining jumps:yes/no?")
        if skip.lower()=="yes" or skip.lower()=="y":
            print("you completes total of",completed,"jumping jacks")
            break
        else:
            print("keep going")
#"I used a for loop to simulate sets of 10 jumping jacks. After each set, the program asks if the user is tired. Depending on the response, it either continues, stops early using break, or congratulates the user after completing all 100 jumping jacks."

