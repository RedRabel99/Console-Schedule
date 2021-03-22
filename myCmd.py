from cmd import Cmd
from datetime import timedelta, datetime
from time import sleep
import myCalendar
import myDatabase
import myTable

Cmd.prompt = "<schedule>"
weekDays = ("monday", "tuesday", "wednesday", "thursday", "friday")


class MyPrompt(Cmd):
    def do_exit(self, inp):
        print("Closing...")
        sleep(1)
        return True

    def help_exit(self):
        print('exit the application. Shorthand: x q Ctrl-D.')

    def do_show(self, arg):
        if arg.lower() in weekDays:
            myTable.single_day(myDatabase.get_subjects(weekday=arg), arg)
        elif arg == '':
            pass
            for x in weekDays:
                myTable.single_day(myDatabase.get_subjects(weekday=x), x)

        else:
            print("Invalid syntax: type 'help show' for more info\n"
                  "usage: show [option] ... [weekday]")

    def help_show(self):
        print("usage: show [option] ... [weekday]\n"
              "no arguments   : prints schedule of everyday\n"
              "weekday        : prints schedule of given day\n"
              "    accepted weekdays:\n        monday tuesday wednesday thursday friday")

    def do_today(self, arg):
        if arg == '':
            today = datetime.today()
            name = today.strftime("%A").lower()
            myTable.single_day(myDatabase.get_subjects(weekday=name), name)
        else:
            print("Invalid syntax: no arguments needed\n"
                  "usage: today")

    def help_today(self):
        print("usage: today\n"
              "no arguments   : prints schedule of today")

    def do_next(self, arg):
        if arg == '':
            now = datetime.now()
            name = now.strftime("%A").lower()
            data = myDatabase.get_subjects(weekday=name)
            value = float(now.strftime("%H.%M"))
            data2 = []
            for element in data:
                #print(f"{element}\n{float(element['start'].replace(':', '.'))} <? {value}")
                if float(element['start'].replace(':', '.')) > value:
                    data2.append(element)
            myTable.single_day(data2, name)

        else:
            print("Invalid syntax: no arguments needed\n"
                  "usage: next")

    def help_next(self):
        print("usage: next\n"
              "no arguments   : prints next class/classes of current day")

    def do_tomorrow(self, arg):
        if arg == '':
            tomorrow = datetime.today() + timedelta(days=1)
            name = tomorrow.strftime("%A").lower()
            myTable.single_day(myDatabase.get_subjects(weekday=name), name)

        else:
            print("Invalid syntax: no arguments needed\n"
                  "usage: tommorow")

    def help_tomorrow(self):
        print("usage: tomorrow\n"
              "no arguments   : prints schedule of tomorrow")

    def do_delete(self, arg, *arg2):
        if arg == '':
            print("Invalid syntax: argument needed\n"
                  "usage: [all] N [N ...]")
            return
        elif arg == 'all':
            myDatabase.delete_all()
        else:
            myDatabase.delete_subject(int(arg))

    def help_delete(self):
        print("usage: delete [all] N [N ...]\n"
              "all            : deletes all saved subjects from schedule\n"
              "N              : deletes subject of given id number\n"
              "[N ...]        : deletes subjects of given id numbers")

    def do_add(self, arg):
        if not arg == '':
            try:
                data = arg.split()
                weekday = data[0]
                start = data[1]
                end = data[2]
                name = data[3:]
                # if not weekday or start or end or name:
                #    print("Invalid syntax: invalid arguments\n"
                #          "type help add for more info")
                # else:
                myDatabase.add_subject(weekday, start, end, ''.join(f'{x} ' for x in name), weekDays)
            except IndexError:
                print("Invalid syntax: invalid arguments\n"
                      "type help add for more info")
        else:
            print("Invalid syntax: invalid arguments\n"
                  "type help add for more info")
    def help_add(self):
        print("add subject to schedule\n"
              "usage: add weekday start end name\n"
              "weekday        : name of the day from monday to friday\n"
              "start          : start time in hh:mm format\n"
              "end            : end time in hh:mm format\n"
              "name           : name of the subject"
              )

    def do_calendar(self, arg):
        if not arg == '':
            print("Invalid syntax: no arguments needed\n"
                  "usage: calendar")
        else:
            today = datetime.today()
            print(myCalendar.highlight_calendar(today.year, today.month, today.day))

    def help_calendar(self):
        print("usage: calendar\n"
              "no arguments   : prints a calendar with current day highlighted")
