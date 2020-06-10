# One Shot Learning

Conventional deep neural networks constructs require large datasets in order to learn classifying labelled images. By one shot 
learning, we try to somehow reduce this barrier of always requiring a large dataset.

Our aim is to create a gesture detector model that takes an input image and converts it to an encoding. This encoding of two
images of the same class is supposed to have small L2 distance.

## Dataset
<a href="https://ieee-dataport.org/open-access/static-hand-gesture-asl-dataset" >
Static Hand Gesture Dataset </a> is used for training. For testing purposes, manual dataset(15 gestures) is created.

## Siamese Neural Nework
This is the architecture generally used for one shot learning purposes. We pass anchor, positive(same class as anchor), 
and negative (different class) images to the same base network, then we define **triplet loss** on the three encodings produced. 
Based on this triplet loss the base network is trained. Implementation can be seen in the IPython notebook here in this subdirectory or can be
seen directly as implemented on <a href="https://colab.research.google.com/drive/1Ku--faEAJWZ-s8vj80TXCLrW4TjfzWys?usp=sharing">
Colab</a>. First try was by manally training the whole base network using binary classification of paired images, but hat didn't
achieve any respectable accuracy, implementation can be seen in
<a href = "https://colab.research.google.com/drive/1LmFwb1p1NyV6KxNJwpmiAydE7MqMuHzg?usp=sharing">this</a> Colab notebook.<br>
Therefore, for base network, weights of pretrained VGG16 network (directly from keras.applications) and 
<a href="https://github.com/iwantooxxoox/Keras-OpenFace">FaceNet</a> are fine-tuned (see references).
VGG16 gave the better train accuracy.

## Results
Test accuracy of 85.8% was achieved using VGG16 network.

## References
1. https://www.coursera.org/learn/convolutional-neural-networks
2. https://sorenbouma.github.io/blog/oneshot/
3. http://www.cs.cmu.edu/~rsalakhu/papers/oneshot1.pdf
4. https://github.com/KinWaiCheuk/Triplet-net-keras
5. https://ieee-dataport.org/open-access/static-hand-gesture-asl-dataset

This is the final project of the two month long SoC organised by WnCC, IITB.