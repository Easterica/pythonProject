open_tabs = int(input())
salary = int(input())
salary_is_lost = False

for i in range(1, open_tabs + 1):
    if salary <= 0:
        salary_is_lost = True
        break
    website = input()


    if website == "Facebook":
        salary -= 150
    elif website == "Instagram":
        salary -= 100
    elif website == "Reddit":
        salary -= 50
if salary_is_lost:
    print("You have lost your salary.")
else:
    print(salary)
