import requests
import sys
import json


def main():
  url = sys.stdin.readline().strip()
  port = int(sys.stdin.readline().strip())
  a = int(sys.stdin.readline().strip())
  b = int(sys.stdin.readline().strip())

  req = requests.get(url=f'{url}:{port}', params={'a': a, 'b': b})

  array = req.json()
  array.sort()

  for x in array:
    print(x)


if __name__ == "__main__":
  main()
