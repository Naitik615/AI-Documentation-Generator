import os
import openai  
from flask import Flask, request, jsonify
from flask_cors import CORS 


# Initialize Flask app
app = Flask(__name__)

# Configure CORS to allow requests from specific origins
CORS(app, resources={r"/*": {"origins": ["http://127.0.0.1:5501", "http://localhost:5501", "http://127.0.0.1:5000/generate", "http://127.0.0.1:5501/templates/index.html","http://127.0.0.1:5501/templates/index.html","http://127.0.0.1:5000","http://127.0.0.1:5501/templates/index.html"]}})

# Set your OpenAI API key
openai.api_key = "SECRATE_KEY"

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    code = data.get("code", "")

    if not code.strip():
        return jsonify({"error": "Code input is empty!"}), 400

    try:
        # ChatGPT-style prompt for generating code documentation
        prompt = f"""
        Generate a humanise response for the inputed text and start a normal conversation
        {code}
        """

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use the latest available model
            messages=[
                {"role": "system", "content": "You are a coding assistant that generates detailed code documentation."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=512  # Increased from 256 to handle longer outputs
        )

        generated_doc = response['choices'][0]['message']['content'].strip()
        return jsonify({"generated_doc": generated_doc})

    except openai.error.AuthenticationError:
        return jsonify({"error": "Invalid OpenAI API key."}), 401
    except openai.error.RateLimitError:
        return jsonify({"error": "Rate limit exceeded. Please try again later."}), 429
    except openai.error.OpenAIError as e:
        return jsonify({"error": f"OpenAI API error: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)