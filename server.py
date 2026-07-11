from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_detector_endpoint():
    """
    Endpoint to analyze the emotion of a given text parameter.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    
    if not text_to_analyze:
        return "Invalid text! Please try again."
        
    response = emotion_detector(text_to_analyze)
    
    anger = response.get('anger', 0)
    disgust = response.get('disgust', 0)
    fear = response.get('fear', 0)
    joy = response.get('joy', 0)
    sadness = response.get('sadness', 0)
    dominant_emotion = response.get('dominant_emotion', 'None')
    
    formatted_response = f"For the given statement, the system response is 'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. The dominant emotion is {dominant_emotion}."

    
    return formatted_response

@app.route("/")
def render_index_page():
    """
    Renders the index.html template from the templates folder.
    """
    return render_template("index.html")

if __name__ == "__main__":
    
    app.run(host="127.0.0.1", port=5000, debug=True)