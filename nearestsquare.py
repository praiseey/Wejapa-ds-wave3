#Nearest Square
#Write a while loop that finds the largest square number less than an integerlimit and stores it in a variable nearest_square. A square number is the product of an integer multiplied by itself, for example 36 is a square number because it equals 6*6.

#For example, if limit is 40, your code should set the nearest_square to 36.

limit = 40

# write your while loop here
squares = []
count = 1
while count < 40:
    square_root = count ** 0.5
    if square_root % 1 == 0:
        squares.append(count)
    count += 1

nearest_square = max(squares)
print(nearest_square)