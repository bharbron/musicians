class Musician(object):
  def __init__(self, sounds):
    self.sounds = sounds
    
  def solo(self, length):
    for i in range(length):
      print self.sounds[i % len(self.sounds)],
    print ""
    
class Bassist(Musician): # The Musician class is the parent of the Bassist class
  def __init__(self):
    #Call the __init__ method of the parent class
    super(Bassist, self).__init__(["Twang", "Thrumb", "Bling"])
    
class Guitarist(Musician):
  def __init__(self):
    #Call the __init__ method of the parent class
    super(Guitarist, self).__init__(["Boink", "Bow", "Boom"])
    
  def tune(self):
    print "Be with you in a moment"
    print "Twoning, sproing, splang"
    
class Drummer(Musician):
  def __init__(self):
    #Call the __init__ method of the parent class
    super(Drummer, self).__init__(["Ratta", "Tat", "Tap"])
    
  def count_to_four(self):
    print "One, two, three, four!"
    
  def spontaneously_combust(self):
    print "Boom! ......"
    
class Band(object):
  def __init__(self):
    self.members = []
    
  def hire(self, musician):
    self.members.append(musician)
    
  def fire(self, musician):
    pass