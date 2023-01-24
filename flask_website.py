import os
import smtplib
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_bootstrap import Bootstrap

load_dotenv()

# .env variables for sending & receiving emails from contact form
SENDER_EMAIL = os.environ["SENDER_EMAIL"]
SENDER_PASS = os.environ["SENDER_PASS"]
RECEIVE_EMAIL = os.environ["RECEIVE_EMAIL"]

# Set up app
app = Flask(__name__)
app.secret_key = os.environ["SECRET_KEY"]
bootstrap = Bootstrap(app)


# Set up contact form
class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    number = StringField("Phone Number", validators=[DataRequired()])
    email = StringField("Email Address", validators=[Email()])
    message = TextAreaField("Your Message", validators=[DataRequired()])
    submit = SubmitField("Contact Me!")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    contact_form = ContactForm()
    contact_form.validate_on_submit()
    if request.method == "POST":
        # Gather data from form and put into message
        name = contact_form.name.data
        number = contact_form.number.data
        email = contact_form.email.data
        message = contact_form.message.data
        contact_message = f"{name} has submitted a contact request.\nNumber: {number}" \
                          f"\nEmail: {email}\nMessage: {message}"

        # Send email with contact info and message
        with smtplib.SMTP("smtp-mail.outlook.com", 587) as connection:
            connection.starttls()
            connection.login(user=SENDER_EMAIL, password=SENDER_PASS)
            connection.sendmail(
                from_addr=SENDER_EMAIL,
                to_addrs=RECEIVE_EMAIL,
                msg=f"Subject:Contact Requested!\n\n{contact_message}"
            )
        return redirect(url_for("home"))

    else:
        return render_template("contact.html", form=contact_form)


if __name__ == "__main__":
    app.run()
