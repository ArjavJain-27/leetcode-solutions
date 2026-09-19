class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int,
                     x1: int, y1: int, x2: int, y2: int) -> bool:

        # Find the closest x-coordinate in the rectangle
        closest_x = max(x1, min(xCenter, x2))

        # Find the closest y-coordinate in the rectangle
        closest_y = max(y1, min(yCenter, y2))

        # Distance from circle center to closest point
        dx = xCenter - closest_x
        dy = yCenter - closest_y

        # Check if the point is inside or on the circle
        return dx * dx + dy * dy <= radius * radius