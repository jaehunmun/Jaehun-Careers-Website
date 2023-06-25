from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Bucheon',
        'salary': 'working with passion'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Seoul'
    },
    {
        'id': 3,
        'title': 'Teaching Assistance',
        'location': 'Remote',
        'salary': '1000 Won'
    }
]


@app.route("/")
def hello_world():
    return render_template('home.html', jobs=JOBS, company_name = "Jaehun")

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

print(__name__)
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
