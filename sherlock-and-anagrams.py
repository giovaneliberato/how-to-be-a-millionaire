

sort = lambda s: "".join(sorted(s))

def permutations(n):
    aggr = 0
    for i in range(1, n + 1):
        aggr += n - i
    return aggr
        

def sherlock_and_anagrams(query):
    occurences = {}
    for i in range(len(query)):
        for j in range(i, len(query) + 1):
            if i != j:
                s = sort(query[i:j])
                occurences[s] = occurences.get(s, 0) + 1
    
    anagrams = 0
    for v in occurences.values():
        anagrams += permutations(v)
        
    return anagrams
