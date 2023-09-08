import random

counter = 0
with open("solution/validation_input.csv", encoding="utf-8") as file:
    for row in file:
        if row[:3] == "die" or random.uniform(0, 1) < 0.1:
            print(f'"{row.strip()}",')
            counter += 1
            if counter >= 100:
                break