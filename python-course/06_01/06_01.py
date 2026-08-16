score_lists=[60,70,80,55,65,64,75,84,73,56,59,92,74,78,71,77,66,58,57,62,63,67,68,89,90]
def get_grade_counts(scores):
    counts={"S":0,"A":0,"B":0,"C":0,"E":0}
    for score in scores:
        if score>=90:
            counts["S"]+=1
        elif score>=80:
            counts["A"]+=1
        elif score>=70:
            counts["B"]+=1
        elif score>=60:
            counts["C"]+=1
        else:
            counts["E"]+=1
    return counts
def get_pass_count(grade_counts):
    return grade_counts["S"]+grade_counts["A"]+grade_counts["B"]+grade_counts["C"]

def get_avarage(scores):
    return sum(scores)/len(scores)

def analyze_scores(scores):
    total_students=len(scores)
    grade_counts=get_grade_counts(scores)
    pass_count=get_pass_count(grade_counts)
    avg=get_avarage(scores)
    pass_rate=(pass_count/total_students)*100
    max_score=max(scores)

    print(f"生徒数は{total_students}です")
    print(f"評価がSの生徒は{grade_counts["S"]}人Aの生徒は{grade_counts["A"]}人Bの生徒は{grade_counts["B"]}人Cの生徒は{grade_counts["C"]}人Eの生徒は{grade_counts["E"]}人です")
    print(f"試験に合格した生徒は{pass_count}人不合格の生徒は{total_students-pass_count}人です  ")
    print(f"一番点数が高い人の点数は{max_score}です")
    print(f"得点の平均は{avg}で、得点率は{pass_rate}です")

analyze_scores(score_lists)