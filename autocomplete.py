import math
import matplotlib.pyplot as plt

class Autocomplete:
    def __init__(self, filename):
        """
        Load in a set of terms with their counts from a file, and
        setup a list of these terms in alphabetical order

        Paramters
        ---------
        filename: string
            Path to file containing terms.  Each line should have
            a count, followed by a tab, followed by a term
        """
        fin = open(filename)
        self._terms = []
        for line in fin.readlines():
            line = line.lstrip().rstrip()
            fields = line.split("\t")
            term = fields[0]
            count = int(fields[1])
            self._terms.append((term, count))
        fin.close()
        self._terms = sorted(self._terms, key=lambda term: term[0])
    
    def _first_index_of(self, prefix):
        """
        Find the index of the first term in the alphabetical 
        list of _terms that starts with prefix

        Parameters
        ----------
        prefix: string
            A prefix to search 
        
        Returns
        -------
        index: int
            The index of the first occurrence of a word with
            prefix in the dictionary, or None if no such word exists
        """
        idx = None
        ## TODO: Fill this in
        return idx

    def _last_index_of(self, prefix):
        """
        Find the index of the last term in the alphabetical 
        list of _terms that starts with prefix

        Parameters
        ----------
        prefix: string
            A prefix to search 
        
        Returns
        -------
        index: int
            The index of the last occurrence of a word with
            prefix in the dictionary, or None if no such word exists
        """
        idx = None
        ## TODO: Fill this in
        return idx

    def all_matches(self, prefix):
        """
        Find all words that start with a particular prefix,
        and sort them in decreasing order of their counts

        Parameters
        ----------
        prefix: string
            A prefix to search 
        
        Returns
        -------
        list of (string, int)
            A list of words with this prefix, sorted in descending
            order of counts.  If no words exist with the given prefix,
            then return an empty list
        """
        ret = []
        ## TODO: Fill this in
        return ret

a = Autocomplete("words.txt")
for m in a.all_matches("urs"):
    print(m)