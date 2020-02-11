from time import strptime, strftime

n = input()
string_to_time_format = strptime(n, "%I:%M:%S%p")
converted_time = strftime("%H:%M:%S",string_to_time_format)
print(converted_time)



#strptime() method −

#time.strptime(string[, format])

#Parameters

#   string − This is the time in string format which would be parsed based on the given format.

#  format − This is the directive which would be used to parse the given string.



# so, firstly the 'srtptime' method will take the input n and will convert it
#into a time formated string. then the result will be passed into the
#'strftime' method to convert it into 24 hour format
