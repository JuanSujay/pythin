max = 1000


class employee:
	def __init__(self):
		self.age = ''
		self.name = ''
		self.id = ''
		self.department = ''
		self.gender = ''
		self.phone = ''
		self.address = ''
		self.order = ''
		self.completed = ''
		self.progress = ''
		self.rating = ''
		self.recent = ''
num = 0
emp = [employee() for i in range(max)]
tempemp = [employee() for i in range(max)]
sortemp = [employee() for i in range(max)]
sortemp1 = [employee() for i in range(max)]


def build():
	global num, emp

	print("Build The Table")
	print("Maximum Entries can be", max)

	num = int(input("Number of Entries: "))

	if num > max :
		print("Maximum number of Entries are 1000")
		num = 2000

	print("Enter the following data:")
	for i in range(num):
		emp[i].id = int(input("ID: "))
		emp[i].name = (input("Name: "))
		emp[i].age = input("Age: ")
		emp[i].gender = (input("Gender: "))
		emp[i].phone = int(input("Phone Number: "))
		emp[i].address = (input("Address: "))
		emp[i].problem = int(input("Number of Orders till date : "))
	else:
		print("Employee Report Full")

	showMenu()

	

def insert():
	global num, emp

	if num < max:
		i = num
		num += 1

		print("Enter the information of the Employee:")
		emp[i].id = int(input("ID: "))
		emp[i].name = (input("Name: "))
		emp[i].age = input("Age: ")
		emp[i].department = input("Department: ")
		emp[i].gender = input("Gender: ")
		emp[i].phone = input("Phone Number: ")
		emp[i].address = input("Address: ")
		emp[i].completed = input("Total Task completed: ")
		emp[i].progress = input("Task in Progress: ")
		emp[i].rating = input("Task Rating: ")
		emp[i].recent = input("Recent or Ongoing Project: ")

		
		
	else:
		print("Employee Report Full")

	showMenu()



def deleteRecord():
	global num, emp

	code = int(input("Enter the ID to Delete Report: "))

	for i in range(num):
		if emp[i].id == id:
			deleteRecord(i)
			num -= 1
			break

	showMenu()

def searchRecord():
	global num, emp

	code = int(input("Enter the ID to Search Report: "))

	for i in range(num):
		
		if emp[i].id == id:
			print("ID:", emp[i].id)
			print("Name:", emp[i].name)
			print("Supervisior:", emp[i].supervisior)
			print("Department:", emp[i].department)
			print("Job Knowledge:", emp[i].jobknowledge)
			print("Quality of Work:", emp[i].quality)
			print("Initiative:", emp[i].initiative)
			print("Problem Solving:", emp[i].problem)
			print("Attitude and Behaviour:", emp[i].attitude)
			print("Skills:", emp[i].skills)
			print("Attendence:", emp[i].attendence)
			print("Work Efforts:", emp[i].efforts)
			break

	showMenu()


def showMenu():
	print("-------------------------Data Information-------------------------\n")
	print("Available Options:\n")
	print("Information about Customers		 (1)")
	print("Information about Employees (2)")
	print("Delete Report	 (3)")
	print("Search a Report	 (4)")
	print("Exit			 (5)")

	
	option = int(input())

	
	if option == 1:
		build()
	elif option == 2 :
		insert()
	elif option == 3 :
		deleteRecord()
	elif option == 4 :
		searchRecord()
	elif option == 5 :
		return
	else:
		print("Expected Options")
		print("are 1/2/3/4/5")
		showMenu()

showMenu()
	
