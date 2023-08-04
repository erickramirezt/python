# PYTHON DATETIME

# PYTHON DATES
# A DATE IN PYTHON IS NOT A DATA TYPE OF ITS OWN, BUT WE CAN IMPORT A MODULE NAMED DATETIME
# TO WORK WITH DATES AS DATE OBJECTS.

# EXAMPLE
# IMPORT THE DATETIME MODULE AND DISPLAY THE CURRENT DATE:
import datetime

x = datetime.datetime.now()
print(x)

# DATE OUTPUT
# WHEN WE EXECUTE THE CODE FROM THE EXAMPLE ABOVE THE RESULT WILL BE:
# 2020-07-28 12:53:18.993000
# THE DATE CONTAINS YEAR, MONTH, DAY, HOUR, MINUTE, SECOND, AND MICROSECOND.
# THE DATETIME MODULE HAS MANY METHODS TO RETURN INFORMATION ABOUT THE DATE OBJECT.
# HERE ARE A FEW EXAMPLES, YOU WILL LEARN MORE ABOUT THEM LATER IN THIS CHAPTER.

# EXAMPLE
# RETURN THE YEAR AND NAME OF WEEKDAY:
print(x.year)
print(x.strftime("%A"))

# CREATING DATE OBJECTS
# TO CREATE A DATE, WE CAN USE THE DATETIME() CLASS (CONSTRUCTOR) OF THE DATETIME MODULE.
# THE DATETIME() CLASS REQUIRES THREE PARAMETERS TO CREATE A DATE: YEAR, MONTH, DAY.

# EXAMPLE
# CREATE A DATE OBJECT:
x = datetime.datetime(2020, 5, 17)
print(x)

# THE DATETIME() CLASS ALSO TAKES PARAMETERS FOR TIME AND TIMEZONE (HOUR, MINUTE, SECOND,
# MICROSECOND, TZONE), BUT THEY ARE OPTIONAL, AND HAS A DEFAULT VALUE OF 0, (NONE FOR
# TIMEZONE).

# THE strftime() METHOD
# THE DATETIME OBJECT HAS A METHOD FOR FORMATTING DATE OBJECTS INTO READABLE STRINGS.
# THE METHOD IS CALLED strftime(), AND TAKES ONE PARAMETER, FORMAT, TO SPECIFY THE FORMAT OF
# THE RETURNED STRING:

# EXAMPLE
# DISPLAY THE NAME OF THE MONTH:
print(x.strftime("%B"))

# A REFERENCE OF ALL THE LEGAL FORMAT CODES:
# DIRECTIVE     DESCRIPTION	                            EXAMPLE
# %a	        Weekday, short version	                Wed
# %A	        Weekday, full version	                Wednesday
# %w	        Weekday as a number 0-6, 0 is Sunday	3
# %d	        Day of month 01-31	                    31
# %b	        Month name, short version	            Dec
# %B	        Month name, full version	            December
# %m	        Month as a number 01-12	                12
# %y	        Year, short version, without century	18
# %Y	        Year, full version	                    2018
# %H	        Hour 00-23	                            17
# %I	        Hour 00-12	                            05
# %p	        AM/PM	                                PM
# %M	        Minute 00-59	                        41
# %S	        Second 00-59	                        08
# %f	        Microsecond 000000-999999	            548513
# %z	        UTC offset	                            +0100
# %Z	        Timezone	                            CST
# %j	        Day number of year 001-366	            365
# %U	        Week number of year, Sunday as the first day of week,   00-53	52
# %W	        Week number of year, Monday as the first day of week,   00-53	52
# %c	        Local version of date and time	        Mon Dec 31 17:41:00 2018
# %x	        Local version of date	                12/31/18
# %X	        Local version of time	                17:41:00
# %%	        A % character	                        %
# %G            ISO 8601 year	                        2018
# %u	        ISO 8601 weekday (1-7)	                1
# %V	        ISO 8601 weeknumber (01-53)	            01
