from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)



# @app.context_processor
# def override_url_for():
#     return dict(url_for=dated_url_for)
#
#
# def dated_url_for(endpoint, **values):
#     if endpoint == 'static':
#         filename = values.get('filename', None)
#         if filename:
#             file_path = os.path.join(app.root_path,
#                                      endpoint, filename)
#             values['q'] = int(os.stat(file_path).st_mtime)
#     return url_for(endpoint, **values)


@app.route("/")
def home():
    return render_template("homepage.html")


@app.route("/shop")
def shop():
    return render_template("shop.html")


@app.route("/contacts")
def contacts():
    return render_template("contacts.html")

@app.route("/partners")
def partners():
    return render_template("partners.html")


if __name__ == "__main__":
    app.run()
    app.config['FLASK_ENV'] = True
    # app.run(debug=True)
    # app.config['TEMPLATE_AUTO_RELOAD'] = True
