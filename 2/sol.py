def find_safe_reports():
    reports = []
    with open('input.txt', 'r') as f:
        for line in f:
            reports.append(list(map(int, line.strip().split(' '))))
    cnt = 0
    for report in reports:
        is_safe = True
        increasing = False
        if report[1]>report[0]:
            increasing = True
        for i in range(1, len(report)):
            if report[i]<=report[i-1] and increasing:
                is_safe = False
                break
            elif report[i]>=report[i-1] and not increasing:
                is_safe = False
                break
        for i in range(1, len(report)):
            diff = abs(report[i]-report[i-1])
            if diff < 1 or diff > 3:
                is_safe = False
                break
        if is_safe:
            cnt += 1
    return cnt

print(find_safe_reports())