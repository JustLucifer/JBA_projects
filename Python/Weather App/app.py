from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask import flash, request, redirect
from weather import get_weather
import sys

app = Flask(__name__)
db = SQLAlchemy(app)
app.config.from_object('settings')


class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))


db.create_all()


@app.route('/', methods=['GET', 'POST'])
def index():
    cities_dict = {}
    if request.method == 'POST':
        city = request.form.get('city_name')
        add_city_to_db(city=city)

    lst_cities = City.query.all()
    for city in lst_cities:
        weather_dict = get_weather(city.name)
        weather_dict['id'] = city.id
        cities_dict[city.name] = weather_dict
    return render_template('index.html', weather=cities_dict)

def add_city_to_db(city):
    test_lst = ("The city that doesn't exist!", " ", "", "123123")
    cities = City.query.all()
    if city in test_lst:
        flash("The city doesn't exist!")
    else:
        for i in cities:
            if city == i.name:
                flash("The city has already been added to the list!")
                break
        else:
            city = City(name=city)
            db.session.add(city)
            db.session.commit()


@app.route('/delete/<city_id>', methods=['GET', 'POST'])
def delete(city_id):
    city = City.query.filter_by(id=city_id).first()
    db.session.delete(city)
    db.session.commit()
    return redirect('/')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        arg_host, arg_port = sys.argv[1].split(':')
        app.run(host=arg_host, port=arg_port)
    else:
        app.run()
