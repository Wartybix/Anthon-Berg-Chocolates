import random
import os.path

CHOCOLATE_DIR = os.path.dirname(__file__) #Directory of chocolate python file

EATEN_FILE = CHOCOLATE_DIR + "/eaten.txt"

CHOCS = {"Malibu", "Cointreau", "Southern Comfort", "Vodka", "Remy Martin",
         "Matusalem", "Kahlua", "Famous Grouse"}

eaten = set()

file_write_mode = "a" #Set to append to eaten file by default

if os.path.isfile(EATEN_FILE):
    with open(EATEN_FILE) as file:
        for line in file:
            eaten.add(line.rstrip())

print(f"Eaten: {eaten}")
        
remaining = list(CHOCS - eaten)
if not remaining:
    file_write_mode = "w" #Now set to overwrite eaten file
    remaining = list(CHOCS)

print(f"\nRemaining: {remaining}")

chosen_choc = random.choice(remaining)
print(f"\nGenerated chocolate: {chosen_choc} 😋")

file = open(EATEN_FILE, file_write_mode)
file.write(chosen_choc + "\n")
file.close()
