import calendar
def number_of_days(year,month):
    '''
    This function output the number of calendar days in a given year and month.
    :param year:given year
    :param month:given month
    :return:number of calendar days in a given year and month
    '''
    assert isinstance(year,int) and year>0
    assert isinstance(month,int)
    assert month in range(1,13)
    x = calendar.monthrange(year, month)
    y = x[1]
    return y

def number_of_leap_years(year1,year2):
    '''
    This function  is used to find out the leap-years between
     (including both endpoints) two given years.
    :param year1:given year1
    :param year2:given year2
    :return:leap-years between (including both endpoints) two given years.
    '''
    assert isinstance(year1,int)
    assert isinstance(year2,int)
    assert year1<=year2
    x = calendar.leapdays(year1, year2)
    return x
def get_day_of_week(year,month,day):
    '''
    This function is used to find the string name (e.g., Monday, Tuesday)
     of the day of the week on a given month,day, and year.
    :param year:given year
    :param month:given month
    :param day:given day
    :return:the string name(e.g., Monday, Tuesday)
    '''
    assert isinstance(year,int)
    assert isinstance(month, int)
    assert isinstance(day, int)
    assert month in range(1,13)
    assert day in range(1,number_of_days(year,month)+1)
    x=calendar.weekday(year,month,day)
    x=str(x)
    dict={'0':'Monday','1':'Tuesday','2':'Wednesday','3':'Thursday','4':'Friday','5':'Saturday','6':'Sunday'}

    return dict.get(x)

