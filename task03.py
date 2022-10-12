"""
num1 : 값
num2 : 진수
"""

hash_table = {
  10: "a",
  11: "b",
  12: "c",
  13: "d",
  14: "e",
  15: "f",
  16: "g",
  17: "h",
  18: "i",
  19: "j",
  20: "k",
  21: "l",
  22: "m",
  23: "n",
  24: "o",
  25: "p",
  26: "q",
  27: "r",
  28: "s",
  29: "t",
  30: "u",
  31: "v",
  32: "w",
  33: "x",
  34: "y",
  35: "z"
}


# 36진수까지 지원
def deci_to_any(num1, num2):
  arr = []
  while num1:
    arr.append(num1 % num2)
    num1 //= num2
  arr.reverse()
  result = ""
  for v in arr:
    if v >= 10:
      result += hash_table[v]
    else:
      result += str(v)
  return result
