bottles = int(input())

detergent = bottles * 750
count = input()
days = 0
dishes = 0
pots = 0
detergent_used = 0

while count != "End":
    count = int(count)
    days += 1
    if days % 3 == 0:
        pots += count
        detergent_used += count * 15
    else:
        dishes += count
        detergent_used += count * 5

    if detergent_used > detergent:
         break


    count = input()

if detergent_used < detergent:
    print("Detergent was enough!")
    print(f"{dishes} dishes and {pots} pots were washed.")
    print(f"Leftover detergent {detergent - detergent_used} ml.")
else:
    print(f"Not enough detergent, {detergent_used - detergent} ml. more necessary!")

