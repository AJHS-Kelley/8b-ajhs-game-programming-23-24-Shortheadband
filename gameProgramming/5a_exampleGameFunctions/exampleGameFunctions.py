# Example Game Function project, Gabriel Coffey, v0.2
import random
def functionOne():
    pass

def functionTwo(param1):
    pass
    
def functionThree(param1 = "Default Value"):
    pass    

def functionFour(param1, Param2, param3):
    pass

# def catchBall(throwQuality, passCatchScore, weather):
#    if throwQuality > 5.0 and passCatchScore >=99 and weather == 'sunny':
#        ballcaught = True
#    elif throwQuality > 4.0 and passCatchScore >= 75 and weather == 'Windy':
#        ballcaught = False
#    else:
#        print('Oh, no, interception!\n')
#        ballIntercepted = True
#        return ballIntercepted
#    return ballcaught

#catchBall(4.25, 107, 'Rainy')

# Game Type: Platformer

def stamina(playerStamina, exhausted):
    if playerStamina >= 1:
        sprint = True
        glide = False    
    elif playerStamina >= 3:
        sprint = True
        glide = True 
    elif playerStamina == 0:
        print("You're exhausted, Take your time.")
        exhausted = True
        playerStamina = 0
        while playerStamina < 10:
            print(playerStamina)
            playerStamina += 1


def sprintBurst(playerStamina, burstUnlocked):
    if burstUnlocked == True:
        burstMeter = 0
        if playerStamina == 10:
            burstMeter = 1
            print("sprintBurst is ready")
if burstMeter == 1:
    sprintBurst = True
    playerStamina = 10
    while playerStamina > 0:
        print(playerStamina)
        playerStamina - 1


def glide(gliderCollected):
    if gliderCollected == True:
        if ((playerStamina >= 3) and (exhausted == False)):
            glide = True
        elif (playerStamina = 0) 