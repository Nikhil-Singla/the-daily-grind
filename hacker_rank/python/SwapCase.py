def swap_case(s):
    ret = []
    for i in s:        
        ascii = ord(i)
        if 65 <= ascii <= 90:
            ret.append(chr(ascii + 32))
        elif 97 <= ascii <= 122:
            ret.append(chr(ascii - 32))
        else:
            ret.append(i)
            
    return "".join(ret)
  

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
