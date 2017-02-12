/*
// File Handling
var source_code = document.getElementById('aisis_data').value;
var data_lines = source_code.split("\n");
var cum_data_qpi = data_lines[29];
var cum_qpi = parseFloat(cum_data_qpi);
var course_list = data_lines.slice(32);

var grade_lookup = {};
grade_lookup['A'] = 4.0;
grade_lookup['B+'] = 3.5;
grade_lookup['B'] = 3.0;
grade_lookup['C+'] = 2.5;
grade_lookup['C'] = 2.0;
grade_lookup['D'] = 1.0;
grade_lookup['F'] = 0.0;

// Data Parsing
var academic_units_taken = 0
var grade_total = 0.0
var invalid_tags = [' PE', 'NSTP', 'INTAC']
var invalid_grades = ['W', 'S', 'AUD']

for(course in course_list) {
    if !(course.startsWith('20')) {
        break;
    }

    // TODO: Filter ITM?
    // TODO: Refactor
    for (tag in invalid_tags) {
        if course.contains(tag) {
            continue;
        }
    }

    course = course.replace(" ", "")
    last_in = course.length - 2 // One whitespace to the right
    units_in = 1

    // TODO: Refactor
    var len = course.length
    for (grade in invalid_grade) {
        if course.substring()
    }


}
*/

function present_metadata() {
    $("#results_metadata").empty();
    var metadata = "<h2>Current Cumulative QPI: 3.58</h2>" +
                    "Check if the above information is correct before proceeding!" +
                    "<div class=\"form-group\">" +
                        "<label for=\"example-number-input\">Target Cumulative QPI by Graduation</label>" +
                        "<input class=\"form-control\" type=\"number\" id=\"number_of_units\">" +
                        "<button type=\"button\" class=\"btn btn-default\" id=\"retention\">Retention</button>" +
                        "<button type=\"button\" class=\"btn btn-default\" id=\"honorable_mention\">Honorable Mention</button>" +
                        "<button type=\"button\" class=\"btn btn-default\" id=\"cum_laude\">Cum Laude</button>" +
                        "<button type=\"button\" class=\"btn btn-default\" id=\"magna_cum_laude\">Magna Cum Laude</button>" +
                        "<button type=\"button\" class=\"btn btn-default\" id=\"summa_cum_laude\">Summa Cum Laude</button>" +
                    "</div>";
    $("#results_metadata").append(metadata);
}
