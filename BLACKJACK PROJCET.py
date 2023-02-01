logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
import random
interest=int(input("Do you want to play a game of Blackjack? Type '1' or '0' :"))
print(logo)
digits_list= [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
display=[]
digit1=random.choice(digits_list)
digit2=random.choice(digits_list)
display=[digit1,digit2]
your_total=int(digit1+digit2)
print(f"Your card's:{display},current score:{your_total}")
computer1 = random.choice(digits_list)
print(f"computer's first card score:{computer1}")
y=1
wish=int(input("Type '1' to ask another card, or '0' to pass:"))
print(wish)

 
if wish>0:
  digit3=random.choice(digits_list)
  display1=[digit1,digit2,digit3]
  your_total=int(digit1+digit2+digit3)
  print(f"Your cards:{display1},current score:{your_total}")
  if your_total>21:
    print("You lose")
  
  wish=int(input("Type '1' to ask another card, or '0' to pass:"))
  if wish>0:
    digit4=random.choice(digits_list)
    display2=[digit1,digit2,digit3,digit4]
    your_total=int(digit1+digit2+digit3+digit4)
    print(f"Your cards:{display2},current score:{your_total}")
    
  def Your_total():
    if your_total>21:
      print('You lose')
      return False
    else:
      return True
    Your_total()
else:
  def Your_total():
    if your_total<21:
      return True
    
 
 
while Your_total() :
  print(f"computer's first card score:{computer1}")
  computer2 = random.choice(digits_list)
  comp_cards1=[computer1,computer2]
  computer_total=int(computer1+computer2)
  print(f"computer's final cards:{comp_cards1},final score:{computer_total}")
   
  
  if computer_total>your_total:
    print("computer won")
  elif computer_total==your_total:
    print("It's is a draw")
  elif computer_total<(your_total):
    computer3 = random.choice(digits_list)
    comp_cards1=[computer1,computer2,computer3]
    computer_total=int(computer1+computer2+computer3)
    print(f"computer's final cards:{comp_cards1},final score:{computer_total}")
  else:
    computer4 = random.choice(digits_list)
    comp_cards1=[computer1,computer2,computer3,computer4]
    computer_total=int(computer1+computer2+computer3+computer4)
    print(f"computer's final cards:{comp_cards1},final score:{computer_total}")
      
  if computer_total>21:     
    print("You win")
  elif your_total>computer_total:
   print("You win")
  elif your_total==computer_total:
    print("It's a draw")
  elif your_total>computer_total:
    print("You win")
  else:
    print("computer won")
  break