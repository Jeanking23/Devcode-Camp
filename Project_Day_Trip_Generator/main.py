def marks_obtained():

    sum_of_marks = sum(marks)
    total_subjects = len(marks)
    average_marks = sum_of_marks / total_subjects
    return average_marks
average_marks = marks_obtained()


# def find_average(marks):
#     if average_marks == 80:
#      grade ="A"
#     elif average_marks >= 60 and average_marks < 80:
#      grade = "B"
#     elif average_marks >= 50 and average_marks < 60:
#         grade = "C"
#     elif average_marks < 50:
#         grade = "f"
#     marks =[55, 64, 75,80, 65]
#     average_marks = find_average(marks)
#     print(average_marks)
# marks =[55, 64, 75,80, 65]
# find_average(marks)
# print(average_marks)