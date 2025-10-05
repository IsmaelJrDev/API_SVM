from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "API SVM is running"})

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    # Aquí iría la lógica de predicción con SVM
    # Por ejemplo: resultado = modelo.predict([data['features']])
    resultado = "predicción_de_ejemplo"
    return jsonify({"prediction": resultado})

if __name__ == '__main__':
    app.run(debug=True)