# // 1. Write a function named printLeapYears
# // 2. It should take two integer inputs, a start year and an end year
# // 3. It should print to the console, in order, every "leap year" in that range.
# // 4. A year which is divisible by 4 but not divisible by 100 will be considered a "leap year"
# // 5. A year which is divisible by 400 is also considered a "leap year".

def printLeapYears(start, end):
    for year in range(start, end):
        if (year%4==0 and year%100!=0):
            print(year)
            continue
        elif year%400==0:
            print(year)
            continue
        else:
            continue

        
test = 1

#dici a Sabrina

print(test)
print(type(test))