def mutate_string(string, position, character):
    n = len(string)
    retval = ['a'] * n
    
    for i in range(n):
        retval[i] = string[i]

        if i == position:
            retval[i] = character        
    
    return "".join(retval)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
