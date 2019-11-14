from flask import render_template
from app import app

@app.errorhandler(404)
def four_0w_four(error):
    '''
    Function to render the 404 page
    '''
    return render_template(four_0w_four.html),404