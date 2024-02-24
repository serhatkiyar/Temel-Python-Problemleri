import datetime
import locale

locale.setlocale(locale.LC_ALL, 'tr_TR.utf-8')

print(datetime.ctime(datetime.now()))
print(datetime.strftime(datetime.now(), "%Y"))
print(datetime.now().strftime("%Y"))