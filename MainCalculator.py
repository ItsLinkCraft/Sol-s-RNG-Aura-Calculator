import math

print("Sol's RNG Aura Rarity Calculator")
print("Currently only works for Era 6. If outdated, ping @ItsLinkCraft in the discord server.")
print("This system only uses decimals. For example, natural rarity of 1/8 would be 0.125.")
print("If the sum equals a 1 it means you cannot roll that aura[for normal rolls just type n for both grav and 2x bonus]")

# Initialize base luck, luck buffs, and aura rarity
base = 1.0
lb = float(input("Enter your luck buffs added together [100% = +1 luck]: "))
ayw = float(input("Enter the aura rarity: "))

# Ask about Gravitational Device usage
grav = input("Are you using Gravitational Device? ").lower() in ['yes', 'y', 'true']

# Apply gravitational device multiplier (6x)
if grav:
    base *= 6
    lb *= 6

# Ask about Base Bonus 2x Luck usage
b2 = input("Are you using the Base Bonus 2x Luck? [answer no if you said yes to the grav gauntlet] ").lower() in ['yes', 'y', 'true']

# Apply Base Bonus 2x Luck multiplier (2x)
if b2:
    base *= 2
    lb *= 2

# Calculate aura value
aura_value = (base + lb) * ayw

# Set minimum and maximum limits for aura rarity
minn = 0.000000000000001
maxn = 1

# Ensure aura_value is within the specified range
result = max(minn, min(aura_value, maxn))

# hope and pray to god it works
print("Aura Rarity Calculation Result:", result)
input()
