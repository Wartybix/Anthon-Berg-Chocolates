import random
import os.path

EATEN_FILE = "eaten.txt"

CHOCS = {"Malibu", "Cointreau", "Southern Comfort", "Vodka", "Remy Martin",
         "Matusalem", "Drambuie", "Famous Grouse"}

eaten = set()

chocs_reset = False

if os.path.isfile(EATEN_FILE):
    with open(EATEN_FILE) as file:
        for line in file:
            eaten.add(line.rstrip())

print(f"Eaten: {eaten}")
        
remaining = list(CHOCS - eaten)
if not remaining:
    chocs_reset = True
    remaining = list(CHOCS)

print(f"\nRemaining: {remaining}")

chosen_choc = random.choice(remaining)
print(f"\nGenerated chocolate: {chosen_choc} 😋")

if chocs_reset:
    file_write_mode = "w"
else:
    file_write_mode = "a"

file = open(EATEN_FILE, file_write_mode)
file.write(chosen_choc + "\n")
file.close()
