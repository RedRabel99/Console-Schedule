import calendar
import colorama
colorama.init()

def highlight_calendar(year, month, day):
    """Returns a month's calendar string(multi-line), with given day highlighted in ansi code"""
    cal = calendar.month(year, month)
    tens, units = str(int(day/10)) if int(day/10)  else ' ', str(day % 10)
    for i in range(len(cal) - 2):
        if (cal[i + 1], cal[i]) == (units, tens):
            cal = cal[:i] + "\033[1;35;43m" + cal[i: i + 2] + "\033[1;35;0m" + cal[i + 2:]
            break
    return cal
