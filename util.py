
def print_multi_table(a,b):
    for i in range(2, 13):          
        print(f"แม่ {i}")
        for j in range(1, 13):    
            if (i * j) % 2 == 0: 
                print(f"{i} x {j} = {i*j}")

print_multi_table(5,20)

students = [{'name': 'Mark', 'grade': 'A'},
            {'name': 'John', 'grade': 'B'} ]
students.append({'name': 'Mary', 'grade': 'A'})
(students.append({'name': 'Jane', 'grade': 'A'}))
(students.append({'name': 'Peter', 'grade': 'B'})) 
(students.append({'name': 'Lucy', 'grade': 'C'}))
(students.append({'name': 'Bob', 'grade': 'B'}))
(students.append({'name': 'Alice', 'grade': 'A'}))

print(len(students))
for s in students:
    if s ['grade'] == 'A':
        print(s['name'])

print(sum(1 for s in students if s['grade'] == 'A'))
