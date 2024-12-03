def is_safe(report):
    diffs = [report[i+1] - report[i] for i in range(len(report)-1)]
    increasing = all(0 < d <= 3 for d in diffs)
    decreasing = all(-3 <= d < 0 for d in diffs)
    return increasing or decreasing

def safe_dampener(report):
    if is_safe(report):
        return True
    
    for i in range(len(report)):
        new_report = report[:i] + report[i+1:]
        if is_safe(new_report):
            return True
    return False

with open('input/day02.txt', 'r') as file:
    reports = [list(map(int, line.strip().split())) for line in file]
print(sum(is_safe(report) for report in reports), sum(safe_dampener(report) for report in reports))
