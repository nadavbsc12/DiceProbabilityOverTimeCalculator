import random
# Define a dictionary to hold the Item names and probabilities
items = {
    "2": 0.0277777777777778,
    "3": 0.0555555555555556,
    "4": 0.0833333333333333,
    "5": 0.1111111111111111,
    "6": 0.1388888888888889,
    "7": 0.1666666666666667,
    "8": 0.1388888888888889,
    "9": 0.1111111111111111,
    "10": 0.0833333333333333,
    "11": 0.0555555555555556,
    "12": 0.0277777777777778
}

# Define a function to generate a random item based on the probabilities
def generate_item():
    # Generate a random number between 0 and 1
    rand = random.random()

    # Iterate through the items and check if the random number falls within the probability range
    for item, probability in items.items():
        if rand <= probability:
            return item
        else:
            rand -= probability

# Calculate the probability and number of picks of each item over a specified number of runs
def calculate_probability(runs):
    probabilities = {}
    for item in items:
        count = 0
        for i in range(runs):
            picked_item = generate_item()
            if picked_item == item:
                count += 1
        probability = count / runs
        probabilities[item] = (probability, count, runs)
    return probabilities

# Normalize the probabilities by dividing each probability by the sum of all probabilities
probability_sum = sum(items.values())
for item in items:
    items[item] /= probability_sum

# Get the number of runs from the user
while True:
    try:
        runs = int(input("Amount of runs: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Calculate the probability of picking each item over the specified number of runs
probabilities = calculate_probability(runs)

# Print the results to the console
for item, probability in probabilities.items():
    probability, picks, total_picks = probability
    print(f"Probability of {item}: {format(probability * 100, '.10f')}% ({picks}/{total_picks} picks)")
