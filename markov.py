# -*- encoding: utf-8 -*-
"""Markov-Tools zur Erzeugung von Text, der die korrekte n-Gramm-Zusammensetzung
aufweist.
"""


import random
r = random.Random()

# Demo-Daten
from fvornamen import fvor
from mvornamen import mvor
from nachnamen import nachnamen

START_MARKER = '⁚'   # das hier ist KEIN Doppelpunkt!
END_MARKER = '⁝'     # sondern Unicode!


def ngrams(s, n):
    """Generator that produces n-grams from s.
    
    >>> list(ngrams('hello', 2))
    ['he', 'el', 'll', 'lo']
    >>> list(ngrams('hello', 10))
    ['hello']
    """
    
    if len(s) < n:
        n = len(s)
        
    for i in range(len(s) - n + 1):
        yield s[i:i+n]
    
    
def counter(ngramlist):
    """Count the occurances of ngrams.
    
    Returns a dictionary of the counts.
    
    # unfortunately, the tests don't work well with dictionaries.
    >>> counter(['a', 'a', 'b'])['a']
    2
    >>> counter(['a', 'a', 'b'])['b']
    1
    """
    
    res = {}
    
    for ngram in ngramlist:
        ct = res.get(ngram, 0)
        res[ngram] = ct + 1
        
    return res


def combiner(strings, n=3):
    """Combine a list of strings into a counted ngram dict.
    
    Adds START_ and END_ markers.
    
    # dicts again!
    >>> len(combiner(['a', 'a', 'b']))
    2
    >>> combiner(['a', 'a', 'b'])['⁚a⁝']  # START_ and END_!
    2
    >>> combiner(['a', 'a', 'b'])['⁚b⁝']
    1
    """
    
    def combined(slist):
        
        for s in slist:
            for ngram in ngrams(START_MARKER + s + END_MARKER, n):
                yield ngram
                
    return counter(combined(strings))
    
    
def weighted_combiner(weighted_strings, n=3):
    """Combine a list of strings with weights into a counted ngram dict."""
    
    # TODO
    
    raise NotImplemented("that's an exercise for you!")
    
    
    
    
def c_matrix(counted):
    """Generate a count matrix for a dict of counted ngrams.

    If the doctests fail, check the dict's for yourself!
    
    >>> c_matrix(combiner(['aaa', 'aaa', 'aab'])) == {'⁚': {'aa': 3}, 'aa': {'aa': 2, 'ab': 1, '⁝': 2}, 'ab': {'⁝': 1}}
    True
    """
    
    mat = {}
    
    for key, val in counted.items():
        
        if key[0] == START_MARKER:
            from_state = START_MARKER
        else:
            from_state = key[:-1]
            
        if key[-1] == END_MARKER:
            to_state = END_MARKER
        else:
            to_state = key[1:]
            
        column = mat.setdefault(from_state, {})[to_state] = val

    return mat

def p_matrix(c_mat):
    """Generate a p-matrix for a c-matrix
    
    I.e. turn a count into a probability, by dividing the individual count
    values by the total count for each state.
    
    >>> p_matrix(c_matrix(combiner(['aaa', 'aaa', 'aab']))) == {'⁚': {'aa': 1.0}, 'aa': {'aa': 0.4, 'ab': 0.2, '⁝': 0.4}, 'ab': {'⁝': 1.0}}
    True
    
    """
    
    p_mat = {}
    
    for from_state in c_mat:
        
        column = {}
        total = sum(c_mat[from_state].values())
        for key, val in c_mat[from_state].items():
            column[key] = val / total
        
        p_mat[from_state] = column
        
    return p_mat
        
def flat_p_matrix(p_mat):
    """Flatten a p-matrix so we can use it for simulation.
    
    This means that instead of denoting actual p values of probabilities, the
    matrix contains the interval boundaries necessary for simulation.
    """
    # Examples are too hard. Check it for yourself!

    fp_mat = {}

    for from_state, column in p_mat.items():
        
        newcol = []
        current_p = 0.0
        for to_state, p in column.items():
            current_p += p
            newcol.append( (to_state, current_p) )
            
        fp_mat[from_state] = newcol
        
    return fp_mat

def markov_matrix(string_l, n=3):
    """Create a markov matrix from a given list of strings.
    """

    return flat_p_matrix(p_matrix(c_matrix(combiner(string_l, n))))


def simulate(fp_mat):
    """Run a simulation on the given flat p-matrix."""
    
    # no examples because of random numbers!
    
    def select(column):
        p = r.random()
        for to_state, pval in column:
            if pval > p:
                return to_state
        # no break necessary because p < 1.0 and pval[-1] == 1.0
    
    
    res = select(fp_mat[START_MARKER])
    from_state = res
    
    while True:
        to_state = select(fp_mat[from_state])
        if to_state[-1] == END_MARKER:
            return res
            
        from_state = to_state
        res += to_state[-1]

# tests!
if __name__ == "__main__":
    import doctest
    doctest.testmod()

# if you want to play with it, remove the X, and probably some comments
if __name__ == '__main__X':
    #from pprint import pprint as print
    
    
    fp_mat = flat_p_matrix(p_matrix(c_matrix(combiner([s[0] for s in fvor], 3))))
    #print(fp_mat)
    
    for i in range(100):
        print(simulate(fp_mat), end=" ", flush=True)
    print()