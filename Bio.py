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
	file_Name = raw_input("Enter the file storing genetic data: \t")
	print("\n")
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
	result_G = "Number of G's: " + str(G) + "\n"
	result_C = "Number of C's: " + str(C) + "\n"
	result_A = "Number of A's: " + str(A) + "\n"
	result_T = "Number of T's: " + str(T) + "\n"

	# Checks to see if you user wants to output result in a file.
	######INSERT CODE HERE, GQ.###########






	# Opens/creates targeted file to output.
	result_Doc = open ("Genome Results.txt",'w')

	# Entering data into file.
	print(result_G)
	result_Doc.write (result_G)
	print (result_C)
	result_Doc.write (result_C)
	print(result_A)
	result_Doc.write (result_A)
	print (result_T)
	result_Doc.write (result_T)
	 
	# Closing document for editing. 
	result_Doc.close()
	print ("Check your root directory for the txt file of this result.")

	# Checks to see if user wants to continue.
	is_Continue = raw_input("Would you like to count another DNA sequence? (yes/no): ")
	if (is_Continue == "yes"):
		file_Name
	else:
		still_Count = False
