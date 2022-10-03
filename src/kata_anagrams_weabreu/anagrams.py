
def search_anagrams(words_list: list[str]) -> tuple[list[str], int]:

    if not isinstance(words_list, list):
       raise TypeError("Should be a list of strings") 

    words_dict: dict[str, str] = {}
    words_count: int = 0

    for word in words_list:
        words_letters: str = "".join(sorted(word))

        if words_dict.__contains__( words_letters ):
            words_dict[words_letters] += f" {word}"

            if words_dict[words_letters].count(" ") == 1: words_count += 2
            else: words_count += 1
        else:
            words_dict[words_letters] = word
    
    anagrams_set = [val for val in words_dict.values() if val.__contains__(" ")]

    return (anagrams_set, words_count)

def search_anagrams_advanced(words_list: list[str]) -> tuple[list[str], int, str, str]:
    longest_word = ""
    most_words = ""

    if not isinstance(words_list, list):
       raise TypeError("Should be a list of strings") 

    words_dict: dict[str, dict] = {}
    longest_word_key: str = ""

    for word in words_list:
        word_letters = "".join(sorted(word))

        if words_dict.__contains__(word_letters):
            words_dict[word_letters]["set"] += f" {word}"
            words_dict[word_letters]["count"] += 1

            if len(word_letters) > len(longest_word_key):
                longest_word_key = word_letters
        else:
            words_dict[word_letters] = { "set": word, "count": 1 }

    anagrams = [val for val in words_dict.values() if val["count"] > 1]

    anagrams_list = [val["set"] for val in anagrams]
    words_count = sum([val["count"] for val in anagrams])
    
    if len(anagrams) > 1:
        longest_word = words_dict[longest_word_key]["set"]
        most_words = max(anagrams, key=lambda dct: dct["count"])["set"]

    return (anagrams_list, words_count, longest_word, most_words)

class AnagramsAnalyzer:
    def __init__(self):
        self.words_dict: dict[str, dict] = {}
        self.longest_word_key: str = ""

    def load_word(self, word: str) -> None:
        word_letters = "".join(sorted(word))

        if self.words_dict.__contains__( word_letters ):
            self.words_dict[word_letters]["set"] += f" {word}"
            self.words_dict[word_letters]["count"] += 1

            if len(word_letters) > len( self.longest_word_key ):
                self.longest_word_key = word_letters
        else:
            self.words_dict[word_letters] = { "set": word, "count": 1 }

    def get_anagrams(self) -> list[str]:
        return [val["set"] for val in self.words_dict.values() if val["count"] > 1]

    def get_anagrams_words_count(self) -> int:
        return sum([val["count"] for val in self.words_dict.values() if val["count"] > 1])

    def get_longest_word_set(self) -> str:
        if self.longest_word_key == "":
            return ""

        return self.words_dict[self.longest_word_key]["set"]

    def get_most_words_set(self) -> str:
        if len( self.words_dict ) == 0:
            return ""

        return max(self.words_dict.values(), key=lambda dct: dct["count"])["set"]

    def get_set_count(self) -> int:
        return len( self.get_anagrams() )
