import math
import datetime

def get_float_idx(v, values):
    idx = 0
    for t in values:
        if t >= v:
            break
        idx += 1
    if values[idx - 1] == values[-1]:
        idx -= 1
    elif values[idx] == v:
        pass
    else:
        duration = values[idx] - values[idx - 1]
        distance = values[idx] - v
        idx = idx - distance / float(duration)
    return max(0, idx)


def get_p_score(time, score):
    times = [0, 5, 10, 20, 30, 45, 60, 75, 90, 120, 200, 300, 450, 600, 800]
    t_idx = get_float_idx(time, times)

    scores = [0, 10, 20, 30, 40, 50, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82]
    s_idx = get_float_idx(score, scores)

    p_scores = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 3, 3, 2, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
        [4, 3.5, 3, 3, 2, 2, 2, 2, 1, 1, 0, 0, 0, 0, 0],
        [5, 4.5, 4, 3, 2, 2, 1.5, 1, 1, 1, 1, 0, 0, 0, 0],
        [6, 5.5, 5, 5, 4, 4, 3.5, 3, 3, 2, 2, 1, 1, 0, 0],
        [7, 7, 7, 6, 6, 5, 4.5, 4, 4, 3, 3, 2, 2, 1, 1],
        [8, 8, 8, 7, 7, 7, 6, 5, 5, 5, 4, 3, 3, 2, 2],
        [8, 8, 8, 8, 7, 7, 6.5, 6, 5.5, 5, 4, 3, 3, 2, 2],
        [9, 9, 9, 8, 7, 7, 6.75, 6.5, 6, 5, 4, 4, 3, 3, 3],
        [9, 9, 9, 8, 8, 7, 7, 7, 6, 5, 5, 4, 3, 3, 3],
        [9, 9, 9, 8.33, 8.33, 7.33, 7.33, 7.33, 6.33, 5.66, 5, 4.66, 3.66, 3.66, 3.66],
        [9, 9, 9, 8.66, 8.66, 7.66, 7.66, 7.66, 6.66, 6.33, 5.5, 5.33, 4.33, 4.33, 4.33],
        [9, 9, 9, 9, 9, 8, 8, 8, 7, 7, 6, 6, 5, 5, 5],
        [9, 9.25, 9.5, 9, 9, 8.5, 8.25, 8, 7.5, 7.5, 6.5, 6.5, 6, 6, 5],
        [10, 10, 10, 9, 9, 9, 8.5, 8, 8, 8, 7, 7, 7, 7, 6],
        [10, 10, 10, 10, 9, 9, 9, 9, 9, 8, 8, 8, 7, 7, 7],
        [10, 10, 10, 10, 10, 9, 9, 9, 9, 9, 9, 8, 8, 8, 8],
        [10, 10, 10, 10, 10, 10, 10, 10, 9, 9, 9, 9, 9, 8, 8]
    ]

    a1 = p_scores[int(math.floor(s_idx))][int(math.floor(t_idx))]
    a2 = p_scores[int(math.floor(s_idx))][int(math.ceil(t_idx))]
    b1 = p_scores[int(math.ceil(s_idx))][int(math.floor(t_idx))]
    b2 = p_scores[int(math.ceil(s_idx))][int(math.ceil(t_idx))]

    percentage_time = t_idx - math.floor(t_idx)
    a_avg = a1 * (1 - percentage_time) + a2 * percentage_time
    b_avg = b1 * (1 - percentage_time) + b2 * percentage_time

    percentage_score = s_idx - math.floor(s_idx)
    return a_avg * (1 - percentage_score) + b_avg * percentage_score


def get_m_score(time, m1, m2, m3):
    times = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140,
             150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270,
             280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400,
             500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600,
             1700, 1800]
    t_idx = get_float_idx(time, times)

    scores = [10, 10, 10, 9.666666667, 9.333333333, 8.666666667, 8.333333333,
              8, 7.666666667, 7.333333333, 7, 6.666666667, 6.333333333, 6,
              5.666666667, 5.333333333, 5, 5, 5, 5, 5, 5, 4.666666667,
              4.333333333, 4, 4, 4, 4, 4, 4, 3.666666667, 3.333333333, 3, 3, 3,
              3, 3, 3, 3, 3, 2.666666667, 2.333333333, 2, 2, 2, 1.666666667,
              1.333333333, 1, 1, 1, 1, 1, 1, 0.6666666667, 0]
    percentage_time = t_idx - math.floor(t_idx)
    score_avg = scores[int(math.floor(t_idx))] * (1 - percentage_time) + \
                scores[int(math.ceil(t_idx))] * percentage_time
    points = (0.5 * m1 + 0.3 * m2 + 0.2 * m3) / 100.0
    return score_avg * points


def duration_minutes(a, b):
    time_duration = a - b
    return int(abs(time_duration.total_seconds()) / 60)


def process_submissions(starting_time, submissions):
    # Assume submissions are sorted by date
    m_problem1 = 1
    m_problem2 = 2
    m_problem3 = 3
    p_problem = 4
    total_time_p = 0
    total_time_m = 0
    points_p = 0
    points_m = [0, 0, 0]

    high_score_p = 0
    best_time_p = 0
    high_score_m = 0
    best_time_m = 0
    total_points_m = 0
    total_points_p = 0
    for s in submissions:
        if s.problem == m_problem1:
            total_time_m += duration_minutes(starting_time, s.date)
            starting_time = s.date
            points_m[0] = max(points_m[0], s.case_points)
            new_m_score = get_m_score(
                total_time_m, points_m[0], points_m[1], points_m[2])
            if new_m_score > high_score_m:
                high_score_m = new_m_score
                best_time_m = total_time_m
                total_points_m = points_m[0] + points_m[1] + points_m[2]
        elif s.problem == m_problem2:
            total_time_m += duration_minutes(starting_time, s.date)
            starting_time = s.date
            points_m[0] = max(points_m[0], s.case_points)
            points_m[1] = max(points_m[1], s.case_points)
            if points_m[1] <= 50:
                points_m[1] = 0
            new_m_score = get_m_score(
                total_time_m, points_m[0], points_m[1], points_m[2])
            if new_m_score > high_score_m:
                high_score_m = new_m_score
                best_time_m = total_time_m
                total_points_m = points_m[0] + points_m[1] + points_m[2]
        elif s.problem == m_problem3:
            total_time_m += duration_minutes(starting_time, s.date)
            starting_time = s.date
            points_m[0] = max(points_m[0], s.case_points)
            points_m[1] = max(points_m[1], s.case_points)
            points_m[2] = max(points_m[2], s.case_points)
            if points_m[1] <= 50:
                points_m[1] = 0
            if points_m[2] <= 50:
                points_m[2] = 0
            new_m_score = get_m_score(
                total_time_m, points_m[0], points_m[1], points_m[2])
            if new_m_score > high_score_m:
                high_score_m = new_m_score
                best_time_m = total_time_m
                total_points_m = points_m[0] + points_m[1] + points_m[2]
        elif s.problem == p_problem:
            total_time_p += duration_minutes(starting_time, s.date)
            starting_time = s.date
            points_p = max(points_p, s.case_points)
            new_p_score = get_p_score(total_time_p, points_p)
            if new_p_score > high_score_p:
                high_score_p = new_p_score
                best_time_p = total_time_p
                total_points_p = points_p
    return ((high_score_m, best_time_m, total_points_m),
            (high_score_p, best_time_p, total_points_p))


class Submission:
    def __init__(self, problem, date, case_points):
        self.problem = problem
        self.date = date
        self.case_points = case_points

start_time = datetime.datetime(year=2019, month=1, day=1, hour=1)
submissions = []
submissions.append(Submission(1, start_time + datetime.timedelta(hours=1), 100))
submissions.append(Submission(2, start_time + datetime.timedelta(hours=2), 100))
submissions.append(Submission(4, start_time + datetime.timedelta(hours=3), 67))
calculated_score = process_submissions(start_time, submissions)

print('FINAL SCORE [0-10]: ', 0.4 * calculated_score[0][0] + 0.6 * calculated_score[1][0])