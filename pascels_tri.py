import copy
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        self.base = [1]
        tri_list = self.base
        temp_list = []
        self.rows = numRows
        self.final = [self.base]
        for i in range(self.rows - 1):
            temp_list = self.add_zeros(tri_list)
            tri_list = []
            while temp_list != [0]:
                ind1 = temp_list[0]
                ind2 = temp_list[1]
                sum = ind1 + ind2
                tri_list.append(sum)
                temp_list.pop(0)
            self.final.append(tri_list)
        return self.final
 
 
    def add_zeros(self, base):
        temp = copy.deepcopy(base)
        temp.insert(0, 0)
        temp.append(0)
        return temp
 
 
if __name__ == "__main__":
    sol = Solution()
    print(sol.generate(5))