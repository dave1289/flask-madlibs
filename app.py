from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from random import randint, choice, sample
class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""
        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


story_test_1 = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

story_test_2 = Story(
    ["plural_noun", "year", "adjective", "noun", "past_verb"],
    """{plural_noun} were all the rage in {year}, me and my {adjective} {noun} would {past_verb} the cats."""
)


STORIES = [
    "1 Once upon a time in a long-ago {place}, there lived a large {adjective} {noun}. It loved to {verb} {plural_noun}.",
    "2 In {place}, you can never be too far from a {adjective} {noun}. But you can always {verb} {plural_noun}.",
    "3 Well children, {place} used to be a lot different. Back in my day when you could buy {adjective} {noun} for a dollar.  Well they can {verb} {plural_noun}.",
    "4 {place} has always been weird.  {adjective} {plural_noun} running around {verb}ing the {noun}."
       ]

app = Flask(__name__)

app.config['SECRET_KEY'] = 'SLAP'
debug = DebugToolbarExtension(app)
"""Madlibs Stories."""

STORIES = [
    "Once upon a time in a long-ago {place}, there lived a large {adjective} {noun}. It loved to {verb} {plural_noun}.",
       ]

@app.route('/')
def show_home():
    prompts = story_test_1.prompts
    return render_template('home.html', prompts=prompts)

@app.route('/generate')
def generate_story():
    story = Story(request.args, "Once upon a time in a long-ago {place}, there lived a large {adjective} {noun}. It loved to {verb} {plural_noun}.")
    return render_template('story.html', story=story.generate(request.args))
