from flask import Flask, render_template, request
import pickle
import pandas as pd 

app = Flask(__name__)

def getpipeline(path):
    with open(path, 'rb') as f:
        pipe = pickle.load(f)

    return pipe 

def convert(prediction):
    converter = {"Not_Canceled":"Likely to cancel", "Canceled":"Unlikely to cancel", ' ':''}
    return converter[prediction]

global pipe

pipe = getpipeline('static/MLpipeline.pkl')

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = ' '
    if request.method == 'POST':
        weekend = int(request.form.get('weekends'))
        weekday = int(request.form.get('weekdays'))
        specialrequest = int(request.form.get('specialrequest'))
        price = float(request.form.get('price'))
        cancelled = int(request.form.get('cancelled'))
        committed = int(request.form.get('committed'))
        market = request.form.get('market')
        roomtype = request.form.get('roomtype')
        mealplan = request.form.get('mealplan')
        leadtime = float(request.form.get('leadtime'))
        month = int(request.form.get('arrivalmonth'))
        guest = int(request.form.get('repeatedguest'))
        input_arr = pd.DataFrame({"no_of_weekend_nights":[weekend], "no_of_week_nights":[weekday], "type_of_meal_plan":[mealplan], "room_type_reserved":[roomtype], "lead_time":[leadtime], "arrival_month":[month], "market_segment_type":[market], "repeated_guest":[guest], "no_of_previous_cancellations":[cancelled], "no_of_previous_bookings_not_canceled":[committed], "avg_price_per_room":[price], "no_of_special_requests":[specialrequest]})
        prediction = pipe.predict(input_arr)
    
    return render_template('index.html', prediction = convert(prediction[0]))

if __name__ == '__main__':
    app.run(debug=True)
    