import sys


def main():
  userLimit, serviceLimit, duration = map(int, sys.stdin.readline().strip().split())
  line = sys.stdin.readline().strip()
  next_time = 1 + duration
  users = {}
  while line != '-1':
    t, userId = map(int, line.split())
    if t > next_time:
      next_time += next_time + duration
    user = users.get(userId, None)
    if user != None:
      users[userId]['count'] += 1
    else:
      users[userId] = { 'count': 1, 'last_time': t }
    
    user = users[userId]
    if user['last_time'] > next_time:
      users[userId]['count'] = 1

    if 

    line = sys.stdin.readline().strip()


if __name__ == "__main__":
  main()
