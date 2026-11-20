class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = set()
        n = len(path)
        x = 0
        y = 0
        visited.add(self.hashFunction(0, 0))
        for i in range(n):
            if path[i] == "N":
                y += 1
            elif path[i] == "S":
                y -= 1
            elif path[i] == "E":
                x += 1
            else:
                x -= 1
            hashValue = self.hashFunction(x, y)
            if hashValue in visited:
                return True
            visited.add(hashValue)
        return False

    def hashFunction(self, x: int, y: int) -> int:
        return (x & 0xFFFFFFFFFFFFFFFF) ^ ((y << 32) & 0xFFFFFFFFFFFFFFFF)