if __name__ == '__main__':
    N = int(input())
    
    workingList = []
    
    for _ in range(N):
        command = input().split()
        # print(command)
        
        match command[0]:
            case "insert":
                workingList.insert(int(command[1]), int(command[2]))
                
            case "print":
                print(workingList)
                
            case "remove":
                workingList.remove(int(command[1]))
                
            case "append":
                workingList.append(int(command[1]))
                
            case "sort":
                workingList.sort()
                
            case "pop":
                if workingList:
                    workingList.pop()
                
            case "reverse":
                workingList = workingList[::-1]
                
            case _:
                print("ERROR IN MATCHING")
    
    
    