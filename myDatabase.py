from tinydb import TinyDB, Query
import myTable

db = TinyDB('db.json')
User = Query()


# weekDays = ("monday", "tuesday", "wednesday", "thursday", "friday")

def is_valid(weekday, start, end, weekdays):
    isvalid = True
    if weekday not in weekdays:
        print("invalid weekday name\n"
              f"must be one of: ", *weekdays)
        isvalid = False

    if not len(start) == 5:
        print("invalid start value\n"
              "format required: HH:MM")
        isvalid = False
    elif not start[0:2].isnumeric() or not start[3:5].isnumeric():
        print("invalid start value\n"
              "format required: HH:MM")
        isvalid = False

    if not len(end) == 5:
        print("invalid end value\n"
              "format required: HH:MM")
        isvalid = False
    elif not end[0:2].isnumeric() or not end[3:5].isnumeric():
        print("invalid end value\n"
              "format required: HH:MM")
        isvalid = False

    return isvalid


def add_subject(weekday, start, end, name, weekdays):
    if is_valid(weekday, start, end, weekdays):
        value = db.insert({'name': name, 'start': start, 'end': end, 'weekday': weekday})
        db.update({'id': value}, doc_ids=[value])
        print("Successfully added subject: \n"
              f"    id: {value}, name : {name}, start: {start}, end: {end}, weekday: {weekday}")


def delete_subject(id):
    if db.contains(doc_id=id):
        db.remove(doc_ids=[id])
        print(f"subject with id: {id} has benn successfully deleted")
    else:
        print("no subject with such id")


def delete_all():
    db.truncate()
    print("all subjects had been successfully deleted")


def get_subjects(**kwargs):
    if len(kwargs):
        for key, value in kwargs.items():
            result = db.search(User[key] == value.lower())
            if not result:
                return ''
            else:
                return sorted([dict(x) for x in result], key=lambda k: float(k['start'].replace(':', '.')))
    else:
        return db.all()

# db.truncate()
# myTable.single_day(get_subjects(weekday='monday'), 'MONDAY')
