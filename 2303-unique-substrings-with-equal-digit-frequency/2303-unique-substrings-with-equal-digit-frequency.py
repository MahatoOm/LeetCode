class Solution:
    def equalDigitFrequency(self, s: str) -> int:
        n = len(s)
        # Set to store unique substrings with equal digit frequency
        valid_substrings = set()

        # Iterate over each possible starting position of a substring
        for start in range(n):
            digit_frequency = [0] * 10  # Frequency array for digits 0-9

            # Extend the substring from 'start' to different end positions
            for end in range(start, n):
                digit_frequency[ord(s[end]) - ord("0")] += 1

                # Variable to store the frequency all digits must match
                common_frequency = 0
                is_valid = True

                for count in digit_frequency:
                    if count == 0:
                        continue  # Skip digits not in the substring
                    if common_frequency == 0:
                        # First digit found, set common_frequency
                        common_frequency = count
                    if common_frequency != count:
                        # Mismatch in frequency, mark as invalid
                        is_valid = False
                        break

                # If the substring is valid, add it to the set
                if is_valid:
                    substring = s[start : end + 1]
                    valid_substrings.add(substring)

        # Return the number of unique valid substrings
        return len(valid_substrings)