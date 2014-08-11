import time
import numpy
import stackexchange

import os
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(DEBUG=True,SECRET_KEY='dev key'))
app.config.from_envvar('SO_SETTINGS', silent=True)

@app.route('/')
def index():
	date = numpy.floor(time.time())
	backtime = date - 200000
	so = stackexchange.Site(stackexchange.StackOverflow, 'Z)iD*QKTXBvP6HbHiwcukg((')
	stackexchange.web.WebRequestManager.debug = True
	so.impose_throttling = True
	so.throttle_stop = False

	questions = list(so.questions(sort=stackexchange.Sort.Creation, order=stackexchange.DESC, from_date=backtime, to_date=date))
	# questions = so.recent_questions(pagesize=10)
	return render_template('index.html', questions=questions)

if __name__ == '__main__':
	app.run(debug=True)