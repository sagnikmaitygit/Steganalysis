from flask import Flask, flash, request, redirect, url_for, jsonify,render_template
from werkzeug.utils import secure_filename
import os
from util import encode,image2Bin
path = os.path.abspath(os.getcwd())
UPLOAD_FOLDER = path + "\\static\\upload"
UPLOAD_FOLDER2 = path + "\\static\\upload\\encoded"
UPLOAD_FOLDER3 = path + "\\static\\upload\\decode"
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['UPLOAD_FOLDER2'] = UPLOAD_FOLDER2
app.config['UPLOAD_FOLDER3'] = UPLOAD_FOLDER3
@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
@app.route('/encode', methods=['POST',"GET"])
def upload_file():
    if request.method =="GET":
        return render_template("encode.html")
    if 'file' not in request.files:
        return render_template("encode_error.html",params={"error":True, "message":"Please Upload A Image"})
    pic = request.files['file']
    if pic.filename == '':
        return render_template("encode_error.html",params={"error":True, "message":"No File Selected"})
    if pic and allowed_file(pic.filename):
        import os
        import datetime
        basename = "encoded"
        suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
        filename = "_".join([basename, suffix])
        filename = filename + "." + pic.filename.rsplit('.', 1)[1].lower()
        if os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'],filename)):
            os.remove(os.path.join(
                app.config['UPLOAD_FOLDER'], filename))
        pic.save(os.path.join(
            app.config['UPLOAD_FOLDER'], filename))
        
        password=request.form.get("pass")
        text=request.form.get("text")
        files_out=filename.split('.')[0] +'_modified.png'
        encode(text,password,os.path.join(app.config['UPLOAD_FOLDER'],filename),os.path.join(app.config['UPLOAD_FOLDER2'],files_out))
        result = {
        "error":False,
        "message":"Data Image Encoded Successfully",
        "link":f"/static/upload/encoded/{files_out}",
        "file_name":f"/upload/encoded/{files_out}"
        }
        return render_template("encode_success.html",params=result)
    return render_template("encode_error.html",params={"error":True, "message":"Please Upload A valid Image."})
@app.route('/decode', methods=['POST',"GET"])
def decode_file():
    if request.method =="GET":
        return render_template("decode.html")
    if 'file' not in request.files:
        return render_template("decode_error.html",params={"error":True, "message":"Please A Image."})
    pic = request.files['file']
    if pic.filename == '':
        return jsonify({"error": True, "data": "No File selected"})
    if pic and allowed_file(pic.filename):
        import os
        import datetime
        basename = "decode"
        suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
        filename = "_".join([basename, suffix])
        filename = filename + "." + pic.filename.rsplit('.', 1)[1].lower()
        if os.path.exists(os.path.join(app.config['UPLOAD_FOLDER3'],filename)):
            os.remove(os.path.join(
                app.config['UPLOAD_FOLDER3'], filename))
        pic.save(os.path.join(
            app.config['UPLOAD_FOLDER3'], filename))
        password=request.form.get("pass")
        msg=image2Bin(os.path.join(app.config['UPLOAD_FOLDER3'],filename),password)
        result = {
        "error":False,
        "message":"Data Image Encoded Successfully",
        "data":msg,
        "link":f"/upload/decode/{filename}"
        }
        if msg=="-1":
            return render_template("decode_error.html",params={"error":True, "message":"Wrong Data Provided"})
        return render_template("decode_success.html",params=result)
    return render_template("decode_error.html",params={"error":True, "message":"Please Upload A valid Image."})
run flask -- port = 10000
app.run()
