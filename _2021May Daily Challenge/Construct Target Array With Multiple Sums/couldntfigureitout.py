class Solution:
    def isPossible(self, target: List[int]) -> bool:
        self.is_ok = False
        A = [1] * len(target)
        if sum(A) > min(target):
            return self.is_ok
        check = [True] * len(target) # always have to put the item in the right slot
        self.rec(A, target, check)
        return self.is_ok

    def rec(self, A, target, check):

        #print('called:', A, check)
        s = sum(A)
        if s > max(target):
            #print(s, max(target), 'returned false')
            return
        
        if s in target:
            A[target.index(s)] = s
            check[target.index(s)] = False
            if A == target:
                #print('ok')
                self.is_ok = True
                return
            self.rec(A, target, check)
            
        else:
            for i in range(len(A)):
                if check[i]: # meaning I havent changed this element of A yet. If I have I must leave it as is
                    print(i, A, check)
                    t = check
                    temp = A
                    temp[i] = s
                    self.rec(temp, target, t)