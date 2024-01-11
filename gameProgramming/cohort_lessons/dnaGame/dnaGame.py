# DNA relpication Game, gabriel Coffey, v0.1

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
