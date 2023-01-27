print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

dir = input('You\'re at a crossroad. Where do you want to go? Type "left" or "right" ').lower()

if dir == "left":
  wait_or_swim = input('You come to a lake. There\'s an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. ').lower()
else:
  print("You've fallen into a hole. Game over.")

if wait_or_swim == "wait":
  door = input("You arrived at the island unharmed. There's a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ").lower()
else:
  print("You've been attacked by an angry trout. Game over.")

if door == "red":
  print("You've been burned alive. Game over.")
elif door == "yellow":
  print("You won!")
elif door == "blue":
  print("You've been eaten by beasts. Game over.")
else:
  print("Game over.")
