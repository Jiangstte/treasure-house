months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December',
]

endings = ['st','nd','rd'] + 17 * ['th'] \
        + ['st','nd','rd'] + 7 * ['th'] \
        + ['st']

year  = raw_input('year:')
month = raw_input('month(1-12):')
day   = raw_input('day(1-31):')

month_number = int(month)
day_number = int(day)

month_number = months[month_number]
ordinal      = day + endings[day_number]

print month_number + ' ' + ordinal + '.' + year

