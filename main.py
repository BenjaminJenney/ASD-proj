from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import DevConfig
import random

app = Flask(__name__)
app.config.from_object(DevConfig)
db = SQLAlchemy(app)

stories_excited = [
    {"text": "Today is my birthday. I am going to have a big birthday party with my friends. I am looking forward to it and I feel very… Select the correct feeling", "image": "../static/imgs/birthday.png", "correctAnswer": "Exited"},
    {"text": "Today I am going to the aquarium with my sister. I look forward to see so many water animals. I feel very… Select the correct feeling", "image": "../static/imgs/aquarium.png", "correctAnswer": "Exited"},
    {"text": "Today I will go to the cinema to watch my favorite cartoon. I feel very… Select the correct feeling", "image": "../static/imgs/cinema.png", "correctAnswer": "Exited"}
]

stories_happy = [
    {"text": "Today my mom took me to the playground and bought me my favorite ice cream. I felt very… Select the correct feeling", "image": "../static/imgs/happy.jpeg", "correctAnswer": "Happy"},
    {"text": "Today my brother read two of my favorite books to me. I love my brother and I felt very… Select the correct feeling", "image": "../static/imgs/readingbook.jpg", "correctAnswer": "Happy"},
    {"text": "Today I visited my grandparents and I swam in the lake with them. I felt very…  Select the correct feeling", "image": "../static/imgs/swimming.jpg", "correctAnswer": "Happy"}
]

stories_creative = [
    {"text": "Yesterday, I did an ocean art project. My idea was to mix blue and white colors for the ocean. The ocean looked so beautiful at the end. I felt very… Select the correct feeling", "image": "../static/imgs/ocean.jpg", "correctAnswer": "Creative"},
    {"text": "Today I organized my toys in a completely different way. Instead of putting all my pretend animals in one basket, I divided them into two groups - water and land animals. I felt very… Select the correct feeling", "image": "../static/imgs/toys.jpg", "correctAnswer": "Creative"},
    {"text": "My sister helped me do a tiger puppet on paper. And then an idea came to my mind. I wanted to add teeth to the tiger puppet. And it looked very beautiful at the end. I felt very…  Select the correct feeling", "image": "../static/imgs/tiger.jpg", "correctAnswer": "Creative"}
]

stories_angry = [
    {"text": "Today my sister took my toy without asking me first. I was feeling very… Select the correct feeling", "image": "../static/imgs/", "correctAnswer": "Angry"},
    {"text": "Today my friend pushed me on purpose and I fell on the ground. She didn't say 'I am sorry', she just walked away. I was feeling very… Select the correct feeling", "image": "../static/imgs/", "correctAnswer": "Angry"},
    {"text": "Today my mom and I went to the park. I started playing with my friends but my mom told me that I have to go home and I didn't want to go home. I was feeling very… Select the correct feeling", "image": "../static/imgs/", "correctAnswer": "Angry"}
]

stories_frustrated = [
    {"text": "Today my friend asked me for my dad's name. I said the name 5 times and he didn't get it. After multiple attempts, I felt very… Select the correct feeling", "image": "../static/imgs/", "correctAnswer": "Frustrated"},
    {"text": "Today I went to the playground with my mom. My mom bought me an ice cream and I dropped it accidentally on the floor. I was feeling very… Select the correct feeling", "image": "../static/imgs/", "correctAnswer": "Frustrated"},
    {"text": "Today I was doing a puzzle in my class when my friend came and stepped on it and ruined it. I was feeling very… Select the correct feeling", "image": "../static/imgs/", "correctAnswer": "Frustrated"}
]

stories_skeptical = [
    {"text": "Today I went to the aquarium and I saw a Jellyfish. My friend told me that it was an Octopus. I was feeling very… Select the correct feeling", "image": "../static/imgs/", "correctAnswer": "Skeptical"}
]

story_set_joyful = stories_excited + stories_happy + stories_creative
story_set_mad = stories_angry + stories_frustrated + stories_skeptical

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/conversationalAI.html')
def conversationaAI():
 return render_template('conversationalAI.html')

@app.route('/emotionsQuiz.html')
def emotionsQuiz():
    random_story = random.choice(story_set_joyful + story_set_mad)
    return render_template('emotionsQuiz.html', story=random_story['text'], image=random_story['image'],correctAnswer=random_story['correctAnswer'])

@app.route('/learnEmotions.html')
def different_emotions_learning():
    return render_template('learnEmotions.html')

@app.route('/game.html')
def happy_expr_matching_game():
    random_story = random.choice(story_set_joyful + story_set_mad)
    return render_template('game.html', story=random_story['text'], image=random_story['image'],correctAnswer=random_story['correctAnswer'])

@app.route('/x_joyful.html')
def joyful():
    random_story = random.choice(story_set_joyful)
    return render_template('x_joyful.html', story=random_story['text'], image=random_story['image'],correctAnswer=random_story['correctAnswer'])
@app.route('/x_mad.html')
def mad():
    random_story = random.choice(story_set_mad)
    return render_template('x_mad.html', story=random_story['text'], image=random_story['image'],correctAnswer=random_story['correctAnswer'])


@app.route('/goodJob.html')
def goodJob():
    return render_template('goodJob.html')

@app.route('/tryAgain.html')
def tryAgain():
    return render_template('tryAgain.html')

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

