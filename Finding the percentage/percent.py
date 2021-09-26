if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    marklist = student_marks.get(query_name)
    avg = float(sum(marklist)/3)
    format_sum = "{:.2f}".format(avg)
    print(format_sum)


    

