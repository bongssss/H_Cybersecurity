import csv

with open("parsed_data.csv", "r" ) as file:
    reader = csv.DictReader(file)
    alice, bob, charlie =0, 0, 0
    for row in reader:
        name = row["Name"]
        if name =="Alice Example":
            alice+=1
        elif name == "Bob Test":
            bob += 1
        elif name == "Charlie Hacker":
            charlie += 1
                        
print(f"Alice: {alice}")
print(f"Bob: {bob} ")
print(f"CHarlie: {charlie}")

            
        
    
       