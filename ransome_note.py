class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_note_char_set = set(ransomNote)
        for character in ransom_note_char_set:
            if ransomNote.count(character) > magazine.count(character):
                return False
        return True