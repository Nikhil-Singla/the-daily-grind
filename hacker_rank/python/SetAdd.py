# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(input())
a = set()

for i in range(N):
    a.add(input())
    
print(len(a))
