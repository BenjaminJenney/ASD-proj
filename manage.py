from main import app, db, User, Post

# this updates the database and allows database management through flask shell
# flask shell needs context, if you want the shell to know where manage.py is
# run export FLASK_APP=manage.py
from main import app, db, User
@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, User=User, Post=Post) # From now on, whenever we create a new model, 
                                           # we will import it and add it to the returned dict.
'''In every storage mechanism for data, there are four basic types of functions: create, read,
update, and delete (CRUD). These allow us to perform all the basic ways of manipulating
and viewing the data that is needed for our web apps. To use these functions, we will use
an object in the database named a session.'''
