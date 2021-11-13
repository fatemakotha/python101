#Write a Python program to test whether a number is within 100 of 1000 or 2000.
def close_to_thousand(n):
    return((abs(1000-n) <= 100) or (abs(2000-n) <= 100))
print(close_to_thousand(1000))# when n=1000
print(close_to_thousand(900))# when n=900
print(close_to_thousand(800))# when n=800
print(close_to_thousand(2200))# when n=2200


