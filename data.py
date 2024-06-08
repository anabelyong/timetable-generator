import random
from jinja2 import Template
import webbrowser

class ClassType:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

# Example class types with durations in hours
class_types = [
    ClassType("MSc Project Thesis Work", 8),
    ClassType("Meeting with Brooks Paige", 2),
    ClassType("Meeting with Ignotalabs.AI", 3),
    ClassType("Swimming", 4),
    #ClassType("Machine Learning Job Applications", 5),
    ClassType("LeetCode", 6),
    ClassType("Machine Learning Job Interviews ", 7)
]

# Define the time slots for the week
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
hours_per_day = 8  # Assuming an 8-hour workday


# Function to create an empty timetable
def create_empty_timetable(days, hours_per_day):
    return {day: [None] * hours_per_day for day in days}

# Function to fill the timetable
def fill_timetable(class_types, days, hours_per_day):
    timetable = create_empty_timetable(days, hours_per_day)
    for class_type in class_types:
        for _ in range(class_type.duration):
            day = random.choice(days)
            hour = random.choice(range(hours_per_day))
            while timetable[day][hour] is not None:
                day = random.choice(days)
                hour = random.choice(range(hours_per_day))
            timetable[day][hour] = class_type.name
    return timetable

timetable = fill_timetable(class_types, days, hours_per_day)

# HTML template
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Timetable</title>
    <style>
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            border: 1px solid black;
            padding: 8px;
            text-align: center;
        }
    </style>
</head>
<body>
    <h1>Weekly Timetable</h1>
    <table>
        <thead>
            <tr>
                <th>Time</th>
                {% for day in days %}
                <th>{{ day }}</th>
                {% endfor %}
            </tr>
        </thead>
        <tbody>
            {% for hour in range(hours_per_day) %}
            <tr>
                <td>{{ hour + 1 }}:00 - {{ hour + 2 }}:00</td>
                {% for day in days %}
                <td>{{ timetable[day][hour] or "Free" }}</td>
                {% endfor %}
            </tr>
            {% endfor %}
        </tbody>
    </table>
</body>
</html>
"""

# Render the timetable in HTML
template = Template(html_template)
html_content = template.render(days=days, hours_per_day=hours_per_day, timetable=timetable)

# Save the HTML content to a file
with open("timetable.html", "w") as file:
    file.write(html_content)

webbrowser.open("timetable.html")
