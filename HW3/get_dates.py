import dateutil.parser
from itertools import chain
import re

# Add more strings that confuse the parser in the list
UNINTERESTING = set(chain(dateutil.parser.parserinfo.JUMP, 
                          dateutil.parser.parserinfo.PERTAIN,
                          ['a']))

def _get_date(tokens):
    for end in xrange(len(tokens), 0, -1):
        region = tokens[:end]
        if all(token.isspace() or token in UNINTERESTING
               for token in region):
            continue
        text = ''.join(region)
        try:
            date = dateutil.parser.parse(text)
            return end, date
        except ValueError:
            pass

def find_dates(text, max_tokens=50, allow_overlapping=False):
    tokens = filter(None, re.split(r'(\S+|\W+)', text))
    skip_dates_ending_before = 0
    for start in xrange(len(tokens)):
        region = tokens[start:start + max_tokens]
        result = _get_date(region)
        if result is not None:
            end, date = result
            if allow_overlapping or end > skip_dates_ending_before:
                skip_dates_ending_before = end
                yield date


# test = """Adelaide was born in Finchley, North London on 12 May 1999. She was a 
# child during the Daleks' abduction and invasion of Earth in 2009. 
# On 1st July 2058, Bowie Base One became the first Human colony on Mars. It 
# was commanded by Captain Adelaide Brooke, and initially seemed to prove that 
# it was possible for Humans to live long term on Mars."""

# print "With no overlapping:"
# for date in find_dates(test, allow_overlapping=False):
#     print date


# print "With overlapping:"
# for date in find_dates(test, allow_overlapping=True):
#     print date