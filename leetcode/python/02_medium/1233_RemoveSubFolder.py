class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        cache = set()

        for i in folder:
            path = i.split(sep="/")[1:]
            ongoing = "/"
            for j in path:
                ongoing += j
                if ongoing in cache:
                    ongoing = "/"
                    break
                ongoing += "/"
            
            if ongoing is not "/":
                cache.add(ongoing[:-1])

        return list(cache)