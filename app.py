from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session
# from databases import query_all

app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"


@app.route('/')
def home_page():
	return render_template("index.html")

@app.route('/work')
def instegram_page():
	return render_template("work.html")

@app.route('/contact')
def contact_page():
	return render_template("contact.html")

@app.route('/about')
def about_page():
	return render_template("about.html")




if __name__ == '__main__':
    app.run(debug=True)