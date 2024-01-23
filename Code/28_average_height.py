student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

i = 0
sum = 0
for c in student_heights:
    c = int(c)
    sum += c
    i += 1

print(f"The average is: {round(sum/i)}")
