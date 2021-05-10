"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app
from flask import render_template, request, redirect, url_for, flash
from app import mail
from app.forms import DecryptionForm
from .rsa_decrypt import RSA


###
# Routing for your application.
###

@app.route('/', methods=['GET', 'POST'])
def home():
    """Render website's home page."""
    form = DecryptionForm()
    results = ''
    if request.method == 'POST':
        if form.validate_on_submit():
            # Extract form data 
            try:
                c = int(request.form['cyphertext'])
                e = int(request.form['exponent'])
                n = int(request.form['public_key'])

                if c > 7000000 or e > 100 or n > 7000000:
                    raise ArithmeticError

                results = RSA.decrypt(c,e,n)
            except ArithmeticError:
                results = 'Let e < 100. Let c and n < 7,000,000'
            except Exception:
                results = "Oh no, those values won't work. Integers only."
        else:
            flash_errors(form)

    success = True if type(results) == dict else False

    return render_template('home.html', form=form, results=results, phi=chr(248), success=success )


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Encryption")


@app.route('/contact/', methods=['GET', 'POST'])
def contact():
    """Render the website's contact page."""
    return render_template('contact.html')

###
# The functions below should be applicable to all Flask apps.
###


# Flash errors from the form if validation fails
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
