def fibonacci(n):

    sequence = [0,1]

    for i in range(2,n+1):

        next_num = sequence[-1] + sequence[-2]

        sequence.append(next_num)

    return sequence

value = int(input("Please enter a number of fibonacci iterations:\n"))

sequence = fibonacci(value)

print("The given fibonacci sequence is: ", sequence)

import datetime

def date_range(start, end):
    r = (end+datetime.timedelta(days=1)-start).days
    return [start+datetime.timedelta(days=i) for i in range(r)]

start = datetime.date(2022,3,7)
end = datetime.date(9000,2,1)
dateList = date_range(start, end)

# convert dates_list to dates

selected_elements = []

for index in sequence:
    selected_elements.append(dateList[index])
print("The required break-up dates are as follows:")
print ('\n'.join([str(date) for date in selected_elements]))
