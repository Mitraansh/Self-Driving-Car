import tensorflow as tf

tf.train.import_meta_graph("./save/model.ckpt.meta")
for n in tf.get_default_graph().as_graph_def().node:
   print(n)