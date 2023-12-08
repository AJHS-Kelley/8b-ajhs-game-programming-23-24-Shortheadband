# Example Game Function project, Gabriel Coffey, v0.3p
import random
# Lily Was Here <3
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

def stamina(playerStamina, exhausted): # I think that you might have to have somestuff to print out. You should try to make it text based
    if playerStamina >= 3: # you could also try to limit what you can do because you are running out of time
        sprint = True
        glide = False    
    elif playerStamina >= 1: # you would want to make the bigger number come first. They will never be able to glide then
        sprint = True
        glide = True 
    elif playerStamina == 0: # there is no else in this if else thing
        print("You're exhausted, Take your time.")
        exhausted = True # you might not need this. What is the point with it?
        playerStamina = 0
        while playerStamina < 10: # you might not want this to be in this function. Maybe make a option function so that you don't gain stamina when you are trying to do something that costs stamina
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
        while playerStamina > 0: # what? Is this tring to use sprintBurst? Cause this will just lower it to 9 stamina automadicly
                print(playerStamina)
                playerStamina - 1

def powerScale(styleScale, playerPower,powerLevel): # what is the ulatme goal is this? How would it be in game play?
    if playerPower == 100:  
        powerLevel  = 1
    elif playerPower == 250: # you might just try to focus on stamina and if there is any kind of movement
        powerLevel = 2
    elif playerPower == 500: # rember to look back at your other code
        powerLevel = 3
    else: print("You're too weak!")    
                  
    if powerLevel == 1 and styleScale >= 0:
        midAirDash = True # what about the false
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

# rember to make a actual game play part of the code. So you can use the functions

    # My suggestion is to make a function that returns each of these status effects as a separate function.  
    


# reviewed by William Castengera
