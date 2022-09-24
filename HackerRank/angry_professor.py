# https://www.hackerrank.com/challenges/angry-professor/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen


def angryProfessor(k, a):
    # Write your code here
    on_time_students = [student for student in a if student <= 0]
    if len(on_time_students) >= k:
        return "NO"
    return "YES"


a = angryProfessor(2, [-1, 0, 2, 1])
print(a)
