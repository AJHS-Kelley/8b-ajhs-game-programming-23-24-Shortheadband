# DNA relpication Game, gabriel Coffey, v0.4

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
    if rnaSequence == dnaBases:
        rnaStop = time.time()
        rnaTime = rnaStop - rnaStart
        return (rnaSequence, rnaTime)
    else:
        print("Nu uh")
        rnaSequence = input("Please enter the matching RNA sequence. Leave no spaces! Then press enter.\n").upper()
        return rnaSequence
        
    

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

def calcScore(rnaSequence: str, rnaTime: float) -> int:
    score = 0
    if rnaTime < 5.0: # Fastest Time, Highest Score
        score += 1000000
    elif rnaTime < 10.0: 
        score += 700000
    elif rnaTime < 15.0: 
        score += 500000
    elif rnaTime < 25.0: 
        score += 250000
    else:
        score += 100000     


    scoreMulti = 0.0
    if len(rnaSequence) >= 15:
        score = 5.0
    elif len(rnaSequence) >= 10:
        scoreMulti = 3.0
    elif len(rnaSequence) >= 5:
        scoreMulti = 1.0
    else:
        scoreMulti = 0.5

    score *= scoreMulti
    return score

def saveScore(dnaSequence: str, rnaSequence: str, rnaTime: float, score: int) -> None:
    playerName = input("What is your first name?\n")
    lastName = input("What is your last name?\n")
    fullName = playerName + " " + lastName

    fileName = "dnaReplicationScore" + fullName + ".txt"
    saveData = open(fileName, "a")
    # File Modes
    # "x" mode -- Create FIle, IF FILE EXISTS, EXIT WITH ERROR
    # "w" mode -- Create FIle, IF FILE EXISTS, OVERWRITE IT
    # "a" mode -- Create FIle, IF FILE EXISTS, APPEND TO IT
    saveData.write(f"DNA Sequence: {dnaSequence}\nRNA Sequence: {rnaSequence}\n")
    saveData.write(f"Transcription Time: {rnaTime}\n")
    saveData.write(f"score: {score}\n")
    saveData.write(f"{fullName}\n")
    saveData.write(f"{datetime.datetime.now()}\n")
    saveData.close

dna = genDNA()
rna = doTranscription(dna)
if verifySequence(dna, rna[0]):
   score = calcScore(rna[0], rna[1])
   saveScore(dna, rna[0], rna[1], score)
