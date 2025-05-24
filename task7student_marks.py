#Work with task7student_marks.csv
import csv

# Step 1: Read the original CSV file
students = []

with open('task7student_marks.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Step 2: Calculate total and average
        maths = int(row['maths'])
        science = int(row['science'])
        english = int(row['english'])

        total = maths + science + english
        average = total / 3

        row['total_marks'] = total
        row['average'] = round(average, 2)

        students.append(row)

# Step 3: Write to a new CSV file
with open('task7student_marks_updated.csv', mode='w', newline='') as file:
    fieldnames = ['name', 'maths', 'science', 'english', 'total_marks', 'average']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    for student in students:
        writer.writerow(student)

print("✅ New file 'task7student_marks_updated.csv' created successfully!")
