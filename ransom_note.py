
# The words in his note are case-sensitive and he must use only whole words
# available in the magazine.
# He cannot use substrings or concatenation to create the words he needs.

#Hash Tables: Ransom Note
def check_magazine(magazine, note):
    """
      Time: O(m + n)
      Space: O(n)
    """
    hash_magazine = {}
    for m_word in magazine:
        hash_magazine[m_word] = hash_magazine.get(m_word, 0) + 1
    
    for n_word in note:
        if hash_magazine.get(n_word) == None or hash_magazine.get(n_word) == 0:
            return "No"
        else:
            hash_magazine[n_word] -= 1
        
    return "Yes"

#has_mag = {two: 1, times: 1, three: 1, is: 1, not: 1, four: 1} 
assert check_magazine('two times three is not four'.split(), 'two times two is four'.split()) == "No"
assert check_magazine('ive got a lovely bunch of coconuts'.split(), 'ive got some coconuts'.split()) == "No"




def check_magazine_2(magazine, note):
    hash_note = {}
    for word in note:
        hash_note[word] = False
    
    for word in magazine:
        if  hash_note.get(word) == None:
            hash_note[word] = True

        if (all(hash_note.values())):
            return "Yes"
    
    return "No"


