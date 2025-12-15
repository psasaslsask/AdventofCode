with open("input.txt", "r") as file:
    start = 50
    count = 0
    for i in file:
        direction = i[0]
        distance = int(i[1::])
        if direction == "L":
            start = (start - distance) % 100
            print("The dial is rotated to point", start)
            
        if direction == "R":
            start = (start + distance) % 100
            print("The dial is rotated to point",start)
            
        if start == 0:
            count +=1
            print(count)
        

print(count)
        