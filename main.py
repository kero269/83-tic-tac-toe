from board import Board

bd = Board()

bd.display_board()
game_count = 0
is_on = True

while is_on:
    user_input = input("Type your position (e.g. a1): ").lower()
    bd.update_board(user=user_input, game_count=game_count)

    bd.display_board()
    game_count += 1
    if game_count >= 3:
        is_on = bd.judgement()

