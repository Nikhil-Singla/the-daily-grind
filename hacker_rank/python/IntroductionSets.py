def average(array):
    pure = set(array)
    ans = sum(pure)/len(pure)
    
    return ans

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
