if __name__ == '__main__':
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort(reverse=True)
    i = a[0]
    j = 0
    while(i == a[j]):
        j+=1
    print(a[j])