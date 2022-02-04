class Solution:
    def reverseWords(self, s: str) -> str:
        split_array = s.split(" ")
        for i in range(len(split_array)):
            split_array[i] = split_array[i][::-1]
        split_array = " ".join(split_array)
        return split_array