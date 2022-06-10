from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = '<secret key>'
toolbar = DebugToolbarExtension(app)

@app.route('/')
def form():
    """returns form html """
    prompts = story.prompts

    return render_template('form.html', prompts=prompts)

@app.route('/story')
def make_story():
    """make story html """
    create = story.generate(request.args)

    return render_template('story.html', create=create)