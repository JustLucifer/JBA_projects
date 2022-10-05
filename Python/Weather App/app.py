from flask import Flask, render_template, abort
from flask_sqlalchemy import SQLAlchemy
from flask import flash, request, redirect
from weather_api import BASE_URL, API_KEY
from weather import get_weather
import requests as r
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
        if weather_dict is None:
            abort(500, 'Internal Server Error')
        weather_dict['id'] = city.id
        cities_dict[city.name] = weather_dict
    return render_template('index.html', weather=cities_dict)


def add_city_to_db(city):
    cities = City.query.all()

    for i in cities:
        if city == i.name:
            flash("The city has already been added to the list!")
            break
    else:
        request_url = f'{BASE_URL}?appid={API_KEY}&q={city}'
        response = r.get(request_url)

        if response.status_code == 200:
            city = City(name=city)
            db.session.add(city)
            db.session.commit()
        else:
            flash("The city doesn't exist!")


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
