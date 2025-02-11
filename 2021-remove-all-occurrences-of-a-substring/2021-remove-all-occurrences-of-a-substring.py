class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        
        part = list(part)
        part_length = len(part)
        check_char  = part[-1]
        s = list(s)
        i = 0
        while True:
            if i == len(s):
                break
            if s[i] == check_char:
                if i >= part_length-1:
                    # print(s[i-part_length+1:i+1] )
                    if s[i-part_length+1:i+1] == part:
                        # print(s[:i])
                        # print(s[i:])
                        # print(s[:i-part_length] )

                        s = s[:i-part_length+1] + s[i+1:]
                        # print(s)
                        i -= part_length
                        # print(i)

            i += 1

        return "".join(s)

            
