#!/bin/python3
from colorama import Fore, Back, Style
import pickle

class MonthArray:
    def __init__(self):
        self._months_normal = [ 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
        self._months_leap = [ 0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
        self._acum_normal = [ sum(self._months_normal[:n]) for n in range(len(self._months_normal)+1) ]
        self._acum_leap = [ sum(self._months_leap[:n]) for n in range(len(self._months_leap)+1) ]

    def __call__(self, yearday, leap=False, at_March=False):
        acum = self._acum_leap if leap else self._acum_normal
        if leap and at_March:
            yearday -= 1
        for m in range(len(acum)):
            if acum[m] < yearday:
                mon = m
                day = yearday - acum[m]
        return day, mon
    
    def last_day(self, month, leap=False):
        if leap:
            return self._months_leap[month]
        else:
            return self._months_normal[month]
    
    def days(self, month, day, leap=False, at_March=False):
        if leap:
            return self._acum_leap[month] + day - (1 if at_March else 0)
        else:
            return self._acum_normal[month] + day
    
class Date:
    montharr = MonthArray()

    def __init__(self, day, month=None, leap=False, at_March=False):
        if month is None:
            if isinstance(day, int):
                self._day, self._month = self.montharr(day, leap, at_March)
            elif day is Date:
                self._day = day._day
                self._month = day._month
                self._leap = day._leap
            else:
                try:
                    self._day = day[0]
                    self._month = day[1]
                except IndexError:
                    self._day = day.day
                    self._month = day.month
        else:
            self._day = day
            self._month = month
        self._leap = leap

    @property
    def day(self):
        return self._day

    @property
    def month(self):
        return self._month
    
    def __getitem__(self, idx):
        if idx == 0:
            return self._day
        elif idx == 1:
            return self._month
        else:
            raise IndexError
        
    def __str__(self):
        return Calendar.format_value(self, 'short')
    
    def __format__(self, fmt):
        if fmt=='':
            return self.__str__()
        elif 's' in fmt:
            s = Calendar.format_value(self, 'long')
            return format(s, fmt)
        else:
            return format(self[Calendar.day_order()], fmt) + '/' + format(self[Calendar.month_order()], fmt)
        
    def __tuple__(self):
        return (self._month, self._day)

    def year_day(self, at_March=False):
        return self.montharr.days(self._month, self._day, self._leap, at_March)
        
class Year:
    _fmt = {
        'norm': '{:3}',
        'fest': Fore.RED + Style.BRIGHT + '{:3}' + Style.RESET_ALL,
        'domi': Fore.RED + Style.DIM  + '{:3}' + Style.RESET_ALL,
        'semi': Fore.YELLOW + '{:3}' + Style.RESET_ALL,
        'saba': Fore.BLUE + '{:3}' + Style.RESET_ALL,
        'blank': '   ',
        'label': ' ' + Fore.BLACK + Back.BLUE + '{:^20s}' + Style.RESET_ALL
    }
    montharr = MonthArray()

    def __init__(self, year):
        year = int(year)
        self._year = year
        self._index = (year + year//4 - year//100 + year//400) % 7
        self._leap = ( year%4 == 0 and year%100 != 0 or year%400 == 0 )

    @classmethod
    def format_value(cls, value, value_type='norm'):
        return cls._fmt[value_type].format(value)
    
    def __int__(self):
        return self._year
    
    def __str__(self):
        return str(self._year)
    
    def __format__(self, fmt):
        if 's' in fmt:
            return format(str(self._year), fmt)
        else:
            return format(self._year, fmt)
    
    def is_leap(self):
        return self._leap
    
    def firstJan(self):
        return (self._index + (6 if self._leap else 0)) % 7
    
    def firstMarch(self):
        return (self._index + 3) % 7
    
    def first(self, month):
        ac = self.montharr._acum_normal[month] + self._index
        if month<=2 and self._leap:
            return (ac-1) % 7
        else:
            return ac % 7
    
    def computus(self, as_date=True):
        year = self._year
        a = year % 19
        b = year % 4
        c = year % 7
        k = year // 100
        p = (13 + 8 * k) // 25
        q = k // 4
        M = (15 - p + k - q) % 30
        N = (4 + k - q) % 7
        d = (19 * a + M) % 30
        e = (2 * b + 4 * c + 6 * d + N) % 7
        days = d + e
        if days == 35:
            days = 28
        elif d == 28 and e == 6 and a > 10:
            days = 27
        delta = 82 if self._leap and not as_date else 81
        return Date(delta + days) if as_date else delta + days
    
    def date(self, days, at_March=False):
        return Date( days, leap=self._leap, at_March=at_March )
    
    def week_day(self, date, at_March=True):
        if isinstance(date, tuple):
            date = Date(date, leap=self._leap)
        days = date.year_day(at_March)
        return (self._index + days - 1) % 7
    
    def next(self, week_day, date, at_March=True):
        days = date.year_day(at_March)
        wd = self.week_day(date)
        days += (week_day - wd) % 7
        return Date( days, leap=self._leap, at_March=at_March )
    
    def prt_week(self, first, month, holidays=None, semidays=None, last=None):
        if last is None:
            last = self.montharr.last_day(month)
        s = ''
        for n in range(first, first+7):
            if n<1 or n>last:
                s += self._fmt['blank']
                continue
            d = Date(n, month, leap=self._leap)
            wd = self.week_day(d)
            if holidays and d in holidays:
                s += self.format_value(n, 'fest')
            elif semidays and d in semidays:
                s += self.format_value(n, 'semi')
            elif wd == 0:
                s += self.format_value(n, 'domi')
            elif wd == 6:
                s += self.format_value(n, 'saba')
            else:
                s += self.format_value(n)
        return s
    
class DateList:
    def __init__(self, year):
        self._year = Year(year)
        self._dates = []

    def add(self, day, month=None, next=None, at_March=False):
        date = None
        leap = self._year.is_leap()
        if isinstance( month, str ):
            if month.lower() in ('pascua', 'easter'):
                easter = self._year.computus(False)
                date = Date( easter+day, leap=leap, at_March=at_March )
            else:
                month = Calendar.month_index(month) or int(month)
        if date is None:
            date = Date( day, month, leap, at_March )
        if next is not None:
            date = self._year.next(next, date, at_March)
        self._dates.append(date)
        return date
    
    def add_list(self, dates, at_March=False):
        if not dates: return
        for date in dates:
            month, day = tuple(date)
            self.add(day, month, at_March=at_March)
    
    def sort(self):
        self._dates.sort(key = lambda d: d.year_day() )

    def __iter__(self):
        return iter(self._dates)
    
    def __getitem__(self, idx):
        return self._dates[idx]
    
    def __contains__(self, date):
        return tuple(date) in [tuple(d) for d in self._dates]
    
    def __len__(self):
        return len(self._dates)
    
    def __bool__(self):
        return bool(self._dates)
    
    def __str__(self):
        ar = [str(d) for d in self._dates]
        return '[' + ', '.join(ar) + ']'

    def __format__(self, fmt):
        ar = [format(d, fmt) for d in self._dates]
        return '[' + ', '.join(ar) + ']'
    
    def _reset(self):
        self._dates = []

class Calendar(Year):
    _months = []
    _months_d = []
    _weekdays = []
    _date_str_format = '{0:d} {1:s}'
    _date_num_format = '{1:d}/{0:d}'
    _date_order = [0,1]

    def __init__(self, year, language='es', country=None, holidays=None, semidays=None, columns=3, vertical=False, first_day=0, args=None):
        super().__init__(year)
        self._holidays = [ DateList(year), DateList(year) ]
        self._sep = '  '
        if args:
            self._first = args.first_day
            self._columns = args.columns
            self._vertical = args.vertical
            self._set_language(args.language)
            self._set_country(args.country)
        else:
            self._first = first_day
            self._holidays[0].add_list(holidays)
            self._holidays[1].add_list(semidays)
            self._columns = columns
            self._vertical = vertical
            self._set_language(language)
            self._set_country(country)

    @classmethod
    def format_value(cls, value, fmt_type='norm'):
        if fmt_type in cls._fmt:
            return cls._fmt[fmt_type].format(value)
        if isinstance(value, int):
            month, day = value, value
            wd = value % 7
        elif isinstance(value, Date):
            month, day = value.month, value.day
        elif isinstance(value, tuple):
            month, day = value
        if fmt_type == 'month':
            return cls._months[month]
        if fmt_type == 'month_d':
            return cls._months_d[month]
        if fmt_type == 'weekday':
            return cls._weekdays[value]
        if fmt_type == 'long':
            return cls._date_str_format.format(day, cls._months_d[month])
        if fmt_type == 'short':
            return cls._date_num_format.format(day, month)
        if '{' in fmt_type:
            fmt_type.format(value)
        return value.__format__(fmt_type)
    
    @classmethod
    def month_index(cls, month):
        month = month.lower()
        months = [m.lower() for m in cls._months]
        if month in months:
            return months.index(month)
        months = [m.lower() for m in cls._months_d]
        if month in months:
            return months.index(month)
        return False
    
    @classmethod
    def day_order(cls):
        return cls._date_order[0]
    
    @classmethod
    def month_order(cls):
        return cls._date_order[1]
    
    def weekday(self, day):
        if isinstance(day, Date):
            day = self.week_day(day)
        return self._weekdays[day]
    
    def _set_language(self, language):
        self._language = language.lower()
        label_file = 'labels_' + self._language + '.bin'
        try:
            with open(label_file, 'rb') as file:
                labels = pickle.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f'No labels file for language {language}.')
        Calendar._months = labels['MONTHS']
        Calendar._months_d = labels['MONTHS_D'] if 'MONTHS_D' in labels else labels['MONTHS']
        Calendar._weekdays = labels['WEEKDAYS']
        Calendar._date_str_format = labels['FORMAT_STR']
        Calendar._date_num_format = labels['FORMAT_NUM']
        Calendar._date_order = labels['ORDER']

    def _set_country(self, code):
        if code == -1:
            self._country_code = None
            self._holidays[0]._reset()
            self._holidays[1]._reset()
        elif code:
            self._country_code = code.lower()
            holidays_file = 'holidays_' + self._country_code + '.bin'
            try:
                with open(holidays_file, 'rb') as file:
                    holiday_dict = pickle.load(file)
            except FileNotFoundError:
                raise FileNotFoundError(f'No holidays file for country {code}.')
            self.add_holidays(holiday_dict)
        else:
            self._country_code = None

    @property
    def year(self):
        return int(self)
    
    @year.setter
    def year(self, value: int):
        super().__init__(value)
    
    @property
    def language(self):
        return self._language
    
    @language.setter
    def language(self, code):
        self._set_language(code)

    @property
    def country(self):
        return self._country_code
    
    @country.setter
    def country(self, code):
        self._set_country(code)

    @property
    def columns(self):
        return self._columns
    
    @columns.setter
    def columns(self, number: int):
        assert 0 < number <= 12
        self._columns = number

    @property
    def rows(self):
        return (12 // self._columns) + (12 % self._columns > 0)

    @property
    def vertical(self):
        return self._vertical
    
    @vertical.setter
    def vertical(self, value: bool):
        self._vertical = value

    @property
    def sep(self):
        return self._sep
    
    @sep.setter
    def sep(self, value: str):
        self._sep = value

    @property
    def first_day(self):
        return self._first
    
    @first_day.setter
    def first_day(self, value: int):
        self._first = value % 7
    
    @property
    def easter(self):
        return self.computus(as_date=True)

    def add_holiday(self, day, month, next=None, at_March=False, semi=False):
        index = 1 if semi else 0
        self._holidays[index].add(day, month, next=next, at_March=at_March)

    def add_holidays(self, holidays, semi=False):
        index = int(semi)
        if isinstance(holidays, (list, DateList)):
            self._holidays[index].add_list(holidays)
        elif isinstance(holidays, (tuple, Date)):
            month, day = tuple(holidays)
            self._holidays[index].add(day, month)
        elif isinstance(holidays, dict):
            for key, items in holidays.items():
                index = int(key[0]=='@')
                key = key[index:]

                if ':' in key:
                    pre, target = key.split(':')
                    target = int(target)
                    if pre == 'N':
                        for m, d in items:
                            self._holidays[index].add(d, m, next=target)
                    elif pre[0] == 'M':
                        pre = int(pre[1:])
                        if pre < target:
                            target_range = list(range(pre, target))
                        else:
                            target_range = list(range(pre, 7)) + list(range(0, target))
                        for m, d in items:
                            if self.week_day((d, m)) not in target_range:
                                self._holidays[index].add(d, m, next=target)
                            else:
                                self._holidays[index].add(d, m)
                    else:
                        pre = int(pre)
                        if pre < target:
                            target_range = list(range(pre, target))
                        else:
                            target_range = list(range(pre, 7)) + list(range(0, target))
                        for m, d in items:
                            if self.week_day((d, m)) in target_range:
                                self._holidays[index].add(d, m, next=target)
                            else:
                                self._holidays[index].add(d, m)
                elif key == 'FIX':
                    for m, d in items:
                        self._holidays[index].add(d, m)
                elif key == 'PASC':
                    for d in items:
                        self._holidays[index].add(d, 'Pascua')
        return self._holidays[int(semi)]

    def _reset(self, columns=None, vertical=None, language=None, sep=None, first=None, holidays=None, semidays=None):
        if columns is not None:
            self.columns = columns
        if vertical is not None:
            self.vertical = vertical
        if language is not None:
            self.language = language
        if sep is not None:
            self.sep = sep
        if first is not None:
            self.first_day = first
        return (self.columns, self.rows, self.vertical,
                self.language, self.sep, self.first_day,
                self._holidays[0] if holidays is None else holidays,
                self._holidays[1] if semidays is None else semidays)

    def __call__(self, write=False, columns=None, vertical=None, language=None, holidays=None, semidays=None, sep=None, first=None):
        columns, rows, vertical, language, sep, first, holidays, semidays = self._reset(columns, vertical, language, sep, first, holidays, semidays)
        output = []

        year = int(self)
        year_fmt = ' {:^' + str(columns * (len(sep) + 21) - len(sep) - 1) + 's}'
        output.append(year_fmt.format(str(year)))

        for row in range(rows):
            labels = []
            lines = [[] for _ in range(6)]

            for col in range(columns):
                month = 1 + row + col * rows if vertical else 1 + row * columns + col

                if month > 12:
                    continue

                labels.append(self._fmt['label'].format(self._months[month]))
                d = -((self.first(month) - first - 1) % 7)

                for w in range(6):
                    s = self.prt_week(d + 7 * w, month, holidays, semidays)
                    lines[w].append(s)

            output.append(sep.join(labels))

            for line in lines:
                output.append(sep.join(line))
        
        if write:
            print('\n'.join(output))
        else:
            return '\n'.join(output)
    
    def test(self, write=False):
        easter = self.easter
        output = []
        output.append(f'{self.year}: {self.is_leap()}')
        output.append( f'{easter:s}, {easter:d}, {easter}' )
        output.append( '(' + ', '.join([self._weekdays[self.first(n)] for n in range(1, 13)]) + ')' )
        for d in self._holidays[0]:
            output.append( f'{d}, {self.weekday(d)}' )
        if write:
            print('\n'.join(output))
        else:
            return '\n'.join(output)

    def test_easter(self, write=False):
        string = f'{self.year}: {self.easter:s}'
        if write:
            print(string)
        else:
            return string

if __name__ == '__main__':
    import argparse
    from datetime import date
    today = date.today()

    parser = argparse.ArgumentParser(description='Calendar generator')
    parser.add_argument('year', type=int, default=today.year, nargs='?', help='Year')
    parser.add_argument('year_to', type=int, default=None, nargs='?', help='Last Year')
    parser.add_argument('-t', '--test', action='store_true', help='Test mode')
    parser.add_argument('-p', '--easter', action='store_true', help='Only calculate Easter')
    location = parser.add_argument_group('Location')
    location.add_argument('-f', '--holidays', dest='country', type=str, default=None, help='Country code for holidays')
    location.add_argument('-l', '--language', type=str, default='es', help='Display language')
    display = parser.add_argument_group('Display')
    display.add_argument('-c', '--columns', type=int, default=3, help='Columns of months to display')
    display.add_argument('-v', '--vertical', action='store_true', help='Display months vertically')
    display.add_argument('-d', '--first-day', type=int, default=0, help='First day of week; 0: Sunday, 1: Monday')

    args = parser.parse_args()

    year_to = args.year_to or args.year
    for y in range(args.year, year_to+1):
        frame = Calendar(y, args=args)
        if args.test:
            frame.test(True)
        elif args.easter:
            frame.test_easter(True)
        else:
            frame(True)
            if y!=year_to:
                print()
