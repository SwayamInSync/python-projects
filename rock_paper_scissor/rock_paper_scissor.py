import random

r = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

p = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

s = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choice=int(input("1. Rock 2. Paper 3. Scissor"))
group=[r,p,s]
print("you choosen\n")
print(group[choice-1])
c=random.randint(1,3)
print("computer chosen")
print(group[c-1])
if(choice==1 and c==3):
  print("loose")
elif(choice==1 and c==1):
  print("tie")
elif(choice==1 and c==2):
  print("win")
elif(choice==2 and c==1):
  print("win")
elif(choice==2 and c==2):
  print("tie")
elif(choice==2 and c==3):
  print("loose")
elif(choice==3 and c==1):
  print("loose")
elif(choice==3 and c==3):
  print("tie")
else:
  print("loose")
