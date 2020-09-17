def squares(a,b):
    if x == a and y ==b:
        print(reitur{a}_{b})
        direction = input("Direction: ")

direction = ""
x = 1
y = 1

reitur1_1 = "N"
reitur1_2 = "N or E or S"
reitur1_3 = "E or S"
reitur2_1 = "N"
reitur2_2 = "S or W"
reitur2_3 = "E or W"
reitur3_1 = "N"
reitur3_2 = "N or S"

# if x == 1 and y == 1:
#     print(reitur1_1)
#     direction = input("Direction:")
squares(x,y)

if direction == "N":
    y += 1
elif direction == "E":
    x += 1
elif direction == "W":
    x-= 1
elif direction == "S":
    y-= 1
else:
    print("Invalid direction")
print(x,y)