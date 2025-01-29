import random

def main():
    total_jenga_dice = 100
    roll_d6s(total_jenga_dice)

def roll_d6s(total_dice):
    rounds = 0
    while total_dice > 0:
        rounds += 1
        print(f"Round {rounds}: Rolling {total_dice}")

        rolled_results = [random.randint(1,6) for _ in range(total_dice)]
        ones_count = rolled_results.count(1)
 
        print(f"Removing {ones_count} chances")

        total_dice -= ones_count
        print(f"Chances left: {total_dice}\n")

    print(f"Game Over after {rounds} rounds")

    
if __name__ == "__main__":
    main()
