# 1) Creating employees
# --------------------
alice = Employee.objects.create(fname="Alice", lname="Johnson", boss=True)
bob = Employee.objects.create(fname="Bob", lname="Smith", boss=False)
carol = Employee.objects.create(fname="Carol", lname="Davis", boss=False)
dave = Employee.objects.create(fname="Dave", lname="Miller", boss=True)


# 2) Assign Supervisors
# ---------------------
# Assign Bob and Carol to be supervised by Alice
alice.subordinates.add(bob, carol)

# Assign Dave to supervise Alice
dave.subordinates.add(alice)


# 3) Get All Supervisors of a Specific Employee
# ---------------------------------------------
# Find all supervisors of Bob
bob_supervisors = bob.supervisors.all()  # Should return Alice



# 4) Get All Subordinates of a Specific Employee
# ----------------------------------------------
# Find all subordinates of Alice
alice_subordinates = alice.subordinates.all()  # Should return Bob and Carol


# 5) Check if an Employee Has Supervisors
# ---------------------------------------
# Check if Bob has any supervisors
bob_has_supervisors = bob.supervisors.exists()  # Should return True


# 6) Get Subordinates for a Specific Employee
# -------------------------------------------
# Get all subordinates of Alice
alice_subordinates = alice.subordinates.all()


# 7) Count the Number of Subordinates for a Specific Supervisor
# -------------------------------------------------------------
# Count how many subordinates Alice has
alice_subordinate_count = alice.subordinates.count()  # Should return 2


# 8) Find Employees Without Any Supervisors
# -----------------------------------------
# Find all employees with no supervisors
employees_with_no_supervisors = Employee.objects.filter(supervisors__isnull=True)  


# 9) Find Employees Without Any Subordinates
# ------------------------------------------
# Find all employees who do not supervise anyone
employees_with_no_subordinates = Employee.objects.filter(subordinates__isnull=True)


# 10) Get All Bosses
# ------------------
# Get all employees who are bosses (boss=True)
bosses = Employee.objects.filter(boss=True)


# 11) Get All Employees Supervised by a Specific Boss
# ---------------------------------------------------
# Find all employees supervised by Alice, who is a boss
alice_supervised = alice.subordinates.all()


# 12) Remove a Supervisor from an Employee
# ----------------------------------------
# Remove Alice as Bob's supervisor
bob.supervisors.remove(alice)


# 13) Clear All Subordinates of a Supervisor
# ------------------------------------------
# Remove all subordinates from Alice
alice.subordinates.clear()


# 14) Return All Employees that are Supervisors
# ---------------------------------------------
# Get all employees who are supervisors
supervisors = Employee.get_all_supervisors()
for supervisor in supervisors:
    print(supervisor.fname, supervisor.lname)


# 15) Create a Boss Using a Class Method
# --------------------------------------
# Create a new employee who is a boss
new_boss = Employee.create_boss(fname="Jane", lname="Doe")
print(new_boss)












