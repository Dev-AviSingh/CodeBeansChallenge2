courseCount = int(input("Enter the number of courses: "))
prerequisitesString = input("Enter the prerequisites: ")

prerequisites = []
courseNumbers = []

# Getting all the course numbers order
for c in prerequisitesString:
	try:
		courseNumbers.append(int(c))
	except ValueError:
		pass

# Arrangin the course numbers in relevent format
for i in range(0, len(courseNumbers), 2):
	prerequisites.append([courseNumbers[i], courseNumbers[i + 1]])

answer = "True"

# If the reverse of any prerequisite is present then the courses are impossible.
for prerequisite in prerequisites:
	if prerequisites[::-1] in prerequisites:
		answer = "False"

print(answer)

x = input()