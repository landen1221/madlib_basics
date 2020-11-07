from flask import Flask, request, render_template
from stories import Story
# from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

# app.config['SECRET_KEY'] = "madlib"
# debug = DebugToolbarExtension(app)

story = Story(
    ["place", "adjective", "noun", "verb", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

@app.route('/')
def home_page():
    word_types = story.prompts
    return render_template('home.html', word_types=word_types)


@app.route('/madlib')
def create_madlib():
   
    
    text = story.generate(request.args)

    return render_template("madlib.html", text=text)


# username = request.args["username"]
