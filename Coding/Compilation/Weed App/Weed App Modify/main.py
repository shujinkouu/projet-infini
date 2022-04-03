import kivy
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
#Dependencies For the Time Module
import datetime as dt
import pytz
from datetime import date

timezone_nw = pytz.timezone('EST')
x = dt.datetime.now(timezone_nw)
x = x.strftime("%m") + '-' + x.strftime("%d") + '-' + x.strftime("%Y")

global f
f = open("weed.txt", 'a')

def Call_Variables():
  while True:
    try:
      global a
      global b
      a = float(var1)
      b = float(var2)
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
  var1 = "You\'re smoking " + str(c) + " $\nlogit? [y/n]"
  c = '\n' + str (c) + '$' + ' - ' + '[' + x + ']'
  c = str(c)
  d = c

def logit():
  f = ObjectProperty(None)
  print(f)
  if f != open('weed.txt', 'a'):
    f = open('weed.txt', 'a')
  else:
    pass
  if i == 'y':
    f.write(d)
    print('this was logged')
  else:
    print('This wasn\'t logged')
  f.close()

def extrapolate():
  if extrapol == 'y':
    f = open('weed.txt', 'r+')
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

class MyGrid(Widget):
    var1 = ObjectProperty(None)
    var2 = ObjectProperty(None)
    var3 = ObjectProperty(None)
    
    def btn(self):
        global var1
        global var2
        global var3
        var1 = self.var1.text
        var2 = self.var2.text
        var3 = self.var3.text
        Call_Variables()
        Function(a,b,c)
        pass

class MyApp(App):
    def build(self):
      return MyGrid()
    var = ObjectProperty(None)
    var = "bonjour"
    labeltxt = ObjectProperty(None)
    labeltxt = 'hi :)'

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

if __name__ == "__main__":
    MyApp().run()