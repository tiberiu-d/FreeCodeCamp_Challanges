def pretty_print(hours, minutes, tod, extra):
    if minutes < 10:
        new_minutes = "0" + str(minutes)
    else:
        new_minutes = str(minutes)

    if extra == "":
        return f"{hours}:{new_minutes} {tod}"
    else:
        return f"{hours}:{new_minutes} {tod} {extra}"


def add_time(start, duration):
    start_HH = int(start.split(":")[0])
    start_MI = int(start.split(":")[1].split(" ")[0])
    start_TOD = start.split(":")[1].split(" ")[1]

    duration_HH = int(duration.split(":")[0])
    duration_MI = int(duration.split(":")[1])

    # let's add the minutes/hours and set everything up
    result_extra = ""
    result_HH = 0
    result_MI = start_MI + duration_MI
    result_HH = start_HH + duration_HH

    # new minutes are greater than 1h?
    if result_MI >= 60:
        result_MI -= 60
        result_HH += 1

    # let's account for AM/PM
    if result_HH >= 12:
        if start_TOD == "AM":
            start_TOD = "PM"
        else:
            start_TOD = "AM"
            result_extra = "(next day)"

    if result_HH > 12:
        result_HH -= 12

    return pretty_print(result_HH, result_MI, start_TOD, result_extra)


# print(add_time("2:59 AM", "24:00"))
