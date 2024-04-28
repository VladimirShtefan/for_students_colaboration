class Dog:
    def __init__(self, color, size):
        self.color = "black"
        self.size = "XXl"

    def add_all(self, *nums: int) -> int:
        """Сложение всех циферок"""
        result = 0
        for num in nums:
            result += num
        return result
