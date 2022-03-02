from flask import Flask,jsonify
import csv

app=Flask(__name__)
with open('articles.csv',encoding="utf-8")as f:
    reader=csv.reader(f)
    data=list(reader)
    all_articles=data[1:]

liked_articles=[]
not_likes_articles=[]
@app.route("/get-articles")
def get_articles():
    return jsonify({
        "data":all_articles[0],
        "status":"success"
    })

@app.route("/liked_articles",methods=["POST"])
def liked_articles():
    article=all_articles[0]
    all_movies=all_movies[1:]
    liked_articles.append(article)
    return jsonify({
        "status":"success"
    }),201

@app.route("/not_likes_articles",methods=["POST"])
def not_likes_articles():
    article=all_movies[0]
    all_movies=all_movies[1:]
    not_likes_articles.append(article)
    return jsonify({
        "status":"success"
    }),201

if __name__=="__main__":
    app.run()