# This program was written by Gordon Quach to practice more Python related skills.
# The premise of it is to take inputs of the element symbol OR name and then print
# out its molar mass. In addition, another option for the user is to enter the 
# mass, and the program will give the corresponding element.

# Initializing a dictionary with keys and values of elements and their molar mass values.
periodic_Table = {"H": 1.0079, "He": 4.0026, "Li": 6.941, "Be": 9.0122,
     		  "B": 10.811, "C": 12.011, "N": 14.007, "O": 15.999, "F": 18.998,
		  "Ne": 20.180, "Na": 22.990, "Mg": 24.305, "Al": 26.982,
		  "Si": 28.086, "P": 30.974, "S": 32.065, "Cl": 35.453,
		      "Ar": 39.948, "K": 39.098, "Ca": 40.078, "Sc": 44.956,
		      "Ti": 47.867, "V": 50.942, "Cr": 51.996, "Mn": 54.938,
		      "Fe": 55.845, "Co": 58.933, "Ni": 58.693, "Cu": 63.546,
		      "Zn": 65.39, "Ga": 69.723, "Ge": 72.61, "As": 74.922,
		      "Se":78.96, "Br": 79.904, "Kr": 83.80, "Rb": 85.468, "Sr": 87.62,
		      "Y": 88.906, "Zr": 91.224, "Nb": 92.906, "Mo": 95.94,
		      "Tc": 97.61, "Ru": 101.07, "Rh": 102.91, "Pd": 106.42,
		      "Ag": 107.87, "Cd": 112.41, "In": 114.82, "Sn": 118.71,
		      "Sb": 121.76, "Te": 127.60, "I": 126.90, "Xe": 131.29,
		      "Cs": 132.91, "Ba": 137.33, "La": 138.91, "Ce": 140.12,
		      "Pr": 140.91, "Nd": 144.24, "Pm": 145.0, "Sm": 150.36, "Eu": 151.96,
		      "Gd": 157.25, "Tb": 158.93, "Dy": 162.50, "Ho": 164.93, "Er": 167.26,
		      "Tm": 168.93, "Yb": 173.04, "Lu": 174.97, "Hf": 178.49, "Ta": 180.95,
		      "W": 183.84, "Re": 186.21, "Os": 190.23, "Ir": 192.22, "Pt": 196.08,
		      "Au": 196.08, "Hg": 200.59, "Tl": 204.38, "Pb": 207.2, "Bi": 208.98,
		      "Po": 209.0, "At": 210.0, "Rn": 222.0, "Fr": 223.0, "Ra": 226.0,
		      "Ac": 227.0, "Th": 232.04, "Pa": 231.04, "U": 238.03, "Np": 237.0,
		      "Pu": 244.0, "Am": 243.0, "Cm": 247.0, "Bk": 247.0, "Cf": 251.0, "Es": 252.0,
		      "Fm": 257.0, "Md": 258.0, "No": 259.0, "Lr": 262.0, "Rf": 261.0, "Db": 262.0,
		      "Sg": 266.0, "Bh": 264.0, "Hs": 269.0, "Mt": 268.0}

# Asks if user would like to find the element or mass.

decision = raw_input("What would you wish to find today? \nElement or Mass \t")

if (decision.upper() == "ELEMENT"):
	pass
	#element_Symbol = raw_input("Please enter unknown element's atomic mass. \t")
	#if (element_Symbol in periodic_Table):
	#	print (periodic_Table[element_Symbol])

if (decision.upper() == "MASS"):
	element_Mass = raw_input("Please enter element. \t")

	# Assigning variable to TRUE to initiate loop.
	in_Table = True

	# If the element was inputted correctly and is in the periodic table, the program will return the molar mass.
	# However, if it isn't, the while loop will ask the user for the element again until it is found in the periodic
	# table.
	while (in_Table):
		if (element_Mass in periodic_Table):
			print (str(periodic_Table[element_Mass]) + " grams/mole")
			# Once found, set to false.
			in_Table = False
		else:
			print("The element you inputted, " + element_Mass + ", was not in the periodic table... yet.")
			element_Mass = raw_input("Please enter element. \t")

# Checks if the user would like to continue or quie the program.
cont = raw_input("Would you like to find another mass or element? Y/N \t")
if (cont.upper() == "Y"):
	decision
else:
	quit()




