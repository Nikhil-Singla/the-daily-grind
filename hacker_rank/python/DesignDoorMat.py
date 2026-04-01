# Enter your code here. Read input from STDIN. Print output to STDOUT

N = input()
N, M = map(int, N.split())

pattern = '.|.'
mid = ((N//2))

for i in range(N):
    if i == mid:
        print("WELCOME".center(M, '-'))
    elif i < mid:
        print((pattern*((2*i)+1)).center(M, '-'))
    elif i > mid:
        print((pattern*((2*(N-i-1))+1)).center(M, '-'))        
