# def is_invalid_id(n):
#     s = str(n) #convert number to string
#     if len(s) % 2 != 0:
#         return None #reject odd length numbers
#     half = len(s) // 2 
#     if s[:half] == s[half:]: #check if 2 identical halfs
        
#         return n #return that id

#     return None

# totalsum = 0
# with open("input2.txt", "r") as file:
#     data = file.read()
#     tokens = data.split(",")
#     # print(type(tokens), tokens)
#     ranges=[]
#     for i in tokens:
#         start, end = i.split("-")
#         ranges.append((int(start), int(end))) #range
#     print(ranges)
#     for start, end in ranges: #scan each range
#         invalid_id = []
#         for x in range(start, end+1): #iterate thru every id
#             invalid = is_invalid_id(x) #detect invalid
#             if invalid is not None:
#                 totalsum +=invalid #sum invalid
        
# print(totalsum)
      
        
#hash maps since we want to group equal things
def is_invalid_id(n):
    s = str(n) #convert number to string
    L = len(s)
    
    for d in range(1, L// 2+1): # 2d <= L , d has to be atleast 2 so d should stop at L//2
        if L % d !=0:
            continue
        freq ={}
        for i in range(0, L, d):
            block = s[i:i+d]
            freq[block] = freq.get(block, 0) + 1
        # if all blocks identical and repeated at least twice
        if len(freq) == 1 and list(freq.values())[0] >= 2:
            return n

    return None

totalsum = 0
with open("input2.txt", "r") as file:
    data = file.read()
    tokens = data.split(",")
    # print(type(tokens), tokens)
    ranges=[]
    for i in tokens:
        start, end = i.split("-")
        ranges.append((int(start), int(end))) #range
    print(ranges)
    for start, end in ranges: #scan each range
        invalid_id = []
        for x in range(start, end+1): #iterate thru every id
            invalid = is_invalid_id(x) #detect invalid
            if invalid is not None:
                totalsum +=invalid #sum invalid
        
print(totalsum)
        
        
    