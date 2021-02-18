from flask import Blueprint, request, redirect
from flask.templating import render_template
from application.models import Post
from application.main.utils import location_codes
from application.main.forms import LocationForm

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

@main.route('/weather',methods=['GET', 'POST'])
def weather():
    codes = location_codes
    form = LocationForm()
    form.location.choices = list(codes.keys())
    if form.validate_on_submit():
        location = form.location.data
        return redirect("https://www.accuweather.com/en/in/" + location + "/" + codes[location] +\
     "/current-weather/" + codes[location])
    return render_template('weather.html',title='Weather', form=form, legend='Weather')
        
