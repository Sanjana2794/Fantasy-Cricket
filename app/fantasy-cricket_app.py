import sys
import sqlite3
from PyQt5 import QtWidgets, uic
from scoring import batting_points, bowling_points, fielding_points

class FantasyCricket(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("../ui/fantasy_cricket.ui", self)

        self.conn = sqlite3.connect("../database/fantasy_cricket.db")
        self.cursor = self.conn.cursor()

        self.team_players = []

        self.addButton.clicked.connect(self.add_player)
        self.removeButton.clicked.connect(self.remove_player)
        self.evaluateButton.clicked.connect(self.evaluate_score)

    def add_player(self):
        player = self.playersList.currentItem().text()
        if player not in self.team_players:
            self.team_players.append(player)
            self.selectedList.addItem(player)

    def remove_player(self):
        player = self.selectedList.currentItem().text()
        self.team_players.remove(player)
        self.selectedList.takeItem(self.selectedList.currentRow())

    def evaluate_score(self):
        total = 0
        for player in self.team_players:
            self.cursor.execute("SELECT * FROM match WHERE player=?", (player,))
            row = self.cursor.fetchone()

            if row:
                total += batting_points(row[1], row[2], row[3], row[4])
                total += bowling_points(row[8], row[7], row[5])
                total += fielding_points(row[9], row[10], row[11])

        QtWidgets.QMessageBox.information(self, "Final Score", f"Team Score: {total}")


app = QtWidgets.QApplication(sys.argv)
window = FantasyCricket()
window.show()
sys.exit(app.exec_())
