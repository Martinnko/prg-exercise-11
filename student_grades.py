class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)
    def get_grade(self, index):
        score = self.scores[index]

        if score >= 90:
            znamka = "A"
        elif score >= 80 and score < 90:
            znamka = "B"
        elif score >= 70 and score < 80:
            znamka = "C"
        elif score >= 60 and score < 70:
            znamka = "D"
        elif score >= 50 and score < 60:
            znamka = "E"
        else:
            znamka = "F"
        return znamka


    def find(self, body):
        results = []
        for i, j in enumerate(self.scores):
            if j == body:
                results.append(i)
        return results

    def get_sorted(self):
        scores = self.scores.copy()
        for j in range(len(scores) - 1):
            for val in range(len(scores) - j - 1):
                if scores[val] > scores[val + 1]:
                    scores[val], scores[val + 1] = scores[val + 1], scores[val]
        return scores


if __name__ == "__main__":
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])

    print(results.count())  # 9
    print(results.get_by_index(2))  # 91
    print(results.scores)  # [85, 42, 91, 67, 50, 73, 100, 38, 58]
    print(results.get_grade(2))  # A (91 bodů)
    print(results.get_grade(6))  # A (100 bodů)
    print(results.get_grade(7))  # F (38 bodů)
    print(results.find(100))  # [6]
    print(results.find(50))  # [4]
    print(results.find(77))  # []
    print(results.get_sorted())  # [38, 42, 50, 58, 67, 73, 85, 91, 100]
    print(results.scores)  # [85, 42, 91, 67, 50, 73, 100, 38, 58]  ← beze změny

    def main():
        results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
        mnozstvo = results.count()
        print(mnozstvo)
        for r in range(mnozstvo):
            body = results.get_by_index(r)
            znamka = results.get_grade(r)
            print(f" Student {r}: {body} bodov - {znamka}")
        print(f"{results.find(100)}")
        print(f"{results.get_sorted()}")