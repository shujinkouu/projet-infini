#We should seek to separate the app functions from the app logic

#Kivy required for our app
import kivy
#App required from kivy to make an app (TO READ)
kivy.require('1.1.1')
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.factory import Factory
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.textinput import TextInput
#Dependencies For the Time Module
import datetime as dt
import pytz
from datetime import date
import os

timezone_nw = pytz.timezone('EST')
x = dt.datetime.now(timezone_nw)
x = x.strftime("%m") + '-' + x.strftime("%d") + '-' + x.strftime("%Y")

global DocumentName
DocumentName = "weed.txt"
  
global f

def DocumentSelector():
  global DocumentName
  global f
  f = ObjectProperty(None)
  #DocumentName = input("what's the name of the document?") + ".txt"
  cwd = os.getcwd()
  f = open(cwd + "\Database\\" + DocumentName, 'r+')
  #f = open("C:\\Users\Asus\Documents\Git\Weed-App-test\Database\\" + DocumentName, 'r+')









DocumentSelector()
f = list(f)
#print(f)


#if one replace weed.txt by 'x1' this permits the user to choose the name of the used document
#x1 = input("what's the name of the document?") + ".txt"

#Doesn't work but in the end I'd love for it to work as this line would work if working
#f = open("weed.txt" in 'C:\Users\Asus\Documents\Git\Weed-App-test\database', 'a')

#f = open("C:\\Users\Asus\Documents\Git\Weed-App-test\Database\weed.txt", 'a')
"""
Fixed value option, this has to be built and adapted for the UI version
#those are fixed value for a and b
#a=5
#b=0.7
"""
a=160
b=28

def Call_Variables():
  while True:
    try:
#!!! INPUT !!!
#Now connected to the UI version
      global a
      global b
      b = float(var1)
      a = float(var2)
      global c
      c = float(var3)
    #How many squares of chocolate \nare you eating?
    except ValueError:
      pass
    else:
      break



def Function(a,b,c):
  global d
  c = (a / b) * c
  c = round(c, 2)
  #deving change for ui version
  # var should be a global variable that represent c
  # a, b and c are var1, var2 and var3
  #This prompt is supposed to show up in the first pop-up, logit is  part of the pop-up and the buttons should be connected to the y/n options
  #print('\nYou\'re smoking', c, '$')
  global var1
  #here this works but information have to be found about label and how to center text on a label so this is clean
  var1 = "You\'re smoking " + str(c) + " $\nlogit? [y/n]"
  c = '\n' + str (c) + '$' + ' - ' + '[' + x + ']'
  c = str(c)
  d = c

def logit():
  f = ObjectProperty(None)
  print(f)
  if f != open("C:\\Users\Asus\Documents\Git\Weed-App-test\Database\\" + DocumentName, 'a'):
    f = open("C:\\Users\Asus\Documents\Git\Weed-App-test\Database\\" + DocumentName, 'a')
  else:
    pass
  #i = input('logit? [y/n]')
  """
  here is the first error happening the c string start with /n for displaying it to the user we could .splice() it and 
  save the rest back in c before it's outputed to the .txt file
  however if we do that for any value of n greater than 1 then the data is gonna pile up on the same line 
  instead of being 1 data point per line has it should be and has this initial /n makes it. 
  So we could check if weed.txt is empty and if yes use the splice function to patch this edge case.
  """
  if i == 'y':
    f.write(d)
  #All print event need to be changed for the UI version
    print('this was logged')
  else:
    print('This wasn\'t logged')
  f.close()


def extrapolate():
  #print event change needed
  #print('\nOn est en date du\n'+ x)
  #input event need to be changed for UI version
  #extrapol = input('\nDo you want to extrapol? [y/n]')
  #print(type(extrapol))
  if extrapol == 'y':
    f = open("C:\\Users\Asus\Documents\Git\Weed-App-test\Database\\" + DocumentName, 'r+')
    f = list(f)
    counter = 0
    moyenne = 0
    LastMonth = 0
    LastYear = 0
    LastDay = 0
    DayCounter = 0
    Total = 0
    lenght = len(f)
    while counter<lenght:
      b = f[counter]
      b = b.split('-')
      if counter == 0:
        InitialAmount = b[0]
        InitialMonth = b[1]
        InitialDay = b[2]
        InitialYear = b[3]
        InitialMonth = int(InitialMonth[InitialMonth.find('[') + 1:])
        InitialYear = int(InitialYear[:InitialYear.find(']')])

          #debug line
  #      print('Initial:\n' + str(InitialAmount) + str(InitialMonth) + str(InitialDay) + str(InitialYear) + '\n')

      if counter == lenght-1:
        FinalAmount = b[0]
        FinalMonth = b[1]
        FinalDay = b[2]
        FinalYear = b[3]
        FinalMonth = int(FinalMonth[FinalMonth.find('[') + 1:])
        FinalYear = int(FinalYear[:FinalYear.find(']')])
        
        #debug line
  #      print('Final:\n' + str(FinalAmount) + str(FinalMonth) + str(FinalDay) + str(FinalYear) + '\n')   

        d0 = date(int(InitialYear), int(InitialMonth), int(InitialDay))
        d1 = date(int(FinalYear), int(FinalMonth), int(FinalDay))
        delta = d1 - d0

        #debug line
  #     print('il y a: ' + str(delta.days))
        deltadays = delta.days
      counter = counter + 1
      amount = b[0]
      month = b[1]
      jour = b[2] 
      annee = b[3]
      amount = amount[:amount.find('$')]
      month = month[month.find('[') + 1:]
      annee = annee[:annee.find(']')]
      Total = float(Total) + float(amount)
      Total = round(Total, 2)

      """
      Total = le chiffre
      the user could query to display le chiffre

      """
      if LastMonth == month and LastYear == annee and LastDay == jour:
        pass
      else:
        DayCounter = DayCounter + 1
      LastMonth = month
      LastYear = annee
      LastDay = jour
    moyenne = float(Total) / float(deltadays)
    moyenne = round(moyenne, 2)

    #print event need change for UI version
    #print('\nla moyenne de dépense journalière est: \n' + str(moyenne) + '$')

    MoyenneSemaine = round(moyenne * 7, 2)
    MoyenneMois = round(moyenne * 30.5, 2)
    MoyenneAnnee = round(moyenne * 365, 2) 

    #Print event need change
    global labeltxt2
    labeltxt2 = '\nLa moyenne de dépense journalière est: \n' + str(moyenne) + '$\n' + 'La moyenne de dépense semestrielle est: \n' + str(MoyenneSemaine) + '$\n' + 'La moyenne de dépense mensuelle est: \n' + str(MoyenneMois) + '$\n' + 'La moyenne de dépense annuelle est: \n' + str(MoyenneAnnee) + '$'
    #print('la moyenne de dépense semestrielle est: \n' + str(MoyenneSemaine) + '$')
    #print('la moyenne de dépense mensuelle est: \n' + str(MoyenneMois) + '$')
    #print('la moyenne de dépense annuelle est: \n' + str(MoyenneAnnee) + '$')

class MyGrid(Widget):
    var1 = ObjectProperty(None)
    var2 = ObjectProperty(None)
    var3 = ObjectProperty(None)
    state = ObjectProperty(None)
    state = "on"

    def btn(self):
        #app.var = 'lol'
#debug line
        #print('hi')
#debug line
        #print(str(Factory.MyPopup().testlabel.text))
#debug line
        #print(Factory.MySecondPopup().label2.text)
        
        #debug line
        #print('hi'+ self.var1.text + "$  !")
        global var1
        global var2
        global var3
        var1 = self.var1.text
        var2 = self.var2.text
        var3 = self.var3.text
        global state
        if (var1 or var2 or var3 != 0 or defined):
          try:
            MyGrid.state = 'on'
            int(var1)
            int(var2)
            int(var3)
            print(var1)
            #print even need to be changed for UI version
            #print(var1 + var2 + var3)
            #!!! This need to be placed on actuation of the first button
            
            Call_Variables()
            #This needs to be placed strategically in the UI version
            Function(a,b,c)
            #extrapol()
#            self.var1.text = ""
#            self.var2.text = ""
#            self.var3.text = ""


          except ValueError:
            MyGrid.state = 'off'
            pass

#Build the app with my basic widget rest is done in .kv file
class MyApp(App):

    var = ObjectProperty(None)
    labeltxt = ObjectProperty(None)
    global DocumentName
    DocumentName = ObjectProperty(None)

    def build(self):
      return MyGrid()

    #!!!! OUTPUT !!!!! 
    #This is the plug to change the value of the text for my second popup
    def btn(self):
      self.var = var1
      pass       

    def btn2(self):
      global i
      i = ObjectProperty(None)
      i = "y"
      logit()
      pass

    def btn3(self):
      global i
      i = ObjectProperty(None)
      i = "n"
      logit()
      pass

    def btn4(self):
      global extrapol
      extrapol = ObjectProperty(None)
      extrapol = "y"
      extrapolate()
      self.labeltxt = labeltxt2
      pass

    def btn5(self):
      global DocumentName
      DocumentName = str(Factory.MyHome().doc.text)
      print(DocumentName)
      DocumentSelector()


if __name__ == "__main__":
    MyApp().run()