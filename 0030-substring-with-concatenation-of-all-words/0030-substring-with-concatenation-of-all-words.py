from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        n_words = len(words)
        total_len = word_len * n_words
        if len(s) < total_len:
            return []

        need = Counter(words)
        result = []


        for off in range(word_len):
            left = off
            count = 0
            window = Counter()

            for right in range(off, len(s) - word_len + 1, word_len):
                word = s[right:right + word_len]

                if word in need:
                    window[word] += 1
                    count += 1


                    while window[word] > need[word]:
                        left_word = s[left:left + word_len]
                        window[left_word] -= 1
                        count -= 1
                        left += word_len

  
                    if count == n_words:
                        result.append(left)

                        left_word = s[left:left + word_len]
                        window[left_word] -= 1
                        count -= 1
                        left += word_len
                else:

                    window.clear()
                    count = 0
                    left = right + word_len

        return result