#!/bin/python3
"""Yoy shall edit and run this file to define the labels for the calendar for missing languages and holidays that fix your needs."""
import pickle

# For each language define the months and weekdays
# use a two letter language code for common languages, and hyphen for regional variants, all lowercase.
# 'MONTHS' is a list of month names, shall start with None as firts ([0]) element.
# 'WEEKDAYS' is a list of week day names, shall start with Sunday as firts ([0]) element.
# 'FORMAT_STR' is the format string used to display the date in the calendar in long format. The {0} and {1} are the day and month.
# 'FORMAT_NUM' is the format string used to display the date in the calendar in short format. The {0} and {1} are the day and month.
# 'ORDER' is the order of the day and month in the format string: [0,1] for day first, [1,0] for month first
lab = {
    'ar': { # Arabic
        'MONTHS': [None, 'جانفي', 'فيفري', 'مارس', 'أفريل', 'ماي', 'جوان', 'جويلية', 'أوت', 'سبتمبر', 'أكتوبر', 'نوفمبر', 'ديسمبر'],
        'WEEKDAYS': ['السبت', 'الأحد', 'الاثنين', 'الثلاثاء', 'الأربعاء', 'الخميس', 'الجمعة'],
        'FORMAT_STR': '{0:2d} {1:s}',
        'FORMAT_NUM': '{0:2d}/{1:02d}',
        'ORDER': [0,1]
    },
    'de': { # German
        'MONTHS': [None, 'Januar', 'Februar', 'März', 'April', 'Mai', 'Juni', 'Juli', 'August', 'September', 'Oktober', 'November', 'Dezember'],
        'WEEKDAYS': ['Sonntag', 'Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag'],
        'FORMAT_STR': '{0:2d} {1:s}',
        'FORMAT_NUM': '{0:2d}/{1:02d}',
        'ORDER': [0,1]
    },
    'da': { # Danish
        'MONTHS': [None, 'januar', 'februar', 'marts', 'april', 'maj', 'juni', 'juli', 'august', 'september', 'oktober', 'november', 'december'],
        'WEEKDAYS': ['søndag', 'mandag', 'tirsdag', 'onsdag', 'torsdag', 'fredag', 'lørdag'],
        'FORMAT_STR': '{0:2d} {1:s}',
        'FORMAT_NUM': '{0:2d}/{1:02d}',
        'ORDER': [0,1]
    },
    'el': { # Greek
        'MONTHS': [None, 'Ιανουάριος', 'Φεβρουάριος', 'Μάρτιος', 'Απρίλιος', 'Μάιος', 'Ιούνιος', 'Ιούλιος', 'Αύγουστος', 'Σεπτέμβριος', 'Οκτώβριος', 'Νοέμβριος', 'Δεκέμβριος'],
        'MONTHS_D': [None, 'Ιανουαρίου', 'Φεβρουαρίου', 'Μαρτίου', 'Απριλίου', 'Μαΐου', 'Ιουνίου', 'Ιουλίου', 'Αυγούστου', 'Σεπτεμβρίου', 'Οκτωβρίου', 'Νοεμβρίου', 'Δεκεμβρίου'],
        'WEEKDAYS': ['Κυριακή', 'Δευτέρ', 'Τρίτη', 'Τετάρτη', 'Πέμπτη', 'Παρασκευή', 'Σάββατο'],
        'FORMAT_STR': '{0:2d} {1:s}',
        'FORMAT_NUM': '{0:2d}/{1:02d}',
        'ORDER': [0,1]
    },
    'en': { # English
        'MONTHS': [None, 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
        'WEEKDAYS': ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],
        'FORMAT_STR': '{0:2d} {1:s}',
        'FORMAT_NUM': '{0:2d}/{1:02d}',
        'ORDER': [0,1]
    },
    'en-us': { # English - United States
        'MONTHS': [None, 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
        'WEEKDAYS': ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],
        'FORMAT_STR': '{1:s} {0:2d}',
        'FORMAT_NUM': '{1:2d}/{0:d}',
        'ORDER': [1,0]
    },
    'eo': { # Esperanto
        'MONTHS': [None, 'januaro', 'februaro', 'marto', 'aprilo', 'majo', 'junio', 'julio', 'aŭgusto', 'septembro', 'oktobro', 'novembro', 'decembro'],
        'WEEKDAYS': ['dimanĉo', 'lundo', 'mardo', 'merkredo', 'ĵaŭdo', 'vendredo', 'sabato'],
        'FORMAT_STR': '{0:2d} {1:s}',
        'FORMAT_NUM': '{0:2d}/{1:02d}',
        'ORDER': [0,1]
    },
    'es': { # Spanish
        'MONTHS': [None, 'enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'],
        'WEEKDAYS': ['domingo', 'lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado'],
        'FORMAT_STR': '{0:2d} de {1:s}',
        'FORMAT_NUM': '{0:2d}/{1:02d}',
        'ORDER': [0,1]
    },
    'fi': { # Finnish
        'MONTHS': [None, 'tammikuu', 'helmikuu', 'maaliskuu', 'huhtikuu', 'toukokuu', 'kesäkuu', 'heinäkuu', 'eläkuu', 'syyskuu', 'lokakuu', 'marraskuu', 'joulukuu'],
        'WEEKDAYS': ['sunnuntai', 'maanantai', 'tiistai', 'keskiviikko', 'torstai', 'perjantai', 'lauantai'],
        'FORMAT_STR': '{0:2d} {1:s}',
        'FORMAT_NUM': '{0:2d}/{1:02d}',
        'ORDER': [0,1]
    },
    'fr': { # French
        'MONTHS': [None, 'janvier', 'fevrier', 'mars', 'avril', 'mai', 'juin', 'juillet', 'aout', 'septembre', 'octobre', 'novembre', 'decembre'],
        'WEEKDAYS': ['dimanche', 'lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi'],
        'FORMAT_STR': '{0:2d} de {1:s}',
        'FORMAT_NUM': '{0:2d}/{1:02d}',
        'ORDER': [0,1]
    },
    'it': { # Italian
        'MONTHS': [None, 'gennaio', 'febbraio', 'marzo', 'aprile', 'maggio', 'giugno', 'luglio', 'agosto', 'settembre', 'ottobre', 'novembre', 'dicembre'],
        'WEEKDAYS': ['domenica', 'lunedì', 'martedì', 'mercoledì', 'giovedì', 'venerdì', 'sabato'],
        'FORMAT_STR': '{0:2d} {1:s}',
        'FORMAT_NUM': '{0:2d}/{1:02d}',
        'ORDER': [0,1]
    },
    'ja': { # Japanese
        'MONTHS': [None, '1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月'],
        'WEEKDAYS': ['日', '月', '火', '水', '木', '金', '土'],
        'FORMAT_STR': '{1:s}{0:2d}日',
        'FORMAT_NUM': '{1:2d}-{0:02d}',
        'ORDER': [1,0]
    },
    'ko': { # Korean
        'MONTHS': [None, '1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月'],
        'WEEKDAYS': ['일', '월', '요', '화', '수', '목', '금'],
        'FORMAT_STR': '{1:s}{0:2d}일',
        'FORMAT_NUM': '{1:2d}-{0:02d}',
        'ORDER': [1,0]
    },
    'nl': { # Dutch
        'MONTHS': [None, 'januari', 'februari', 'maart', 'april', 'mei', 'juni', 'juli', 'augustus', 'september', 'oktober', 'november', 'december'],
        'WEEKDAYS': ['zondag', 'maandag', 'dinsdag', 'woensdag', 'donderdag', 'vrijdag', 'zaterdag'],
        'FORMAT_STR': '{0:2d} {1:s}',
        'FORMAT_NUM': '{0:2d}/{1:02d}',
        'ORDER': [0,1]
    },
    'nb': { # Norwegian bokmål
        'MONTHS': [None, 'januar', 'februar', 'mars', 'april', 'mai', 'juni', 'juli', 'august', 'september', 'oktober', 'november', 'desember'],
        'WEEKDAYS': ['søndag', 'mandag', 'tirsdag', 'onsdag', 'torsdag', 'fredag', 'lørdag'],
        'FORMAT_STR': '{0:2d} {1:s}',
        'FORMAT_NUM': '{0:2d}/{1:02d}',
        'ORDER': [0,1]
    },
    'nn': { # Norwegian nynorsk
        'MONTHS': [None, 'januar', 'februar', 'mars', 'april', 'mai', 'juni', 'juli', 'august', 'september', 'oktober', 'november', 'desember'],
        'WEEKDAYS': ['søndag', 'mandag', 'tirsdag', 'onsdag', 'torsdag', 'fredag', 'lørdag'],
        'FORMAT_STR': '{0:2d} {1:s}',
        'FORMAT_NUM': '{0:2d}/{1:02d}',
        'ORDER': [0,1]
    },
    'pl': { # Polish
        'MONTHS': [None, 'stycznia', 'lutego', 'marca', 'kwietnia', 'maja', 'czerwca', 'lipca', 'sierpnia', 'września', 'października', 'listopada', 'grudnia'],
        'WEEKDAYS': ['niedziela', 'poniedziałek', 'wtorek', 'sroda', 'czwartek', 'piętek', 'sobota'],
        'FORMAT_STR': '{0:2d} {1:s}',
        'FORMAT_NUM': '{0:2d}/{1:02d}',
        'ORDER': [0,1]
    },
    'pt': { # Portuguese
        'MONTHS': [None, 'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'],
        'WEEKDAYS': ['domingo', 'segunda-feira', 'terça-feira', 'quarta-feira', 'quinta-feira', 'sexta-feira', 'sábado'],
        'FORMAT_STR': '{0:2d} de {1:s}',
        'FORMAT_NUM': '{0:2d}/{1:02d}',
        'ORDER': [0,1]
    },
    'sv': { # Swedish
        'MONTHS': [None, 'januari', 'februari', 'mars', 'april', 'maj', 'juni', 'juli', 'augusti', 'september', 'oktober', 'november', 'december'],
        'WEEKDAYS': ['söndag', 'lärngdag', 'märtdag', 'onsdag', 'tisdag', 'onsdag', 'fredag'],
        'FORMAT_STR': '{0:2d}:e {1:s}',
        'FORMAT_NUM': '{0:2d}/{1:02d}',
        'ORDER': [0,1]
    },
    'th': { # Thai
        'MONTHS': [None, 'ม.ค.', 'ก.พ.', 'มี.ค.', 'เม.ย.', 'พ.ค.', 'มิ.ย.', 'ก.ค.', 'ส.ค.', 'ก.ย.', 'ต.ค.', 'พ.ย.', 'ธ.ค.'],
        'WEEKDAYS': ['อาทิตย์', 'จันทร์', 'อังคาร', 'พุธ', 'พฤหัสบดี', 'ศุกร์', 'เสาร์'],
        'FORMAT_STR': '{0:2d} {1:s}',
        'FORMAT_NUM': '{0:2d}/{1:02d}',
        'ORDER': [0,1]
    },
    'zh': { # Chinese
        'MONTHS': [None, '一月', '二月', '三月', '四月', '五月', '六月', '七月', '八月', '九月', '十月', '十一月', '十二月'],
        'WEEKDAYS': ['星期日', '星期一', '星期二', '星期三', '星期四', '星期五', '星期六'],
        'FORMAT_STR': '{1:s}{0:2d}日',
        'FORMAT_NUM': '{1:2d}-{0:02d}',
        'ORDER': [1,0]
    }
}

# Holidays
# use a two letter code for country, and hyphens for country subdivisions.
# These comes in the format (month, day), numeric.
# 'FIX' refer to fixed holidays, these are holidays that allways fall in a given date.
# 'N:n' refer to holidyas that are alwys shifted to the next weekday n,
#     'N:1' referes wo holidays shifted to next Monday, 'N:4' referes wo holidays shifted to next Thursday, etc.
# 'm:n' refer to holodyas that are shifted to the next weekday n if they occur after weekday m. For example
#     '6:1' are shifted to Monday if they occur on or after Saturday.
# 'PASC' refer to holidays that occur n days after Easter sunday (or n days before if negatives)
# If you want to mark special holidays, for example unoficial holidays or holidays that only apply to public sector
#     you shall prefix them with a '@'
hol = {
    'co': { # Colombia
        # fixed holidays
        'FIX': [(1,1), (5,1), (7,20), (8,7), (12,8), (12,25)],
        # holidays that are always shifted to next Monday
        'N:1': [(1,6), (3,19), (6,29), (8,15), (10,12), (11,1), (11,11)],
        # holidays that refer to Eastern Sunday
        'PASC': [-3, -2, 0, 43, 64, 71]
    },
    'fr': { # France
        'FIX': [(1,1), (5,1), (5,8), (7,14), (8,15), (11,1), (11,11), (12,25)],
        'PASC': [0, 1, 39],
        '@FIX': [(12,26)],
        '@PASC': [-2, 50]
    },
    'mx': { # Mexico
        'FIX': [(1,1), (5,1), (9,16), (12,25)],
        'N:1': [(2,1), (3,15), (11,15)],
        # Holy Thursday and Long Friday are not official holidays in Mexico, but are commonly taken as holidays, they are marked differently
        '@PASC': [-3, -2]
    },
    'pe': { # Peru
        'FIX': [(1,1), (5,1), (6,7), (6,29), (7,23), (7,28), (7,29), (8,6), (8,30), (10,8), (11,1), (12,8), (12,9), (12,25)],
        # Second day of Christmas and New Year are holidays for public sector, so they are marked differently.
        '@FIX': [(1,2), (12,26)],
        'PASC': [-3, -2, 0]
    },
    'se': { # Sweden
        'FIX': [(1,1), (1,6), (5,1), (6,6), (12,25), (12,26)],
        'N:6': [(6,20), (10,31)],
        'PASC': [-2, 0, 1, 39, 49],
        '@FIX': [(12,24), (12,31)],
        '@N:5': [(6,19)],
        '@PASC': [-1, 48]
    },
    'us': { # United States
        'FIX': [(1,1), (6,19), (7,4), (11,11), (12,25)],
        # Memorial day occurs last Monday in May, this could be translated as (6,-7) for "Monday in or after June minus 7 days"
        #    or as (5, 25) "Monday in or after May 25"
        'N:1': [(1,15), (2,15), (6,-7), (9,1), (10,8)],
        # Forth Thursday of November referes to the Thrusday in or after November 22.
        'N:4': [(11,22)],
        'PASC': []
    },
    've': { # Venezuela
        'FIX': [(1,1), (4,19), (5,1), (6,24), (6,29), (7,5), (7,24), (8,15), (10,12), (12,24), (12,25), (12,31)],
        'N:1': [(11,1)],
        'PASC': [-48, -47, -3, -2, 0],
        '@FIX': [(3,19), (12,8)],
        '@N:1': [(1,6), (9,11)],
        '@PASC': [-6, -5, -4, 39, 60]
    },
    'xx': { # Hypothetical country with different holiday cases.
        'FIX': [(1,1), (5,1), (12,25)],
        'N:4': [(6,21),(11,22)],
        '6:1': [(3,19), (8,15), (9,22), (10,12)],
        'PASC': [-7, -3, -2, 0, 40, 50],
        # If New Year, Labor Day or Christmans fall on weekend, next Monday is special holiday.
        '@6:1': [(1,1), (5,1), (12,25)],
        '@6:5': [(6,22), (11,23)],
        '@PASC': [-48, -47, 51]
    }
}

def write_down(labels, holidays):
    for code, dic in labels.items():
        month = dic['MONTHS_D'][1] if 'MONTHS_D' in dic else dic['MONTHS'][1]
        date = dic['FORMAT_STR'].format(1, month)
        print(f"Labels for {code:<8s} v.g. '{date}'")
        with open(f'labels_{code}.bin', 'wb') as file:
            pickle.dump(dic, file)

    for code, dic in holidays.items():
        holiday_count = sum([len(v) for k, v in dic.items() if k[0] != '@'])
        other_holiday_count = sum([len(v) for k, v in dic.items() if k[0] == '@'])
        number = f'{holiday_count:2d}+{other_holiday_count:2d}' if other_holiday_count > 0 else f'{holiday_count:2d}   '
        print(f'Holidays for {code:<5s} ({number} holidays)')
        with open(f'holidays_{code}.bin', 'wb') as file:
            pickle.dump(dic, file)

if __name__=='__main__': write_down(lab, hol)
