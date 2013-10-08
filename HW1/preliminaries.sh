#!/bin/sh

# this script run all the necessary preliminaries for you

python ./tools/download_webpages.py ./data/train/train-links.txt
python ./tools/download_webpages.py ./data/test/test-links.txt
python ./tools/generate_labels.py ./data/train
python ./tools/generate_labels.py ./data/test
python ./feat_extract.py ./data/train
python ./feat_extract.py ./data/test