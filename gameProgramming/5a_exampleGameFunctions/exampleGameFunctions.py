# Example Game Function project, Gabriel Coffey, v0.3p
import random
# Lily Was Here
# Need to use the random.randint() function. 
# Go back and add the function calls to test them. 

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
        playerStamina = 10
        while playerStamina > 0:
                print(playerStamina)
                playerStamina - 1

def powerScale(styleScale, playerPower,powerLevel):
    if playerPower == 100:  
        powerLevel  = 1
    elif playerPower == 250:
        powerLevel = 2
    elif playerPower == 500:
        powerLevel = 3
    else: print("You're too weak!")    
                  
    if powerLevel == 1 and styleScale >= 0:
        midAirDash = True
    elif powerLevel == 1 and styleScale >= 10:
        midAirDashPlus = True
        maximumLeap = True   
    
def powerStance(powerStance,styleScale,playerPower):
    if playerPower >= 300 and styleScale >= 50:
        powerStance = True
    elif playerPower >= 375 and styleScale >= 120:
        powerStancePlus = True
    if powerStance == True:
        playerStamina = 0
        exhausted = False
        burstMeter = 0
        blazingKick = True
    elif powerStancePlus == True:
        playerStamina = 100
        exhausted = False
        burstMeter = 1
        blazingKick = True
        auraStorm = True
    return blazingKick 

    # My suggestion is to make a function that returns each of these status effects as a separate function.  
    


# reviewed by William Castengera
