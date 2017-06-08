from app import app
import datetime

@app.route('/')
@app.route('/index')
def index():
	timestamp = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
	return timestamp + " Hello, World! DEV_1-v4.0\n"
