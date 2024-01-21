from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Email
from flask_ckeditor import CKEditorField

app = Flask(__name__)
app.config['SECRET_KEY'] = "KEY"

class ContactForm(FlaskForm):
    name = StringField("Name")
    email = StringField("Email", validators=[Email()])
    subject = StringField("Subject")
    message = CKEditorField("Message")
    submit = SubmitField("Send Message")


@app.route("/", methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if request.method == "POST":
        name = request.form('name')
        email = request.form('email')
        subject = request.form('subject')
        message = request.form('message')
    return render_template("index.html", form=form)
    
if __name__ == "__main__":
    app.run(debug=True)