

def sherlock_anagrams(word):
    """
      Time: O(n^2 * nlogn) + O(n)
      Space: O(n^2)
    """
    size = len(word)
    occ = {}

    # calculate all substrings and yours occurencies
    for i in range(size):
        sub_string = ''
        for j in range(i, n):
            sub_string = ''.join(sorted(sub_string + word[j]))
            occ[sb] = occ.get(sub_string, 0)

            occ[sub_string] += 1

    anagrams = 0

    # loop over all different dictionary
    # items and aggregate substring count
    for k, v in occ.items():
        anagrams += (v*(v-1))//2
    return anas


def test_sherlock_anagrams():
    string = "abb"
    assert sherlock_anagrams(string) == 1
