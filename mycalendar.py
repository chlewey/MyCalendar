#!/bin/python3
from colorama import Fore, Back, Style
import pickle
fmt_norm = '{:3}'
fmt_fest = Fore.RED + Style.BRIGHT + '{:3}' + Style.RESET_ALL
fmt_domi = Fore.RED + Style.DIM  + '{:3}' + Style.RESET_ALL
fmt_semi = Fore.YELLOW + '{:3}' + Style.RESET_ALL
fmt_saba = Fore.BLUE + '{:3}' + Style.RESET_ALL
fmt_blank = '   '
fmt_label = ' ' + Fore.BLACK + Back.BLUE + '{:^20s}' + Style.RESET_ALL

months = []
weekdays = []
date_str_format = '{0:d} {1:s}'
date_num_format = '{1:d}/{0:d}'
date_order = [0,1]

class MonthArray:
    def __init__(self):
        self._months_normal = [ 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
        self._months_lap = [ 0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
        self._acum_normal = [ sum(self._months_normal[:n]) for n in range(len(self._months_normal)+1) ]
        self._acum_lap = [ sum(self._months_lap[:n]) for n in range(len(self._months_lap)+1) ]

    def __call__(self, yearday, lap=False, at_March=False):
        acum = self._acum_lap if lap else self._acum_normal
        if lap and at_March:
            yearday -= 1
        for m in range(len(acum)):
            if acum[m] < yearday:
                mon = m
                day = yearday - acum[m]
        return day, mon
    
    def last_day(self, month, lap=False):
        if lap:
            return self._months_lap[month]
        else:
            return self._months_normal[month]
    
    def days(self, month, day, lap=False, at_March=False):
        #print(f"DEB: {month}: {self._acum_normal[month]} {self._acum_lap[month]} {lap}")
        if lap:
            return self._acum_lap[month] + day - (1 if at_March else 0)
        else:
            return self._acum_normal[month] + day
    
class Date:
    montharr = MonthArray()

    def __init__(self, day, month=None, lap=False, at_March=False):
        if month is None:
            if isinstance(day, int):
                self._day, self._month = self.montharr(day, lap, at_March)
            elif day is Date:
                self._day = day._day
                self._month = day._month
                self._lap = day._lap
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
        self._lap = lap

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
        return date_num_format.format(self._day, self._month)
    
    def __format__(self, fmt):
        if fmt=='':
            return self.__str__()
        elif 's' in fmt:
            s = date_str_format.format(self._day, months[self._month])
            return format(s, fmt)
        else:
            return format(self[date_order[0]], fmt) + '/' + format(self[date_order[1]], fmt)
        
    def __tuple__(self):
        return (self._month, self._day)

    def year_day(self, at_March=False):
        return self.montharr.days(self._month, self._day, self._lap, at_March)
        
class Year:
    montharr = MonthArray()

    def __init__(self, year):
        year = int(year)
        self._year = year
        self._index = (year + year//4 - year//100 + year//400) % 7
        self._lap = ( year%4 == 0 and year%100 != 0 or year%400 == 0 )
    
    def __int__(self):
        return self._year
    
    def __str__(self):
        return str(self._year)
    
    def __format__(self, fmt):
        if 's' in fmt:
            return format(str(self._year), fmt)
        else:
            return format(self._year, fmt)
    
    def is_lap(self):
        return self._lap
    
    def firstJan(self):
        return (self._index + (6 if self._lap else 0)) % 7
    
    def firstMarch(self):
        return (self._index + 3) % 7
    
    def first(self, month):
        ac = self.montharr._acum_normal[month] + self._index
        if month<=2 and self._lap:
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
        delta = 82 if self._lap and not as_date else 81
        return Date(delta + days) if as_date else delta + days
    
    def date(self, days, at_March=False):
        return Date( days, lap=self._lap, at_March=at_March )
    
    def week_day(self, date, at_March=True):
        if isinstance(date, tuple):
            date = Date(date, lap=self._lap)
        days = date.year_day(at_March)
        return (self._index + days - 1) % 7
    
    def next(self, week_day, date, at_March=True):
        days = date.year_day(at_March)
        wd = self.week_day(date)
        days += (week_day - wd) % 7
        return Date( days, lap=self._lap, at_March=at_March )
    
    def prt_week(self, first, month, holidays=None, semidays=None, last=None):
        if last is None:
            last = self.montharr.last_day(month)
        s = ''
        for n in range(first, first+7):
            if n<1 or n>last:
                s += fmt_blank
                continue
            d = Date(n, month, lap=self._lap)
            wd = self.week_day(d)
            if holidays and d in holidays:
                s += fmt_fest.format(n)
            elif semidays and d in semidays:
                s += fmt_semi.format(n)
            elif wd == 0:
                s += fmt_domi.format(n)
            elif wd == 6:
                s += fmt_saba.format(n)
            else:
                s += fmt_norm.format(n)
        return s
    
class DateList:
    def __init__(self, year):
        self._year = Year(year)
        self._dates = []

    def add(self, day, month=None, next=None, at_March=False):
        date = None
        lap = self._year.is_lap()
        if isinstance( month, str ):
            if month.lower() in months:
                month = months.index(month.lower())
            elif month.lower() in ('pascua', 'easter'):
                easter = self._year.computus(False)
                date = Date( easter+day, lap=lap, at_March=at_March )
        if date is None:
            date = Date( day, month, lap, at_March )
        if next is not None:
            date = self._year.next(next, date, at_March)
        self._dates.append(date)
        return date
    
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

def make_calendar(year, columns=3, vertical=False, language='es', holidays=None, semidays=None, sep='  ', first=0):
    rows = (12 // columns) + (12 % columns > 0)
    year_fmt = ' {:^' + str(columns * (len(sep)+21) - len(sep) - 1) + 's}'
    print( year_fmt.format(year) )
    for row in range(rows):
        labels = []
        lines = [[] for r in range(6)]
        for col in range(columns):
            month = 1 + row + col*rows if vertical else 1 + row*columns + col
            if month>12:
                continue
            labels.append( fmt_label.format(months[month]) )
            d = -((year.first(month) - first - 1) % 7)
            for w in range(6):
                s = year.prt_week(d+7*w, month, holidays, semidays)
                lines[w].append( s )
        print( sep.join(labels) )
        for line in lines:
            print( sep.join(line) )

def get_holidays(year, country_code):
    try:
        holiday_data = pickle.load(open('holidays_' + country_code.lower() + '.bin', 'rb'))
    except FileNotFoundError:
        raise FileNotFoundError(f'No holidays files for country {country_code.lower()}.')
    holidays = DateList( year )
    semidays = DateList( year )
    for key, items in holiday_data.items():
        if key=='FIX':
            for m,d in items:
                holidays.add( d, m )
        elif key=='@FIX':
            for m,d in items:
                semidays.add( d, m )
        elif key[:2]=='N:':
            for m,d in items:
                holidays.add( d, m, next=int(key[2:]) )
        elif key[:3]=='@N:':
            for m,d in items:
                semidays.add( d, m, next=int(key[3:]) )
        elif key[1]==':':
            p,q = int(key[0]), int(key[2:])
            if p < q:
                tg = range(p, q)
            else:
                tg = list(range(p, 7)) + list(range(0, q))
            for m,d in items:
                if year.week_day((d,m)) in tg:
                    holidays.add( d, m, next=q )
                else:
                    holidays.add( d, m )
        elif key[0]=='@' and key[2]==':':
            p,q = int(key[1]), int(key[3:])
            if p < q:
                tg = range(p, q)
            else:
                tg = list(range(p, 7)) + list(range(0, q))
            for m,d in items:
                if year.week_day((d,m)) in tg:
                    semidays.add( d, m, next=q )
                else:
                    semidays.add( d, m )
        elif key=='PASC':
            for d in items:
                holidays.add( d, 'Pascua' )
        elif key=='@PASC':
            for d in items:
                semidays.add( d, 'Pascua' )
    return holidays, semidays

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

    label_file = 'labels_' + args.language.lower() + '.bin'
    try:
        labels = pickle.load(open(label_file, 'rb'))
    except FileNotFoundError:
        raise FileNotFoundError(f'No lables files for language {args.language.lower()}.')
    months = labels['MONTHS']
    weekdays = labels['WEEKDAYS']
    date_str_format = labels['FORMAT_STR']
    date_num_format = labels['FORMAT_NUM']
    date_order = labels['ORDER']

    if args.country:
        try:
            festivities = pickle.load(open('holidays_' + args.country.lower() + '.bin', 'rb'))
        except FileNotFoundError:
            raise FileNotFoundError(f'No holidays files for country {args.country.lower()}.')

    if args.year_to is None:
        args.year_to = args.year
    for y in range(args.year, args.year_to+1):
        year = Year(y)
        if args.test:
            easter = year.computus()
            print( year, year.is_lap() )
            print( f'{easter:s}, {easter:d}, {easter}' )
            print( [year.first(n) for n in range(1, 13)] )
            if args.country:
                holidays, _ = get_holidays( year, args.country )
                for d in holidays:
                    print( d, weekdays[year.week_day(d)] )
        elif args.easter:
            easter = year.computus()
            print( f'{year}: {easter:s}' )
        else:
            holidays = DateList( year )
            if args.country:
                holidays, semidays = get_holidays( year, args.country )
            else:
                semidays = holidays
            make_calendar( year, args.columns, args.vertical, args.language,
                          holidays=holidays,
                          semidays=semidays,
                          first=args.first_day )
