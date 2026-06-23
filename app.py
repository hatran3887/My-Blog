import json
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """
    The index route, which shows all the blog posts
    """
    with open('storage/blog_posts.json') as f:
        blog_posts = json.load(f)
    return render_template('index.html', posts=blog_posts)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)