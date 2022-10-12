def is_triangle(num1: float, num2: float, num3: float) -> bool:
  arr = [num1, num2, num3]
  max_num = max(arr)
  arr.pop(arr.index(max_num))
  if max_num < sum(arr):
    return True
  return False