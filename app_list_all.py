from flask import Flask
from flask import request
from flask import render_template
from flask import send_from_directory

import os

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
	return render_template("upload.html")

@app.route("/upload",methods=['POST'])
def upload():
	target = os.path.join(APP_ROOT,'images/')
	print target

	if not os.path.isdir(target):
		os.mkdir(target)
	else:
		print "Could not create the directory {}".format(target)

	for upload in request.files.getlist("files"):
		print upload
		filename = upload.filename
		destination = "/".join([target,filename])
		print "Accepting incoming file: ",filename
		print "Destination of the file: ",destination
		upload.save(destination)

	return render_template("complete.html",image_name=filename)

@app.route("/upload/<filename>")
def send_image(filename):
	return send_from_directory("images",filename)

@app.route("/gallery")
def get_gallery():
	image_names = os.listdir('./images')
	print image_names
	return render_template("gallery.html",image_names=images)


if __name__ == '__main__':
	app.run(debug=True)
