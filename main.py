import openai
from flask import Flask, request, jsonify, render_template

openai.api_key = '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'  # Replace 'your-api-key-here' with your actual API key

app = Flask(__name__)


def generate_combined_recipe(ukrainian_meal, german_meal):
    prompt = (
        f"Create a unique recipe that combines the Ukrainian meal '{ukrainian_meal}' and "
        f"the German meal '{german_meal}'. Provide detailed steps and ingredients."
    )

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message["content"].strip()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate_recipe', methods=['POST'])
def generate_recipe():
    data = request.json
    ukrainian_meal = data.get('ukrainian_meal')
    german_meal = data.get('german_meal')

    if not ukrainian_meal or not german_meal:
        return jsonify({"error": "Both meals must be provided"}), 400

    recipe = generate_combined_recipe(ukrainian_meal, german_meal)
    return jsonify({"recipe": recipe})


if __name__ == "__main__":
    app.run(debug=True)
