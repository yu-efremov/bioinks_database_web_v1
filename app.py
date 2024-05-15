from flask import Flask, render_template, jsonify, request

from database import load_bioinks_from_db


app = Flask(__name__)

@app.route("/")
def hello_bioinks():
  bioinks = load_bioinks_from_db()
  return render_template('home.html', 
                         bioinks=bioinks)


@app.route("/api/bioinks/<id>")
def list_bioinks():
  bioinks = load_bioinks_from_db()
  return jsonify(bioinks)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)