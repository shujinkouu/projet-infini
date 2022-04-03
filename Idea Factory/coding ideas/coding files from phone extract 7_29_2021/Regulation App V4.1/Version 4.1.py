# importing datetime as dt and pytz for accurate EST time in the time module
import datetime as dt
import pytz

#this has been put on comment for now to test if it is useful {2020-05-07}
from datetime import date

# This is the time module it imports utc convert it to est and stores it
# in the variable X for later output to the user
timezone_nw = pytz.timezone('EST')
x = dt.datetime.now(timezone_nw)
x = x.strftime("%m") + '-' + x.strftime("%d") + '-' + x.strftime("%Y")

#this code opens a document for appending
#f = open ( 'tes01' , 'a' )
f = open('weed.txt', 'a')

#this is the unit conversion function it takes a price and b unit as well as c unit and tells you the price of c which should be a fraction of b. So this output the corresponding fraction of a.

'''a = what you paid ; b = how many gram you bought ;
c = how much you're smoking in grams ;
this function return how much the weed you're smoking cost'''

def Function(a,b,c):
  c = (a / b) * c
#this code rounds c to 2 digit after the .
  c = round(c, 2)
  print('\nYou\'re smoking', c, '$')

# this formats the output string as $ amount - [MM-DD-YYYY]\n
  c = '\n' + str (c) + '$' + ' - ' + '[' + x + ']'
# this writes the c string in the opened document if the user input 'y'
# This ask the user if he wants to logit and stock the answer in the i variable.
  i = input('logit? [y/n]')
# If the user answer is the string 'y' it logs the data using f.write() and print that it was successfully logged
  if i == 'y':
    f.write(c)
    print('this was logged')
# Else it prints to the user that it wasn't logged
  else:
    print('This wasn\'t logged')
  
# No matter what the answer is this closes the document
  f.close()

#those are fixed value for a and b
a=165
b=28

# This piece has been put in comment since it has been re-added with a security
# measure to ensure the user always enter valid data.
# c=float(input('How many grams are you\nsmoking?\n'))

# This contraption ensure the user furnish valid data
while True:
  try:
# Those are prompt for dynamic value of a and b as well as c it converts a and b in integers and c as a float. a and b are in comment since we are using fix value for them right now.
# a = int(input('how much did you pay\n'))
# b = int(input('how many gram did you buy\n'))
    c=float(input('How many grams are you\nsmoking?\n'))
    # How many squares of chocolate \nare you eating?
# This piece of code acts in a way where if there is any error at the previous step it just loops back on itself
  except ValueError:
    pass
# This piece of code ensure that if there is no error the loop stops.
  else:
    break

# Calling my weed function
Function(a,b,c)

# Prints the date
print('\nOn est en date du\n'+ x)

# This is just a piece of code for testing purposes to know if the code successfully ran
# Print('\n\n\nSucessfully ran')


# Everything up was already commented and done in version 3.1 it's all clean
# Everything down needs some work and comment before version 4.0 can be finished
# ---------------------------------------
# From this point this is new code
# This all comes from a repl called experiments:
# https://repl.it/@merlierj/Experiments

'''
This is an extrapolator it extracts lines from weed.txt and read them outputs total
and devides it by the number of days to get an average and then use that average to
make prediction nd extrapolate, the goal of the next update (4.1) is to be able to
extrapolate based on the current week or based on yesterday or the current day.

Some of the code before the while loop is redundant and dates the time I was testing
and trying out things most of it is non necessary anymore and should be cleaned and
removed for the final version of 4.0
'''

# Option as to ask a question or run the new code
extrapol = input('\nDo you want to extrapol? [y/n]')
# extrapol = 'y'

#If the new code is to run 
if extrapol == 'y':
  # This opens the document
  f = open('weed.txt', 'r+')
  # This saves the document as a list
  f = list(f)
  
  # Setting up my variables
  # Counter is gonna be used to count the number of times the while loop iterates
  # Moyenne takes the Total and and then devides it by the number of days (DayCounter)
  # Last_ Variables will be user to compare last with current of dates to accurately count the
  # number of different days
  # DayCounter counts the number of different days
  # Total is gonna be incremented by all my $ data to make the total $ amount
  counter = 0
  moyenne = 0
  LastMonth = 0
  LastYear = 0
  LastDay = 0
  DayCounter = 0
  Total = 0
  
  # Setting up the lenght variables it equals the number of lines in f
  lenght = len(f)
# test code fore lenght of the list
#  print(len(f))

  # This is the start of my while loop it will stops once it will have iterated through every line in my document.
  while counter<lenght:
    # This makes b equal to the current line (starting at the first line finishing with the last)
    b = f[counter]
    
    # This splits the current line by the - thus creating a list with my 4 informations, amount being the first then month, day, year
    b = b.split('-')
    ''' this is new code and needs to be commented to update to 4.1 this code gives an accurate time delta of weed.txt '''
    # Here I'm opening an if that will save the initial variable, so all the variable stored in the first line of weed.txt
    if counter == 0:
      # This is new variables to save my variable corresponding to the first line
      InitialAmount = b[0]
      InitialMonth = b[1]
      InitialDay = b[2]
      InitialYear = b[3]
      # This is formating for my variables so they are usable in the rest of my code
      InitialMonth = int(InitialMonth[InitialMonth.find('[')  +1:])
      InitialYear = int(InitialYear[:InitialYear.find(']')])

      # This is a debug line it's there so I'm able to read what is stored at this step 
      #print('Initial:\n' + str(InitialAmount) + str(InitialMonth) + str(InitialDay) + str(InitialYear) + '\n')

    # This is new variables to save my variable corresponding to the last line
    if counter == lenght -1:
    
      # This is new variables to save my variable corresponding to the last line
      FinalAmount = b[0]
      FinalMonth = b[1]
      FinalDay = b[2]
      FinalYear = b[3]
      # This is formating for my variables so they are usable in the rest of my code
      FinalMonth = int(FinalMonth[FinalMonth.find('[') + 1:])
      FinalYear = int(FinalYear[:FinalYear.find(']')])
      
      # This is a debug line it's there so I'm able to read what is stored at this step 
      #print('Final:\n' + str(FinalAmount) + str(FinalMonth) + str(FinalDay) + str(FinalYear) + '\n')   

      # This is converting my different saved variable to int for the first and last line of weed.txt and then converting them in dates then storing those in D0 and D1 then doing the delta between those two by subtracting my initial line variable to the final line variable so I get a dela that I then convert in a delta in days that I then store in deltadays so that I can calculate my average using this
      d0 = date(int(InitialYear), int(InitialMonth), int(InitialDay))
      d1 = date(int(FinalYear), int(FinalMonth), int(FinalDay))
      delta = d1 - d0
      #print('il y a: ' + str(delta.days))
      #fixed a bug by adding 1 to the delta simply because delta represent the difference not the count. to get the count, count = difference + 1. assuming theres always at least one day (today)
      deltadays = delta.days + 1
      #print(deltadays)
      
    # Incrementing the counter so that it text the next line the next time through the loop
    counter = counter + 1


    # This is saving my four variable for the current line in diffecerent variables
    amount = b[0]
    month = b[1]
    jour = b[2] 
    annee = b[3]
    # This is formating my variable for use, removing '$' as well as  '[]' so I end up with
    # only usable information
    amount = amount[:amount.find('$')]
    month = month[month.find('[') + 1:]
    annee = annee[:annee.find(']')]

    # Incrementing my total with the current line amount
    Total = float(Total) + float(amount)
    # Rouding my total so it's readable
    Total = round(Total, 2)

    # This is code for the dayCounter it compares Last_ variable with current variables
    # so that if they match the day isn't counted and if they don't match the day is counted as being different
    if LastMonth == month and LastYear == annee and LastDay == jour:
      pass
    # Else we incrementing the day counter
    else:
      DayCounter = DayCounter + 1

    # Here I'm saving my current variation for the comparison the next time through
    LastMonth = month
    LastYear = annee
    LastDay = jour

  # This calculated my moyenne and then prints it as a string
  moyenne = float(Total) / float(deltadays)

  # This rounds the moyenne so it may be used to extrapolation
  moyenne = round(moyenne, 2)

  # This just spits the average as a daily spending
  print('\nla moyenne de dépense journalière est: \n' + str(moyenne) + '$')

  # This calculates the different extrapolated value, for week, month, year.
  MoyenneSemaine = round(moyenne * 7, 2)
  MoyenneMois = round(moyenne * 30.5, 2)
  MoyenneAnnee = round(moyenne * 365, 2) 

  # This prints my different extrapolations
  print('la moyenne de dépense semestrielle est: \n' + str(MoyenneSemaine) + '$')
  print('la moyenne de dépense mensuelle est: \n' + str(MoyenneMois) + '$')
  print('la moyenne de dépense annuelle est: \n' + str(MoyenneAnnee) + '$')