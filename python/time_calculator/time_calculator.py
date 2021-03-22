def add_minutes(start_minutes, min_to_add):
    extra_hour = False
    new_minutes = start_minutes + min_to_add
    if new_minutes > 60:
        new_minutes -= 60
        extra_hour = True
    return new_minutes, extra_hour


def add_hours(start_hour, hrs_to_add, tod):
    extra_day = False
    new_tod = tod
    new_hours = start_hour + hrs_to_add

    if new_hours == 24:
        new_hours -= 12
        extra_day = True

    if new_hours > 12:
        if tod == "AM":
            new_tod = "PM"
        else:
            new_tod = "AM"

    return new_hours, extra_day, new_tod


def pretty_print(hours, minutes, tod):
    if minutes < 10:
        new_minutes = "0" + str(minutes)
    else:
        new_minutes = str(minutes)

    return f"{hours}:{new_minutes} {tod}"


def add_time(start, duration):
    start_hour = int(start.split(":")[0])
    start_minute = int(start.split(":")[1].split(" ")[0])
    start_tod = start.split(":")[1].split(" ")[1]

    duration_hour = int(duration.split(":")[0])
    duration_minute = int(duration.split(":")[1])

    # print(f"{start} + {duration}")
    # print(f" minute : {add_minutes(start_minute, duration_minute)}")
    # print(f" ore : {add_hours(start_hour, duration_hour)}")

    result_hours = add_hours(start_hour, duration_hour, start_tod)[0]
    # result_hours_extra = add_hours(start_hour, duration_hour, start_tod)[1]
    result_hours_tod = add_hours(start_hour, duration_hour, start_tod)[2]
    result_minutes = add_minutes(start_minute, duration_minute)[0]
    result_minutes_extra = add_minutes(start_minute, duration_minute)[1]

    if result_minutes_extra == True:
        result_hours += 1

    if result_hours > 12:
        result_hours -= 12

    return pretty_print(result_hours, result_minutes, result_hours_tod)
