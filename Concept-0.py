# File Handling
source_code = open('source_code.txt')
cum_qpi_data = source_code.readlines()[29]
cum_qpi = float(cum_qpi_data[16:])
course_list = source_code.readlines()[32:]

grade_lookup = {'A' : 4.0, 'B+': 3.5, 'B' : 3, 'C+': 2.5. 'C' : 2, 'D' : 1.5, 'F' : 0}

# Parse Data
academic_units_taken = 0
grade_total = 0
last_in = len(course)-1
units_in = 1

for course in course_list:

    # Base Loop Case
    if not course.startswith('20'):
        break

    # Filter ITM
    if [' PE ', 'NSTP'] in course or
        ['  W', '  S', 'AUD'] in course [-3:]
        continue
    
    str.strip('\s+')
    if course[last_in] == '+':
        units_index = 2
    else:
        units_index = 1
    
    # Parse Course Information
    grade_total += coursegrade_lookup[course[last_in]] * course[last_in - units_in]
    academic_units_taken += int(course[last_in - units_in])

current_cumulative_qpi = grade_total / academic_units_taken
print (current_cumulative_qpi)