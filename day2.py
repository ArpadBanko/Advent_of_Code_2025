with open('input.txt', 'r') as file:
    input = file.read().split(",")

sol = 0
for i in range(len(input)):
    fst, sec = input[i].split("-")
    for j in range(int(fst), int(sec)+1):


        for k in range(1, len(str(j))//2+1):
            # get all subsets with specified length
            chunks = [str(j)[max(i - k, 0):i] for i in range(len(str(j)), 0, -k)]
            chunks.reverse()
            #print(chunks)
            if all(x == chunks[0] for x in chunks):
                sol += j
                break


print(sol)