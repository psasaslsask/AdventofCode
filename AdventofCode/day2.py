def is_invalid_id(n):
    s = str(n) #convert number to string
    if len(s) % 2 != 0:
        return None #reject odd length numbers
    half = len(s) // 2 
    if s[:half] == s[half:]: #check if 2 identical halfs
        return n #return that id

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
        
        
    
    