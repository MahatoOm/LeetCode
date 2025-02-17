class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        
        possible_sequence = set()
        seen = [False] * len(tiles)

        self.generate_sequence(tiles, "", seen, possible_sequence)


        return len(possible_sequence) - 1


    def generate_sequence(self, tiles, current_element, seen, possible_sequence ):

        possible_sequence.add(current_element)

        for pos, char in enumerate(tiles):
            if not seen[pos]:
                seen[pos] = True
                self.generate_sequence(tiles, current_element + char, seen , possible_sequence)
                seen[pos] = False