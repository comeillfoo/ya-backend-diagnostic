from datetime import datetime, timedelta
import sys


def last_day_of_month(date):
  next_month = date.replace(day=28) + timedelta(days=4)
  return next_month - timedelta(days=next_month.day)


def next_month(date):
  try:
    return (date.replace(day=1) + timedelta(days=31)).replace(day=date.day)
  except ValueError:
    return (date + timedelta(days=31)).replace(day=1) - timedelta(days=1)


def next_review(start):
  end_of_review =  [3, 3, 3, 9, 9, 9, 9, 9, 9, 3, 3, 3]
  old_month = start.month
  start = start.replace(month=end_of_review[old_month - 1])
  if old_month >= 10:
    start = start.replace(year=start.year + 1)

  # print(start)
  if start.month == 3:
    start = start.replace(day=31) # 31 of march
  else: 
    start = start.replace(day=30) # 30 of september
  return start


def get_end_by_type(start, type):
  if type == 'WEEK':
    return (start - timedelta(days=start.weekday()) + timedelta(days=6), lambda x: x + timedelta(days=7))
  elif type == 'MONTH':
    return (last_day_of_month(start), lambda x: last_day_of_month(next_month(x)))
  elif type == 'QUARTER':
    end_of_quarter = [3, 3, 3, 6, 6, 6, 9, 9, 9, 12, 12, 12]
    return (last_day_of_month(start.replace(day=1, month=end_of_quarter[start.month - 1])), lambda x: last_day_of_month(next_month(next_month(next_month(x)))))
  elif type == 'YEAR':
    return (start.replace(month=12, day=31), lambda x: x.replace(year=x.year + 1, month=12, day=31))
  elif type == 'REVIEW':
    return (next_review(start), next_review)


def main():
  date_pattern = "%Y-%m-%d"

  type = sys.stdin.readline().strip()

  start, end = sys.stdin.readline().strip().split()

  start = datetime.strptime(start, date_pattern)
  end = datetime.strptime(end, date_pattern)

  it, f = get_end_by_type(start, type)

  result = []
  while it < end:
    result.append(f'{start.strftime(date_pattern)} {it.strftime(date_pattern)}')
      
    start = it + timedelta(days=1)
    if type == 'REVIEW':
      it = f(start)
    else:
      it = f(it)
  
  result.append(f'{start.strftime(date_pattern)} {end.strftime(date_pattern)}')
  
  print(len(result))
  for date in result:
    print(date)


if __name__ == "__main__":
  main()
