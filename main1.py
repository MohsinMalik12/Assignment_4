from functools import reduce

Numbers = [2, 4, 6, 8, 10]
First_Update_Numbers = list(map(lambda x : x * 2, Numbers))
Second_Update_Numbers = reduce(lambda x , y : x * y, First_Update_Numbers)
print(f"{Second_Update_Numbers} is a product of {First_Update_Numbers}")