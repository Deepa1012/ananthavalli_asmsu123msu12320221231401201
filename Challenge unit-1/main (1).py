def LeapYear(year):
  return bool(year % 4 == 0 and year % 100 != 0 or year % 400 == 0)

year=2016
if LeapYear(year):
  print("{} is a leap year.".format(year))
else:
  print("{} is not a leap year.".format(year))