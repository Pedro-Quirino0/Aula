from flask import Flask

app = Flask(__name__)
app.config["SECRET_KEY"] = "c326ba044c898d434eed2d7c8288291c"

from projeto import routes
