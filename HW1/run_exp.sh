#!/bin/sh


### README
# this script runs all of our experiments using WEKA
# and saves the models, stats and prediction in a new folder under ./results/


# path to Weka's jar file
weka_jar=/home/apps/weka-3-7-9/weka.jar

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
results_dir=./results/
if test -d ./results/; then
    continue
else
    echo "creating results directory"
    mkdir $results_dir
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

###################
# Task 1 of 5: MEDIA
###################

echo "Task 1 of 5 : MEDIA"
task=MEDIA
# choose appropriate target feature
target=2
# ignore all but the text
ignore_list=1,3,4,5,6

# make sub-exp directory
task_dir=$exp_dir/$task
mkdir $task_dir

###################
# Representation 1 of 3: bag-of-words
###################

echo "Representation 1 of 3: bag-of-words"
# make representation directory
sub_task=rep--bag-of-words
sub_task_dir=$exp_dir/$task/$sub_task
mkdir $sub_task_dir

# name to save the model under
model=$sub_task_dir/$task-$sub_task.model


# training phase
echo "training the model"

# start time
START=$(date +%s)

# call to weka
java -Xmx$jvm_mem -classpath $weka_jar \
weka.classifiers.meta.FilteredClassifier -i -c $target -t $train_set -T $test_set -d $model \
-F "weka.filters.MultiFilter -F \"weka.filters.unsupervised.attribute.Remove -R $ignore_list\" -F \"weka.filters.unsupervised.attribute.StringToWordVector -R first-last -W 1000 -prune-rate -1.0 -N 0 -stemmer weka.core.stemmers.NullStemmer -M 1 -tokenizer \\\"weka.core.tokenizers.WordTokenizer -delimiters \\\\\\\" \\\\\\\\r\\\\\\\\n\\\\\\\\t.,;:\\\\\\\\\\\\\\\'\\\\\\\\\\\\\\\"()?!\\\\\\\"\\\"\"" \
-W weka.classifiers.functions.SMO -- -C 1.0 -L 0.001 -P 1.0E-12 -N 0 -V -1 -W 1 \
-K "weka.classifiers.functions.supportVector.PolyKernel -C 250007 -E 1.0" \
> $sub_task_dir/$task-$sub_task.stats
# | tee -a $sub_task_dir/$task-$sub_task.stats

# end time
END=$(date +%s)
DIFF=$(( $END - $START ))
echo "training took $DIFF seconds"

# testing phase
echo "testing the model"
java -Xmx$jvm_mem -classpath $weka_jar \
weka.classifiers.meta.FilteredClassifier -c $target -l "$model" \
-T $test_set -p $target -distribution \
> $sub_task_dir/$task-$sub_task.predictions

# convert weka style predictions to homework style
python ./tools/convert_predictions.py $sub_task_dir/$task-$sub_task.predictions $test_set

echo "Task 1 of 5, representation 1 of 3 finished. Results in $sub_task_dir \n"


###################
# Representation 2 of 3: bi-grams
###################

echo "Task 1 of 5 : MEDIA"
echo "Representation 2 of 3: bi-grams"
# make representation directory
sub_task=rep--bi-grams
sub_task_dir=$exp_dir/$task/$sub_task
mkdir $sub_task_dir

# name to save the model under
model=$sub_task_dir/$task-$sub_task.model


# training phase
echo "training the model"

# start time
START=$(date +%s)

# call to weka
java -Xmx$jvm_mem -classpath $weka_jar \
weka.classifiers.meta.FilteredClassifier -i -c $target -t $train_set -T $test_set -d $model \
-F "weka.filters.MultiFilter -F \"weka.filters.unsupervised.attribute.Remove -R $ignore_list\" -F \"weka.filters.unsupervised.attribute.StringToWordVector -R first-last -W 1000 -prune-rate -1.0 -N 0 -stemmer weka.core.stemmers.NullStemmer -M 1 -tokenizer \\\"weka.core.tokenizers.NGramTokenizer -delimiters \\\\\\\" \\\\\\\\r\\\\\\\\n\\\\\\\\t.,;:\\\\\\\\\\\\\\\'\\\\\\\\\\\\\\\"()?!\\\\\\\" -max 2 -min 2\\\"\"" \
-W weka.classifiers.functions.SMO -- -C 1.0 -L 0.001 -P 1.0E-12 -N 0 -V -1 -W 1 \
-K "weka.classifiers.functions.supportVector.PolyKernel -C 250007 -E 1.0" \
> $sub_task_dir/$task-$sub_task.stats
# | tee -a $sub_task_dir/$task-$sub_task.stats

# end time
END=$(date +%s)
DIFF=$(( $END - $START ))
echo "training took $DIFF seconds"

# testing phase
echo "testing the model"
java -Xmx$jvm_mem -classpath $weka_jar \
weka.classifiers.meta.FilteredClassifier -c $target -l "$model" \
-T $test_set -p $target -distribution \
> $sub_task_dir/$task-$sub_task.predictions

# convert weka style predictions to homework style
python ./tools/convert_predictions.py $sub_task_dir/$task-$sub_task.predictions $test_set

echo "Task 1 of 5, representation 2 of 3 finished. Results in $sub_task_dir \n"


###################
# Representation 3 of 3: tri-grams
###################

echo "Task 1 of 5 : MEDIA"
echo "Representation 3 of 3: tri-grams"
# make representation directory
sub_task=rep--tri-grams
sub_task_dir=$exp_dir/$task/$sub_task
mkdir $sub_task_dir

# name to save the model under
model=$sub_task_dir/$task-$sub_task.model


# training phase
echo "training the model"

# start time
START=$(date +%s)

# call to weka
java -Xmx$jvm_mem -classpath $weka_jar \
weka.classifiers.meta.FilteredClassifier -i -c $target -t $train_set -T $test_set -d $model \
-F "weka.filters.MultiFilter -F \"weka.filters.unsupervised.attribute.Remove -R $ignore_list\" -F \"weka.filters.unsupervised.attribute.StringToWordVector -R first-last -W 1000 -prune-rate -1.0 -N 0 -stemmer weka.core.stemmers.NullStemmer -M 1 -tokenizer \\\"weka.core.tokenizers.NGramTokenizer -delimiters \\\\\\\" \\\\\\\\r\\\\\\\\n\\\\\\\\t.,;:\\\\\\\\\\\\\\\'\\\\\\\\\\\\\\\"()?!\\\\\\\" -max 3 -min 3\\\"\"" \
-W weka.classifiers.functions.SMO -- -C 1.0 -L 0.001 -P 1.0E-12 -N 0 -V -1 -W 1 \
-K "weka.classifiers.functions.supportVector.PolyKernel -C 250007 -E 1.0" \
> $sub_task_dir/$task-$sub_task.stats
# | tee -a $sub_task_dir/$task-$sub_task.stats

# end time
END=$(date +%s)
DIFF=$(( $END - $START ))
echo "training took $DIFF seconds"

# testing phase
echo "testing the model"
java -Xmx$jvm_mem -classpath $weka_jar \
weka.classifiers.meta.FilteredClassifier -c $target -l "$model" \
-T $test_set -p $target -distribution \
> $sub_task_dir/$task-$sub_task.predictions

# convert weka style predictions to homework style
python ./tools/convert_predictions.py $sub_task_dir/$task-$sub_task.predictions $test_set

echo "Task 1 of 5, representation 3 of 3 finished. Results in $sub_task_dir \n"


###################
# Task 2 of 5: GRADE
###################

echo "Task 2 of 5: GRADE"
task=GRADE
# choose appropriate target feature
target=3
# ignore all but the text
ignore_list=1,2,4,5,6

# make sub-exp directory
task_dir=$exp_dir/$task
mkdir $task_dir

###################
# Representation 1 of 3: bag-of-words
###################

echo "Representation 1 of 3: bag-of-words"
# make representation directory
sub_task=rep--bag-of-words
sub_task_dir=$exp_dir/$task/$sub_task
mkdir $sub_task_dir

# name to save the model under
model=$sub_task_dir/$task-$sub_task.model


# training phase
echo "training the model"

# start time
START=$(date +%s)

# call to weka
java -Xmx$jvm_mem -classpath $weka_jar \
weka.classifiers.meta.FilteredClassifier -i -c $target -t $train_set -T $test_set -d $model \
-F "weka.filters.MultiFilter -F \"weka.filters.unsupervised.attribute.Remove -R $ignore_list\" -F \"weka.filters.unsupervised.attribute.StringToWordVector -R first-last -W 1000 -prune-rate -1.0 -N 0 -stemmer weka.core.stemmers.NullStemmer -M 1 -tokenizer \\\"weka.core.tokenizers.WordTokenizer -delimiters \\\\\\\" \\\\\\\\r\\\\\\\\n\\\\\\\\t.,;:\\\\\\\\\\\\\\\'\\\\\\\\\\\\\\\"()?!\\\\\\\"\\\"\"" \
-W weka.classifiers.functions.SMO -- -C 1.0 -L 0.001 -P 1.0E-12 -N 0 -V -1 -W 1 \
-K "weka.classifiers.functions.supportVector.PolyKernel -C 250007 -E 1.0" \
> $sub_task_dir/$task-$sub_task.stats
# | tee -a $sub_task_dir/$task-$sub_task.stats

# end time
END=$(date +%s)
DIFF=$(( $END - $START ))
echo "training took $DIFF seconds"

# testing phase
echo "testing the model"
java -Xmx$jvm_mem -classpath $weka_jar \
weka.classifiers.meta.FilteredClassifier -c $target -l "$model" \
-T $test_set -p $target -distribution \
> $sub_task_dir/$task-$sub_task.predictions

# convert weka style predictions to homework style
python ./tools/convert_predictions.py $sub_task_dir/$task-$sub_task.predictions $test_set

echo "Task 2 of 5, representation 1 of 3 finished. Results in $sub_task_dir \n"

###################
# Representation 2 of 3: bi-grams
###################

echo "Task 2 of 5 : GRADE"
echo "Representation 2 of 3: bi-grams"
# make representation directory
sub_task=rep--bi-grams
sub_task_dir=$exp_dir/$task/$sub_task
mkdir $sub_task_dir

# name to save the model under
model=$sub_task_dir/$task-$sub_task.model


# training phase
echo "training the model"

# start time
START=$(date +%s)

# call to weka
java -Xmx$jvm_mem -classpath $weka_jar \
weka.classifiers.meta.FilteredClassifier -i -c $target -t $train_set -T $test_set -d $model \
-F "weka.filters.MultiFilter -F \"weka.filters.unsupervised.attribute.Remove -R $ignore_list\" -F \"weka.filters.unsupervised.attribute.StringToWordVector -R first-last -W 1000 -prune-rate -1.0 -N 0 -stemmer weka.core.stemmers.NullStemmer -M 1 -tokenizer \\\"weka.core.tokenizers.NGramTokenizer -delimiters \\\\\\\" \\\\\\\\r\\\\\\\\n\\\\\\\\t.,;:\\\\\\\\\\\\\\\'\\\\\\\\\\\\\\\"()?!\\\\\\\" -max 2 -min 2\\\"\"" \
-W weka.classifiers.functions.SMO -- -C 1.0 -L 0.001 -P 1.0E-12 -N 0 -V -1 -W 1 \
-K "weka.classifiers.functions.supportVector.PolyKernel -C 250007 -E 1.0" \
> $sub_task_dir/$task-$sub_task.stats
# | tee -a $sub_task_dir/$task-$sub_task.stats

# end time
END=$(date +%s)
DIFF=$(( $END - $START ))
echo "training took $DIFF seconds"

# testing phase
echo "testing the model"
java -Xmx$jvm_mem -classpath $weka_jar \
weka.classifiers.meta.FilteredClassifier -c $target -l "$model" \
-T $test_set -p $target -distribution \
> $sub_task_dir/$task-$sub_task.predictions

# convert weka style predictions to homework style
python ./tools/convert_predictions.py $sub_task_dir/$task-$sub_task.predictions $test_set

echo "Task 2 of 5, representation 2 of 3 finished. Results in $sub_task_dir \n"


###################
# Representation 3 of 3: tri-grams
###################

echo "Task 2 of 5 : GRADE"
echo "Representation 3 of 3: tri-grams"
# make representation directory
sub_task=rep--tri-grams
sub_task_dir=$exp_dir/$task/$sub_task
mkdir $sub_task_dir

# name to save the model under
model=$sub_task_dir/$task-$sub_task.model


# training phase
echo "training the model"

# start time
START=$(date +%s)

# call to weka
java -Xmx$jvm_mem -classpath $weka_jar \
weka.classifiers.meta.FilteredClassifier -i -c $target -t $train_set -T $test_set -d $model \
-F "weka.filters.MultiFilter -F \"weka.filters.unsupervised.attribute.Remove -R $ignore_list\" -F \"weka.filters.unsupervised.attribute.StringToWordVector -R first-last -W 1000 -prune-rate -1.0 -N 0 -stemmer weka.core.stemmers.NullStemmer -M 1 -tokenizer \\\"weka.core.tokenizers.NGramTokenizer -delimiters \\\\\\\" \\\\\\\\r\\\\\\\\n\\\\\\\\t.,;:\\\\\\\\\\\\\\\'\\\\\\\\\\\\\\\"()?!\\\\\\\" -max 3 -min 3\\\"\"" \
-W weka.classifiers.functions.SMO -- -C 1.0 -L 0.001 -P 1.0E-12 -N 0 -V -1 -W 1 \
-K "weka.classifiers.functions.supportVector.PolyKernel -C 250007 -E 1.0" \
> $sub_task_dir/$task-$sub_task.stats
# | tee -a $sub_task_dir/$task-$sub_task.stats

# end time
END=$(date +%s)
DIFF=$(( $END - $START ))
echo "training took $DIFF seconds"

# testing phase
echo "testing the model"
java -Xmx$jvm_mem -classpath $weka_jar \
weka.classifiers.meta.FilteredClassifier -c $target -l "$model" \
-T $test_set -p $target -distribution \
> $sub_task_dir/$task-$sub_task.predictions

# convert weka style predictions to homework style
python ./tools/convert_predictions.py $sub_task_dir/$task-$sub_task.predictions $test_set

echo "Task 2 of 5, representation 3 of 3 finished. Results in $sub_task_dir \n"


###################
# Task 3 of 5: OLD/NEW
###################

echo Task 3 of 5: OLD/NEW
task=OLDNEW
# choose appropriate target feature
target=4
# ignore all but the text
ignore_list=1,2,3,5,6

# make sub-exp directory
task_dir=$exp_dir/$task
mkdir $task_dir

###################
# Representation 1 of 3: bag-of-words
###################

echo "Representation 1 of 3: bag-of-words"
# make representation directory
sub_task=rep--bag-of-words
sub_task_dir=$exp_dir/$task/$sub_task
mkdir $sub_task_dir

# name to save the model under
model=$sub_task_dir/$task-$sub_task.model


# training phase
echo "training the model"

# start time
START=$(date +%s)

# call to weka
java -Xmx$jvm_mem -classpath $weka_jar \
weka.classifiers.meta.FilteredClassifier -i -c $target -t $train_set -T $test_set -d $model \
-F "weka.filters.MultiFilter -F \"weka.filters.unsupervised.attribute.Remove -R $ignore_list\" -F \"weka.filters.unsupervised.attribute.StringToWordVector -R first-last -W 1000 -prune-rate -1.0 -N 0 -stemmer weka.core.stemmers.NullStemmer -M 1 -tokenizer \\\"weka.core.tokenizers.WordTokenizer -delimiters \\\\\\\" \\\\\\\\r\\\\\\\\n\\\\\\\\t.,;:\\\\\\\\\\\\\\\'\\\\\\\\\\\\\\\"()?!\\\\\\\"\\\"\"" \
-W weka.classifiers.functions.SMO -- -C 1.0 -L 0.001 -P 1.0E-12 -N 0 -V -1 -W 1 \
-K "weka.classifiers.functions.supportVector.PolyKernel -C 250007 -E 1.0" \
> $sub_task_dir/$task-$sub_task.stats
# | tee -a $sub_task_dir/$task-$sub_task.stats

# end time
END=$(date +%s)
DIFF=$(( $END - $START ))
echo "training took $DIFF seconds"

# testing phase
echo "testing the model"
java -Xmx$jvm_mem -classpath $weka_jar \
weka.classifiers.meta.FilteredClassifier -c $target -l "$model" \
-T $test_set -p $target -distribution \
> $sub_task_dir/$task-$sub_task.predictions

# convert weka style predictions to homework style
python ./tools/convert_predictions.py $sub_task_dir/$task-$sub_task.predictions $test_set

echo "Task 3 of 5, representation 1 of 3 finished. Results in $sub_task_dir \n"

###################
# Representation 2 of 3: bi-grams
###################

echo "Task 3 of 5 : OLD-NEW"
echo "Representation 2 of 3: bi-grams"
# make representation directory
sub_task=rep--bi-grams
sub_task_dir=$exp_dir/$task/$sub_task
mkdir $sub_task_dir

# name to save the model under
model=$sub_task_dir/$task-$sub_task.model


# training phase
echo "training the model"

# start time
START=$(date +%s)

# call to weka
java -Xmx$jvm_mem -classpath $weka_jar \
weka.classifiers.meta.FilteredClassifier -i -c $target -t $train_set -T $test_set -d $model \
-F "weka.filters.MultiFilter -F \"weka.filters.unsupervised.attribute.Remove -R $ignore_list\" -F \"weka.filters.unsupervised.attribute.StringToWordVector -R first-last -W 1000 -prune-rate -1.0 -N 0 -stemmer weka.core.stemmers.NullStemmer -M 1 -tokenizer \\\"weka.core.tokenizers.NGramTokenizer -delimiters \\\\\\\" \\\\\\\\r\\\\\\\\n\\\\\\\\t.,;:\\\\\\\\\\\\\\\'\\\\\\\\\\\\\\\"()?!\\\\\\\" -max 2 -min 2\\\"\"" \
-W weka.classifiers.functions.SMO -- -C 1.0 -L 0.001 -P 1.0E-12 -N 0 -V -1 -W 1 \
-K "weka.classifiers.functions.supportVector.PolyKernel -C 250007 -E 1.0" \
> $sub_task_dir/$task-$sub_task.stats
# | tee -a $sub_task_dir/$task-$sub_task.stats

# end time
END=$(date +%s)
DIFF=$(( $END - $START ))
echo "training took $DIFF seconds"

# testing phase
echo "testing the model"
java -Xmx$jvm_mem -classpath $weka_jar \
weka.classifiers.meta.FilteredClassifier -c $target -l "$model" \
-T $test_set -p $target -distribution \
> $sub_task_dir/$task-$sub_task.predictions

# convert weka style predictions to homework style
python ./tools/convert_predictions.py $sub_task_dir/$task-$sub_task.predictions $test_set

echo "Task 3 of 5, representation 2 of 3 finished. Results in $sub_task_dir \n"


###################
# Representation 3 of 3: tri-grams
###################

echo "Task 3 of 5 : OLD-NEW"
echo "Representation 3 of 3: tri-grams"
# make representation directory
sub_task=rep--tri-grams
sub_task_dir=$exp_dir/$task/$sub_task
mkdir $sub_task_dir

# name to save the model under
model=$sub_task_dir/$task-$sub_task.model


# training phase
echo "training the model"

# start time
START=$(date +%s)

# call to weka
java -Xmx$jvm_mem -classpath $weka_jar \
weka.classifiers.meta.FilteredClassifier -i -c $target -t $train_set -T $test_set -d $model \
-F "weka.filters.MultiFilter -F \"weka.filters.unsupervised.attribute.Remove -R $ignore_list\" -F \"weka.filters.unsupervised.attribute.StringToWordVector -R first-last -W 1000 -prune-rate -1.0 -N 0 -stemmer weka.core.stemmers.NullStemmer -M 1 -tokenizer \\\"weka.core.tokenizers.NGramTokenizer -delimiters \\\\\\\" \\\\\\\\r\\\\\\\\n\\\\\\\\t.,;:\\\\\\\\\\\\\\\'\\\\\\\\\\\\\\\"()?!\\\\\\\" -max 3 -min 3\\\"\"" \
-W weka.classifiers.functions.SMO -- -C 1.0 -L 0.001 -P 1.0E-12 -N 0 -V -1 -W 1 \
-K "weka.classifiers.functions.supportVector.PolyKernel -C 250007 -E 1.0" \
> $sub_task_dir/$task-$sub_task.stats
# | tee -a $sub_task_dir/$task-$sub_task.stats

# end time
END=$(date +%s)
DIFF=$(( $END - $START ))
echo "training took $DIFF seconds"

# testing phase
echo "testing the model"
java -Xmx$jvm_mem -classpath $weka_jar \
weka.classifiers.meta.FilteredClassifier -c $target -l "$model" \
-T $test_set -p $target -distribution \
> $sub_task_dir/$task-$sub_task.predictions

# convert weka style predictions to homework style
python ./tools/convert_predictions.py $sub_task_dir/$task-$sub_task.predictions $test_set

echo "Task 3 of 5, representation 3 of 3 finished. Results in $sub_task_dir \n"


###################
# Task 4 of 5: SCORE
###################

echo "Task 4 of 5: SCORE"
task=SCORE
# choose appropriate target feature
target=5
# ignore all but the text
ignore_list=1,2,3,4,6

# make sub-exp directory
task_dir=$exp_dir/$task
mkdir $task_dir

###################
# Representation 1 of 3: bag-of-words
###################

echo "Representation 1 of 3: bag-of-words"
# make representation directory
sub_task=rep--bag-of-words
sub_task_dir=$exp_dir/$task/$sub_task
mkdir $sub_task_dir

# name to save the model under
model=$sub_task_dir/$task-$sub_task.model


# training phase
echo "training the model"

# start time
START=$(date +%s)

# call to weka
java -Xmx$jvm_mem -classpath $weka_jar \
weka.classifiers.meta.FilteredClassifier -i -c $target -t $train_set -T $test_set -d $model \
-F "weka.filters.MultiFilter -F \"weka.filters.unsupervised.attribute.Remove -R $ignore_list\" -F \"weka.filters.unsupervised.attribute.StringToWordVector -R first-last -W 1000 -prune-rate -1.0 -N 0 -stemmer weka.core.stemmers.NullStemmer -M 1 -tokenizer \\\"weka.core.tokenizers.WordTokenizer -delimiters \\\\\\\" \\\\\\\\r\\\\\\\\n\\\\\\\\t.,;:\\\\\\\\\\\\\\\'\\\\\\\\\\\\\\\"()?!\\\\\\\"\\\"\"" \
-W weka.classifiers.functions.SMOreg -- -C 1.0 -N 0 \
-I "weka.classifiers.functions.supportVector.RegSMOImproved -L 0.001 -W 1 -P 1.0E-12 -T 0.001 -V" \
-K "weka.classifiers.functions.supportVector.PolyKernel -C 250007 -E 1.0" \
> $sub_task_dir/$task-$sub_task.stats
# | tee -a $sub_task_dir/$task-$sub_task.stats

# end time
END=$(date +%s)
DIFF=$(( $END - $START ))
echo "training took $DIFF seconds"

# testing phase
echo "testing the model"
java -Xmx$jvm_mem -classpath $weka_jar \
weka.classifiers.meta.FilteredClassifier -c $target -l "$model" \
-T $test_set -p $target -distribution \
> $sub_task_dir/$task-$sub_task.predictions

# convert weka style predictions to homework style
python ./tools/convert_predictions.py $sub_task_dir/$task-$sub_task.predictions $test_set

awk '/Correlation coefficient/{i++}i==2' $sub_task_dir/$task-$sub_task.stats
echo "Task 4 of 5, representation 1 of 3 finished. Results in $sub_task_dir \n"


###################
# Representation 2 of 3: bi-grams
###################

echo "Task 4 of 5: SCORE"
echo "Representation 2 of 3: bi-grams"
# make representation directory
sub_task=rep--bi-grams
sub_task_dir=$exp_dir/$task/$sub_task
mkdir $sub_task_dir

# name to save the model under
model=$sub_task_dir/$task-$sub_task.model


# training phase
echo "training the model"

# start time
START=$(date +%s)

# call to weka
java -Xmx$jvm_mem -classpath $weka_jar \
weka.classifiers.meta.FilteredClassifier -i -c $target -t $train_set -T $test_set -d $model \
-F "weka.filters.MultiFilter -F \"weka.filters.unsupervised.attribute.Remove -R $ignore_list\" -F \"weka.filters.unsupervised.attribute.StringToWordVector -R first-last -W 1000 -prune-rate -1.0 -N 0 -stemmer weka.core.stemmers.NullStemmer -M 1 -tokenizer \\\"weka.core.tokenizers.NGramTokenizer -delimiters \\\\\\\" \\\\\\\\r\\\\\\\\n\\\\\\\\t.,;:\\\\\\\\\\\\\\\'\\\\\\\\\\\\\\\"()?!\\\\\\\" -max 2 -min 2\\\"\"" \
-W weka.classifiers.functions.SMOreg -- -C 1.0 -N 0 \
-I "weka.classifiers.functions.supportVector.RegSMOImproved -L 0.001 -W 1 -P 1.0E-12 -T 0.001 -V" \
-K "weka.classifiers.functions.supportVector.PolyKernel -C 250007 -E 1.0" \
> $sub_task_dir/$task-$sub_task.stats
# | tee -a $sub_task_dir/$task-$sub_task.stats

# end time
END=$(date +%s)
DIFF=$(( $END - $START ))
echo "training took $DIFF seconds"

# testing phase
echo "testing the model"
java -Xmx$jvm_mem -classpath $weka_jar \
weka.classifiers.meta.FilteredClassifier -c $target -l "$model" \
-T $test_set -p $target -distribution \
> $sub_task_dir/$task-$sub_task.predictions

# convert weka style predictions to homework style
python ./tools/convert_predictions.py $sub_task_dir/$task-$sub_task.predictions $test_set

awk '/Correlation coefficient/{i++}i==2' $sub_task_dir/$task-$sub_task.stats
echo "Task 4 of 5, representation 2 of 3 finished. Results in $sub_task_dir \n"


###################
# Representation 3 of 3: tri-grams
###################

echo "Task 4 of 5: SCORE"
echo "Representation 3 of 3: tri-grams"
# make representation directory
sub_task=rep--tri-grams
sub_task_dir=$exp_dir/$task/$sub_task
mkdir $sub_task_dir

# name to save the model under
model=$sub_task_dir/$task-$sub_task.model


# training phase
echo "training the model"

# start time
START=$(date +%s)

# call to weka
java -Xmx$jvm_mem -classpath $weka_jar \
weka.classifiers.meta.FilteredClassifier -i -c $target -t $train_set -T $test_set -d $model \
-F "weka.filters.MultiFilter -F \"weka.filters.unsupervised.attribute.Remove -R $ignore_list\" -F \"weka.filters.unsupervised.attribute.StringToWordVector -R first-last -W 1000 -prune-rate -1.0 -N 0 -stemmer weka.core.stemmers.NullStemmer -M 1 -tokenizer \\\"weka.core.tokenizers.NGramTokenizer -delimiters \\\\\\\" \\\\\\\\r\\\\\\\\n\\\\\\\\t.,;:\\\\\\\\\\\\\\\'\\\\\\\\\\\\\\\"()?!\\\\\\\" -max 3 -min 3\\\"\"" \
-W weka.classifiers.functions.SMOreg -- -C 1.0 -N 0 \
-I "weka.classifiers.functions.supportVector.RegSMOImproved -L 0.001 -W 1 -P 1.0E-12 -T 0.001 -V" \
-K "weka.classifiers.functions.supportVector.PolyKernel -C 250007 -E 1.0" \
> $sub_task_dir/$task-$sub_task.stats
# | tee -a $sub_task_dir/$task-$sub_task.stats

# end time
END=$(date +%s)
DIFF=$(( $END - $START ))
echo "training took $DIFF seconds"

# testing phase
echo "testing the model"
java -Xmx$jvm_mem -classpath $weka_jar \
weka.classifiers.meta.FilteredClassifier -c $target -l "$model" \
-T $test_set -p $target -distribution \
> $sub_task_dir/$task-$sub_task.predictions

# convert weka style predictions to homework style
python ./tools/convert_predictions.py $sub_task_dir/$task-$sub_task.predictions $test_set

awk '/Correlation coefficient/{i++}i==2' $sub_task_dir/$task-$sub_task.stats
echo "Task 4 of 5, representation 3 of 3 finished. Results in $sub_task_dir \n"


###################
# Task 5 of 5: NUM-RATINGS
###################

echo "Task 5 of 5: NUM-RATINGS"
task=NUMRATINGS
# choose appropriate target feature
target=6
# ignore all but the text
ignore_list=1,2,3,4,5

# make sub-exp directory
task_dir=$exp_dir/$task
mkdir $task_dir

###################
# Representation 1 of 3: bag-of-words
###################

echo "Representation 1 of 3: bag-of-words"
# make representation directory
sub_task=rep--bag-of-words
sub_task_dir=$exp_dir/$task/$sub_task
mkdir $sub_task_dir

# name to save the model under
model=$sub_task_dir/$task-$sub_task.model


# training phase
echo "training the model"

# start time
START=$(date +%s)

# call to weka
java -Xmx$jvm_mem -classpath $weka_jar \
weka.classifiers.meta.FilteredClassifier -i -c $target -t $train_set -T $test_set -d $model \
-F "weka.filters.MultiFilter -F \"weka.filters.unsupervised.attribute.Remove -R $ignore_list\" -F \"weka.filters.unsupervised.attribute.StringToWordVector -R first-last -W 1000 -prune-rate -1.0 -N 0 -stemmer weka.core.stemmers.NullStemmer -M 1 -tokenizer \\\"weka.core.tokenizers.WordTokenizer -delimiters \\\\\\\" \\\\\\\\r\\\\\\\\n\\\\\\\\t.,;:\\\\\\\\\\\\\\\'\\\\\\\\\\\\\\\"()?!\\\\\\\"\\\"\"" \
-W weka.classifiers.functions.SMOreg -- -C 1.0 -N 0 \
-I "weka.classifiers.functions.supportVector.RegSMOImproved -L 0.001 -W 1 -P 1.0E-12 -T 0.001 -V" \
-K "weka.classifiers.functions.supportVector.PolyKernel -C 250007 -E 1.0" \
> $sub_task_dir/$task-$sub_task.stats
# | tee -a $sub_task_dir/$task-$sub_task.stats

# end time
END=$(date +%s)
DIFF=$(( $END - $START ))
echo "training took $DIFF seconds"

# testing phase
echo "testing the model"
java -Xmx$jvm_mem -classpath $weka_jar \
weka.classifiers.meta.FilteredClassifier -c $target -l "$model" \
-T $test_set -p $target -distribution \
> $sub_task_dir/$task-$sub_task.predictions

# convert weka style predictions to homework style
python ./tools/convert_predictions.py $sub_task_dir/$task-$sub_task.predictions $test_set

awk '/Correlation coefficient/{i++}i==2' $sub_task_dir/$task-$sub_task.stats
echo "Task 5 of 5, representation 1 of 3 finished. Results in $sub_task_dir \n"


###################
# Representation 2 of 3: bi-grams
###################

echo "Task 5 of 5: NUM-RATINGS"
echo "Representation 2 of 3: bi-grams"
# make representation directory
sub_task=rep--bi-grams
sub_task_dir=$exp_dir/$task/$sub_task
mkdir $sub_task_dir

# name to save the model under
model=$sub_task_dir/$task-$sub_task.model


# training phase
echo "training the model"

# start time
START=$(date +%s)

# call to weka
java -Xmx$jvm_mem -classpath $weka_jar \
weka.classifiers.meta.FilteredClassifier -i -c $target -t $train_set -T $test_set -d $model \
-F "weka.filters.MultiFilter -F \"weka.filters.unsupervised.attribute.Remove -R $ignore_list\" -F \"weka.filters.unsupervised.attribute.StringToWordVector -R first-last -W 1000 -prune-rate -1.0 -N 0 -stemmer weka.core.stemmers.NullStemmer -M 1 -tokenizer \\\"weka.core.tokenizers.NGramTokenizer -delimiters \\\\\\\" \\\\\\\\r\\\\\\\\n\\\\\\\\t.,;:\\\\\\\\\\\\\\\'\\\\\\\\\\\\\\\"()?!\\\\\\\" -max 2 -min 2\\\"\"" \
-W weka.classifiers.functions.SMOreg -- -C 1.0 -N 0 \
-I "weka.classifiers.functions.supportVector.RegSMOImproved -L 0.001 -W 1 -P 1.0E-12 -T 0.001 -V" \
-K "weka.classifiers.functions.supportVector.PolyKernel -C 250007 -E 1.0" \
> $sub_task_dir/$task-$sub_task.stats
# | tee -a $sub_task_dir/$task-$sub_task.stats

# end time
END=$(date +%s)
DIFF=$(( $END - $START ))
echo "training took $DIFF seconds"

# testing phase
echo "testing the model"
java -Xmx$jvm_mem -classpath $weka_jar \
weka.classifiers.meta.FilteredClassifier -c $target -l "$model" \
-T $test_set -p $target -distribution \
> $sub_task_dir/$task-$sub_task.predictions

# convert weka style predictions to homework style
python ./tools/convert_predictions.py $sub_task_dir/$task-$sub_task.predictions $test_set

awk '/Correlation coefficient/{i++}i==2' $sub_task_dir/$task-$sub_task.stats
echo "Task 5 of 5, representation 2 of 3 finished. Results in $sub_task_dir \n"


###################
# Representation 3 of 3: tri-grams
###################

echo "Task 5 of 5: NUM-RATINGS"
echo "Representation 3 of 3: tri-grams"
# make representation directory
sub_task=rep--tri-grams
sub_task_dir=$exp_dir/$task/$sub_task
mkdir $sub_task_dir

# name to save the model under
model=$sub_task_dir/$task-$sub_task.model


# training phase
echo "training the model"

# start time
START=$(date +%s)

# call to weka
java -Xmx$jvm_mem -classpath $weka_jar \
weka.classifiers.meta.FilteredClassifier -i -c $target -t $train_set -T $test_set -d $model \
-F "weka.filters.MultiFilter -F \"weka.filters.unsupervised.attribute.Remove -R $ignore_list\" -F \"weka.filters.unsupervised.attribute.StringToWordVector -R first-last -W 1000 -prune-rate -1.0 -N 0 -stemmer weka.core.stemmers.NullStemmer -M 1 -tokenizer \\\"weka.core.tokenizers.NGramTokenizer -delimiters \\\\\\\" \\\\\\\\r\\\\\\\\n\\\\\\\\t.,;:\\\\\\\\\\\\\\\'\\\\\\\\\\\\\\\"()?!\\\\\\\" -max 3 -min 3\\\"\"" \
-W weka.classifiers.functions.SMOreg -- -C 1.0 -N 0 \
-I "weka.classifiers.functions.supportVector.RegSMOImproved -L 0.001 -W 1 -P 1.0E-12 -T 0.001 -V" \
-K "weka.classifiers.functions.supportVector.PolyKernel -C 250007 -E 1.0" \
> $sub_task_dir/$task-$sub_task.stats
# | tee -a $sub_task_dir/$task-$sub_task.stats

# end time
END=$(date +%s)
DIFF=$(( $END - $START ))
echo "training took $DIFF seconds"

# testing phase
echo "testing the model"
java -Xmx$jvm_mem -classpath $weka_jar \
weka.classifiers.meta.FilteredClassifier -c $target -l "$model" \
-T $test_set -p $target -distribution \
> $sub_task_dir/$task-$sub_task.predictions

# convert weka style predictions to homework style
python ./tools/convert_predictions.py $sub_task_dir/$task-$sub_task.predictions $test_set

awk '/Correlation coefficient/{i++}i==2' $sub_task_dir/$task-$sub_task.stats
echo "Task 5 of 5, representation 3 of 3 finished. Results in $sub_task_dir \n"


