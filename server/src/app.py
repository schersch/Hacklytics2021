from flask import Flask, jsonify, request

def get_predictions(county):
    predictions = []
    #countyShapes = gpd.read_file("NRI_Shapefile_Counties/NRI_Shapefile_Counties.shp")
    #countyShapes.plot()

    #probably need to pre-generate all the .jpg files and just upload them
    county_img = 'us.jpg'
    #plt.savefig(county_img)
    risk_level = 'TotalRisk: OMG'
    predictions.append(county_img)
    predictions.append(risk_level)
    return predictions


app = Flask(__name__)

@app.route('/')
@app.route('/index')
def show_index():
    prediction = get_predictions()
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
    app.run(host="0.0.0.0", port=8080, debug=False)
