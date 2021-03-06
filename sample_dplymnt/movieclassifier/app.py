from flask import Flask, render_template, request
from wtforms import Form, TextAreaField, validators
import pickle
import os
import sqlite3
import numpy as np

from vectorizer import vect

app = Flask(__name__)

cur_dir = os.path.dirname(__file__)
clf = pickle.load(open(os.path.join(cur_dir,'pkl_objects', 'classifier.pkl'), 'rb'))

db = os.path.join(cur_dir, 'reviews.sqlite')

def classify(document):
	label = {0: 'negative', 1: 'positive'}
	X = vect.transform([document])
	y = clf.predict(X)[0]
	proba = np.max(clf.predict_proba(X))
	return label[y], proba*100

def train(document, y):
	X = vect.transform([document])
	clf.partial_fit(X, [y])

def sqlite_entry(path, document, y):
	conn = sqlite3.connect(path)
	c = conn.cursor()
	c.execute("INSERT INTO review_db VALUES (?, ?, DATETIME('now'))", (document, y))
	conn.commit()
	conn.close()

## FLASK

class ReviewForm(Form):
	movieReview = TextAreaField('', [validators.DataRequired(), validators.length(min=15)])


@app.route('/')
def index():
	form = ReviewForm(request.form)
	return render_template('reviewform.html', form=form)

@app.route('/results', methods=['POST'])
def results():
	form = ReviewForm(request.form)
	if request.method == 'POST' and form.validate():
		review = request.form['movieReview']
		y, proba = classify(review)
		return render_template('results.html', content=review, prediction=y, proba=round(proba))
	return render_template('reviewform.html', form=form)

@app.route('/thanks', methods=['POST'])
def thanks():
	feedback = request.form['feedback_button']
	review = request.form['review']
	prediction = request.form['prediction']

	inv_label = {'negative':0, 'positive':1}
	y = inv_label[prediction]
	if feedback == 'Incorrect':
		y = int(not(y))
	train(review, y)
	sqlite_entry(db, review, y)
	return render_template('thanks.html')

if __name__ == '__main__':
	app.run(debug=True)
