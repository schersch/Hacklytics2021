from flask import Flask, jsonify, request
from risker import get_pedictions


app = Flask(__name__)

@app.route('/')
@app.route('/index')
def show_index():
    prediction = get_predictions(request)
    imageName = prediction[0]
    riskLevel = prediction[1]
    return render_template("index.html", county_img = imageName, risk_level = riskLevel)

    #full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'shovon.jpg')
    #return render_template("index.html", user_image = full_filename)

@app.route("/predict", methods=["POST"])
def predict():
    predictions = get_predictions(request)

    return jsonify(predictions)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=False)
