# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 


month = input('Enter the month of the year (Jan - Dec): ')
day = input('Enter the day of the month: ')

if month in ('Jan', 'Feb', 'Mar'):
  season = 'Winter'
elif month in ('Apr', 'May', 'Jun'):
  season = 'Spring'
elif month in ('Jul', 'Aug', 'Sept'):
  season = 'Summer'
elif month in ('Oct', 'Nov', 'Dec'):
  season = 'Autumn'

if month == 'Mar' and day > 19:
  season = 'Spring'
elif month == 'Jun' and day > 20:
  season = 'Summer'
elif month == 'Sep' and day > 21:
  season = 'Fall'
elif month == 'Dec' and day > 21:
  season = 'Winter'  

print(f'{month} {day} is in {season}')