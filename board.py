import random

class Board:
    def __init__(self):
        self.dict = {
            "a1": "-",
            "a2": "-",
            "a3": "-",
            "b1": "-",
            "b2": "-",
            "b3": "-",
            "c1": "-",
            "c2": "-",
            "c3": "-",
        }
        self.board_list = ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]
        self.board_position = {
            "computer": [],
            "user": []
        }

    def display_board(self):
        board = f"""
           a     b     c
        1  {self.dict["a1"]}  |  {self.dict["b1"]}  |  {self.dict["c1"]}
         -----------------
        2  {self.dict["a2"]}  |  {self.dict["b2"]}  |  {self.dict["c2"]}
         -----------------
        3  {self.dict["a3"]}  |  {self.dict["b3"]}  |  {self.dict["c3"]}

        """
        print(board)

    def computer_play(self):
        computer_choice = self.board_list[random.randint(0,len(self.board_list)-1)]
        return computer_choice

    def update_board(self, user, game_count):
        try:
            self.board_list.remove(user)
        except ValueError:
            print("Sorry. This position has been taken.. ")
        else:
            self.dict[user] = "🍏"
            self.board_position["user"].append(user)

            if game_count < 9:
                computer_choice = self.computer_play()
            self.dict[computer_choice] = "🐥"

            self.board_list.remove(computer_choice)
            self.board_position["computer"].append(computer_choice)


    def judgement(self):
        pattern1 = ['a1', 'b2', 'c3']
        pattern2 = ['a3', 'b2', 'c1']
        pattern3 = ['a', 'b', 'c']
        pattern4 = ['1', '2', '3']

        split_user_position = [i for i in ''.join(self.board_position["user"])]
        split_computer_position = [i for i in ''.join(self.board_position["computer"])]
        if set(pattern1) <= set(self.board_position["user"]) or set(pattern2) <= set(self.board_position["user"]) or set(pattern3) <= set(split_user_position) or set(pattern4) <= set(split_user_position):
            print("Congratulation! You win!")
            return False
        elif set(pattern1) <= set(self.board_position["computer"]) or set(pattern2) <= set(self.board_position["computer"]) or set(pattern3) <= set(split_computer_position) or set(pattern4) <= set(split_computer_position):
            print("Computer win!")
            return False
        elif len(self.board_position) == 0:
            print("Game is draw")
            return False

