from flask import Flask,url_for,render_template
app = Flask(__name__)
from datetime import datetime
from pytz import timezone    

def tomtime():
    bama = timezone('US/Central')
    bama_time = datetime.now(bama)
#    return bama_time.strftime('%Y-%m-%d_%H-%M-%S')
    return bama_time.strftime("%I:%M %p")

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html",tomtime=tomtime())


if __name__ == '__main__':
    app.run(host="127.0.0.1",port=9999)
