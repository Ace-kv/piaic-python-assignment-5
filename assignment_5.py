# Instructions: Implement Python programs to accomplish the following task

# Task

# You are tasked with developing a Python program to manage a student database. The user should be able to add new students 
# or stop the input process by entering "stop." Each student's name, along with a sequentially generated ID starting from 1, 
# should be stored in a tuple, with these tuples kept in a list. The program must check for duplicate names before adding a 
# new student and display a message if a duplicate is found. After the input process ends, the program should first display 
# the complete list of student tuples and then display each student's ID and name individually. Additionally, the program 
# should show the total number of students, calculate and display the total length of all student names combined, and 
# identify the student with the longest and shortest name using appropriate operators. Implement these operations within 
# a function named manage_student_database() and ensure you call this function at the end of your code.

id: int = 1
student_list: list[tuple[int, str]] = []

while True:
    user_input = input("Please enter the student's name (or type 'stop' to finish): ")

    if user_input == "stop" or user_input == '':
        break
    
    duplicate = [user_input for tuple in student_list if user_input in tuple]
    if duplicate:
        print("This name is already in the list.")

    else:
        student_list.append((id, user_input))
        id += 1

print(f"\nComplete List of Students (Tuples):\n{student_list}\n")

print("List of Students with IDs:")

for tuple in student_list:
    print(f"ID: {tuple[0]}, Name: {tuple[1]}")

print(f"\nTotal number of students: {len(student_list)}\n")

names: list[str] = [student[1] for student in student_list]

combined_names_len: int = 0
longest_name: str = ''
shortest_name: str = ''

for name in names:
    combined_names_len += len(name)

    if len(name) > len(longest_name):
        longest_name = name

    if len(name) < len(shortest_name) or shortest_name == '':
        shortest_name = name

print(f"Total length of all student names combined: {combined_names_len}")
print(f"The student with the longest name is: {longest_name}")
print(f"The student with the shortest name is: {shortest_name}")



# Same, but optimised code as per ChatGPT for future reference
# id = 1
# student_list = []

# while True:
#     user_input = input("Please enter the student's name (or type 'stop' to finish): ")

#     if user_input.lower() in ["stop", '']:
#         break

#     if any(user_input == student_name for _, student_name in student_list):
#         print("This name is already in the list.")
#     else:
#         student_list.append((id, user_input))
#         id += 1

# print(f"\nComplete List of Students (Tuples):\n{student_list}\n")

# print("List of Students with IDs:")
# for student_id, student_name in student_list:
#     print(f"ID: {student_id}, Name: {student_name}")

# print(f"\nTotal number of students: {len(student_list)}\n")

# # Calculating combined lengths, longest and shortest names
# combined_names_len = sum(len(student_name) for _, student_name in student_list)
# longest_name = max(student_list, key=lambda x: len(x[1]))[1] if student_list else ''
# shortest_name = min(student_list, key=lambda x: len(x[1]))[1] if student_list else ''

# print(f"Total length of all student names combined: {combined_names_len}")
# print(f"The student with the longest name is: {longest_name}")
# print(f"The student with the shortest name is: {shortest_name}")
