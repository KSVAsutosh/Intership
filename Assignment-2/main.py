import os
print("Current Working Directory:", os.getcwd())

with open(r"C:\Users\appua\OneDrive\Documents\GitHub\Intership\Assignment-2\file1.txt", "r") as f1:
    data1 = f1.read()

with open(r"C:\Users\appua\OneDrive\Documents\GitHub\Intership\Assignment-2\file2.txt", "r") as f2:
    data2 = f2.read()

with open(r"C:\Users\appua\OneDrive\Documents\GitHub\Intership\Assignment-2\merged.txt", "w") as f3:
    f3.write(data1 + "\n" + data2)

print("Files merged successfully!")
#####################################################
#2 queston
import os

merged_path = r"C:\Users\appua\OneDrive\Documents\GitHub\Intership\Assignment-2\merged.txt"

with open(merged_path, "r") as f:
    content = f.read()
    print("\n--- Reversed Entire Content (character-by-character) ---\n")
    print(content[::-1])
###########################################################
#3 question
# ----- TASK 3: Parse CSV file into a Python dictionary -----
import csv
csv_path = r"C:\Users\appua\OneDrive\Documents\GitHub\Intership\Assignment-2\task3.csv"
student_dict = {}
with open(csv_path, "r") as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        student_id = int(row['id'])
        student_dict[student_id] = {
            "name": row['name'],
            "class": row['class'],
            "dob": row['dob']
        }

print("\nParsed Student Dictionary:")
print(student_dict)
#############################################################33
#4 question
from collections import Counter
merged_path = r"C:\Users\appua\OneDrive\Documents\GitHub\Intership\Assignment-2\merged.txt"
with open(merged_path, "r") as f:
    content = f.read().lower()
words = content.split()
word_freq = Counter(words)

print("\nWord Frequency in merged.txt:\n")
for word, count in word_freq.items():
    print(f"{word}: {count}")

