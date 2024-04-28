def add_all(*nums: int) -> int:
    """Сложение всех циферок"""
    result = 0
    for num in nums:
        result += num
    return result
