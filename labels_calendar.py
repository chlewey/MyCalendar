
import pickle

lab = {
    'es': {
        'MONTHS': [None, 'enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'],
        'WEEKDAYS': ['domingo', 'lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado'],
        'FORMAT_STR': '{0:2d} de {1:s}',
        'FORMAT_NUM': '{0:2d}/{1:02d}',
        'ORDER': [0,1]
    },
    'en': {
        'MONTHS': [None, 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
        'WEEKDAYS': ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],
        'FORMAT_STR': '{0:2d} {1:s}',
        'FORMAT_NUM': '{0:2d}/{1:02d}',
        'ORDER': [0,1]
    },
    'en-us': {
        'MONTHS': [None, 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
        'WEEKDAYS': ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],
        'FORMAT_STR': '{1:s} {0:2d}',
        'FORMAT_NUM': '{1:2d}/{0:d}',
        'ORDER': [1,0]
    },
    'sv': {
        'MONTHS': [None, 'januari', 'februari', 'mars', 'april', 'maj', 'juni', 'juli', 'augusti', 'september', 'oktober', 'november', 'december'],
        'WEEKDAYS': ['söndag', 'lärngdag', 'märtdag', 'onsdag', 'tisdag', 'onsdag', 'fredag'],
        'FORMAT_STR': '{0:2d}:e {1:s}',
        'FORMAT_NUM': '{0:2d}/{1:02d}',
        'ORDER': [0,1]
    },
    'fr': {
        'MONTHS': [None, 'janvier', 'fevrier', 'mars', 'avril', 'mai', 'juin', 'juillet', 'aout', 'septembre', 'octobre', 'novembre', 'decembre'],
        'WEEKDAYS': ['dimanche', 'lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi'],
        'FORMAT_STR': '{0:2d} de {1:s}',
        'FORMAT_NUM': '{0:2d}/{1:02d}',
        'ORDER': [0,1]
    },
    'de': {
        'MONTHS': [None, 'Januar', 'Februar', 'März', 'April', 'Mai', 'Juni', 'Juli', 'August', 'September', 'Oktober', 'November', 'Dezember'],
        'WEEKDAYS': ['Sonntag', 'Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag'],
        'FORMAT_STR': '{0:2d} {1:s}',
        'FORMAT_NUM': '{0:2d}/{1:02d}',
        'ORDER': [0,1]
    },
    'it': {
        'MONTHS': [None, 'gennaio', 'febbraio', 'marzo', 'aprile', 'maggio', 'giugno', 'luglio', 'agosto', 'settembre', 'ottobre', 'novembre', 'dicembre'],
        'WEEKDAYS': ['domenica', 'lunedì', 'martedì', 'mercoledì', 'giovedì', 'venerdì', 'sabato'],
        'FORMAT_STR': '{0:2d} {1:s}',
        'FORMAT_NUM': '{0:2d}/{1:02d}',
        'ORDER': [0,1]
    },
    'po': {
        'MONTHS': [None, 'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'],
        'WEEKDAYS': ['domingo', 'segunda-feira', 'terça-feira', 'quarta-feira', 'quinta-feira', 'sexta-feira', 'sábado'],
        'FORMAT_STR': '{0:2d} de {1:s}',
        'FORMAT_NUM': '{0:2d}/{1:02d}',
        'ORDER': [0,1]
    },
    'nl': {
        'MONTHS': [None, 'januari', 'februari', 'maart', 'april', 'mei', 'juni', 'juli', 'augustus', 'september', 'oktober', 'november', 'december'],
        'WEEKDAYS': ['zondag', 'maandag', 'dinsdag', 'woensdag', 'donderdag', 'vrijdag', 'zaterdag'],
        'FORMAT_STR': '{0:2d} {1:s}',
        'FORMAT_NUM': '{0:2d}/{1:02d}',
        'ORDER': [0,1]
    },
    'dk': {
        'MONTHS': [None, 'januar', 'februar', 'marts', 'april', 'maj', 'juni', 'juli', 'august', 'september', 'oktober', 'november', 'december'],
        'WEEKDAYS': ['søndag', 'mandag', 'tirsdag', 'onsdag', 'torsdag', 'fredag', 'lørdag'],
        'FORMAT_STR': '{0:2d} {1:s}',
        'FORMAT_NUM': '{0:2d}/{1:02d}',
        'ORDER': [0,1]
    },
    'no': {
        'MONTHS': [None, 'januar', 'februar', 'mars', 'april', 'mai', 'juni', 'juli', 'august', 'september', 'oktober', 'november', 'desember'],
        'WEEKDAYS': ['søndag', 'mandag', 'tirsdag', 'onsdag', 'torsdag', 'fredag', 'lørdag'],
        'FORMAT_STR': '{0:2d} {1:s}',
        'FORMAT_NUM': '{0:2d}/{1:02d}',
        'ORDER': [0,1]
    },
    'fi': {
        'MONTHS': [None, 'tammikuu', 'helmikuu', 'maaliskuu', 'huhtikuu', 'toukokuu', 'kesäkuu', 'heinäkuu', 'eläkuu', 'syyskuu', 'lokakuu', 'marraskuu', 'joulukuu'],
        'WEEKDAYS': ['sunnuntai', 'maanantai', 'tiistai', 'keskiviikko', 'torstai', 'perjantai', 'lauantai'],
        'FORMAT_STR': '{0:2d} {1:s}',
        'FORMAT_NUM': '{0:2d}/{1:02d}',
        'ORDER': [0,1]
    },
    'pl': {
        'MONTHS': [None, 'stycznia', 'lutego', 'marca', 'kwietnia', 'maja', 'czerwca', 'lipca', 'sierpnia', 'września', 'października', 'listopada', 'grudnia'],
        'WEEKDAYS': ['niedziela', 'poniedziałek', 'wtorek', 'sroda', 'czwartek', 'piętek', 'sobota'],
        'FORMAT_STR': '{0:2d} {1:s}',
        'FORMAT_NUM': '{0:2d}/{1:02d}',
        'ORDER': [0,1]
    },
    'jp': {
        'MONTHS': [None, '1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月'],
        'WEEKDAYS': ['日', '月', '火', '水', '木', '金', '土'],
        'FORMAT_STR': '{1:s}{0:2d}日',
        'FORMAT_NUM': '{1:2d}-{0:02d}',
        'ORDER': [1,0]
    },
    'kr': {
        'MONTHS': [None, '1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月'],
        'WEEKDAYS': ['일', '월', '요', '화', '수', '목', '금'],
        'FORMAT_STR': '{1:s}{0:2d}일',
        'FORMAT_NUM': '{1:2d}-{0:02d}',
        'ORDER': [1,0]
    },
    'th': {
        'MONTHS': [None, 'ม.ค.', 'ก.พ.', 'มี.ค.', 'เม.ย.', 'พ.ค.', 'มิ.ย.', 'ก.ค.', 'ส.ค.', 'ก.ย.', 'ต.ค.', 'พ.ย.', 'ธ.ค.'],
        'WEEKDAYS': ['อาทิตย์', 'จันทร์', 'อังคาร', 'พุธ', 'พฤหัสบดี', 'ศุกร์', 'เสาร์'],
        'FORMAT_STR': '{0:2d} {1:s}',
        'FORMAT_NUM': '{0:2d}/{1:02d}',
        'ORDER': [0,1]
    },
    'zh': {
        'MONTHS': [None, '一月', '二月', '三月', '四月', '五月', '六月', '七月', '八月', '九月', '十月', '十一月', '十二月'],
        'WEEKDAYS': ['星期日', '星期一', '星期二', '星期三', '星期四', '星期五', '星期六'],
        'FORMAT_STR': '{1:s}{0:2d}日',
        'FORMAT_NUM': '{1:2d}-{0:02d}',
        'ORDER': [1,0]
    }
}

hol = {
    'co': {
        'FIX': [(1,1), (5,1), (7,20), (8,7), (12,8), (12,25)],
        'N:1': [(1,6), (3,19), (6,29), (8,15), (10,12), (11,1), (11,11)],
        'PASC': [-3, -2, 0, 43, 64, 71]
    },
    'us': {
        'FIX': [(1,1), (6,19), (7,4), (11,11), (12,25)],
        'N:1': [(1,15), (2,15), (6,-7), (9,1), (10,8)],
        'N:4': [(11,22)],
        'PASC': []
    },
    'pe': {
        'FIX': [(1,1), (5,1), (6,7), (6,29), (7,23), (7,28), (7,29), (8,6), (8,30), (10,8), (11,1), (12,8), (12,9), (12,25)],
        '@FIX': [(1,2), (12,26)],
        'PASC': [-3, -2, 0]
    },
    'mx': {
        'FIX': [(1,1), (5,1), (9,16), (12,25)],
        'N:1': [(2,1), (3,15), (11,15)],
        '@PASC': [-3, -2]
    },
    'se': {
        'FIX': [(1,1), (1,6), (5,1), (6,6), (12,25), (12,26)],
        'N:6': [(6,20), (10,31)],
        'PASC': [-2, 0, 1, 39, 49],
        '@FIX': [(12,24), (12,31)],
        '@N:5': [(6,19)],
        '@PASC': [-1, 48]
    },
    'xx': {
        'FIX': [(1,1), (5,1), (12,25)],
        'N:4': [(6,21),(11,22)],
        '6:1': [(3,19), (8,15), (9,22), (10,12)],
        'PASC': [-7, -3, -2, 0, 40, 50],
        '@6:1': [(1,1), (5,1), (12,25)],
        '@6:5': [(6,22), (11,23)],
        '@PASC': [-48, -47, 51]
    }
}

for code, dic in lab.items():
    pickle.dump( dic, open(f'labels_{code}.bin', 'wb') )

for code, dic in hol.items():
    pickle.dump( dic, open(f'holidays_{code}.bin', 'wb') )
