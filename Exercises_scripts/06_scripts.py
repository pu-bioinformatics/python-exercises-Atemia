#!/Users/ATEMIA/miniconda3/bin/python

### Exercise
#Let's return to our earlier exercise: calculating %GC content. In this exercise:
#- Write a function `percentageGC` that calculates the GC content of a DNA sequence
#- The function should return the %GC content
#- The Function should return a message if the provided sequence is not DNA (This should be checked by a different function, called by your function)

# earler exercise on calculating GC content
trna = 'AAGGGCTTAGCTTAATTAAAGTGGCTGATTTGCGTTCAGTTGATGCAGAGTGGGGTTTTGCAGTCCTTA'
# counting each base in the sequence
A_count = trna.count('A')
C_count = trna.count('C')
G_count = trna.count('G')
T_count = trna.count('T')
# calculating the GC and AC content
GC_content = ((G_count + C_count)/ len(trna)) * 100
print("The GC content is,", GC_content)
AT_content = 100 - GC_content
print("The GC content is,", AT_content)
print(" In summary;\n The tRNA has GC content of %.3f and AT content of %.3f" % (GC_content, AT_content))

#function 1 testing the bases in the dna sequence
def test_dna(sequence):
    """The function tests you sequence for non-DNA bases"""
    bases = 'ATGC'
    status = True 
    for base in sequence:
        if base in bases:
            pass
        else:
            status = False
            print("At position", sequence.find(base),"invalid dna base", base)
    return status

# Function 2 calculates GC content 
def percentageGC(sequence):
    """This function calculates the Percentage of GC bases nucleotides in your sequence;
    and also checks if the imput sequence is a Dna sequence"""
    if test_dna(sequence):
        #A_count = sequence.count('A')
        C_count = sequence.count('C')
        G_count = sequence.count('G')
        #T_count = sequence.count('T')
        GC_content = (((G_count + C_count)/ len(sequence)) * 100)
        return print("The percentage GC content in the sequence is %.2f" % (GC_content))
    else:
        print("Input not DNA")
