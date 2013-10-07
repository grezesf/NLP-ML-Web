#!/bin/sh

# path to Weka's jar file
# weka_jar=/cygdrive/c/Program\ Files\ \(x86\)/Weka-3-7/weka.jar
# weka_jar=/cygdrive/c/weka.jar

weka_jar=/home/apps/weka-3-7-1/weka.jar

# test if weka_jar found
if test -f "$weka_jar"; then
    echo "found Weka JAR in"
    echo $weka_jar
else
    echo "Weka JAR not found "
    exit -1 
fi

# echo "found Weka JAR in" && echo $weka_jar
# echo "Weka JAR not found " &&


# memory to allocate for the JVM
jvm_mem=4096m
# jvm_mem=10240m

# results dir/
if test -d ./results/; then
    results_dir=./results/
else
    echo "results directory not found"
    exit -1
fi


# training features
if test -f ./data/train/train-feats.arff; then
    train_set=./data/train/train-feats.arff
else
    echo "training data not found"
    exit -1
fi

# test features
if test -f ./data/test/test-feats.arff; then
    test_set=./data/test/test-feats.arff
else
    echo "test data not found"
    exit -1
fi

# create subdirs with timestamp
exp_dir=$results_dir/`date +%Y-%h-%T`
echo "making new experiment directory named $exp_dir\n"
mkdir $exp_dir

echo "Task 1 : MEDIA"
task=MEDIA
# choose appropriate target feature
target=2
# ignore all but the text
ignore_list=1,3,4,5,6

# make sub-exp directory
task_dir=$exp_dir/$task
mkdir $task_dir

echo "Representation: bag-of-words\n"
# make representation directory
sub_task=rep--bag-of-words
sub_task_dir=$exp_dir/MEDIA/$sub_task
mkdir $sub_task_dir

# name to save the model under
model=$sub_task_dir/$task-$sub_task.model


# training phase
echo "start training the model"

# start time
START=$(date +%s)

# call to weka
java -Xmx$jvm_mem -classpath $weka_jar \
weka.classifiers.meta.FilteredClassifier  -i -c $target -t $train_set -T $test_set -d $model \
-F "weka.filters.MultiFilter -F \"weka.filters.unsupervised.attribute.Remove -R $ignore_list\" -F \"weka.filters.unsupervised.attribute.StringToWordVector -R first-last -W 1000 -prune-rate -1.0 -N 0 -stemmer weka.core.stemmers.NullStemmer -M 1 -tokenizer \\\"weka.core.tokenizers.WordTokenizer -delimiters \\\\\\\" \\\\\\\\r\\\\\\\\n\\\\\\\\t.,;:\\\\\\\\\\\\\\\'\\\\\\\\\\\\\\\"()?!\\\\\\\"\\\"\"" \
-W weka.classifiers.functions.SMO -- -C 1.0 -L 0.001 -P 1.0E-12 -N 0 -V -1 -W 1 \
-K "weka.classifiers.functions.supportVector.PolyKernel -C 250007 -E 1.0" \
> $sub_task_dir/$task-$sub_task.stats

# end time
END=$(date +%s)
DIFF=$(( $END - $START ))
echo "training took $DIFF seconds"

# testing phase
echo "testing the model\n"
java -Xmx$jvm_mem -classpath $weka_jar \
weka.classifiers.meta.FilteredClassifier -o -c $target -l "$model" \
-T $test_set -p 0 -distribution \
> $sub_task_dir/$task-$sub_task.predictions

echo "Task 1 finished. Results in $task_dir/$sub_task_dir"


