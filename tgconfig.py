import datetime

import bs4
import requests

TOKEN = ''


def getbotip():
    return (bs4.BeautifulSoup(requests.get('https://2ip.ua/ru/').text, "html.parser").select(
        " .ipblockgradient .ip")[0].getText()).split()[0]


def checkdata():
    return datetime.datetime.today().isoweekday()


# spb_nevs_school569
spb_nevs_school569__students = []
spb_nevs_school569__admins = [505848766]
# spb_nevs_school569__Saturdaysub = []

# -----------------Timetable Timings
spb_nevs_school569__timetable_timings_1to4 = {
    'lesson1from': '08:30',
    'lesson1to': '09:15',
    'lesson2from': '09:35',
    'lesson2to': '10:20',
    'lesson3from': '10:40',
    'lesson3to': '11:25',
    'lesson4from': '11:45',
    'lesson4to': '12:30',
    'lesson5from': '12:50',
    'lesson5to': '13:25',
    'lesson6from': '14:50',
    'lesson6to': '15:35',
    'lesson7from': '15:45',
    'lesson7to': '16:25',
}

spb_nevs_school569__timetable_timings_5to11 = {
    'lesson1from': '08:30',
    'lesson1to': '09:15',
    'lesson2from': '09:35',
    'lesson2to': '10:20',
    'lesson3from': '10:40',
    'lesson3to': '11:25',
    'lesson4from': '11:45',
    'lesson4to': '12:30',
    'lesson5from': '12:50',
    'lesson5to': '13:35',
    'lesson6from': '13:55',
    'lesson6to': '14:40',
    'lesson7type1from': '14:50',
    'lesson7type1to': '15:35',
    'lesson7type2from': '15:00',
    'lesson7type2to': '15:40',
    'lesson8from': '15:45',
    'lesson8to': '16:25',
}

spb_nevs_school569_Saturday_timetable_timings_ = {
    'lesson1from': '08:30',
    'lesson1to': '09:15',
    'lesson2from': '09:15',
    'lesson2to': '10:10',
    'lesson3from': '10:20',
    'lesson3to': '12:05',
    'lesson4from': '12:15',
    'lesson4to': '13:00',
    'lesson5from': '13:10',
    'lesson5to': '13:55',
    'lesson6from': '14:05',
    'lesson6to': '14:50',
}

#       Spb_Nevs_School569__TimeTable 10 A

# Monday
spb_nevs_school569__timetable_Monday_10a_s = {
    'lesson1': 'Немецкий язык',
    'lesson2': 'Немецкий язык',
    'lesson3': 'Экономика',
    'lesson4': 'География',
    'lesson5': 'История',
    'lesson6': 'Литература',
}

spb_nevs_school569__timetable_Monday_10a_t = {
    'classname': 'Технический профиль',
    'lesson1': 'Немецкий язык',
    'lesson2': 'Немецкий язык',
    'lesson3': 'Черчение',
    'lesson4': 'Физика',
    'lesson5': 'История',
    'lesson6': 'Литература',
}

# Tuesday
spb_nevs_school569__timetable_Tuesday_10a_s = {
    'classname': 'Социально-экономический профиль',
    'lesson1': 'Английский язык',
    'lesson2': 'Английский язык',
    'lesson3': 'Обществознание',
    'lesson4': 'Обществознание',
    'lesson5': 'ОБЖ',
    'lesson6': 'Физкультура',
}

spb_nevs_school569__timetable_Tuesday_10a_t = {
    'classname': 'Технический профиль',
    'lesson1': 'Английский язык',
    'lesson2': 'Английский язык',
    'lesson3': 'Физика',
    'lesson4': 'Физика',
    'lesson5': 'ОБЖ',
    'lesson6': 'Физкультура',
}

# Wednesday
spb_nevs_school569__timetable_Wednesday_10a_s = {
    'classname': 'Социально-экономический профиль',
    'lesson1': 'Литература',
    'lesson2': 'Алгебра',
    'lesson3': 'Информатика',
    'lesson4': 'Естествознание',
    'lesson5': 'Естествознание',
    'lesson6': 'Физкультура',
    'lesson7': 'Русский*',
}
spb_nevs_school569__timetable_Wednesday_10a_t = {
    'classname': 'Технический профиль',
    'lesson1': 'Литература',
    'lesson2': 'Алгебра',
    'lesson3': 'Химия',
    'lesson4': 'Информатика',
    'lesson5': 'Информатика',
    'lesson6': 'Физкультура',
    'lesson7': 'Русский*',
}

# Thursday
spb_nevs_school569__timetable_Thursday_10a_s = {
    'classname': 'Социально-экономический профиль',
    'lesson1': 'Немецкий язык',
    'lesson2': 'Немецкий язык',
    'lesson3': 'Право',
    'lesson4': 'Алгебра',
    'lesson5': 'Геометрия',
    'lesson6': 'Английский',
    'lesson7': 'Астрономия'
}
spb_nevs_school569__timetable_Thursday_10a_t = {
    'classname': 'Технический профиль',
    'lesson1': 'Немецкий язык',
    'lesson2': 'Немецкий язык',
    'lesson3': 'Физика',
    'lesson4': 'Алгебра',
    'lesson5': 'Геометрия',
    'lesson6': 'Английский',
    'lesson7': 'Астрономия'
}

# Friday
spb_nevs_school569__timetable_Friday_10a_s = {
    'classname': 'Социально-экономический профиль',
    'lesson1': 'Английский язык',
    'lesson2': 'Экономика',
    'lesson3': 'Алгебра',
    'lesson4': 'Русский',
    'lesson5': 'Литература',
    'lesson6': 'История',
    'lesson7': 'Проект'
}
spb_nevs_school569__timetable_Friday_10a_t = {
    'classname': 'Технический профиль',
    'lesson1': 'Английский язык',
    'lesson2': 'Физика',
    'lesson3': 'Алгебра',
    'lesson4': 'Русский',
    'lesson5': 'Литература',
    'lesson6': 'История',
    'lesson7': 'Проект'
}

# Saturday
spb_nevs_school569__timetable_Saturday_10a_s = {
    'classname': 'Социально-экономический профиль',
    'lesson1': 'Алгебра',
    'lesson2': 'Геометрия',
    'lesson3': 'Естествознание',
    'lesson4': 'Право',
    'lesson5': 'История',
    'lesson6': 'Физкультура',
}
spb_nevs_school569__timetable_Saturday_10a_t = {
    'classname': 'Технический профиль',
    'lesson1': 'Алгебра',
    'lesson2': 'Геометрия',
    'lesson3': 'Информатика',
    'lesson4': 'Информатика',
    'lesson5': 'История',
    'lesson6': 'Физкультура',
}


def senttimetable(day):
    ttdata = checkdata()
    if day == 'tomorrow':
        if checkdata() < 7:
            ttdata += 1
        else:
            ttdata = 1
    ttmessage = ''
    if ttdata == 1:
        ttmessage += ('1. ' + spb_nevs_school569__timetable_Monday_10a_t.get('lesson1') + '\n')
        ttmessage += ('2. ' + spb_nevs_school569__timetable_Monday_10a_t.get('lesson2') + '\n')
        ttmessage += ('3. ' + spb_nevs_school569__timetable_Monday_10a_t.get('lesson3') + '\n')
        ttmessage += ('4. ' + spb_nevs_school569__timetable_Monday_10a_t.get('lesson4') + '\n')
        ttmessage += ('5. ' + spb_nevs_school569__timetable_Monday_10a_t.get('lesson5') + '\n')
        ttmessage += ('6. ' + spb_nevs_school569__timetable_Monday_10a_t.get('lesson6'))
    elif ttdata == 2:
        ttmessage += ('1. ' + spb_nevs_school569__timetable_Tuesday_10a_t.get('lesson1') + '\n')
        ttmessage += ('2. ' + spb_nevs_school569__timetable_Tuesday_10a_t.get('lesson2') + '\n')
        ttmessage += ('3. ' + spb_nevs_school569__timetable_Tuesday_10a_t.get('lesson3') + '\n')
        ttmessage += ('4. ' + spb_nevs_school569__timetable_Tuesday_10a_t.get('lesson4') + '\n')
        ttmessage += ('5. ' + spb_nevs_school569__timetable_Tuesday_10a_t.get('lesson5') + '\n')
        ttmessage += ('6. ' + spb_nevs_school569__timetable_Tuesday_10a_t.get('lesson6'))
    elif ttdata == 3:
        ttmessage += ('1. ' + spb_nevs_school569__timetable_Wednesday_10a_t.get('lesson1') + '\n')
        ttmessage += ('2. ' + spb_nevs_school569__timetable_Wednesday_10a_t.get('lesson2') + '\n')
        ttmessage += ('3. ' + spb_nevs_school569__timetable_Wednesday_10a_t.get('lesson3') + '\n')
        ttmessage += ('4. ' + spb_nevs_school569__timetable_Wednesday_10a_t.get('lesson4') + '\n')
        ttmessage += ('5. ' + spb_nevs_school569__timetable_Wednesday_10a_t.get('lesson5') + '\n')
        ttmessage += ('6. ' + spb_nevs_school569__timetable_Wednesday_10a_t.get('lesson6') + '\n')
        ttmessage += ('7. ' + spb_nevs_school569__timetable_Wednesday_10a_t.get('lesson7'))
    elif ttdata == 4:
        ttmessage += ('1. ' + spb_nevs_school569__timetable_Thursday_10a_t.get('lesson1') + '\n')
        ttmessage += ('2. ' + spb_nevs_school569__timetable_Thursday_10a_t.get('lesson2') + '\n')
        ttmessage += ('3. ' + spb_nevs_school569__timetable_Thursday_10a_t.get('lesson3') + '\n')
        ttmessage += ('4. ' + spb_nevs_school569__timetable_Thursday_10a_t.get('lesson4') + '\n')
        ttmessage += ('5. ' + spb_nevs_school569__timetable_Thursday_10a_t.get('lesson5') + '\n')
        ttmessage += ('6. ' + spb_nevs_school569__timetable_Thursday_10a_t.get('lesson6') + '\n')
        ttmessage += ('7. ' + spb_nevs_school569__timetable_Thursday_10a_t.get('lesson7'))
    elif ttdata == 5:
        ttmessage += ('1. ' + spb_nevs_school569__timetable_Friday_10a_t.get('lesson1') + '\n')
        ttmessage += ('2. ' + spb_nevs_school569__timetable_Friday_10a_t.get('lesson2') + '\n')
        ttmessage += ('3. ' + spb_nevs_school569__timetable_Friday_10a_t.get('lesson3') + '\n')
        ttmessage += ('4. ' + spb_nevs_school569__timetable_Friday_10a_t.get('lesson4') + '\n')
        ttmessage += ('5. ' + spb_nevs_school569__timetable_Friday_10a_t.get('lesson5') + '\n')
        ttmessage += ('6. ' + spb_nevs_school569__timetable_Friday_10a_t.get('lesson6') + '\n')
        ttmessage += ('7. ' + spb_nevs_school569__timetable_Friday_10a_t.get('lesson7'))
    elif ttdata == 6:
        ttmessage += ('1. ' + spb_nevs_school569__timetable_Saturday_10a_t.get('lesson1') + '\n')
        ttmessage += ('2. ' + spb_nevs_school569__timetable_Saturday_10a_t.get('lesson2') + '\n')
        ttmessage += ('3. ' + spb_nevs_school569__timetable_Saturday_10a_t.get('lesson3') + '\n')
        ttmessage += ('4. ' + spb_nevs_school569__timetable_Saturday_10a_t.get('lesson4') + '\n')
        ttmessage += ('5. ' + spb_nevs_school569__timetable_Saturday_10a_t.get('lesson5') + '\n')
        ttmessage += ('6. ' + spb_nevs_school569__timetable_Saturday_10a_t.get('lesson6'))
    return str(ttmessage)
