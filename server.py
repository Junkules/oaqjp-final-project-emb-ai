"""Flask web application for detecting emotions in text."""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector


app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def sent_detector():
    """Analyze the text supplied to the emotion detector endpoint."""
    text_to_analyze = request.args.get("textToAnalyze", "")

    if not text_to_analyze.strip():
        return {"error": "Invalid text! Please try again!"}, 200

    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return {"error": "Invalid text! Please try again!"}, 200

    return response


@app.route("/")
def render_index_page():
    """Render the application's main page."""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    