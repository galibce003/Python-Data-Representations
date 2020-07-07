x = "I am Omuk "+\
    "My name is Omuk "+\
    "I am Tomuk"

#after the "+", "\" tells python that I'm not finish yet
#We use it for long string, for readiability



f1 = x.find('am')          #find starts searching from left
print(f1, x[f1])


f1 = x.rfind('am')         #rfind starts searching from right
print(f1, x[f1])


f1 = x.index('am')         #index and find is same
print(f1, x[f1])


f1 = x.rindex('am')        #But if the word isn't in the string
print(f1, x[f1])           #find returns "-1"
                           #index returns Traceback Error



print(x.count('M'))



print(x.startswith("I"))
print(x.endswith("am"))
