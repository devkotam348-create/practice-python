from collections import defaultdict

d = defaultdict(list)

for _ in range(int(input())):
    name = input()
    score = float(input())
    d[score].append(name)


            
       
        