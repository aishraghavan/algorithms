"""
Resources:
http://www.geeksforgeeks.org/searching-for-patterns-set-2-kmp-algorithm/
https://www.youtube.com/watch?v=2ogqPWJSftE
"""
from compute_prefix_array import compute_prefix_array_for_kmp

def search_pattern_in_text_kpm(pat, txt):
    if pat == None or txt == None:
        return None
    if len(pat) > len(txt):
        return None
    lps_prefix_array = compute_prefix_array_for_kmp(pat)

    pat_len = len(pat)
    txt_len = len(txt)
    txt_i = 0
    pat_j = 0
    while txt_i < txt_len:
        # increment pat and txt when the pattern is found.
        if (pat[pat_j] == txt[txt_i]):
            pat_j += 1
            txt_i += 1
        # when the pattern index is equal to the length of pattern
        # meaning reached end of pattern
        if pat_j == pat_len:
            print "Found at location: ", txt_i-pat_j
            # reset pattern
            pat_j = lps_prefix_array[pat_j-1]
        # if the pattern is not in text, then
        elif (txt_i < txt_len and pat[pat_j] != txt[txt_i]):
            if pat_j != 0:
                #reset pattern
                pat_j = lps_prefix_array[pat_j-1]
            else:
                txt_i += 1

if __name__ == "__main__":
    print "search_pattern_in_text_kpm({0}, {1})".format("hello", "hello there hello party")
    search_pattern_in_text_kpm("hello", "hello there hello party")
    print "search_pattern_in_text_kpm({0}, {1})".format("llo", "hello there hello party")
    search_pattern_in_text_kpm("llo", "hello there hello party")
    print "search_pattern_in_text_kpm({0}, {1})".format("AABA", "AABAACAADAABAAABAA")
    search_pattern_in_text_kpm("AABA", "AABAACAADAABAAABAA")
    print "best case: search_pattern_in_text_kpm({0}, {1}) not found".format("FAA","AABCCAADDEE")
    search_pattern_in_text_kpm("FAA","AABCCAADDEE")
    print "worst case: search_pattern_in_text_kpm({0}, {1})".format("AAAAA", "AAAAAAAAAAAAAAAAAA")
    search_pattern_in_text_kpm("AAAAA", "AAAAAAAAAAAAAAAAAA")
    print "worst case: search_pattern_in_text_kpm({0}, {1})".format("AAAAB", "AAAAAAAAAAAAAAAAAB")
    search_pattern_in_text_kpm("AAAAB", "AAAAAAAAAAAAAAAAAB")
