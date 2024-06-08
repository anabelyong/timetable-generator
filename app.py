from flask import Flask, render_template, request
import random

app = Flask(__name__)

class ClassType:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

# Define the time slots for the week
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

def create_empty_timetable(days, hours_per_day):
    return {day: [None] * hours_per_day for day in days}

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

@app.route('/schedule_generator/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        hours_per_day = int(request.form.get('hours_per_day'))
        class_types = []
        for i in range(len(request.form.getlist('class_name'))):
            name = request.form.getlist('class_name')[i]
            duration = int(request.form.getlist('class_duration')[i])
            class_types.append(ClassType(name, duration))
        timetable = fill_timetable(class_types, days, hours_per_day)
        return render_template('timetable.html', days=days, hours_per_day=hours_per_day, timetable=timetable)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

