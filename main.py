import numpy as np
from collections import Counter
import random
# Define a dictionary to hold the Item names and probabilities

random.seed(random.randint(1, 100))
items = [
    ("Hanzo Kabuto", 0.0002),
    ("Hanzo Yori", 0.0002),
    ("Hanzo Haidate", 0.0002),
    ("Hanzo Kote", 0.0002),
    ("Hanzo Kogake", 0.0002),
    ("Hanzo Mempo", 0.0002),
    ("Hanzo Sashimono", 0.0002),
    ("Hattori Kabuto", 0.0002),
    ("Hattori Yori", 0.0002),
    ("Hattori Haidate", 0.0002),
    ("Hattori Kote", 0.0002),
    ("Hattori Kogake", 0.0002),
    ("Hattori Mempo", 0.0002),
    ("Hattori Sashimono", 0.0002),
    ("Golden Warrior", 0.0002),
    ("Musashi Headgear", 0.0002),
    ("Musashi Glare", 0.0002),
    ("Musashi Armor", 0.0002),
    ("Musashi Greaves", 0.0002),
    ("Musashi Gauntlets", 0.0002),
    ("Musashi Boots", 0.0002),
    ("Gozen Headgear", 0.0002),
    ("Gozen Glare", 0.0002),
    ("Gozen Armor", 0.0002),
    ("Gozen Greaves", 0.0002),
    ("Gozen Gauntlets", 0.0002),
    ("Gozen Boots", 0.0002),
    ("Ronin HeadBand", 0.0002),
    ("Ronin Armor", 0.0002),
    ("Ronin Greaves", 0.0002),
    ("Ronin Gauntlets", 0.0002),
    ("Red Ronin HeadBand", 0.0002),
    ("Red Ronin Armor", 0.0002),
    ("Red Ronin Greaves", 0.0002),
    ("Red Ronin Gauntlets", 0.0002),
    ("Hanzo Kabuto", 0.0002),
    ("Hanzo Yori", 0.0002),
    ("Hanzo Haidate", 0.0002),
    ("Hanzo Kote", 0.0002),
    ("Hanzo Kogake", 0.0002),
    ("Hattori Kabuto", 0.0002),
    ("Hattori Yori", 0.0002),
    ("Hattori Haidate", 0.0002),
    ("Hattori Kote", 0.0002),
    ("Hattori Kogake", 0.0002),
    ("Genshin G-Dadao (Select Capsule)", 0.0002),
    ("Genshin S-Dadao (Select Capsule)", 0.0002),
    ("Genshin B-Dadao (Select Capsule)", 0.0002),
    ("Oda G-Shotgun (Select Capsule)", 0.0002),
    ("Oda S-Shotgun (Select Capsule)", 0.0002),
    ("Oda B-Shotgun (Select Capsule)", 0.0002),
    ("Jubei B-Rifle (Select Capsule)", 0.0002),
    ("Jubei S-Rifle (Select Capsule)", 0.0002),
    ("Jubei G-Rifle (Select Capsule)", 0.0002),
    ("Musa G-Bazooka (Select Capsule)", 0.0002),
    ("Musa S-Bazooka (Select Capsule)", 0.0002),
    ("Musa B-Bazooka (Select Capsule)", 0.0002),
    ("Gracious Hair", 0.0155),
    ("Gracious Top", 0.0155),
    ("Noble Top", 0.0155),
    ("Gracious Gloves", 0.0155),
    ("Gracious Boots", 0.0155),
    ("Gold Bottle Cap", 0.0155),
    ("Stitches and Scars", 0.0155),
    ("Energy Can", 0.0155),
    ("Energy Hands", 0.0155),
    ("Plain Skinny Legs", 0.0155),
    ("Energy Boots", 0.0155),
    ("Samurai Hair", 0.0155),
    ("Hip Hop Tee", 0.0155),
    ("Blue Shorts", 0.0155),
    ("Powerful Hands", 0.0155),
    ("Orange Star Boots", 0.0155),
    ("Blue Jacket", 0.0155),
    ("White Line Socks", 0.0155),
    ("Dj Khan Jeans", 0.0155),
    ("Tecktonik Gloves", 0.0155),
    ("Tecktonik Shoes", 0.0155),
    ("DJ Khan Abs", 0.0155),
    ("DJ Khan Headset", 0.0155),
    ("Short Brown Hair", 0.0155),
    ("Blue Basic Top", 0.0155),
    ("Blue Basic Pants", 0.0155),
    ("Fitted Gloves", 0.0155),
    ("Blue Basic Shoes", 0.0145),
    ("Sacred Hair", 0.0145),
    ("Sacred Face", 0.0145),
    ("Sophitia Negligee", 0.0145),
    ("Sacred Bracelets", 0.0145),
    ("Sophitia Heels", 0.0145),
    ("Sophitia Legs", 0.0145),
    ("Pink Wing V-Cut", 0.0145),
    ("Belted Thigh Highs", 0.0145),
    ("Stunning Hands", 0.0145),
    ("Triple Buckle Boots", 0.0145),
    ("Steel Hammer (A)", 0.0145),
    ("Steel Hammer (B)", 0.0145),
    ("Steel Hammer (C)", 0.0145),
    ("Mad Wrench (A)", 0.0145),
    ("Mad Wrench (B)", 0.0145),
    ("Mad Wrench (C)", 0.0145),
    ("Sherlock (A)", 0.0145),
    ("Sherlock (B)", 0.0145),
    ("Sherlock (C)", 0.0145),
    ("KW-79 (A)", 0.0145),
    ("KW-79 (B)", 0.0145),
    ("KW-79 (C)", 0.0145),
    ("Venom (A)", 0.0145),
    ("Venom (B)", 0.0145),
    ("Venom (C)", 0.0145),
    ("Venom (D)", 0.0145),
    ("Firefly (A)", 0.0145),
    ("Firefly (B)", 0.0145),
    ("Firefly (C)", 0.0145),
    ("Pocket Rocket (A)", 0.0145),
    ("Pocket Rocket (B)", 0.0145),
    ("Pocket Rocket (C)", 0.0145),
    ("Pulse (A)", 0.0145),
    ("Pulse (B)", 0.0145),
    ("Pulse (C)", 0.0145),
    ("500 MP Coin", 0.0125),
    ("1,000 MP Coin", 0.01),
    ("1,500 MP Coin", 0.008),
    ("2,000 MP Coin", 0.007),
    ("2,500 MP Coin", 0.005),
    ("3,500 MP Coin", 0.0041),
    ("4,000 MP Coin", 0.0022),
    ("4,500 MP Coin", 0.0004),
    ("5,000 MP Coin", 0.0003)
    ]


# Check if the probabilities sum to 1 (or very close to 1 due to floating-point inaccuracies)
total_probability = sum([prob for _, prob in items])
if not 0.99 <= total_probability <= 1.01:
    total_probability = sum([prob for _, prob in items])
    if total_probability != 1:
        raise ValueError(f"The probabilities do not sum up to 1! the sum is {total_probability}")


def generate_item_np():
    item_names = [item[0] for item in items]
    item_probs = [item[1] for item in items]

    total_probability = sum(item_probs)
    normalized_probs = [prob / total_probability for prob in item_probs]

    return np.random.choice(item_names, p=normalized_probs)


def calculate_probability_np(runs):
    picked_items = [generate_item_np() for _ in range(runs)]
    observed_counts = Counter(picked_items)
    probabilities = {item: (count / runs, count, runs) for item, count in observed_counts.items()}
    return probabilities

# For stopping when a certain item is picked
def calculate_probability_until_item_np(target_item):
    run_count = 0
    while True:
        run_count += 1
        picked_item = generate_item_np()
        if picked_item == target_item:
            break
    return run_count

# Getting the number of runs (your code remains unchanged here)
while True:
    try:
        runs = int(input("Amount of runs: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Calculate probabilities and print them
probabilities_np = calculate_probability_np(runs)
for item, data in probabilities_np.items():
    observed_prob, picks, total_picks = data
    print(f"Probability of {item}: {observed_prob * 100:.4f}% ({picks}/{total_picks} picks)")

# Finding runs needed to get a specific item
target = "Golden Warrior"
max_spins = 1000
temp_list = []
for _ in range(max_spins):
    runs_needed_np = calculate_probability_until_item_np(target)
    temp_list.append(runs_needed_np)

final_result = sum(temp_list) / len(temp_list)
print(f"It took AVG {final_result} (Based on 1000) runs to get {target}.")