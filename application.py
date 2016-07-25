from flask import Flask, render_template,request
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

@app.route("/")
def index_page():
    """Show an index page."""

    # return "<html><body>This is the homepage.</body></html>"

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    return render_template("index.html")

@app.route("/application-form")
def application_page():
    """ Take user to application form"""

    return render_template("application-form.html")

@app.route("/application",methods=["POST"])
def application():
    """Take user to application screen"""

    first_name=request.form.get("firstname")
    job_title=request.form.get("job-titile")
    salary=request.form.get("salary")

    return render_template("/application-response.html",
                           first_name=first_name,
                           job_title=job_title,
                           salary_requirement=salary)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="127.0.0.1", port=5000)

