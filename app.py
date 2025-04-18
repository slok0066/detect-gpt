from flask import Flask, request, jsonify
from detectgpt_utils import load_data, compute_fluency_scores

app = Flask(__name__)

@app.route('/')
def index():
    return "DetectGPT is running!"

@app.route('/detect', methods=['POST'])
def detect():
    input_text = request.json.get('text')

    if not input_text:
        return jsonify({"error": "No text provided"}), 400

    # Example: detect using perplexity (dummy logic)
    # Replace with actual DetectGPT method if needed
    try:
        score = compute_fluency_scores([input_text])[0]
        return jsonify({
            "text": input_text,
            "score": float(score),
            "likely_ai_generated": score < -1.5  # Example threshold
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500
