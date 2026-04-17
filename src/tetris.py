import pygame
import random

# 初始化游戏
pygame.init()

# ============== 游戏基础配置 ==============
BLOCK_SIZE = 30
COLS = 10
ROWS = 20
SCREEN_WIDTH = COLS * BLOCK_SIZE + 200
SCREEN_HEIGHT = ROWS * BLOCK_SIZE
FPS = 60

# 颜色配置
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [
    (0, 255, 255),
    (255, 255, 0),
    (160, 32, 240),
    (255, 165, 0),
    (0, 0, 255),
    (0, 255, 0),
    (255, 0, 0)
]

# 俄罗斯方块7种形状
SHAPES = [
    [[1,1,1,1]],
    [[1,1],[1,1]],
    [[0,1,0],[1,1,1]],
    [[1,0,0],[1,1,1]],
    [[0,0,1],[1,1,1]],
    [[0,1,1],[1,1,0]],
    [[1,1,0],[0,1,1]]
]

# ============== 游戏变量 ==============
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("经典俄罗斯方块 - Python版")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)

board = [[None for _ in range(COLS)] for _ in range(ROWS)]
current_shape = None
current_color = None
current_x = 0
current_y = 0
score = 0
level = 1
game_over = False
fall_time = 0
fall_speed = 1000

def new_shape():
    global current_shape, current_color, current_x, current_y, game_over
    idx = random.randint(0, len(SHAPES)-1)
    current_shape = SHAPES[idx]
    current_color = COLORS[idx]
    current_x = COLS // 2 - len(current_shape[0]) // 2
    current_y = 0
    if check_collision(current_shape, current_x, current_y):
        game_over = True

def check_collision(shape, x, y):
    for row in range(len(shape)):
        for col in range(len(shape[row])):
            if shape[row][col]:
                new_x = x + col
                new_y = y + row
                if new_x < 0 or new_x >= COLS or new_y >= ROWS:
                    return True
                if new_y >= 0 and board[new_y][new_x]:
                    return True
    return False

def draw_block(x, y, color):
    rect = pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE - 1, BLOCK_SIZE - 1)
    pygame.draw.rect(screen, color, rect)
    pygame.draw.rect(screen, WHITE, rect, 1)

def draw_game():
    screen.fill(BLACK)
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col]:
                draw_block(col, row, board[row][col])
    for row in range(len(current_shape)):
        for col in range(len(current_shape[row])):
            if current_shape[row][col]:
                draw_block(current_x + col, current_y + row, current_color)
    score_text = font.render(f"分数: {score}", True, WHITE)
    level_text = font.render(f"等级: {level}", True, WHITE)
    screen.blit(score_text, (COLS * BLOCK_SIZE + 20, 50))
    screen.blit(level_text, (COLS * BLOCK_SIZE + 20, 100))
    tip1 = font.render("←→移动", True, WHITE)
    tip2 = font.render("↑旋转", True, WHITE)
    tip3 = font.render("↓加速", True, WHITE)
    tip4 = font.render("空格落地", True, WHITE)
    screen.blit(tip1, (COLS * BLOCK_SIZE + 20, 200))
    screen.blit(tip2, (COLS * BLOCK_SIZE + 20, 250))
    screen.blit(tip3, (COLS * BLOCK_SIZE + 20, 300))
    screen.blit(tip4, (COLS * BLOCK_SIZE + 20, 350))

def merge_shape():
    for row in range(len(current_shape)):
        for col in range(len(current_shape[row])):
            if current_shape[row][col]:
                board[current_y + row][current_x + col] = current_color

def clear_lines():
    global score, level, fall_speed
    lines = 0
    for row in range(ROWS-1, -1, -1):
        if all(cell is not None for cell in board[row]):
            del board[row]
            board.insert(0, [None for _ in range(COLS)])
            lines += 1
    if lines == 1: score += 100
    elif lines == 2: score += 300
    elif lines == 3: score += 500
    elif lines >= 4: score += 800
    level = score // 1000 + 1
    fall_speed = max(100, 1000 - (level-1)*100)

def drop():
    global current_y
    if not check_collision(current_shape, current_x, current_y + 1):
        current_y += 1
    else:
        merge_shape()
        clear_lines()
        new_shape()

def rotate_shape():
    global current_shape
    rotated = list(zip(*current_shape[::-1]))
    rotated = [list(row) for row in rotated]
    if not check_collision(rotated, current_x, current_y):
        current_shape = rotated

def hard_drop():
    while not check_collision(current_shape, current_x, current_y + 1):
        current_y += 1
    drop()

new_shape()
running = True

while running:
    current_time = pygame.time.get_ticks()
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and not game_over:
            if event.key == pygame.K_LEFT:
                if not check_collision(current_shape, current_x - 1, current_y):
                    current_x -= 1
            elif event.key == pygame.K_RIGHT:
                if not check_collision(current_shape, current_x + 1, current_y):
                    current_x += 1
            elif event.key == pygame.K_DOWN:
                drop()
            elif event.key == pygame.K_UP:
                rotate_shape()
            elif event.key == pygame.K_SPACE:
                hard_drop()

    if not game_over and current_time - fall_time > fall_speed:
        drop()
        fall_time = current_time

    draw_game()

    if game_over:
        game_over_text = font.render("游戏结束!", True, WHITE)
        final_score = font.render(f"最终分数: {score}", True, WHITE)
        screen.blit(game_over_text, (COLS * BLOCK_SIZE//2 - 50, SCREEN_HEIGHT//2))
        screen.blit(final_score, (COLS * BLOCK_SIZE//2 - 70, SCREEN_HEIGHT//2 + 50))

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
