from flask import Flask, send_from_directory, render_template_string

app = Flask(__name__)


@app.route("/")
@app.route("/<path:path>")
def index(path=""):
    try:
        with open("templates/contacts.html", "r", encoding="utf-8") as file:
            content = file.read()
        return render_template_string(content)
    except FileNotFoundError:
        return "Page not found", 404


@app.route("/css/<path:filename>")
def css_files(filename):
    return send_from_directory("css", filename)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
