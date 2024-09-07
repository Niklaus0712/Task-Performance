import pygame
import sys
import time

# Initialize pygame
pygame.init()

# Constants
WINDOW_SIZE = 600
GRID_SIZE = 3
CELL_SIZE = WINDOW_SIZE // GRID_SIZE
LINE_WIDTH = 15
BOARD_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
X_COLOR = (255, 0, 0)  # Change X color to red for better visibility
O_COLOR = (239, 231, 200)
CIRCLE_COLOR = (239, 231, 200)
CIRCLE_RADIUS = CELL_SIZE // 3
CIRCLE_WIDTH = 15
X_WIDTH = 25
SPACE = CELL_SIZE // 4
FONT_SIZE = 50
INTRO_TEXT_COLOR = (0, 0, 0)  # Black color for intro text

# Set up the display
window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Tic-Tac-Toe")
font = pygame.font.Font(None, FONT_SIZE)

# Board
board = [[None] * GRID_SIZE for _ in range(GRID_SIZE)]

def draw_board():
    window.fill(BOARD_COLOR)
    # Draw vertical lines
    for row in range(1, GRID_SIZE):
        pygame.draw.line(window, LINE_COLOR, (0, row * CELL_SIZE), (WINDOW_SIZE, row * CELL_SIZE), LINE_WIDTH)
    # Draw horizontal lines
    for col in range(1, GRID_SIZE):
        pygame.draw.line(window, LINE_COLOR, (col * CELL_SIZE, 0), (col * CELL_SIZE, WINDOW_SIZE), LINE_WIDTH)

def draw_x(row, col):
    x_start = col * CELL_SIZE + SPACE
    y_start = row * CELL_SIZE + SPACE
    x_end = x_start + CELL_SIZE - 2 * SPACE
    y_end = y_start + CELL_SIZE - 2 * SPACE

    # Draw X with thicker lines
    pygame.draw.line(window, X_COLOR, (x_start, y_start), (x_end, y_end), X_WIDTH)
    pygame.draw.line(window, X_COLOR, (x_end, y_start), (x_start, y_end), X_WIDTH)

def draw_o(row, col):
    # Draw O
    center = (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2)
    pygame.draw.circle(window, O_COLOR, center, CIRCLE_RADIUS, CIRCLE_WIDTH)

def draw_markers():
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if board[row][col] == 'X':
                draw_x(row, col)
            elif board[row][col] == 'O':
                draw_o(row, col)

def draw_intro():
    window.fill(BOARD_COLOR)
    
    # Draw the welcome message
    welcome_text = font.render("Welcome to Tic Tac Toe!", True, INTRO_TEXT_COLOR)
    welcome_rect = welcome_text.get_rect(center=(WINDOW_SIZE // 2, WINDOW_SIZE // 3))
    window.blit(welcome_text, welcome_rect)
    
    pygame.display.update()
    time.sleep(2)  # Show the welcome message for 2 seconds

    # Draw the countdown
    countdown_texts = ["3", "2", "1", "Ready!"]
    for i, text in enumerate(countdown_texts):
        text_surface = font.render(text, True, INTRO_TEXT_COLOR)
        text_rect = text_surface.get_rect(center=(WINDOW_SIZE // 2, WINDOW_SIZE // 2 + i * 60))
        window.blit(text_surface, text_rect)
        pygame.display.update()
        time.sleep(1)  # Wait for 1 second between each message

def check_winner():
    # Check rows and columns
    for i in range(GRID_SIZE):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not None:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not None:
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]

    return None

def check_draw():
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if board[row][col] is None:
                return False
    return True

def main():
    draw_intro()  # Show the intro sequence

    turn = 'X'
    game_over = False

    draw_board()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                x, y = pygame.mouse.get_pos()
                row = y // CELL_SIZE
                col = x // CELL_SIZE

                if board[row][col] is None:
                    board[row][col] = turn
                    draw_board()  # Redraw the board
                    draw_markers()  # Draw the Xs and Os
                    pygame.display.update()  # Update the display
                    winner = check_winner()
                    if winner:
                        print(f"Player {winner} wins!")
                        game_over = True
                        pygame.time.wait(2000)
                    elif check_draw():
                        print("It's a draw!")
                        game_over = True
                        pygame.time.wait(2000)
                    turn = 'O' if turn == 'X' else 'X'

        pygame.display.update()

if __name__ == "__main__":
    main()
