import random
def play():
  global user
  global computer
  user = input("What is your choice? 'r' for rock, 'p' for paper, 's' for scissors ")
  computer = random.choice(['r','p','s'])
  if user == computer:
    return "tie game "
  if win(user,computer):
    return "you win"
  return "you lost "
    
def win(user,computer):
  if (user == 'r' and computer == 's') or (user == 'p' and computer == 'r') or (user == 's' and computer == 'p'):
    return True 

print(play())
  