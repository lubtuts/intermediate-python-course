import random


def main():
  die_rolls = 2
  dice_sum = 0
  for i in range(die_rolls):
    roll = random.randint(1,6)
    print(f'You rolled a {roll}')
    dice_sum += roll
  print(f"You have rolled a total of {dice_sum}")

if __name__== "__main__":
  main()