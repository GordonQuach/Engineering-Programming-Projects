from itertools import permutations

# Initializing the document.
result_doc = open("Permutation Simulation.txt", 'w')

permSize = int(input("What's the size of your permutation?\t"))

# Preset Iterable
perm = list(permutations([1, 3, 5, 7, 8, 0], permSize))

for combo in perm:
    # Use map here, which converts all the items in the tuple to strings, because otherwise you will get a TypeError.
    withoutParen = ', '.join(map(str, (combo)))

    print(withoutParen)

    # Writing each result into document.
    result_doc.write(withoutParen + "\n")

permAmt = str(len(perm))
print("\nThere are " + permAmt + " permutations available.\n")

# Closing document.
result_doc.write("\nThere are " + permAmt + " permutations available.\n")
result_doc.close()

print("Check your root directory for the text file of these results.")
