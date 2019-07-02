from knight_tour import KnightTour
import pygame
import sys


def draw_background():
    screen.fill(blackTileColor)
    for i in range(board_size[0]):
        for j in range(board_size[1]):
            if (i + j) % 2 == 0:
                pygame.draw.rect(screen, whiteTileColor, (tileSize * j, tileSize * i, tileSize, tileSize), 0)
            pygame.draw.circle(screen, knightTileColor,
                               (tileSize * j + tileSize // 2, tileSize * i + tileSize // 2), tileSize // 4, 0)

#
# def draw_tiles():
#     for i in range(board_size[0]):
#         for j in range(board_size[1]):
#             if knight_pos == (i, j):
#                 pygame.draw.circle(screen, knightTileColor,
#                                    (tileSize * j + tileSize // 2, tileSize * i + tileSize // 2), tileSize // 4, 0)
#             elif knight_tour.board[i][j] != 0:
#                 pygame.draw.circle(screen, visitedTileColor,
#                                    (tileSize * j + tileSize // 2, tileSize * i + tileSize // 2), tileSize // 4,  0)


def draw_line(start, end):
    pygame.draw.line(screen, lineColor,
                     (tileSize * start[1] + tileSize // 2, tileSize * start[0] + tileSize // 2),
                     (tileSize * end[1] + tileSize // 2, tileSize * end[0] + tileSize // 2), 10)


board_size = (6, 6)
screenSizeX = 800
screenSizeY = 800

if screenSizeX//board_size[1] >= screenSizeY//board_size[0]:
    tileSize = screenSizeY // board_size[0]
else:
    tileSize = screenSizeX // board_size[1]

knight_tour = KnightTour(board_size=board_size)
pygame.init()
screen = pygame.display.set_mode((tileSize*board_size[1], tileSize*board_size[0]))
clock = pygame.time.Clock()
fps = 5

whiteTileColor = (245, 245, 245)
blackTileColor = (100, 100, 100)
visitedTileColor = (153, 51, 51)
knightTileColor = (255, 102, 102)
lineColor = (255, 102, 102)

draw_background()

skip = True
runUpdate = True
even = False
time = 0
while True:
    iterations = 0
    knight_tour.initialize_neurons()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    runUpdate = False

                if event.key == pygame.K_q:
                    fps += 1
                if event.key == pygame.K_a:
                    fps -= 1
                    if fps == 0:
                        fps = 1
                # if event.key == pygame.K_r:
                #     board = [[emptyTile for _ in range(n)] for _ in range(n)]
                #     knightXPos = 0
                #     knightYPos = 0
                #     board[knightYPos][knightXPos] = knightTile
                #     draw_background()
                #     draw_tiles()
                #     moveNum = 0
                #     skip = True
        if runUpdate:
            num_of_active, num_of_changes = knight_tour.update_neurons()
            print('active', num_of_active, 'changes', num_of_changes)
            draw_background()
            for vertex_set in knight_tour.get_active_neurons_vertices():
                vertex1, vertex2 = vertex_set
                draw_line(vertex1, vertex2)

            if num_of_changes == 0:
                print('wow!')
                break

            if knight_tour.check_degree():
                even = True
                print('yaaay')
                break
            iterations += 1
            if iterations == 20:
                break
        time += 1
        if even:
            print('yuppp')
            runUpdate = False
            break

        pygame.display.set_caption("Knight\'s Tour " + str(fps) + "fps")
        pygame.display.update()
        # msElapsed = clock.tick(fps)