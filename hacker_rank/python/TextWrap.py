import textwrap

def wrap(string, max_width):
    n = len(string)
    s = []
    i = 0
    while i < n:
        s.extend(list(string[i:i+max_width]))
        s.append("\n")
        i += max_width
    
    return "".join(s)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
