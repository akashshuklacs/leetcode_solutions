class Solution:
    init_color = int()
    image = list()
    color = int()
    num_rows = int()
    num_cols = int()
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.image = image
        self.color = color
        self.num_rows = len(image)
        self.num_cols = len(image[0])
        self.init_color = image[sr][sc]
        self.dfs(sr, sc)       
        return self.image
    
    def dfs(self, r, c):
        if self.image[r][c] == self.color:
            return
            
        if self.image[r][c] == self.init_color:
            self.image[r][c] = self.color
            
            if r>=1: self.dfs(r-1, c)
            if r<self.num_rows-1: self.dfs(r+1, c)
            if c>=1: self.dfs(r, c-1)    
            if c<self.num_cols-1 : self.dfs(r, c+1)
        else:
            return