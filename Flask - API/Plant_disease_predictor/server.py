import numpy as np
from flask import Flask, request, render_template, jsonify
from classifier import Classifier
from PIL import Image
from processed_image import Show_image


app = Flask(__name__)
clf = Classifier()
output = Show_image()

labels = ["Healthy","Early blight","Late blight","Bacterial spot"]

@app.route("/UploadImage", methods=['POST'])
def UploadImage():
    if request.method == "POST":
        
        file = request.files['image']
        img = Image.open(file.stream)
        
        status = clf.predict(img)
        output_image = output.show(img)
        output_image = "data:image/jpeg;base64," + output_image
        # labels = ["Bacterial Spot", "Early Blight", "Healthy", "Late Blight"]
        # status = labels[np.argmax(status)]
    #     cv2.imsave("Image/1.jpeg",output_image)
    # return render_template('main_page.html',var = "Image/1.jpeg")  
    return jsonify({"status": status , "output_image": output_image})

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=8030)
