# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
from collections import Counter

lines = sys.stdin.readlines()
n = len(lines)
for i in range(n):
    lines[i] = lines[i].strip()

if not lines:
    raise ValueError("Lines should not be null")

shoe_sizes = Counter(map(int, lines[1].split()))
customers = int(lines[2])
earnings = 0

for i in range(3, customers+3):
    size, price = map(int, lines[i].split()) 
    if shoe_sizes[size] > 0:
        earnings += price
        shoe_sizes[size] -= 1

print(earnings)