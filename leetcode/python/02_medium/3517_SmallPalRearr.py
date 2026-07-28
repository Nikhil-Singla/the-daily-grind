class Solution:
    def smallestPalindrome(self, s: str) -> str:
        items = Counter(s)
        mid = ""
        str_list = []
        for i in sorted(items.keys()):
            if items[i] % 2 != 0:
                mid = i
                items[i] -= 1

            str_list.append(i * (items[i]//2))

        return "".join(str_list) + mid + "".join(str_list[::-1])
