if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    
    query_name = input()
    
    avg = 0
    if query_name in student_marks.keys():
        for mark in student_marks[query_name]:
            avg += mark
        
        avg /= 3
        
    print(f"{avg:.2f}")