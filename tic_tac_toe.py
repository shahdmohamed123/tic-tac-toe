from tkinter import *
import random

# Detect who is playing and turn on the next player
def next_turn(row, col):
    global player
    if game_btns[row][col]['text'] == ' ' and not check_winner():
        game_btns[row][col]['text'] = player
        if check_winner():
            
            
            label.config(text=(player + ' Wins!'))
        elif check_empty_spaces():
            player = players[1] if player == players[0] else players[0]
            label.config(text=(player + "'s Turn"))
        else:
            label.config(text=('Tie, No winner!'))

# Check wins
def check_winner():
    for row in range(3):
        if game_btns[row][0]['text'] == game_btns[row][1]['text'] == game_btns[row][2]['text'] != ' ':
            
             game_btns[row][0].config(text=' ', bg='green')
             game_btns[row][1].config(text=' ', bg='green')
             game_btns[row][2].config(text=' ', bg='green')
             return True
    for col in range(3):
        if game_btns[0][col]['text'] == game_btns[1][col]['text'] == game_btns[2][col]['text'] != ' ':
            
            game_btns[0][col].config(text=' ', bg='green')
            game_btns[1][col].config(text=' ', bg='green')
            game_btns[2][col].config(text=' ', bg='green')
            return True
    if game_btns[0][0]['text'] == game_btns[1][1]['text'] == game_btns[2][2]['text'] != ' ':
        
            game_btns[0][0].config(text=' ', bg='green')
            game_btns[1][1].config(text=' ', bg='green')
            game_btns[2][2].config(text=' ', bg='green')
            return True
    elif game_btns[0][2]['text'] == game_btns[1][1]['text'] == game_btns[2][0]['text'] != ' ':
            game_btns[0][2].config(text=' ', bg='green')
            game_btns[1][1].config(text=' ', bg='green')
            game_btns[2][0].config(text=' ', bg='green')
            return True
    return False

# Check if there are any empty spaces left
def check_empty_spaces():
    for row in range(3):
        for col in range(3):
            if game_btns[row][col]['text'] == ' ':
                return True
    return False

# Start new game
def start_new_game():
    global player
    player = random.choice(players)
    label.config(text=(player + "'s Turn"))
    for row in range(3):
        for col in range(3):
            game_btns[row][col].config(text=' ', bg='SystemButtonFace')

window = Tk()
window.title('Tic-Tac-Toe')

players = ['X', 'O']
player = random.choice(players)

game_btns = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

label = Label(text=(player + "'s Turn"), font=('consolas', 40))
label.pack(side='top')

restart_btn = Button(text='Restart', font=('consolas', 20), command=start_new_game)
restart_btn.pack(side='top')

btns_frame = Frame(window)
btns_frame.pack()

for row in range(3):
    for col in range(3):
        game_btns[row][col] = Button(btns_frame, text=' ', font=('consolas', 50), width=4, height=1, command=lambda row=row, col=col: next_turn(row, col))
        game_btns[row][col].grid(row=row, column=col)

window.mainloop()
