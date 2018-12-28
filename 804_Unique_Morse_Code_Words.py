#International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows: "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.
#
#For convenience, the full table for the 26 letters of the English alphabet is given below:
#
#[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
#Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter. For example, "cba" can be written as "-.-..--...", (which is the concatenation "-.-." + "-..." + ".-"). We'll call such a concatenation, the transformation of a word.
#
#Return the number of different transformations among all words we have.

#Mine
class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        Morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        newWords = []
        for word in words:
            i = 0
            while 1:
                idx = ord(word[i]) - ord('a')
                word = word.replace(word[i],Morse[idx],1)
                i = i + len(Morse[idx])
                if i >= len(word):
                    newWords.append(word)
                    break
        return len(set(newWords))

#Better
 def uniqueMorseRepresentations(self, words):
        Morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
             "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        return len({''.join(Morse[ord(i) - ord('a')] for i in w) for w in words})
