# Console Scheduler
Save and manage your schedule in fast and easy way.
## What is Console Scheduler?
Console Scheduler is a python application that allows you to view and edit your schedule by specially prepared commands in console window.
## System Requirements
Script (.py)
* Python 3.9+
* Modules:
  * tinydb
  * cmd
  * terminaltables
  * datetime, time, ctypes, sys, colorama, calendar
Windows (.exe)
* none
## Setup
#### Python Script
Go to to the directory where the script is present and type:
```console
C:\yourdirectory>python console-schedule.py
<schedule>
```
### .exe
Run .exe file using console:
```console
C:\yourdirectory>console-scheduler.exe
<schedule>
```
or just by using file explorer:
![image](https://user-images.githubusercontent.com/72413391/112042299-a4dfc780-8b47-11eb-8703-636d8c4820b3.png)

## Usage/Important commands
### help
Lists all available commands.
```console
<schedule>help

Documented commands (type help <topic>):
========================================
add  calendar  delete  exit  help  next  show  today  tomorrow
```
Add command name as help argument to see more specific info.
```console
<schedule>help show
usage: show [option] ... [weekday]
no arguments   : prints schedule of everyday
weekday        : prints schedule of given day
    accepted weekdays:
        monday tuesday wednesday thursday friday
<schedule>
```
### add
Adds subject/activity to your schedule.
Syntax:
```add subject to schedule
usage: add weekday start end name
weekday        : name of the day from monday to friday
start          : start time in hh:mm format
end            : end time in hh:mm format
name           : name of the subject
```
Example:
```console
<schedule>add monday 11:30 13:00 Math
Successfully added subject:
    id: 1, name : Math , start: 11:30, end: 13:00, weekday: monday
<schedule>show monday
┌monday──────┬───────────────┐
│ ID │  NAME │  START - END  │
├────┼───────┼───────────────┤
│ 1  │ Math  │ 11:30 - 13:00 │
└────┴───────┴───────────────┘
```
### show
Prints all schedule for every day(if no arguments are given), or schedule for given day.</br>Examples:
```console
<schedule>show friday
┌friday───────────────────────┬───────────────┐
│ ID │          NAME          │  START - END  │
├────┼────────────────────────┼───────────────┤
│ 4  │ Programming in Python  │ 09:00 - 11:00 │
└────┴────────────────────────┴───────────────┘
```
```console
<schedule>show
┌monday──────┬───────────────┐
│ ID │  NAME │  START - END  │
├────┼───────┼───────────────┤
│ 1  │ Math  │ 11:30 - 13:00 │
└────┴───────┴───────────────┘
┌tuesday────────┬───────────────┐
│ ID │   NAME   │  START - END  │
├────┼──────────┼───────────────┤
│ 2  │ Biology  │ 16:00 - 17:00 │
└────┴──────────┴───────────────┘
┌wednesday───────┬───────────────┐
│ ID │    NAME   │  START - END  │
├────┼───────────┼───────────────┤
│ 5  │ Swimming  │ 19:00 - 20:00 │
└────┴───────────┴───────────────┘
┌thursday───────┬───────────────┐
│ ID │   NAME   │  START - END  │
├────┼──────────┼───────────────┤
│ 3  │ English  │ 12:00 - 12:45 │
└────┴──────────┴───────────────┘
┌friday───────────────────────┬───────────────┐
│ ID │          NAME          │  START - END  │
├────┼────────────────────────┼───────────────┤
│ 4  │ Programming in Python  │ 09:00 - 11:00 │
└────┴────────────────────────┴───────────────┘
```
### delete 
Deletes subject/activity of given id(```delete <id>```):
```console<schedule>delete 3
subject with id: 3 has benn successfully deleted
```
If 'all' is given as an argument(```delete all```) it deletes whole database:
```console
<schedule>delete all
all subjects had been successfully deleted
```
