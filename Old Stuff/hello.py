from flask import render_template, Flask, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

# @app.route("/timeseries", methods=['GET', 'POST'])
@app.route("/timeseries")
def timeseries():
    # if request.method == 'POST':
    return render_template("potholetimeseries2.html")

@app.route("/completed_potholes")
def completed_potholes():
    return render_template("CompletedPotholesChicago.html")

@app.route("/heatmap")
def heatmap():
    return render_template("pothole_heatmap.html")

@app.route("/eda")
def eda():
    return render_template("eda.html")
# def

app.run()
