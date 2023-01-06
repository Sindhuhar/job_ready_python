# To split the date, we first use the split function to separate the date and time, using the default space character.
# We then split the date into three separate values, specifying the dash as the separator.

d = "2022-12-21 13:27:045367"
(d,t) = d.split()
(year,month,day) = d.split("-")
print(year)
print(month)
print(day)