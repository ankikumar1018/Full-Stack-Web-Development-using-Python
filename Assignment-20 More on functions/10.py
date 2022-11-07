from collections import Counter

def anagram(s1, s2):

	if(Counter(s1) == Counter(s2)):
		print("The strings are anagrams.")
	else:
		print("The strings aren't anagrams.")


s1 = "listen"
s2 = "silent"
anagram(s1, s2)
