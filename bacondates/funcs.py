import re
import datetime as dt
from typing import Union

DateLike = Union[dt.date, dt.datetime]

MONTH_MAX = {
    "1": 31,
    "2": -1,
    "3": 31,
    "4": 30,
    "5": 31,
    "6": 30,
    "7": 31,
    "8": 31,
    "9": 30,
    "10": 31,
    "11": 30,
    "12": 31
    }

def is_leap_year(year: int) -> bool:
    if (dt.date(year, 3, 1) - dt.timedelta(days=1)).day == 29:
        return True
    return False

def add_months(n: int, date: DateLike, fmt: str = None):
    """Increment a date by a number of months.

    Parameters
    ----------
    n : int
        Number of months to increment by.
    
    date : date, datetime, str
        Date to increment. If a string, the format must be specified
        with the `fmt` parameter.
    
    fmt : str, optional
        Format of the date string.

    Returns
    -------
    datetime.date
    """
    if isinstance(date, str):
        date = dt.datetime.strptime(date, fmt)
        _return_type = dt.datetime
    elif isinstance(date, dt.datetime):
        _return_type = dt.datetime
    elif isinstance(date, dt.date):
        _return_type = dt.date
    else:
        raise TypeError('date must be a date, datetime, or str')
    
    dm = divmod(n, 12)
    
    day = date.day
    month_num = date.month + dm[1]
    if month_num > 12:
        year = date.year + dm[0] + 1
        month = month_num - 12
    else:
        year = date.year + dm[0]
        month = month_num
    
    # Ensure that the date is not 'non-existent'
    # If it does NOT exist, it's likely that the 'day' value was set
    #   too high. In this case, the most recent valid date will be
    #   returned  
    # Ex: If 'November 31', return 'November 30'

    if month != 2:
        if date.day <= MONTH_MAX[str(month)]:
            return dt.date(year, month, day)
        else:
            return dt.date(year, month, day - 1)
    else:
        # Check if leap year
        if is_leap_year(year):
            feb_days = 29
        else:
            feb_days = 28
        
        while day > feb_days:
            day -= 1
        
        return dt.date(year, month, day)
