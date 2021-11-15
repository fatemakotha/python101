#Method_1

def sum_thrice(x, y, z):

     sum = x + y + z
  
     if x == y == z:
      sum = sum * 3
     return sum

print(sum_thrice(1, 2, 3))
print(sum_thrice(3, 3, 3))

#Method_2

x = int(input())
y = int(input())
z = int(input())

sum = x+y+z
ex = (x+y+z)*3
if x==y==x:
    print(ex)
else:
    print(sum)
