class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        oldColor = image[sr][sc]
        return self.flood(image, sr, sc, color, oldColor)

    def flood(self, image: List[List[int]], sr: int, sc: int, color: int, oldColor: int) -> List[List[int]]:
        if sr < 0 or sc < 0 or sr >= len(image) or sc >= len(image[0]):
            return image

        if image[sr][sc] != oldColor or image[sr][sc] == color:
            return image

        image[sr][sc] = color

        image = self.flood(image, sr - 1, sc, color, oldColor)
        image = self.flood(image, sr + 1, sc, color, oldColor)
        image = self.flood(image, sr, sc - 1, color, oldColor)
        image = self.flood(image, sr, sc + 1, color, oldColor)

        return image