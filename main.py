from time import sleep
from os import system,name
from replit import db

class versus:
    def __init__(self):
      # Online Settings
      try:
        self.update()
      except:
        # Set all database keys if deleted
        db['room1'] = 0; db['r1p1'] = ""; db['r1p2'] = ""
        db['room2'] = 0; db['r2p1'] = ""; db['r2p2'] = ""
        db['room3'] = 0; db['r3p1'] = ""; db['r3p2'] = ""
        self.__init__()

      # Current Room
      self.croom = 0; self.enemy = 0; self.selfmove = 0

      # Local Settings
      # Bot Settings
      self.botmove = ""
      self.bot = 0

      # Game Stats
      self.win = 0; self.loss = 0; self.tie = 0

      # Menu
      self.menu = ['1. Find a game','2. Browse rooms','3. Bot match','4. Stats']
      print("Welcome!")
        
    def update(self):
        # Room 1 update
        self.room1 = db['room1']; self.r1p1 = db['r1p1']; self.r1p2 = db['r1p2']
        # Room 2 update
        self.room2 = db['room2']; self.r2p1 = db['r2p1']; self.r2p2 = db['r2p2']
        # Room 3 update
        self.room3 = db['room3']; self.r3p1 = db['r3p1']; self.r3p2 = db['r3p2']

    def menu(self):
      for i in self.menu:
          print(i)
      try:
          a = int(input("#"))
          if a == 1:
            print("This is temporarily unavaliable... Sorry.")
            self.menu()
          elif a == 2:
            self.clearscreen()
            print("Checking Rooms...")
            self.rooms()
          elif a == 3:
            print("Okay, we will set up the bot...")
            sleep(3)
          elif a == 4:
            self.clearscreen()
            print("Stats:\nWins:",self.win,"\nLosses:",self.loss,"\nTies:",self.tie,"\n\n\n")
            input("Press enter to return to menu...")
            self.clearscreen()
      except:
        print('Please put in a valid number...')
        self.clearscreen()

    def clearscreen(self):
      if name == 'nt':
          _ = system('cls')
      else:
          _ = system('clear')

    def match(self):
      self.clearscreen()
      print("Rock, paper, or scissors okay? Also the bot doesn't cheat.")
      sleep(1)
      print("Okay, here we go...")
      self.shoot()
      def shoot(self):
        a = input(">")
        if (a == "rock") or (a == "r") or (a == "Rock"):
          a == 'r'
          if self.bot == 0:

    def rooms(self):
      self.update()


v = versus()
v.menu()
