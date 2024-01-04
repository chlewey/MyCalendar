# MyCalendar
 CalendarPrinter

usage: `mycalendar.py [-h] [-t] [-p] [-f COUNTRY] [-l LANGUAGE] [-c COLUMNS] [-v] [-d FIRST_DAY] [year] [year_to]`

Calendar generator

| Usage | |
| ---- | ---- |
| **Positional arguments:** | |
| `year`                    | Year (First year) |
| `year_to`                 | Last Year         |
| **Options:**              | |
| `-h`, `--help`            | show this help message and exit |
| `-t`, `--test`            | Test mode                       |
| `-p`, `--easter`          | Only calculate Easter           |
| **Location:**             | |
| `-f COUNTRY`, `--holidays COUNTRY`      | Country code for holidays |
| `-l LANGUAGE`, `--language LANGUAGE`    | Display language          |
| **Display:**                            | |
| `-c COLUMNS`, `--columns COLUMNS`       | Columns of months to display            |
| `-v`, `--vertical`                      | Display months vertically               |
| `-d FIRST_DAY`, `--first-day FIRST_DAY` | First day of week; 0: Sunday, 1: Monday |

## Limitations

 1. Exclusive Gregorian calendar (which means Propleptic Gregorian calendar before 1582)
 1. Definition of holidays are according to current laws, which means that they estrapolate to years before they were implemented.
 1. Gauß formula for Computus paschalis is used. This is the current formula used by most Christian churches but might vary for actual celebrations before the Gregorian reform.

## Default settings

 1. Current year.
 1. No holidays.
 1. Labels in Spanish.
 1. Sunday as first day of the week.
 1. Three columns, horizontal arrangement (first row is January to March).
