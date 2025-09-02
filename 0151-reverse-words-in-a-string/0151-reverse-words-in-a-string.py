class Solution:
    def reverseWords(self, s: str) -> str:
        
        
        
        n = len(s)
        result = []
        i = 0
        l = 0

        while l < n:
            if s[l] != ' ':
                # add space before new word if not the first word in result
                if i != 0:
                    result.append(' ')
                    i += 1

                # find the end of the word
                r = l
                while r < n and s[r] != ' ':
                    result.append(s[r])
                    i += 1
                    r += 1

                # reverse the current word inside result
                result[i - (r - l):i] = reversed(result[i - (r - l):i])

                # move to next word
                l = r
            l += 1

        # reverse the entire result list to reverse word order
        result = result[::-1]

        # remove extra spaces between reversed words
        return ''.join(result)

                    



                
                