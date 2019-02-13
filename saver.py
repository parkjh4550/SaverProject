import tensorflow as tf

# 1. Variables
weights = tf.Variable(tf.random_normal([2,3], stddev = 0.35),
                      name = "weights")

biases = tf.Variable(tf.ones([3]), name = "biases")

# 2. Intiailize
init_op = tf.global_variables_initializer()
    #saver
saver = tf.train.Saver()

# 3. Session
with tf.Session() as sess:
    #init operation
    sess.run(init_op)
    print(weights)
    print(sess.run(weights))
    save_path = saver.save(sess, './save/model.ckpt')
    print('model saved')