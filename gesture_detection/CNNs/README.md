# Gesture Detection (using TensorFlow)

The model is trained using transfer learning on pretrained model VGG16. The dataset is obtained from kaggle, it can be found 
<a href="https://www.kaggle.com/koryakinp/fingers">here</a>. <br>
The model is achieved by flattening, followed by adding dense layers, toppmost layer being a softmax layer. It is supposed to classify between 6 different gestures.<br>
The loss function used is **sparse_categorical_crossentropy**, optimizer is **Adam** while the activation used in the topmost layer is **sofmax**(due to multiclass nature of the problem). 