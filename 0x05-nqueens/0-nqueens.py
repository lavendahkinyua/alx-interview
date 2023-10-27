#!/usr/bin/python3
""" N queens puzzle"""

import sys


if __name__ == '__main__':
  if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

  try:
    n = int(sys.argv[1])
  except ValueError:
    print('N must be a number')
    exit(1)
 
  if n < 4:
    print('N must be at least 4')
    exit(1)

  solving = []
  queens = []
  stop = False
  r = 0
  c = 0

  while r < n:
    while c < n:
      if len(queens) == 0:
        queens.append([r, c])
        solving.append([r, c])
      else:
        for queen in queens:
          if c == queen[1]:
            stop = True
            break
          if abs(r - queen[0]) == abs(c - queen[1]):
            stop = True
            break
        if not stop:
          queens.append([r, c])
          solving.append([r, c])
      if stop:
        stop = False
      else:
        break
      c += 1
    if len(queens) == r:
      queens.pop()
      if len(queens) == 0:
        print('N must be at least 4')
        exit(1)
      r = queens[-1][0]
      c = queens[-1][1] + 1
      queens.pop()
    else:
      r += 1
      c = 0

    print(solving)
