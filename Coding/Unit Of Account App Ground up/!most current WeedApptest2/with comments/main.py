#We should seek to separate the app functions from the app logic

#Kivy is the ui engine for this app
import kivy
#Version on kivy this is still not clear to me 
kivy.require('1.1.1')
#(TO READ) - *Link*
from kivy.app import App
#(TO READ) - *Link*
from kivy.uix.label import Label
#(TO READ) - *Link*
from kivy.uix.gridlayout import GridLayout
#(TO READ) - *Link*
from kivy.uix.textinput import TextInput
#(TO READ) - *Link*
from kivy.uix.button import Button
#(TO READ) - *Link*
from kivy.uix.widget import Widget
#(TO READ) - *Link*
from kivy.properties import ObjectProperty
#(TO READ) - *Link*
from kivy.uix.floatlayout import FloatLayout
#(TO READ) - *Link*
from kivy.uix.popup import Popup
#(TO READ) - *Link*
from kivy.factory import Factory

#Dependencies For the Time Module
import datetime as dt
import pytz
from datetime import date

#Stores Est time as variable timezone_nw because we live in the EST (timezone_nw prints: EST)
timezone_nw = pytz.timezone('EST')
#Converts the timezone into current data (x prints i.e: 2020-08-06 14:35:36.724505-05:00)
x = dt.datetime.now(timezone_nw)
# This chops the string aaaa-mm-dd HH-MM-SS.     -decalage. into mm-dd-yyyy
x = x.strftime("%m") + '-' + x.strftime("%d") + '-' + x.strftime("%Y")

#Declares the DocumentName as global variables and set it to the default "weed.txt"
global DocumentName
global default
default = "weed"
DocumentName = default + ".txt"

"""
Fixed value option, this has to be built and adapted for the UI version
This can be done by setting a little remember me checkbox near var1,var2,var3 userinput
#this is the old way for fixed value of a and b
#a=5
#b=0.7
"""

#Functions
def DocumentSelector():
  global DocumentName
  global f
  f = ObjectProperty(None)
  if f != open("..\Database\\" + str(DocumentName), 'a'):
    f = open("..\Database\\" + DocumentName, 'a')
  f = ObjectProperty(None)
  f = open("..\Database\\" + DocumentName, 'r+')

def Call_Variables():
  while True:
    try:
      #!!! INPUT !!!
      #Here we can fledge out the input informations
      #Now connected to the UI version
      global a
      global b
      b = float(var1)
      a = float(var2)
      global c
      c = float(var3)
    except ValueError:
      pass
    else:
      break

def Function(a,b,c):
  global d
  c = (a / b) * c
  c = round(c, 2)
  global var1
  #Here this works but information have to be found about label and how to center text on a label so this is clean
  var1 = "You\'re smoking " + str(c) + " $\nlogit? [y/n]"
  c = '\n' + str (c) + '$' + ' - ' + '[' + x + ']'
  c = str(c)
  d = c

def logit():
  f = ObjectProperty(None)
  if f != open("..\Database\\" + str(DocumentName), 'a'):
    f = open("..\Database\\" + DocumentName, 'a')
  else:
    pass
  """
  here is the first error happening the c string start with /n for displaying it to the user we could .splice() it and 
  save the rest back in c before it's outputed to the .txt file
  however if we do that for any value of n greater than 1 then the data is gonna pile up on the same line 
  instead of being 1 data point per line has it should be and has this initial /n makes it. 
  So we could check if weed.txt is empty and if yes use the splice function to patch this edge case.
  """
  if i == 'y':
    f.write(d)
    print('this was logged')
  else:
    print('This wasn\'t logged')
  f.close()

def extrapolate():
  if extrapol == 'y':
    f = open("..\Database\\" + DocumentName, 'r+')
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

      if counter == lenght-1:
        FinalAmount = b[0]
        FinalMonth = b[1]
        FinalDay = b[2]
        FinalYear = b[3]
        FinalMonth = int(FinalMonth[FinalMonth.find('[') + 1:])
        FinalYear = int(FinalYear[:FinalYear.find(']')])
        d0 = date(int(InitialYear), int(InitialMonth), int(InitialDay))
        d1 = date(int(FinalYear), int(FinalMonth), int(FinalDay))
        delta = d1 - d0
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
    MoyenneSemaine = round(moyenne * 7, 2)
    MoyenneMois = round(moyenne * 30.5, 2)
    MoyenneAnnee = round(moyenne * 365, 2) 

    global labeltxt2
    labeltxt2 = '\nLa moyenne de dépense journalière est: \n' + str(moyenne) + '$\n' + 'La moyenne de dépense semestrielle est: \n' + str(MoyenneSemaine) + '$\n' + 'La moyenne de dépense mensuelle est: \n' + str(MoyenneMois) + '$\n' + 'La moyenne de dépense annuelle est: \n' + str(MoyenneAnnee) + '$'

#Calling DocumentSelector() function and then makes a list out of the document f
DocumentSelector()
f = list(f)

class MyGrid(Widget):
    var1 = ObjectProperty(None)
    var2 = ObjectProperty(None)
    var3 = ObjectProperty(None)
    state = ObjectProperty(None)
    state = "on"

    def btn(self):
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
            float(var1)
            float(var2)
            float(var3)
            Call_Variables()
            Function(a,b,c)
            #self.var1.text = ""
            #self.var2.text = ""
            #self.var3.text = ""
          except ValueError:
            MyGrid.state = 'off'
            pass

##experiment zone
##This now works !!! it serialise the database folder and stores the name.txt in a lit
testexample = open("..\Database\weed.txt")
list(testexample)
printtest = testexample
print(printtest)
from os import listdir
from os.path import isfile, join
#onlyfiles = [f for f in listdir("C:\\Users\Asus\Documents\Git\Weed-App-test\Database\\") if isfile(join("C:\\Users\Asus\Documents\Git\Weed-App-test\Database\\", f))]
#onlyfiles = [f for f in listdir("C:\\Users\Asus\Documents\Git\Weed-App-test\Database\\")]
files = listdir("..\Database\\")
global testfileprint
testfileprint = files[0]
print(testfileprint)
###

#Build the app with my basic widget rest is done in .kv file
class MyApp(App):

    def build(self):
      return MyGrid()

    var = ObjectProperty(None)
    #setting it equal to my default value see Factory.MySecondPopup().label2.text in the kivy file for context
    #this corresponds to the text of my second popup
    var = "bonjour"
    labeltxt = ObjectProperty(None)
    labeltxt = 'hi :)'
    txt = ObjectProperty(None)
    txt = testfileprint

    #This creates a function linked to the button on the home page.
    def btn(self):
      #!!!! OUTPUT !!!!! 
      #        
      #This is the plug to change the value of the text for my second popup
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

    def btn5(self, var66):
      global DocumentName
#      x = ObjectProperty(None)
#      x = Factory.MyHome().docname.text

      if (var66 == ""):
        var66 = default

      DocumentName = str(var66) + ".txt"
      #print(str(x))
      DocumentSelector()


if __name__ == "__main__":
    MyApp().run()