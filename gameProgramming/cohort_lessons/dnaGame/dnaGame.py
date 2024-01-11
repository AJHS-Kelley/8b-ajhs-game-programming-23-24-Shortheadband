# DNA relpication Game, gabriel Coffey, v0.2

# Import Entire Modules -- Get whole tool box.
import time, datetime

# Import Specfic Methods -- Get the specfic tool.
from random import choice

# Store the DNA Bases
dnaBases = ["A", "T", "G", "C"]

# Game Functions
def gameIntro() -> None:
    pass

def genDNA() -> str:
    basesGenerated = 0
    BasesRequested = int(input("Please enter a postive integer number of bases to generate.\n"))
    dnaSequence = ""

    while basesGenerated < BasesRequested:
        dnaSequence += choice(dnaBases)
        basesGenerated += 1
    return dnaSequence    

dna = genDNA()
print(dna)
    
    #return "STRING"

def genRNA(dnaSequence: str) -> tuple:
    print(f"The DNA Sequence is {dnaSequence}.\n")
    print("You will now genrerate the RNA sequence that would match.\n")
    print("Please remeber, in the RNA sequence ? matches with A from the DNA sequence")
    rnaStart = time.time() # time.time() returns the number of seconds since 00:00:00 UTC Jan, 01, 1970
    rnaSequence = input("Please enter the matching RNA sequence. Leave no spaces! Then press enter.\n").upper()
    rnaStop = time.time()
    rnaTime = rnaStop - rnaStart

    return (rnaSequence, rnaTime)
    # Tuples are ordered -- you can refernce items with the index.
    # Tuples are UNCHANGEABLE -- you cannot add, modify, or delete after creating
    # Tuples CAN have duplicate values.

rna = genRNA(dna)
print(rna)