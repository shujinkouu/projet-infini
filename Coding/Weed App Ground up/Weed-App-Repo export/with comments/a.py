#import kivy
from kivy.properties import ObjectProperty

global DocumentName
global default
default = "weed"
DocumentName = default + ".txt"


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
