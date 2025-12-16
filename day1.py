with open('input.txt', 'r') as file:
    input = file.read().splitlines()

my_sum = 50
cnt = 0
for i in range(len(input)):
    s = input[i]
    mult = 0
    if s[0] == 'R':
        num = int (s[1:])
        if my_sum + num >= 100:
            mult = (my_sum + num)//100
        my_sum = (my_sum + num) %100

    else:
        num = int(s[1:])
        mult = num // 100
        num = num % 100
        if my_sum - num <= 0 and my_sum != 0:
            mult += 1
        my_sum = (my_sum - num) % 100

    cnt += mult
    #print("test:",i, my_sum,  mult, cnt)

print(cnt)