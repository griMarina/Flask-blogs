from flask import Flask, render_template
from db import *

app = Flask('flask-blogs')


@app.route('/')
def home():
    all_blogs = get_all_blogs()
    return render_template('index.html', blogs=all_blogs, title='HOME')


if __name__ == '__main__':
    app.run()