


### PROJECT OVERVIEW
Stack Exchange question/answer improvements



    * Task 1: Features - Rank/Score correlation
Before anything useful can be done, we need to know what features can be useful for our tasks.

Subtask: build data
build_site_list.py (done)
    tiny script that finds all the Stack Exchange sub-websites
scrape_SE.py
    script that explores and saves the raw html of question links. Adds (not replaces) to the current dataset.
    input: latest list of links
feat_extract.py
    script that build the .arff from the above raw data
    input: folder containing the raw html

Features to extract
    Possible targets:
        vote-count-post (aka score) (for both)
        normalized score (to define) (for both)

        favoritecount (questions only)
        number of answers (questions only)

        Rank (answers only)
        vote-accepted-on (if the question owner accepted this answer) (answers only)

    Possible features:
        text

    * Data exploration: Normalized score
        How does the score (vote-count-post) depend on how old the question/answers is?
        re-score by average? median? threshold?
