class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        count = Counter(moves)
        selected = max(count['L'], count['R'])
        not_selected = min(count['L'], count['R'])
        
        return (selected + count['_'] - not_selected)
