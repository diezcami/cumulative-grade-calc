# File Handling
source_code = open('source_code.txt')
data_lines = source_code.readlines()
cum_qpi_data = data_lines[29]
cum_qpi = float(cum_qpi_data[16:])
course_list = data_lines[32:]
source_code.close()

grade_lookup = {'A' : 4.0, 'B+': 3.5, 'B' : 3.0, 'C+': 2.5, 'C' : 2.0, 'D' : 1.0, 'F' : 0.0, 'INC' : 0.0}

# Parse Data
academic_units_taken = 0
grade_total = 0.0
invalid_tags = ['NSTP', 'INTAC', 'PE1']
invalid_grades = ['W', 'S', 'UD', 'ED']
for course in course_list:
    if not course.startswith('20'):
        break

    course = course.replace(" ", "").replace("	", "") # Removes tabs lol
    last_in = len(course) - 2 # One whitespace to the right
    units_in = 1

    if any(grade in course[last_in - 1:] for grade in invalid_grades):
        continue

    # TODO: Filter ITM
    if any(tag in course for tag in invalid_tags):
        continue

    if course[last_in] == '+':
        units_in = 2

    if course[last_in] == 'C' and course[last_in-1] == 'N' :
        units_in = 3


    # Parse Course Information
    course_units = int(course[last_in - units_in])
    grade_total += (grade_lookup[course[last_in - units_in + 1 : last_in + 1]] * course_units)
    academic_units_taken += course_units
    # print grade_lookup[course[last_in - units_in + 1 : last_in + 1]]


current_cumulative_qpi = grade_total / academic_units_taken
print "Calculated Cumulative QPI:", (round(current_cumulative_qpi,2))
