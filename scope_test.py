import tensorflow as tf
import numpy as np

save_flag = False

var1 = tf.Variable(3., dtype=tf.float64, name="var1")
var1_2 = tf.Variable(4., dtype=tf.float64, name="var2")
var1_3 = tf.Variable(5. , dtype=tf.float64)
with tf.variable_scope("test"):
    var1_4 = tf.Variable(6. , dtype=tf.float64)


var2 = tf.get_variable("var1", [], dtype=tf.float64)

with tf.variable_scope("var3_scope"):
    init = np.random.rand(3,2)
    print(init)
    #if initializer is a contant, do not have to specify the shape
    #  error ex) tf.get_variable("var3", [3,2], initializer=init)
    var3 = tf.get_variable("var3", initializer=init)

init_op = tf.global_variables_initializer()

# Saver
if save_flag is True:
    saver = tf.train.Saver()
else:
    #we can restore them by "variable_scope/variable_name"
    saver = tf.train.Saver({"var1" : var1_2, "test/Variable": var1})



with tf.Session() as sess:
    sess.run(init_op)

    if save_flag is True:
        save_path = saver.save(sess, './save/scope_test/model.ckpt')
    else:
        saver.restore(sess, './save/scope_test/model.ckpt')

    print('-----variable names')
    var_names = [v.name for v in tf.trainable_variables()]
    print('all variables name : ',var_names)

    print('\n each variables name')
    print(var1.name)
    print(var2.name)
    print(var3.name)
    print('\n')

    print('----variable value')
    print(sess.run(var1))
    print(sess.run(var2))
    print(sess.run(var3))

    print('restore test')
    print('var1 value : ', sess.run(var1))
    print('var1_2 value : ', sess.run(var1_2))