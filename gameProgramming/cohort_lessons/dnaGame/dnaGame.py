# DNA relpication Game, gabriel Coffey, v0.3

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

def doTranscription(dnaSequence: str) -> tuple:
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

def verifySequence(dnaSequence: str, rnaSequence: str) -> bool:
    isMatch = False
    if len(dnaSequence) != len(rnaSequence):
        print("The sequences are different lengths and cannot match.\n")
        return isMatch
    for dnaBase, rnaBase in zip(dnaSequence,rnaSequence):
        if dnaBase == "A" and rnaBase == "U":
            isMatch = True
        elif dnaBase == "C" and rnaBase == "C":
            isMatch = True
        elif dnaBase == "G" and rnaBase == "C":
            isMatch = True
        elif dnaBase == "T" and rnaBase == "A":
            isMatch = True
        else:
            print("No match detected")    
    return isMatch        


dna = genDNA()
rna = doTranscription(dna)
print(verifySequence(dna,rna[0]))