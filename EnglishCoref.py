import os
import sys
import time
import json
import numpy as np

import cgi
#from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
#import ssl

import tensorflow as tf
import coref_model as cm
import util

import nltk
nltk.download("punkt")
from nltk.tokenize import sent_tokenize, word_tokenize
class EnglishCorefResolution():
	def _load_model(self,experiment):
		util.set_gpus()
		print "Running experiment: {}.".format(experiment)
		config = util.get_config("experiments.conf")[experiment]
		config["log_dir"] = util.mkdirs(os.path.join(config["log_root"], experiment))
		
		util.print_config(config)
		model = cm.CorefModel(config)
		
		saver = tf.train.Saver()
		log_dir = config["log_dir"]
		
		with tf.Session() as session:
			checkpoint_path = os.path.join(log_dir, "model.max.ckpt")
			saver.restore(session, checkpoint_path)
			self.model=model
			self.session=session
	def __init__(self, experiment):
		self._load_model()
	def _create_example(self,text):
		raw_sentences = sent_tokenize(text)
		sentences = [word_tokenize(s) for s in raw_sentences]
		speakers = [["" for _ in sentence] for sentence in sentences]
		return {
			"doc_key": "nw",
			"clusters": [],
			"sentences": sentences,
			"speakers": speakers,
		}
	def _print_predictions(self,example):
		words = util.flatten(example["sentences"])
		for cluster in example["predicted_clusters"]:
			print(u"Predicted cluster: {}".format([" ".join(words[m[0]:m[1]+1]) for m in cluster]))
	def _make_predictions(self,text):
		example = self._create_example(text)
		tensorized_example = self.model.tensorize_example(example, is_training=False)
		feed_dict = {i:t for i,t in zip(model.input_tensors, tensorized_example)}
		_, _, _, mention_starts, mention_ends, antecedents, antecedent_scores, head_scores = session.run(model.predictions + [model.head_scores], feed_dict=feed_dict)
		
		predicted_antecedents = self.model.get_predicted_antecedents(antecedents, antecedent_scores)
		
		example["predicted_clusters"], _ = self.model.get_predicted_clusters(mention_starts, mention_ends, predicted_antecedents)
		example["top_spans"] = zip((int(i) for i in mention_starts), (int(i) for i in mention_ends))
		example["head_scores"] = head_scores.tolist()
		return example
	def get_clusters(self, document):
		example = self._create_example(document)
		tensorized_example = self.model.tensorize_example(example, is_training=False)
		feed_dict = {i:t for i,t in zip(self.model.input_tensors, tensorized_example)}
		_, _, _, mention_starts, mention_ends, antecedents, antecedent_scores, head_scores = self.session.run(self.model.predictions + [self.model.head_scores], feed_dict=feed_dict)
		predicted_antecedents = self.model.get_predicted_antecedents(antecedents, antecedent_scores)		
		predicted_clusters, _ = self.model.get_predicted_clusters(mention_starts, mention_ends, predicted_antecedents)
		return predicted_clusters
if __name__==__main__
	my_model=EnglishCorefResolution('final')
	my_model.get_clusters("Mohamed did a great job. He finished his task")
