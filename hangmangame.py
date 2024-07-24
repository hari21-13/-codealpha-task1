import random
_=['apple','bag','star']
z=0
randomWord=random.choice(_)
randomString=[]
for i in range(len(randomWord)):
    randomString.append('*')
print(randomString)
num=int(input('Enter a number between 5 to 10- '))
while True:
    if z==num:
       print("You Lost!")
       break
    else:
      letter=input("Enter a letter- ")
      z+=1
      for i in range(len(randomString)):
        if letter==randomWord[i]:
           randomString[i]=letter
      print(randomString)
      if '*' not in randomString:
           print("You Win!")
           break