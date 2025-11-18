from flask import Flask
import random

app = Flask(__name__)

list = [
    "50 percent ppl addicted to phones",
    "Elon Musky think Meta = bad",
    "Elon Musky say alogirthim hook us in like we fish, very bad, very bad",
    "I don't have internet addiction its fake, 67"


]
list2 = [
 "Bumblefluff",
    "Pickleberry",
    "Waffleton",
    "Snickerdoodle",
    "Marshmallowius",
    "Captain Sprinkles",
    "BanjoFizz",
    "ZoodlePop",
    "FroodleBug",
    "GiggleSprout",
    "PumpkinSpork",
    "TwinkleTofu",
    "Sir Noodleworth",
    "Jellybeanicus",
    "Fizzlenut",
    "MuffinThunder",
    "Gumdropson",
    "Professor Pudding",
    "NoodleDoodle",
    "Starlight Quokka"
]

@app.route("/")
def hello_world():
    return'''
    <h1>Hello, dis is home screen, a explain internet addiction
    <br>
    <a href = "/info" > Show me random info</a>
    </h1>
    '''


@app.route("/babynames")
def rando_info2():
    return f'<h1>{random.choice(list2)}<h1>'

@app.route("/info")
def rando_info():
    return f'<h1>{random.choice(list)}<h1>'

app.run(debug=True)