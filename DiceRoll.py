#DiceRoll.py
#Name:Ryan Meegan
#Date:Mar 2 2025
#Assignment:Dice Roll
import random

def main():
  #Create an empty list with possible roll values
  rolls = [0,0,0,0,0,0,0,0,0,0,0]
  #Create two dice values ranging from 1 - 6 each
  for r in range(10000):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2
    rolls[total - 2] += 1

  #find the sum total of the two dice
  
  #print statictics for dice rolls
  dice = 2
  for count in rolls:
    percentage = (count / 10000) * 100
    round(percentage, 2)
    print(dice, ":", count, "(", round(percentage, 2), "% )")
    dice = dice + 1


if __name__ == '__main__':
  main()
