# Задача 4. Хорошего дня!
import sys
from datetime import datetime

day_num = datetime.today().weekday()

# weekdays_dict = {
#     0: 'Monday',
#     1: 'Tuesday',
#     2: 'Wednesday',
#     3: 'Thursday',
#     4: 'Friday',
#     5: 'Saturday',
#     6: 'Sunday',
# }
# print('weekdays_dict', type(weekdays_dict), sys.getsizeof(weekdays_dict))   # weekdays_dict <class 'dict'> 352

weekdays_tuple = ('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday')
print('weekdays_tuple', type(weekdays_tuple), sys.getsizeof(weekdays_tuple))    # weekdays_tuple <class 'tuple'> 96

# weekdays_list = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
# print('weekdays_list', type(weekdays_list), sys.getsizeof(weekdays_list))   # weekdays_list <class 'list'> 120

weekday = weekdays_tuple[day_num]
print(weekday)

