x=0
for t in (1,3,5,7,9,11,13,15):
    for y in (1, 3, 5, 7, 9, 11, 13, 15):
        if y==t:
            continue
        for z in (1, 3, 5, 7, 9, 11, 13, 15):
            if y==z or t==z:
                continue
            if t+y+z==30:
                print(t,y,z)
                x=30
print(x)
print("Eu consegui.")
