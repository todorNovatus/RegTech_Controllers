from datetime import datetime


def months_between(start_date, end_date):
    """
    Given two instances of ``datetime.date``, generate a list of dates on
    the 1st of every month between the two dates (inclusive).

    e.g. "5 Jan 2020" to "17 May 2020" would generate:

        1 Jan 2020, 1 Feb 2020, 1 Mar 2020, 1 Apr 2020, 1 May 2020

    """
    if start_date > end_date:
        raise ValueError(f"Start date {start_date} is not before end date {end_date}")

    year = start_date.year
    month = start_date.month

    while (year, month) <= (end_date.year, end_date.month):
        yield datetime(year, month, 1)

        # Move to the next month.  If we're at the end of the year, wrap around
        # to the start of the next.
        #
        # Example: Nov 2017
        #       -> Dec 2017 (month += 1)
        #       -> Jan 2018 (end of year, month = 1, year += 1)
        #
        if month == 12:
            month = 1
            year += 1
        else:
            month += 1
            
def date_gap_to_dic(start_date, end_date):
    print(type(start_date))
    start_date = datetime.strptime(start_date, '%Y-%m')
    end_date = datetime.strptime(end_date, '%Y-%m')
    storage = {}
    for date in months_between(start_date, end_date):
        print(date.strftime("%Y"))
        print(date.strftime("%m"))
        if date.strftime("%Y") in storage:
            storage[date.strftime("%Y")].append(int(date.strftime("%m")))
        else:
            storage[date.strftime("%Y")] = [int(date.strftime("%m"))]
    storage = {int(k):v for k,v in storage.items()}
    return storage

if __name__ == "__main__":
    # start_of_2020 = datetime.date(2020, 1, 1)
    # today = datetime.date.today()
    
    # print(date_gap_to_dic('2020-03', '2020-08'))
    print()