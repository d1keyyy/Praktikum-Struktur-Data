class Leaderboard:
    def __init__(self):
        self.teams = []

    def add_or_update_team(self, team_name, match_point):
        for team in self.teams:
            if team['name'] == team_name:
                team['match_point'] = match_point
                self._insertion_sort()
                return
        
        self.teams.append({'name': team_name, 'match_point': match_point})
        self._insertion_sort()

    def _insertion_sort(self):
        n = len(self.teams)
        for i in range(1, n):
            key = self.teams[i]
            j = i - 1
            while j >= 0 and self.teams[j]['match_point'] < key['match_point']:
                self.teams[j + 1] = self.teams[j]
                j -= 1
            self.teams[j + 1] = key

    def show_leaderboard(self):
        print(f"{'Rank':<5} {'Team':<20} {'Match Point':<10}")
        print("-" * 35)
        for rank, t in enumerate(self.teams, 1):
            print(f"{rank:<5} {t['name']:<20} {t['match_point']:<10}")

lb = Leaderboard()
data_tim = [
    ("ONIC", 9), ("DEWA UNITED", 7), ("BIGETRON BY VIT", 6),
    ("TEAM LIQUID ID", 6), ("ALTER EGO ESPORTS", 6), ("EVOS", 5),
    ("GEEK FAM", 5), ("NAVI", 3), ("RRQ HOSHI", 1)
]

for nama, poin in data_tim:
    lb.add_or_update_team(nama, poin)

lb.show_leaderboard()