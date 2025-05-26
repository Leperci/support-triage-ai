# app.py
from flask import Flask, request, jsonify, render_template
from model import llama3_response, granite_response, mixtral_response
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    user_message = data.get('message')
    model = data.get('model')

    if not user_message or not model:
        return jsonify({"error": "Missing message or model selection"}), 400

    system_prompt = (
        "You are an AI support assistant. Your job is to analyze a customer message, "
        "categorize the issue, assess sentiment (0–100), summarize it, and suggest the next step. "
        "Respond in structured JSON format only."
    )

    start_time = time.time()
    try:
        if model == 'llama3':
            result = llama3_response(system_prompt, user_message)
        elif model == 'granite':
            result = granite_response(system_prompt, user_message)
        elif model == 'mixtral':
            result = mixtral_response(system_prompt, user_message)
        else:
            return jsonify({"error": "Invalid model selection"}), 400

        result_dict = result.model_dump()  # ✅ Use model_dump() for Pydantic v2
        result_dict['duration'] = round(time.time() - start_time, 2)
        return jsonify(result_dict)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/compare', methods=['POST'])
def compare_models():
    data = request.json
    user_message = data.get('message')

    if not user_message:
        return jsonify({"error": "Missing message"}), 400

    system_prompt = (
        "You are an AI support assistant. Your job is to analyze a customer message, "
        "categorize the issue, assess sentiment (0–100), summarize it, and suggest the next step. "
        "Respond in structured JSON format only."
    )

    responses = {}

    for model_name, fn in {
        "llama3": llama3_response,
        "granite": granite_response,
        "mixtral": mixtral_response
    }.items():
        try:
            start = time.time()
            result = fn(system_prompt, user_message)
            response_data = result.model_dump()
            response_data['duration'] = round(time.time() - start, 2)
            responses[model_name] = response_data
        except Exception as e:
            responses[model_name] = {"error": str(e)}

    return jsonify(responses)  # ✅ Now outside the loop
if __name__ == '__main__':
    app.run(debug=True)
