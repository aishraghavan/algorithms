def compute_prefix_array_for_kmp(pattern):
	lps = [0]*len(pattern)
	s_len = 0  # length of the previous longest prefix suffix
	i = 1

	# the loop calculates lps[i] for i = 1 to M-1
	while i < len(pattern):
		if pattern[i] == pattern[s_len]:
			s_len = s_len + 1
			lps[i] = s_len
			i += 1
		else:
			# This is tricky. Consier the example AAACAAAA
			# and i = 7
			if s_len != 0:
				s_len = lps[s_len -1]
				# not increment i
				# Also, note that we do not increment i here
			else:
				lps[i] = s_len
				i += 1
	return lps

if __name__ == "__main__":
	print compute_prefix_array_for_kmp("ababac")
	print compute_prefix_array_for_kmp("ABABCABAB")
	print compute_prefix_array_for_kmp("ABCDE")
	print compute_prefix_array_for_kmp("AAAAA")
	print compute_prefix_array_for_kmp("AAABAAA")
	print compute_prefix_array_for_kmp("AABAACAABAA")
