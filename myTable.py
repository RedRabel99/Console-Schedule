from terminaltables import SingleTable


def single_day(values, weekday):
    table_data = [['ID', 'NAME', 'START - END']]
    if values:
        for element in values:
            table_data.append([f"{element['id']}", f"{element['name']}", f"{element['start']} - {element['end']}"])
    else:
        table_data.append(["0", "no classes for current day", "-- - --"])

    table_instance = SingleTable(table_data, weekday)
    table_instance.justify_columns[0] = 'center'
    table_instance.justify_columns[1] = 'center'
    table_instance.justify_columns[2] = 'center'
    print(table_instance.table)

