"""
CP1404 Practical
my Guitars
Author: chenzhuangzhuang
"""

class Guitar:
    def __init__(self, name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost

    def __lt__(self, other):
        return self.year < other.year


guitars = []

with open("guitars.csv") as f:
    for line in f:
        name, year, cost = line.strip().split(",")
        year = int(year)
        cost = float(cost)
        guitars.append(Guitar(name, year, cost))

for guitar in guitars:
    print(f"{guitar.name} ({guitar.year}): ${guitar.cost:.2f}")
print()

guitars.sort()

for guitar in guitars:
    print(f"{guitar.name} ({guitar.year}): ${guitar.cost:.2f}")

name = input("Enter the name of the guitar: ")
while name:
    year = int(input("Enter the year the guitar was made: "))
    cost = float(input("Enter the cost of the guitar: "))
    guitars.append(Guitar(name, year, cost))
    name = input("Enter the name of the guitar: ")
else:
    print("Finished entering guitars.")

with open("guitars.csv", "w") as f:
    for guitar in guitars:
        f.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")