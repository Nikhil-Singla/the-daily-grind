if __name__ == '__main__':
    records = {}
    n = int(input())
    scores = [0] * n
    names = [""] * n
    for i in range(n):
        names[i] = input()
        scores[i] = float(input())
        
    target = sorted(set(scores))[1]
    ans = []
    
    for idx, i in enumerate(scores):
        if i == target:
            ans.append(names[idx])
            
    ans.sort()
    for i in ans:
        print(i)
        
    