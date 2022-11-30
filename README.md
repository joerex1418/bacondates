# BaconDates

## Overview
This is supposed to be an extremely small conveniece library for dealing with date objects in Python. No third-party dependencies required as the entire point is to make it as lightweight as possible.

There are only a couple functions so far, but more will be added in the future.

### Usage

```python
>>> import bacondates as bd

>>> date1 = dt.date(2022, 8, 9)
>>> print(f"{date1:%B %d, %Y}")
'August 09, 2022'

>>> date2 = bd.add_months(65, date1)
>>> print(f"{date1:%B %d, %Y}")
'January 09, 2028'
```
