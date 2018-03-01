from flask import Flask , render_template , request
from werkzeug import secure_filename

app = Flask(__name__)

@app.route('/')

def index():
	return render_template('up.html')

@app.route('/uploader',methods=['GET','POST'])
def uploader():
	if request.method == 'POST':
		f = request.files['file']
		f.save(secure_filename(f.filename))
		return 'file uploaded'

	
if __name__ == '__main__':
	app.run(debug=True)
