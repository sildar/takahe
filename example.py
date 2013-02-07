#!/usr/bin/python
# -*- coding: utf-8 -*-

import takahe

################################################################################
sentences = ["The/DT wife/NN of/IN a/DT former/JJ U.S./NNP president/NN \
Bill/NNP Clinton/NNP Hillary/NNP Clinton/NNP visited/VBD China/NNP last/JJ \
Monday/NNP ./PUNCT", "Hillary/NNP Clinton/NNP wanted/VBD to/TO visit/VB China/NNP \
last/JJ month/NN but/CC postponed/VBD her/PRP$ plans/NNS till/IN Monday/NNP \
last/JJ week/NN ./PUNCT", "Hillary/NNP Clinton/NNP paid/VBD a/DT visit/NN to/TO \
the/DT People/NNP Republic/NNP of/IN China/NNP on/IN Monday/NNP ./PUNCT", 
"Last/JJ week/NN the/DT Secretary/NNP of/IN State/NNP Ms./NNP Clinton/NNP \
visited/VBD Chinese/JJ officials/NNS ./PUNCT"]
################################################################################

# Create a word graph from the set of sentences
compresser = takahe.word_graph(sentences, 6, 'en', 'PUNCT')

# Get the 50 best paths
best_paths = compresser.get_compression(5)

# Rerank compressions by path length
for cummulative_score, path in best_paths:

	# Compute the normalized score
	normalized_score = cummulative_score / len(path)

	# Print normalized score and compression
	print round(normalized_score, 3), ' '.join([u[0] for u in path])