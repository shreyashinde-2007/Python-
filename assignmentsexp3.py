assignments=['english','maths','SST','chemistry','physics']
last_assignment=assignments[4]
print("last assigment to cross is: ",last_assignment)
print("orginal list: ",assignments)

assignments.append('biology')
assignments.insert(3,'sanskrit')
assignments.remove('maths')
assignments.count('chemistry')
assignments.reverse()

print("updated list is: ",assignments)


