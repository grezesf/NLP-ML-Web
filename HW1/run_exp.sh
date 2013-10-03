#!/bin/sh

# path to Weka's jar file
weka_jar=/home/apps/weka-3-7-1/weka.jar
test -f $weka_jar || exit -1

# memory to allocate for the JVM
jvm_mem=4096m
# jvm_mem=10240m