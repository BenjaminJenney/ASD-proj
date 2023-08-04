from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import DevConfig

app = Flask(__name__)
app.config.from_object(DevConfig)
db = SQLAlchemy(app)

@app.route('/')
def home_page():
 return render_template('home.html')


@app.route('/game1.html')
def happy_expr_matching_game():
    return render_template('game1.html')

# SQLAlchemy will assume that the name of your table is the lowercase version of your
# model class name
class User(db.Model):
    __tablename__ = 'user_table_name'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    posts = db.relationship(
        'Post',
        backref='user_table_name',
        lazy='dynamic'
    )

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return "<User '{}, {}, {}'>".format(self.username, self.password, self.posts)

class Post(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255))
    text  = db.Column(db.Text())
    publish_date = db.Column(db.DateTime())
    user_id = db.Column(db.Integer, db.ForeignKey('user_table_name.id')) 
    '''A foreign key constraint is a rule in the database that
    forces the value of user_id to exist in the id column in the user table. This is a check in the
    database to make sure that Post will always refer to an existing user. '''
    def __init__(self, title):
        self.title = title
    
    def __repr__(self):
        return "<Post '{}'>".format(self.title)




'''Common DB types: 
  db.String
  db.Text
  db.Integer
  db.Float
  db.Boolean
  db.Date
  db.DateTime
  db.Time '''
if __name__ == '__main__':
    app.run()