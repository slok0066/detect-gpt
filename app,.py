from flask import Flask, request, jsonify
from detectgpt_utils import compute_fluency_scores  # Assuming this method is available in the repo

app = Flask(__name__)

@app.route('/')
def index():
    return "DetectGPT is running!"

@app.route('/detect', methods=['POST'])
def detect():
    input_text = request.json.get('text')

    if not input_text:
        return jsonify({"error": "No text provided"}), 400

    # Perform detection using the detectgpt_utils (or any logic from the repo)
    try:
        # Assuming `compute_fluency_scores` processes the text and returns a score
        score = compute_fluency_scores([input_text])[0]  # Example: Adjust according to your repo methods
        return jsonify({
            "text": input_text,
            "score": float(score),
            "likely_ai_generated": score < -1.5  # Threshold for AI generation likelihood
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
