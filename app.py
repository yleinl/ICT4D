from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///voxmeteo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Weather(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(10), unique=True, nullable=False)
    forecast = db.Column(db.String(200), nullable=False)

class RainfallReport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)

class PlantingSuggestion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    crop = db.Column(db.String(50), nullable=False)
    suggestion = db.Column(db.String(200), nullable=False)

class IndigenousKnowledge(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(50), nullable=False)
    info = db.Column(db.String(200), nullable=False)

class AgriculturalKnowledge(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50), nullable=False)
    tip = db.Column(db.String(200), nullable=False)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)

# db.create_all()
with app.app_context():
    db.create_all()

# Populate initial data if not exists
initial_weather_data = [
    {"date": "Today", "forecast": "Sunny with a high of 30°C."},
    {"date": "One", "forecast": "Cloudy with a chance of rain, high of 28°C."},
    {"date": "Two", "forecast": "Sunny with a high of 31°C."},
    {"date": "Three", "forecast": "Partly cloudy, high of 29°C."},
    {"date": "Four", "forecast": "Rain showers expected, high of 27°C."},
    {"date": "Five", "forecast": "Thunderstorms, high of 26°C."},
    {"date": "Six", "forecast": "Sunny, high of 32°C."},
    {"date": "Seven", "forecast": "Cloudy with occasional rain, high of 28°C."},
    {"date": "Week", "forecast": "This week will be mostly sunny with occasional rain showers."}
]

initial_planting_suggestions = [
    {"crop": "Fruit", "suggestion": "Best time to plant fruits is during the early spring."},
    {"crop": "Grains", "suggestion": "Plant grains during late spring to early summer."},
    {"crop": "Vegetables", "suggestion": "Vegetables can be planted during the spring and fall."},
]

initial_indigenous_knowledge = [
    {"topic": "weather prediction", "info": "Bird activities can indicate the start of the rainy season."},
    {"topic": "weather adaptation", "info": "Traditional methods of soil conservation are effective."},
    {"topic": "story", "info": "Farmers use natural signs to guide their preparations for the season."}
]

initial_agricultural_knowledge = [
    {"category": "soil", "tip": "Use compost to enrich your soil."},
    {"category": "water", "tip": "Irrigate your crops early in the morning."},
    {"category": "pest", "tip": "Use natural pesticides to control pests."},
    {"category": "crop", "tip": "Rotate your crops to maintain soil health."}
]
with app.app_context():
    for data in initial_weather_data:
        if not Weather.query.filter_by(date=data['date']).first():
            db.session.add(Weather(date=data['date'], forecast=data['forecast']))
    db.session.commit()

    for data in initial_planting_suggestions:
        if not PlantingSuggestion.query.filter_by(crop=data['crop']).first():
            db.session.add(PlantingSuggestion(crop=data['crop'], suggestion=data['suggestion']))
    db.session.commit()

    for data in initial_indigenous_knowledge:
        if not IndigenousKnowledge.query.filter_by(topic=data['topic']).first():
            db.session.add(IndigenousKnowledge(topic=data['topic'], info=data['info']))
    db.session.commit()

    for data in initial_agricultural_knowledge:
        if not AgriculturalKnowledge.query.filter_by(category=data['category']).first():
            db.session.add(AgriculturalKnowledge(category=data['category'], tip=data['tip']))
    db.session.commit()

@app.route('/weather', methods=['GET'])
def get_weather():
    date = request.args.get('date', 'Today')
    weather = Weather.query.filter_by(date=date).first()
    if weather:
        return jsonify({
            "date": date,
            "forecast": weather.forecast
        })
    else:
        return jsonify({
            "date": date,
            "forecast": "No forecast available for this date."
        })

@app.route('/planting', methods=['GET'])
def get_planting_suggestions():
    crop = request.args.get('crop', 'General')
    suggestion = PlantingSuggestion.query.filter_by(crop=crop).first()
    if suggestion:
        return jsonify({
            "crop": crop,
            "suggestion": suggestion.suggestion
        })
    else:
        return jsonify({
            "crop": crop,
            "suggestion": "No suggestions available for this crop."
        })

@app.route('/report_rainfall', methods=['POST'])
def report_rainfall():
    data = request.get_json()
    amount = data.get('amount', 0)
    new_report = RainfallReport(amount=amount)
    db.session.add(new_report)
    db.session.commit()
    return jsonify({
        "message": f"Thank you for reporting {amount}mm of rainfall."
    })

@app.route('/indigenous_knowledge', methods=['GET'])
def get_indigenous_knowledge():
    topic = request.args.get('topic', 'General')
    knowledge = IndigenousKnowledge.query.filter_by(topic=topic).first()
    if knowledge:
        return jsonify({
            "topic": topic,
            "info": knowledge.info
        })
    else:
        return jsonify({
            "topic": topic,
            "info": "No information available for this topic."
        })

@app.route('/agricultural_knowledge', methods=['GET'])
def get_agricultural_knowledge():
    category = request.args.get('category', 'General')
    tip = AgriculturalKnowledge.query.filter_by(category=category).first()
    if tip:
        return jsonify({
            "category": category,
            "tip": tip.tip
        })
    else:
        return jsonify({
            "category": category,
            "tip": "No tips available for this category."
        })

@app.route('/alert_subscription', methods=['POST'])
def subscribe_alert():
    data = request.get_json()
    subscription_type = data.get('subscription_type', 'daily')
    return jsonify({
        "message": f"You have subscribed to {subscription_type} alerts."
    })

@app.route('/message', methods=['POST'])
def save_message():
    content = request.get_json().get('message', '')
    new_message = Message(content=content)
    db.session.add(new_message)
    db.session.commit()
    return jsonify({
        "message": "Your message has been recorded."
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
    # app.run(host='117.72.46.192', port=8000)