from datetime import datetime

# A list of days stored in order; python datetime is 0 (monday) - 6 (sunday)
ENG_DAYS = ["Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"]

def day_in_irish(day_number):
    """
    Get the Irish day of the Week

    Translates the number representing the day of the week into its Irish value.

    Parameters:
        day_number (int): The number representing the day of the week; 0 - 6.

    Return:
        str: The Irish value for the day of the week.
    """
    day = "Dé"
    match day_number: #match statement ->
        case 0: #same structure as 'if/else if/elif' -> optimization, this is faster than 'if'
            day += " Luain"
        case 1:
            day += " Máirt"
        case 2:
            day += " Céadaoin"
        case 3:
            day += "ardaoin"
        case 4:
            day += " hAoine"
        case 5:
            day += " Sathairn"
        case default:
            day += " Domhnaigh"
    return day

# Get a new datetime instance.
date  = datetime.now()

# Get the day of the week; 0 (monday) - 6 (sunday)
today = date.weekday()

# Show the user the Irish day of the week.
print(f"Today is {day_in_irish(today)} ({ENG_DAYS[today]}).")
