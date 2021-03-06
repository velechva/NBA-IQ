from IOUtils import loadData

import tensorflow as tf
import numpy as np

trainX, trainY, testX, testY = loadData()

nodeCount_1 = 154
nodeCount_2 = 154

epochCount = 2000
batchSize = 154
classCount = 2

x = tf.placeholder('float')
y = tf.placeholder('float')

hiddenLayerOne = {'f_num': nodeCount_1,
                    'weight': tf.Variable(tf.random_normal([len(trainX[0]), nodeCount_1])),
                    'bias': tf.Variable(tf.random_normal([nodeCount_1]))}

hiddenLayerTwo = {'f_num': nodeCount_2,
                  'weight': tf.Variable(tf.random_normal([nodeCount_1, nodeCount_2])),
                  'bias': tf.Variable(tf.random_normal([nodeCount_2]))}

outputLayer = {'f_num': None,
                'weight': tf.Variable(tf.random_normal([nodeCount_2, classCount])),
                'bias': tf.Variable(tf.random_normal([classCount]))}

def neuralNetworkModel(data):

    print('TrainX: ' + str(len(trainX)))
    print('TestX: ' + str(len(testX)))

    l1 = tf.add(tf.matmul(data, hiddenLayerOne['weight']), hiddenLayerOne['bias'])
    l1 = tf.nn.relu(l1)

    l2 = tf.add(tf.matmul(l1, hiddenLayerTwo['weight']), hiddenLayerTwo['bias'])
    l2 = tf.nn.relu(l2)

    output = tf.matmul(l2, outputLayer['weight'] + outputLayer['bias'])
    
    return output

def trainNet(x):
    predict = neuralNetworkModel(x)
    cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(predict, y))
    optimizer = tf.train.AdamOptimizer(learning_rate = 0.1).minimize(cost)

    with tf.Session() as sess:
        sess.run(tf.initialize_all_variables())

        for epoch in range(epochCount):
            epochLoss = 0

            i = 0
            j = 0
            while i < len(trainX):
                start = i
                end = i + batchSize

                batchX = np.array(trainX[start:end])
                batchY = np.array(trainY[start:end])

                _, c = sess.run([optimizer, cost], feed_dict = {x: batchX,
                                                                y: batchY})

                epochLoss += c
                i += batchSize

        correct = tf.equal(tf.argmax(predict, 1), tf.argmax(y, 1))
        accuracy = tf.reduce_mean(tf.cast(correct, 'float'))

        print('Accuracy: ', accuracy.eval({x: testX, y: testY}))

trainNet(x)