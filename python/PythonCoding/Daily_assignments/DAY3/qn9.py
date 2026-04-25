from datetime import datetime

#current time
now = datetime.now()
print('Current date and time:',now)

#days btw 2
date1 = datetime(2025,1,1)
date2 = datetime(2026,1,1)

diff = date2 - date1
print('Number of days between:', diff.days)

#format

formatted_date = now.strftime('%d-%m-%y')
print('Formatted date:', formatted_date)