number_of_lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
helmets_broken = number_of_lost_fights // 2
sword_broken = number_of_lost_fights // 3
shield_broken = number_of_lost_fights // 6
armor_broken = shield_broken // 2
expenses = helmets_broken * helmet_price + \
    sword_broken * sword_price + \
    shield_broken * shield_price + \
    armor_broken * armor_price
print(f"Gladiator expenses: {expenses:.2f} aureus")