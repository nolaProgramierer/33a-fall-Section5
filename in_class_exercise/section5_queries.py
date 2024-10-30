# 1) Creating employees
# --------------------
alice = Employee.objects.create(fname="Alice", lname="Johnson", boss=True)
bob = Employee.objects.create(fname="Bob", lname="Smith", boss=False)
carol = Employee.objects.create(fname="Carol", lname="Davis", boss=False)
dave = Employee.objects.create(fname="Dave", lname="Miller", boss=True)


# 2) Assign Supervisors
# ---------------------
# Assign Bob and Carol to be supervised by Alice


# Assign Dave to supervise Alice



# 3) Get All Supervisors of a Specific Employee
# ---------------------------------------------
# Find all supervisors of Bob




# 4) Get All Subordinates of a Specific Employee
# ----------------------------------------------
# Find all subordinates of Alice



# 5) Check if an Employee Has Supervisors
# ---------------------------------------
# Check if Bob has any supervisors



# 6) Get Subordinates for a Specific Employee
# -------------------------------------------
# Get all subordinates of Alice



# 7) Count the Number of Subordinates for a Specific Supervisor
# -------------------------------------------------------------
# Count how many subordinates Alice has



# 8) Find Employees Without Any Supervisors
# -----------------------------------------
# Find all employees with no supervisors



# 9) Find Employees Without Any Subordinates
# ------------------------------------------
# Find all employees who do not supervise anyone



# 10) Get All Bosses
# ------------------
# Get all employees who are bosses (boss=True)



# 11) Get All Employees Supervised by a Specific Boss
# ---------------------------------------------------
# Find all employees supervised by Alice, who is a boss



# 12) Remove a Supervisor from an Employee
# ----------------------------------------
# Remove Alice as Bob's supervisor



# 13) Clear All Subordinates of a Supervisor
# ------------------------------------------
# Remove all subordinates from Alice



# 14) Return All Employees that are Supervisors
# ---------------------------------------------
# Get all employees who are supervisors


# 15) Create a Boss Using a Class Method
# --------------------------------------
# Create a new employee who is a boss
