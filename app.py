from flask import Flask, render_template
import random
import platform

app = Flask(__name__)

# list of cat images
images = [
    "https://raw.githubusercontent.com/toontjem/my-tweet-app/master/Pictures/1.png",
    "https://raw.githubusercontent.com/toontjem/my-tweet-app/master/Pictures/2.png",
    "https://raw.githubusercontent.com/toontjem/my-tweet-app/master/Pictures/3.png",
    "https://raw.githubusercontent.com/toontjem/my-tweet-app/master/Pictures/4.png"
]

@app.route('/')
def index():
    url = random.choice(images)
    hostname = platform.node()
    return render_template('index.html', url=url, hostname=hostname)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
