from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

# Define models
class SeasonalWeather(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    outlook = db.Column(db.String(200))

class PlantingSuggestion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    crop = db.Column(db.String(50))
    suggestion = db.Column(db.String(200))

class IndigenousKnowledge(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(50))
    info = db.Column(db.String(200))

class AgriculturalKnowledge(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50))
    tip = db.Column(db.String(200))

class AlertSubscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50))
    status = db.Column(db.String(50))

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(200))

# Initial data
seasonal_weather_data = [
    {"outlook": "Get an outlook on weather patterns for the upcoming months to help you plan your agricultural activities. Insights into expected weather patterns, highlighting rainfall, temperature trends, and significant seasonal wind changes for the upcoming season."}
]

planting_suggestion_data = [
    {"crop": "Fruit", "suggestion": "Plant fruit crops during the appropriate season."},
    {"crop": "Grains", "suggestion": "Sow grains when weather conditions are favorable."},
    {"crop": "Vegetables", "suggestion": "Grow vegetables suitable for the current climate."},
    {"crop": "Specify", "suggestion": "Specify a crop for personalized planting suggestions."},
    {"crop": "Return", "suggestion": "Return to the main menu."}
]

indigenous_knowledge_data = [
    {"topic": "weather prediction", "info": "Detailed examples of how specific birds' activities or the appearance of certain plants are traditionally interpreted as signs predicting the start of the rainy season or indicating the expected season's quality."},
    {"topic": "weather adaptation", "info": "Insights into traditional methods of soil conservation, water management, and crop selection that align with anticipated weather conditions, based on indigenous knowledge."},
    {"topic": "story", "info": "Narratives and anecdotes from farmers illustrating practical applications of indigenous weather prediction and its impact on agricultural decisions, including how a combination of natural signs guides their preparation for wind and seasonal changes."},
    {"topic": "Return", "info": "Return to the main menu."}
]

agricultural_knowledge_data = [
    {"category": "soil", "tip": "Daily tips and best practices for soil management."},
    {"category": "water", "tip": "Daily tips and best practices for water conservation."},
    {"category": "pest", "tip": "Daily tips and best practices for pest control."},
    {"category": "crop", "tip": "Daily tips and best practices for crop rotation."},
    {"category": "Return", "tip": "Return to the main menu."}
]

alert_subscription_data = [
    {"type": "day", "status": "You have subscribed to receive daily alerts."},
    {"type": "week", "status": "You have subscribed to receive weekly alerts."},
    {"type": "cancel", "status": "You have canceled your subscription."},
    {"type": "Return", "status": "Return to the main menu."}
]

# Routes
@app.route('/seasonalWeather', methods=['GET'])
def get_seasonal_weather():
    return jsonify(seasonal_weather_data[0])

@app.route('/plantingSuggestion', methods=['GET'])
def get_planting_suggestion():
    crop = request.args.get('crop')
    suggestion = next((item['suggestion'] for item in planting_suggestion_data if item['crop'] == crop), "No suggestion available for this crop.")
    return jsonify({"suggestion": suggestion})

@app.route('/reportRainfall', methods=['POST'])
def report_rainfall():
    rainfall = request.form.get('rainfall')
    # Here you can handle the reported rainfall data as needed
    return jsonify({"message": f"Rainfall reported: {rainfall}"})

@app.route('/indigenousKnowledge', methods=['GET'])
def get_indigenous_knowledge():
    topic = request.args.get('topic')
    info = next((item['info'] for item in indigenous_knowledge_data if item['topic'] == topic), "No information available for this topic.")
    return jsonify({"info": info})

@app.route('/agriculturalKnowledge', methods=['GET'])
def get_agricultural_knowledge():
    category = request.args.get('category')
    tip = next((item['tip'] for item in agricultural_knowledge_data if item['category'] == category), "No tips available for this category.")
    return jsonify({"tip": tip})

@app.route('/alertSubscribe', methods=['GET'])
def manage_alert_subscription():
    subscription_type = request.args.get('type')
    status = next((item['status'] for item in alert_subscription_data if item['type'] == subscription_type), "Invalid subscription type.")
    return jsonify({"status": status})

@app.route('/message', methods=['POST'])
def leave_message():
    message = request.form.get('message')
    # Here you can handle the received message data as needed
    return jsonify({"message": f"Your message: {message}"})

if __name__ == '__main__':
    app.run(debug=True)
