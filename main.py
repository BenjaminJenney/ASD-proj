from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import DevConfig
import random

app = Flask(__name__)
app.config.from_object(DevConfig)
db = SQLAlchemy(app)

stories_excited = [
    {"text": "Today is my birthday. I am going to have a big birthday party with my friends. I am looking forward to it and I feel very ….. Select the correct feeling", "image": "../static/imgs/birthday.png"},
    {"text": "Today I am going to the aquarium with my sister. I look forward to see so many water animals. I feel very….  Select the correct feeling", "image": "../static/imgs/aquarium.png"},
    {"text": "Today I will go to the cinema to watch my favorite cartoon. I feel very……  Select the correct feeling", "image": "../static/imgs/cinema.png"}
]

@app.route('/')
def home_page():
 return render_template('home.html')

@app.route('/conversationalAI.html')
def conversationaAI():
 return render_template('conversationalAI.html')

@app.route('/emotionsQuiz.html')
def emotionsQuiz():
 random_story = random.choice(stories_excited)
 return render_template('emotionsQuiz.html', story=random_story['text'], image=random_story['image'])

@app.route('/learnEmotions.html')
def different_emotions_learning():
 return render_template('learnEmotions.html')

@app.route('/game.html')
def happy_expr_matching_game():
    random_story = random.choice(stories_excited)
    return render_template('game.html', story=random_story['text'], image=random_story['image'])

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

