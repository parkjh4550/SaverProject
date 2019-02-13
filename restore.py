import tensorflow as tf

# 1. Variables
weights = tf.Variable(tf.random_normal([2,3], stddev = 0.35),
                      name = "weights")

biases = tf.Variable(tf.zeros([3]), name = "biases")

# 2. Intiailize
init_op = tf.global_variables_initializer()
    #saver
saver = tf.train.Saver({"weights": weights})

# 3. Session
with tf.Session() as sess:
    #init operation
    sess.run(init_op)

    print('initialized weights')
    print(sess.run(weights))
    print(sess.run(biases))

    saver.restore(sess, 'save/model.ckpt')
    print('restored weights')
    print(sess.run(weights))
    print(sess.run(biases))

    print('trainable variables')
    var_list = sess.run(tf.trainable_variables())
    var_names = [v.name for v in tf.trainable_variables()]
    print('var_names : ', var_names)
    values = sess.run(var_names)

    for k,v in zip(var_names, values):
        print( 'variable : ', k)
        print( 'value : ', v)