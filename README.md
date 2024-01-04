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
 1. color scheme is fixed.

## Default settings

 1. Current year.
 1. No holidays.
 1. Labels in Spanish.
 1. Sunday as first day of the week.
 1. Three columns, horizontal arrangement (first row is January to March).

## Examples

    # Colombian holidays, 4 columns horizontal
    python3 mycalendar.py -fco -les -c4

    # US holidays, 3 columns vertical
    python3 mycalendar.py -fus -len-us -v

    # French holidays, 4 columns vertical
    python3 mycalendar.py -ffr -lfr -d1 -vc4

    # Swedish holidays, 6 columns horizontal
    python3 mycalendar.py -fse -lsv -d1 -c6

## TODO

 1. Allow to change color scheme, and posible further optimization.
 1. Include option for Propleptic Julian calendar
 1. Allow automatic adjustment between Julian and Gregorian according to country setting
 1. Add support for changing holiday laws.
 1. Add option for different output formats such as HTML