from flask import Flask, render_template
import sqlite3


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/index')
def home():
    return render_template("index.html")

@app.route('/team')
def team():
    return render_template("team.html")

@app.route('/movie')
def moive():
    datalist = []
    connect = sqlite3.connect("database/Movie.db")
    cur = connect.cursor()
    sql = "SELECT * FROM movie250"
    data = cur.execute(sql)
    for item in data:
        datalist.append(item)
    cur.close()
    connect.close()
    return render_template("movie.html", movies = datalist )

@app.route('/rating')
def rating():
    score = []
    count = []
    connect = sqlite3.connect("database/Movie.db")
    cur = connect.cursor()
    sql = "SELECT score, count(score) FROM movie250 group by score"
    data = cur.execute(sql)
    for item in data:
        score.append(item[0])
        count.append(item[1])
    cur.close()
    connect.close()
    return render_template("rating.html",score = score, count = count)


@app.route('/wordcloud')
def wordcloud():
    return render_template("wordcloud.html")

if __name__ == '__main__':
    app.run()
