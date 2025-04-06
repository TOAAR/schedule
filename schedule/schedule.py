from constraint import *

problem = Problem()

variables = ["A", "B", "C", "D", "E", "F", "G"]
# Add each variable individually
for var in variables:
    problem.addVariable(var, ["Monday", "Tuesday", "Wednesday"])

# List of constraints
CONSTRAINS = [("A", "B"), ("A", "C"), ("B", "C"), ("B", "D"),
              ("B", "E"), ("C", "E"), ("C", "F"), ("D", "E"),
              ("E", "F"), ("E", "G"), ("F", "G")]

# Add the constraints to ensure variables are assigned different days
for x, y in CONSTRAINS:
    problem.addConstraint(lambda x, y: x != y, (x, y))

# Retrieve and display all solutions
for solution in problem.getSolutions():
    print(solution)

# Print the number of solutions
print(problem.getSolutions())





"""from constraint import *

problem = Problem()

problem.addVariable(["A","B","C","D","E","F","G"],
                    ["Monday", "Tuesday", "Wednesday"])


CONSTRAINS = [("A","B"),("A","C"),("B","C"),("B","D"),("B","E"),("C","E"),("C","F"),("D","E"),("E","F"),("E","G"),("F","G")]

for x,y in CONSTRAINS:
    problem.constrain(lambda x,y: x != y, (x,y))

for solution in problem.getSolutions():
    print(solution)

print(problem.getSolutionCount())
"""