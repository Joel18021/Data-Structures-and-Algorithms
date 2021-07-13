class Job:
  def __init__(self, n, v, w):
    self.name = n
    self.profit = v
    self.deadline = w
  def __lt__(self, other):
    return self.profit < other.profit
def jobsequencing(iname, iprofit, ideadline):
  ival = []
  for j in range(len(iprofit)):
    ival.append(Job(iname[j], iprofit[j], ideadline[j]))
    ival.sort(reverse=True)
    maxjob = len(iprofit)
    result = [False] * maxjob
    job = [-1] * maxjob
  for i in range(0, maxjob):
    for j in range(min(maxjob-1, ival[i].deadline-1), -1, -1):
      if result[j] is False:
        result[j] = True
        job[j] = ival[i].name
        break
  djob = []
  for k in job:
    if k != -1:
      djob.append(k)
  return djob
print("Job Sequencing with deadlines")
item = int(input("Enter the number of jobs:"))
name = []
profit = []
deadline = []
for i in range(item):
  name.append((input("Enter the " + str(i + 1) + "th job name: ")))
  profit.append(int(input("Enter the " + str(i + 1) + "th job profit: ")))
  deadline.append(int(input("Enter the " + str(i + 1) + "th job deadline: ")))
print("Job order:", jobsequencing(name, profit, deadline))
