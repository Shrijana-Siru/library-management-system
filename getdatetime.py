#getdate fuction is defined using def keyword
def getdate():
    #Importing datetime
    import datetime
    now = datetime.datetime.now
    return str(now().date())#setting time and date

#get_time fuction is defined using def keyword
def get_time():
     #Importing datetime
    import datetime
    now = datetime.datetime.now
    return str(now().time())#setting time and date

