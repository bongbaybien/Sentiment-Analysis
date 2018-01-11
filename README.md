This repo predict movie ratings sentiment from review texts using pre-trained word2vec embeddings and Convolutional Neural Network

To get pre-trained word2vec embeddings: https://code.google.com/archive/p/word2vec/ 
Movie ratings data: https://www.kaggle.com/c/word2vec-nlp-tutorial/data

Implemented Kim's simple CNN structure, only trained for a few epochs, 83% accuracy on test set.
Kim's paper:https://arxiv.org/pdf/1408.5882v2.pdf

LexVec word embedding model(claimed to get better performance): https://github.com/alexandres/lexvec#pre-trained-vectors


Reference:
https://blog.keras.io/using-pre-trained-word-embeddings-in-a-keras-model.html
https://github.com/alexander-rakhlin/CNN-for-Sentence-Classification-in-Keras
http://www.wildml.com/2015/12/implementing-a-cnn-for-text-classification-in-tensorflow/
