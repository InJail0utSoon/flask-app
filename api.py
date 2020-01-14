from flask import Flask
from flask_restful import Resource, Api
import tensorflow as tf
app = Flask(__name__)
api = Api(app)

keras=tf.keras
import numpy as np



class HelloWorld(Resource):
	if request.method == 'POST':
		file=request.files.get('file')
		print(file.filename)
		save_and_upload(file)
    test_model = tf.keras.models.load_model('training7.h5')
    test_gen = tf.keras.preprocessing.image.ImageDataGenerator(
								preprocessing_function=keras.applications.mobilenet.preprocess_input).flow_from_directory(directory='testing',
                                                                                            								target_size=(224, 224),
                                                                                                    						batch_size=1,
                                                                                            								shuffle=False)
    test_gen.reset()
    p = test_model.predict_generator(test_gen, steps=1)
    predicted_label = np.argmax(p, axis=1)
    global var
    if(predicted_label[0]==1):
        var="pothole"
    else:
        var="not-pothole"
    def get(self):
        return {'hello': var}
api.add_resource(HelloWorld, '/')



if __name__ == '__main__':
    app.run(port=4505,debug=True)
