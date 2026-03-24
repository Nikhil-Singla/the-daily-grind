def boolchecker(input_string, function):
    if any([function(x) for x in input_string]):
        print('True')
    else:
        print('False')

if __name__ == '__main__':
    s = input()
    
    boolchecker(s, str.isalnum)
    boolchecker(s, str.isalpha)
    boolchecker(s, str.isdigit)
    boolchecker(s, str.islower)
    boolchecker(s, str.isupper)
