import csv

# Read from the updated file
with open('task7student_marks_updated.csv', mode='r') as infile:
    reader = csv.DictReader(infile)
    simplified_data = []

    for row in reader:
        simplified_data.append({
            'name': row['name'],
            'total_marks': row['total_marks'],
            'average': row['average']
        })

# Write to a new file
with open('task7student_summary.csv', mode='w', newline='') as outfile:
    fieldnames = ['name', 'total_marks', 'average']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)

    writer.writeheader()
    for student in simplified_data:
        writer.writerow(student)

print("✅ Summary file 'task7student_summary.csv' created successfully!")
