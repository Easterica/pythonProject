list_of_people = list(map(int, input().split(", ")))
min_wealth = int(input())
wealthiest = max(list_of_people)
wealth_needed = 0
for i in range(len((list_of_people))):
    if list_of_people[i] < min_wealth:
        wealth_needed = min_wealth - list_of_people[i]
        list_of_people[i] += wealth_needed

    wealthiest -= wealth_needed
