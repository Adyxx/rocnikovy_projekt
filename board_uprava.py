class GameState():
    def __init__(self):
        self.board = [
            ["--", "bl", "--", "bl", "--", "bl", "--", "bl", "", ""],
            ["bl", "--", "bl", "--", "bl", "--", "bl", "--", "", ""],
            ["--", "--", "--", "--", "--", "--", "--", "--", "", ""],
            ["--", "--", "--", "--", "--", "--", "--", "--", "", ""],
            ["--", "--", "--", "--", "--", "--", "--", "--", "", ""],
            ["--", "--", "--", "--", "--", "--", "--", "--", "", ""],
            ["--", "wh", "--", "wh", "--", "wh", "--", "wh", "", ""],
            ["wh", "--", "wh", "--", "wh", "--", "wh", "--", "", ""],
            ["", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", ""],]