#PART ONE

# with open("input.txt", "r") as file:
#     start = 50
#     count = 0
#     for i in file:
#         direction = i[0]
#         distance = int(i[1::])
#         if direction == "L":
#             start = (start - distance) % 100
#             print("The dial is rotated to point", start)
            
#         if direction == "R":
#             start = (start + distance) % 100
#             print("The dial is rotated to point",start)
            
#         if start == 0:
#             count +=1
#             print(count)
        
# print(count)
        
        
#PART TWO
with open("input.txt", "r") as file:
    start = 50
    count = 0
    for i in file:
        direction = i[0]
        distance = int(i[1::])
        if direction == "L":
            
            for j in range(distance):
                start = (start - 1) % 100
                if start == 0:
                    count += 1
            
        if direction == "R":
            for j in range(distance):
                start = (start + 1) % 100
                if start == 0:
                    count += 1
                
        
        

print(count)
        