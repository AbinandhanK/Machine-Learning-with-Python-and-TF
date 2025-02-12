import tensorflow as tf
rank1_tensor=tf.Variable([["Hello","Hi", "Greetings"],["Python","C","C++"]])
print(tf.rank(rank1_tensor))
