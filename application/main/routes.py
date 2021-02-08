from flask import Blueprint, request
from flask.templating import render_template
from application.models import Post


main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
@main.route('/homepage', methods=['GET'])
def home():
    page = request.args.get('page', type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)

@main.route('/about')
def about():
    return render_template('about.html')

