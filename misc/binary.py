# Code for testing matrices.
a = "011000"
second = ["000000", "101010", "010101", "111111"]
ans = ""
third = ["000101", "101111", "010000", "111010"]
for a in third:
    for b in second:
        for x, y in zip(a, b):
            if x == y:
                ans += "0"
            else:
                ans += "1"
        print(ans)
        ans = ""
    print("END")
