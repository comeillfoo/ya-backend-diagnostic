import json
import sys


def main():
  n = int(sys.stdin.readline())
  offers_list = []
  for _ in range(n):
    raw_offers = sys.stdin.readline()
    offers = json.loads(raw_offers)
    for offer in offers['offers']:
      offers_list.append(offer)

  offers_list = sorted(offers_list, key=lambda offer: (offer['price'], offer['offer_id']))
  result = { 'offers': offers_list }
  print(json.dumps(result))


if __name__ == "__main__":
  main()
