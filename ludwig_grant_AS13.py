# File Name: ludwig_grant_AS13.py
# File Path: /home/ludwigg/Python/PyRpi_AS13/ludwig_grant_AS13.py
# Run Command: sudo python3 /home/ludwigg/Python/PyRpi_AS13/ludwig_grant_AS13.py

# Grant Ludwig
# 10/28/2019
# AS.13
# Sort 3 numbers

# Part 1
SQUARE = 5

print("Part 1")
print("======")
for i in range(SQUARE):
	for j in range(SQUARE):
		print("*", end=" ")
	print()
		
print()

# Part 2
HEIGHT = 5

print("Part 2")
print("======")
for i in range(1, HEIGHT + 1):
	for j in range(i):
		print("*", end=" ")
	print()
for i in range(HEIGHT - 1, 0, -1):
	for j in range(i):
		print("*", end=" ")
	print()