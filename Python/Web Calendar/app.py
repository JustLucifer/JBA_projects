from flask_sqlalchemy import SQLAlchemy
from flask import Flask, abort, request
from flask_restful import Api
from flask_restful import Resource, reqparse
from flask_restful import inputs, marshal_with
from marshmallow import Schema, fields
import datetime
import sys


app = Flask(__name__)
db = SQLAlchemy(app)
app.config.from_object('settings')


class Events(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    event = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)


db.create_all()

parser = reqparse.RequestParser()
parser.add_argument(
    'date',
    type=inputs.date,
    help="The event date with the correct format is required! The correct format is YYYY-MM-DD!",
    required=True
)
parser.add_argument(
    'event',
    type=str,
    help="The event name is required!",
    required=True
)


class EventSchema(Schema):
    id = fields.Integer()
    event = fields.String()
    date = fields.Date()
    message = fields.String()


class Todo(Resource):
    def get(self):
        schema = EventSchema(many=True)
        query = db.session.query(Events)\
            .filter(Events.date == datetime.date.today()).all()
        return schema.dump(query)


class Event(Resource):
    def get(self):
        schema = EventSchema(many=True)
        args = request.args
        start = args.get('start_time')
        end = args.get('end_time')
        if start and end:
            query = db.session.query(Events)\
                .filter(Events.date.between(start, end)).all()
            return schema.dump(query)
        query = db.session.query(Events).all()
        return schema.dump(query)

    def post(self):
        schema = EventSchema()
        data = parser.parse_args()
        data['message'] = "The event has been added!"
        query = Events(event=data['event'], date=data['date'])
        db.session.add(query)
        db.session.commit()
        return schema.dump(data)


class EventByID(Resource):
    def get(self, event_id):
        schema = EventSchema()
        query = db.session.query(Events).filter(Events.id == event_id).first()
        if query is None:
            abort(404, "The event doesn't exist!")
        return schema.dump(query)

    def delete(self, event_id):
        query = Events.query.filter(Events.id == event_id).first()
        if query is None:
            abort(404, "The event doesn't exist!")
        db.session.delete(query)
        db.session.commit()
        return {"message": "The event has been deleted!"}


api = Api(app)
api.add_resource(Todo, '/event/today')
api.add_resource(Event, '/event')
api.add_resource(EventByID, '/event/<int:event_id>')

# do not change the way you run the program
if __name__ == '__main__':
    if len(sys.argv) > 1:
        arg_host, arg_port = sys.argv[1].split(':')
        app.run(host=arg_host, port=arg_port)
    else:
        app.run()
