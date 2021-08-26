class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        
        slots = 1
        """ 
        # O(n) space
        for node in preorder.split(','):
            
            slots -= 1
            if slots < 0:
                return False
            if node == "#":
                continue
            slots += 2 # for number nodes
        """
        # O(1) space
        prev = None
        for el in preorder:
            if el == ",":
                slots -= 1
                if slots < 0:
                    return False
                if prev == "#":
                    continue
                slots += 2
            prev = el
            
        slots = slots + 1 if prev != '#' else slots - 1 
        return slots == 0
        