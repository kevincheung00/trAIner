from flask import Flask, render_template, request
from flask.ext.uploads import UploadSet, configure_uploads, IMAGES

ALLOWED_EXTENSIONS = set(['txt', 'jpg'])

app = Flask(__name__)

# photos = UploadSet('photos', Images)
#
# @app.route('/upload', methods=['GET', 'POST'])
#
# def upload():
#     if request.method == 'POST' and 'photo' in request.files:
#         filename = photos.save(request.files['photo'])
#         return filename
#
#     return render_template('upload.html')
#
# if __name__ == '__main__':
#     app.run(debug=True)


@app.route("/")
def index():
    return render_template("abc.html")
