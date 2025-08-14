# My cool and simple python script which reads names from a file, generates username combinations using known policies, writes the output to a file! 

# WARNING: YOU MUST INPUT FIRST NAME AND LAST NAME(AT LEAST, also takes a middle name if any!)!
def generate_combinations(first, last, middle=None):
    # Basic direct combos known to be used by companies
    combos = [
        f"{first}{last}",
        f"{first}.{last}",
        f"{first}_{last}",
        f"{first}-{last}",
        f"{first[0]}{last}",
        f"{first}{last[0]}",
        f"{last}{first}",
        f"{last}.{first}",
        f"{last}_{first}",
        f"{last}-{first}",
        f"{last[0]}{first}",
        f"{first[0]}.{last}",
        f"{first}.{last[0]}",
        f"{first}{last[:4]}",           
        f"{last[:4]}{first}",           
        f"{first[:2]}{last[:2]}",       
        f"{first}{last}1",              
        f"{first[0]}{last}23",          
    ]
    # Email combos, change from example to wtv your target uses
    combos.extend([
        f"{first}.{last}@example.com",
        f"{first[0]}{last}@example.com",
        f"{last}.{first}@example.com" 
    ])
    # Add middle name and initials, if any
    if middle:
        combos.extend([
            f"{first[0]}{middle[0]}{last}",
            f"{first}{middle[0]}{last}",
            f"{first}.{middle[0]}.{last}",
            f"{first[0]}.{middle[0]}.{last}",
            f"{first}{middle}{last}",       
            f"{first[0]}{middle[0]}{last[0]}"
        ])
    # lower for output
    return [c.lower() for c in combos]

# Parse the name into parts
def parse_name(name):
    parts = name.split()
    first = parts[0]
    last = parts[-1] if len(parts) > 1 else ''
    middle = parts[1] if len(parts) > 2 else None
    return first, last, middle

if __name__ == "__main__":
    path = input("Enter the path of the users file: ")

    # Reading all names
    with open(path, 'r') as f:
        names = [line.strip() for line in f if line.strip()]

    # Gen and write combinations for each name
    with open('combinedTargets.txt', 'w') as f:
        for name in names:
            first, last, middle = parse_name(name)
            combos = generate_combinations(first, last, middle)
            for combo in combos:
                f.write(combo + '\n')
