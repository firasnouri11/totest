import random
from collections import Counter

def roll_dice(num_rolls: int, sides: int = 6) -> list[int]:
    """Simulate rolling a die multiple times."""
    return [random.randint(1, sides) for _ in range(num_rolls)]

def analyze_rolls(rolls: list[int]) -> dict[int, int]:
    """Count the frequency of each outcome."""
    return dict(Counter(rolls))

def main():
    num_rolls = 100
    rolls = roll_dice(num_rolls)

    frequencies = analyze_rolls(rolls)
    average = sum(rolls) / len(rolls)

    print(f"Rolled the die {num_rolls} times.")
    print(f"Average roll value: {average:.2f}")
    print("Frequencies:")
    for value in sorted(frequencies):
        print(f"  {value}: {frequencies[value]}")

if __name__ == "__main__":
    main()
