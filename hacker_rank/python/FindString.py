def count_substring(string, sub_string):
    n = len(sub_string)
    count = 0
    m = len(string)
    for i in range(m):
        if string[i:i+n] == sub_string:
            count += 1
            
    return count
    
    

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
