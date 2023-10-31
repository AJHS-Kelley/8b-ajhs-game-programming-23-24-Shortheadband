# Hangman Game by Gabriel Coffey, vo.2

words = 'Cat Bat Rat Car Bar Star Bored Help Belt Tilt Machine Hammer Hourglass Vogage Punishment Divine Rewind Combine TombStone Chrome Celestial Beatiful Guardian Alliance Lyric circular motherboard Critical Mystical Dynasty'.split()
print(words)
HANGMAN_BOARD = ['''
   
    +---+
        |         
        |         
        |         
     ========''', '''            
              
                 
    +---+
    0   |         
        |         
        |         
     ========''', '''            

    +---+
    0   |         
    |   |         
        |         
     ========''', '''            


    +---+
    0   |         
   /|   |         
        |         
     ========''', '''            


    +---+
    0   |         
   /|\  |         
        |         
     ========''', '''            


    +---+
    0   |         
   /|\  |         
   /    |         
     ========''', '''            

    +---+
    0   |         
   /|\  |         
   / \  |         
     ========''']

#i = 0
#while i < len(HANGMANBOARD):
#    print(HANGMAN_BOARD[I])
#    i += 1