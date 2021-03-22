# Commands
### ```help```
List available commands with ```help``` or detailed help with ```help cmd```.</br>
```console
<schedule>help

Documented commands (type help <topic>):</br>
========================================</br>
add  calendar  delete  exit  help  next  show  today  tomorrow
```
```console
<schedule>help help
List available commands with "help" or detailed help with "help cmd".</br>
```
### ```add```
add subject to schedule</br>
usage: add weekday start end name</br>
weekday        : name of the day from monday to friday</br>
start          : start time in hh:mm format</br>
end            : end time in hh:mm format</br>
name           : name of the subject</br>
```console
<schedule>add friday 12:00 13:30 Math
Successfully added subject: 
    id: 2, name : Math , start: 12:00, end: 13:30, weekday: friday
```
### ```show```
usage: show [option] ... [weekday]</br>
no arguments   : prints schedule of everyday</br>
weekday        : prints schedule of given day</br>
    accepted weekdays:</br>
        monday tuesday wednesday thursday friday</br>
```console
<schedule>show
┌monday────────────────┬───────────────┐
│ ID │       NAME      │  START - END  │
├────┼─────────────────┼───────────────┤
│ 1  │ example record  │ 21:37 - 21:37 │
└────┴─────────────────┴───────────────┘
┌tuesday──────────────────────────┬─────────────┐
│ ID │            NAME            │ START - END │
├────┼────────────────────────────┼─────────────┤
│ 0  │ no classes for current day │   -- - --   │
└────┴────────────────────────────┴─────────────┘
┌wednesday────────────────────────┬─────────────┐
│ ID │            NAME            │ START - END │
├────┼────────────────────────────┼─────────────┤
│ 0  │ no classes for current day │   -- - --   │
└────┴────────────────────────────┴─────────────┘
┌thursday─────────────────────────┬─────────────┐
│ ID │            NAME            │ START - END │
├────┼────────────────────────────┼─────────────┤
│ 0  │ no classes for current day │   -- - --   │
└────┴────────────────────────────┴─────────────┘
┌friday──────┬───────────────┐
│ ID │  NAME │  START - END  │
├────┼───────┼───────────────┤
│ 2  │ Math  │ 12:00 - 13:30 │
└────┴───────┴───────────────┘
```
```console
<schedule>show friday
┌friday──────┬───────────────┐
│ ID │  NAME │  START - END  │
├────┼───────┼───────────────┤
│ 2  │ Math  │ 12:00 - 13:30 │
└────┴───────┴───────────────┘
```
### ```delete```
usage: delete [all] N</br>
all            : deletes all saved subjects from schedule</br>
N              : deletes subject of given id number</br>
```console
<schedule>delete all
all subjects had been successfully deleted
```
```console
<schedule> delete 3
subject with id: 3 has benn successfully deleted
```
### ```next```
usage: next
no arguments   : prints next class/classes of current day
```console
<schedule>next
┌monday────────────────┬───────────────┐
│ ID │       NAME      │  START - END  │
├────┼─────────────────┼───────────────┤
│ 1  │ example record  │ 21:37 - 21:37 │
│ 3  │     Running     │ 22:00 - 23:00 │
└────┴─────────────────┴───────────────┘
```
### ```today```
usage: today</br>
no arguments   : prints schedule of today</br>
```console
<schedule>today
┌monday────────────────┬───────────────┐
│ ID │       NAME      │  START - END  │
├────┼─────────────────┼───────────────┤
│ 1  │ example record  │ 21:37 - 21:37 │
│ 3  │     Running     │ 22:00 - 23:00 │
└────┴─────────────────┴───────────────┘
```
### ```tomorrow```
usage: tomorrow</br>
no arguments   : prints schedule of tomorrow</br>
```console
<schedule>tomorrow
┌tuesday──────────────────────────┬─────────────┐
│ ID │            NAME            │ START - END │
├────┼────────────────────────────┼─────────────┤
│ 0  │ no classes for current day │   -- - --   │
└────┴────────────────────────────┴─────────────┘
```
### ```calendar```
usage: calendar</br>
no arguments   : prints a calendar with current day highlighted
```console
<schedule>calendar
     March 2021
Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7
 8  9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
29 30 31
```
### ```exit```
exit the application. Shorthand: x q Ctrl-D.
```console
<schedule>exit
Closing...
```