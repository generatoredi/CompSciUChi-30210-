# This file is intentionally empty
#
# Feel free to add your code from the "Simple practice: Loops" section
# of the tutorial in this file.

# check leap year
# write your code here, and check if 2024 is a leap year
year=2004
leap=False

if year%4==0 and year%100!=0:
 leap=True
elif year%400==0:
 leap=True
else:
  leap=False

print(leap)




# rewrite to a while
n = 1
while n <= 10:
    if (n % 2) == 1:
        print(n, "is odd")
    else:
        print(n, "is even")
    n += 1

      
