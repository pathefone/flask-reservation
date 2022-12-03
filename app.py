from flask import Flask
from routes.contacts import contacts
from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_CONNECTION_URI

app = Flask(__name__)

# settings
app.secret_key = 'mysecret'
print(DATABASE_CONNECTION_URI)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONNECTION_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# no cache
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

db = SQLAlchemy(app)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))

@app.before_first_request
def create_tables():
    db.create_all()



app.register_blueprint(contacts)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
