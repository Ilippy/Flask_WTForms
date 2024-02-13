from flask import Flask, render_template
from login import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = b'8fda4c95f8ced93390919e911abb6b9dcd317ac21a6662e23748d47345e1cb72'


# >>> import secrets
# >>> secrets.token_hex()

@app.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        return 'Form Successfully Submitted!'
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
