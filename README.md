# dtfuncs

## Usage

```python
>>> import bacondates as bd

>>> date1 = dt.date(2022, 8, 9)
>>> print(f"{date1:%B %d, %Y}")
'August 09, 2022'

>>> date2 = bd.add_months(65, date1)
>>> print(f"{date1:%B %d, %Y}")
'January 09, 2028'
```
