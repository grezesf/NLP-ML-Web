import re, collections, os, sys, nltk

### README ###
# This script classifies edits into meaning-preserving and meaning-altering
# Input- text file (pair_edits.txt) 
# Ouptut- text file of labeled edits


### SPELL CHECKER ### Code borrowed from-- http://norvig.com/spell-correct.html
def words(text): return re.findall('[a-z]+', text.lower()) 

def train(features):
    model = collections.defaultdict(lambda: 1)
    for f in features:
        model[f] += 1
    return model

NWORDS = train(words(file('dictionary.txt').read()))

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def edits1(word):
   splits     = [(word[:i], word[i:]) for i in range(len(word) + 1)]
   deletes    = [a + b[1:] for a, b in splits if b]
   transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
   replaces   = [a + c + b[1:] for a, b in splits for c in alphabet if b]
   inserts    = [a + c + b     for a, b in splits for c in alphabet]
   return set(deletes + transposes + replaces + inserts)

def known_edits2(word):
    return set(e2 for e1 in edits1(word) for e2 in edits1(e1) if e2 in NWORDS)

def known(words): return set(w for w in words if w in NWORDS)

def correct(word):
    candidates = known([word]) or known(edits1(word)) or known_edits2(word) or [word]
    return max(candidates, key=NWORDS.get)




### CLASSIFY SPELLING CORRECTIONS ###
# Spelling correction count and capitalization correction count
counter = 0
capital_correction = 0
# Opens text file containing edits and reads them
edit_pairs = open('../data/pair_edits.txt', 'r').readlines()

for line in edit_pairs:

  index = edit_pairs.index(line)

  # If deletion in line, then take the deletion and following addition as an edit pair
  if 'DELETION' in line:
    deletion = line.split(':')[-1].strip()
    addition = edit_pairs[index+1].split(':')[-1].strip()
    # print 'DELETION '+ deletion + ' ADDITION ' + addition

    # for spelling edits only consider revisions that consist of one word, we do not consider revisions that are sentences
    if len(deletion.split()) == 1 and len(addition.split()) ==1:

      #ignores capitalization, lower cases everyword
      word = deletion.split()[0].lower()
      changed_word = addition.split()[0].lower()

      #checks deletion word for corrections, uses the spell checker above to formulate a list of possible corrections
      #if the addition word is in the correction list formulated by the spell checker, it is classified as a spelling correction
      edits_list = known_edits2(word)
      if changed_word in edits_list:
        # print ' SPELLING CORRECTION: ' + word + ' ... ' + changed_word 
        counter +=1
        if word == changed_word:
          # if the addition and the deletion are the same we know that a capitalization correction was made
          capital_correction += 1
          edit_distance = nltk.metrics.distance.edit_distance(deletion,addition)
          print '"%s","%s",%d' %(word,changed_word, edit_distance)
    else:
      # print 'Deletion= ' + deletion + '\n' + 'Addition= ' + addition
      # for any revisions that are more than 1 word, we calculate edit distance between the two strings 
      edit_distance = nltk.metrics.distance.edit_distance(deletion, addition)
      # print 'Edit distance between pre and post string = ' , edit_distance , '\n' 
      print '"%s","%s",%d' %(deletion, addition, edit_distance)

      

print 'Total spelling corrections:',counter
print 'Subtotal capitalization corrections:', capital_correction


    



