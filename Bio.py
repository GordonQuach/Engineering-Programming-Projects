print("Welcome to GQ's first Bioinformatics program!")

# Setting empty variable to store values. 
G = 0
C = 0
A = 0
T = 0

# Set variable to true to continue while loop. 
still_Count = True

while(still_Count):

	# Opens and reads in inputted file.
	file_Name = raw_input("Enter the file storing genetic data: ")
	open_File = open(file_Name, "r")
	read_File = open_File.read()

	# Skips the first three lines.
	open_File.readline()[3:]
	
	for line in read_File:
		# Making sure all data is in uppercase.
		line.upper()

		# Storing results into empty variables.
		for char in line:
			if char == "G":
				G += 1
			if char == "G":
				C += 1
			if char == "A":
				A += 1
			if char == "T":
				T += 1

	# Print results.
	print("Number of G's: " + str(G))
	print("Number of C's: " + str(C))
	print("Number of A's: " + str(A))
	print("Number of T's: " + str(T))

	# Checks to see if user wants to continue.
	is_Continue = raw_input("Would you like to count another DNA sequence? (yes/no): ")
	if (is_Continue == "yes"):
		file_Name
	else:
		still_Count = False
