#!/bin/sh

# path to Weka's jar file
weka_jar=/home/apps/weka-3-7-1/weka.jar
test -f $weka_jar || exit -1

# memory to allocate for the JVM
jvm_mem=4096m
# jvm_mem=10240m

### weka.classifiers.meta.FilteredClassifier -F "weka.filters.unsupervised.attribute.Remove -V -R 5,7" -W weka.classifiers.meta.FilteredClassifier -- -F "weka.filters.unsupervised.attribute.StringToWordVector -R first-last -W 10000 -prune-rate -1.0 -N 0 -stemmer weka.core.stemmers.NullStemmer -M 1 -tokenizer \"weka.core.tokenizers.NGramTokenizer -delimiters \\\" \\\\r \\\\t.,;:\\\\\\\'\\\\\\\"()?! \\\" -max 3 -min 3\"" -W weka.classifiers.lazy.LWL -- -U 0 -K -1 -A "weka.core.neighboursearch.LinearNNSearch -A \"weka.core.EuclideanDistance -R first-last\"" -W weka.classifiers.trees.DecisionStump