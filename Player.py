# #Author: Seth Gochey (http://github.com/sgochey)
# #Last Edit: 11/24/2012

# #Player.py:
# #  Player class:
# #    initializes player object and it's caffeine, tries, and bonusSpeed variables
# #    contains methods to modify these variables.

BNS_SPD_MULTI = 2.0  # Modify this number to change the amount of bonusSpeed per caffeine level

class Player(object):
    
   
  
  def __init__(self, caffeine=1.0, tries=3):
    self.caffeine = caffeine
    self.tries = tries
    self.bonusSpeed = caffeine * BNS_SPD_MULTI


# #  changeTries function:
# #    accepts an integer (intNum) and boolean (tf) as parameters
# #    if the boolean is true, the player's tries are increased by the integer value.
# #    if false, the player's tries are decreased by the int value, though the total
# #    tries may not drop below zero.
  def changeTries(self, intNum, tf):
    if tf:
      self.tries += intNum
    elif (self.tries - intNum) < 0:
      self.tries = 0
    else:
      self.tries -= intNum

  
# #  changeCaffeine function:
# #    accepts a floating-point number (floatNum) and boolean (tf) as parameters
# #    if the boolean is true, the player's caffeine level is increased by the floatNum value,
# #    though the total level may not exceed 1.0 (100%).
# #    if false, the player's caffeine level is decreased by the floatNum value, though the total
# #    level may not drop below zero.
# #    Calls changeBonusSpeed at the end.
  def changeCaffiene(self, floatNum, tf):
    if tf:
      if (self.caffeine + floatNum) > 1.0:
        self.caffeine = 1.0
      else:
        self.caffeine += floatNum
    else:
      if (self.caffeine - floatNum) < 0.0:
        self.caffeine = 0.0
      else:
        self.caffeine -= floatNum
    changeBonusSpeed()


# #  changeBonusSpeed function:
# #    Updates bonusSpeed based on new caffeine level.
  def changeBonusSpeed(self):
      self.bonusSpeed = self.caffeine * BNS_SPD_MULTI
    	         
                 
                 
                 
                 
                 
                 
                 
# ##Test commands to ensure everything works
###-----------------------------------------
# #print 'hello?'
# #test = Player()
# #
# #print test.caffeine, test.tries
# #
# #test.changeTries(1, True)
# #print test.tries
# #test.changeTries(1, False)
# #print test.tries
# #test.changeTries(5, False)
# #print test.tries
# #
# #print test.caffeine, test.tries
# #
# #test.changeCaffiene(0.75, True)
# #print test.caffeine
# #test.changeCaffiene(0.5, False)
# #print test.caffeine
# #test.changeCaffiene(2.0, False)
# #print test.caffeine
# #test.changeCaffiene(3.0, True)
# #print test.caffeine
# #
# #print test.caffeine, test.tries
