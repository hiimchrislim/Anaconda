"""
The Anaconda: A Game

=== Module Description ===
This module is responsible for displaying the UI of the game and running the
overall anaconda game.
"""
from typing import Tuple
import pygame
from random import randint
import linked_list
from grid import Grid

# BODY_HEAD = pygame.Rect((132, 363, 32, 32))
# BODY_PART = pygame.Rect((100, 363, 32, 32))

class Application:
    """
    === Attributes ===
    Sprites: snakeH_sprite, snakeT_sprite, food_sprite
    window_size:
        size of the GUI window
    food_size:
        size of the food the snake eats
    snakeH_size:
        size of the snake's head
    snakeT_size:
        size of the snake's tail
    clock:
        manage how fast the screen refreshes (FPS)
    grid_width:
        width of each grid
    grid_height:
        height of each grid
    margin:
        space between each grid
    """
    window_size: Tuple[int, int]
    food_size: Tuple[int, int]
    snakeH_size: Tuple[int, int]
    snakeT_size: Tuple[int, int]
    grid_width: int
    grid_height: int
    margin: int
    snake_body: linked_list.LinkedList

    def __init__(self) -> None:
        """
        Initialize the pygame module along with the window size and clock.
        Load in all the sprites.
        """
        pygame.init()
        pygame.display.set_caption("Anaconda")

        self.window_size = [590, 590]
        self.grid_height = 32
        self.grid_width = 32
        self.margin = 1
        self.score = 0
        self.screen = pygame.display.set_mode(self.window_size)
        self.clock = pygame.time.Clock()

        self.grid = Grid(16)
        self.grid.draw_original_snake()

        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.green = (126, 200, 80)
        self.red = (255, 0, 0)
        self.brown = (181, 101, 29)
        self.food = None
        self.show_title_screen()

    def show_title_screen(self) -> None:
        """
        Display the title screen of the game. The title screen should show the
        name of the game and its rules.
        """
        intro = True
        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.screen.fill(self.green)

            # Create title text
            render = pygame.font.Font('freesansbold.ttf', 75)
            title = render.render("Anaconda ", 1, self.white)

            # Write title text on screen
            self.screen.blit(title,
                             (self.window_size[0] // 5.6, self.window_size
                             [1] // 5))

            mouse_pos = pygame.mouse.get_pos()

            # Create and draw play text on screen
            render = pygame.font.Font('freesansbold.ttf', 40)
            play_text = render.render("Play", 1, self.white)

            self.screen.blit(play_text, (self.window_size[0] // 5.5,
                                         self.window_size[1] // 1.5))

            # Create and draw rules text on screen
            rules_text = render.render("Rules", 1, self.white)
            self.screen.blit(rules_text, (self.window_size[0] // 1.6,
                                          self.window_size[1] // 1.5))

            # If the mouse is on the play button and is clicked, move to game
            # screen
            if (107 <= mouse_pos[0] <= 192) and (393 <= mouse_pos[1] <= 436):
                play_text_highlight = render.render("Play", 1, self.brown)
                self.screen.blit(play_text_highlight,
                                 (self.window_size[0] // 5.5,
                                  self.window_size[1] // 1.5))

                click = pygame.mouse.get_pressed()
                if click[0] == 1:
                    self.play()

            # If the mouse is on the rules button and is clicked, move to the
            # rules screen

            if (368 <= mouse_pos[0] <= 482) and (396 <= mouse_pos[1] <= 426):
                rules_text_highlight = render.render("Rules", 1, self.brown)
                self.screen.blit(rules_text_highlight,
                                 (self.window_size[0] // 1.6,
                                  self.window_size[1] // 1.5))

                click = pygame.mouse.get_pressed()
                if click[0] == 1:
                    self.show_rules_screen()

            pygame.display.update()
            self.clock.tick(15)

    def show_rules_screen(self):
        """
        Display the rules of the game to the user
        """
        show_rules = True
        while show_rules:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.screen.fill(self.green)

            # --------------Create Rules Text and Back Text-------------

            rules_render = pygame.font.Font('freesansbold.ttf', 24)
            rules_label = rules_render.render("How to play Snake", 1,
                                              self.white)
            self.screen.blit(rules_label, (
            self.window_size[0] // 3.2, self.window_size[1] // 7))

            rule1_label = rules_render.render(
                "1. Eat apples to grow your snake", 1, self.white)
            self.screen.blit(rule1_label, (
            self.window_size[0] // 5, self.window_size[1] // 3))

            rule2_label = rules_render.render(
                "2. Avoid hitting the edge of the grid", 1, self.white)
            self.screen.blit(rule2_label, (
            self.window_size[0] // 5, self.window_size[1] // 2))

            rule3_label = rules_render.render(
                "3. Try to get a score of 252 to win!", 1, self.white)
            self.screen.blit(rule3_label, (self.window_size[0] // 5,
                                           self.window_size[1] // 1.5))

            mouse_pos = pygame.mouse.get_pos()
            back_text = rules_render.render("Back", 1, self.white)
            self.screen.blit(back_text, (self.window_size[0] // 2.2,
                                         self.window_size[1] // 1.1))

            # -----------------Back Click Functionality-------------------

            if (269 <= mouse_pos[0] <= 321) and (537 <= mouse_pos[1] <= 555):
                rules_text_highlight = rules_render.render("Back", 1,
                                                           self.brown)
                self.screen.blit(rules_text_highlight,
                                 (self.window_size[0] // 2.2,
                                  self.window_size[1] // 1.1))

                click = pygame.mouse.get_pressed()
                if click[0] == 1:
                    self.show_title_screen()

            pygame.display.update()
            self.clock.tick(15)

    def display_score(self):
        """
        Whenthe game is over, show the final score of the player.
        """
        # TODO: Implement this method

    def draw_grid(self):
        """
        This method draws the visual grid on the screen
        """
        # Draw grid
        #print(self.grid.get_grid())
        for row in range(1, 17):
            for column in range(1, 17):
                color = self.white
                if type(self.grid.get_item(row - 1,
                                           column - 1)) == linked_list._Node:
                    color = self.green
                rect = pygame.Rect(
                    column * (self.grid_height + self.margin) - 1,
                    row * (self.grid_width + self.margin),
                    self.grid_height, self.grid_width)
                pygame.draw.rect(self.screen, color, rect)
        if self.food is None:
            food_pos = self.place_food()
            self.food = food_pos
        else:
            column = self.food[1]
            row = self.food[0]
            color = self.red
            rect = pygame.Rect(column * (self.grid_height + self.margin) - 1,
                               row * (self.grid_width + self.margin),
                               self.grid_height, self.grid_width)
            pygame.draw.rect(self.screen, color, rect)

    def play(self) -> None:
        """
        Main GUI Application Loop. Runs the game.
        # TODO: This method still needs to implement the interactions with
        # TODO: spawning food, growing snake, and incrementing score
        """
        game_over = False

        render = pygame.font.Font('freesansbold.ttf', 16)

        label = render.render("Score: " + str(self.score), 1, self.white)

        # -------- Main Program Loop -----------
        while not game_over:
            # game_over = self.grid.is_game_over() # Fix this
            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    pygame.quit()
                    quit()
                    game_over = True

                if event.type == pygame.KEYUP:
                    self.grid.move_snake(event)

            # Set the screen background
            self.screen.fill(self.green)
            self.grid.update_snake()
            self.draw_grid()
            self.screen.blit(label, (0, 1))

            # Draw the borders of the grid
            # The borders are not hardcoded, meaning you can move outside.
            pygame.draw.line(self.screen, self.black, (31, 31), (560, 31), 4)
            pygame.draw.line(self.screen, self.black, (31, 31), (31, 560), 4)
            pygame.draw.line(self.screen, self.black, (31, 560), (560, 560), 4)
            pygame.draw.line(self.screen, self.black, (560, 560), (560, 31), 4)

            # Move the snake
            # TODO: The snake should move within the grid lines
            #
            # for i in range(len(self.snake.snake_body)):
            #     self.snake.snake_body[i].x += self.snake.get_snake_direction()[0]
            #     self.snake.snake_body[i].y += self.snake.get_snake_direction()[1]
            #
            # for j in range(len(self.snake.snake_body)):
            #     pygame.draw.rect(self.screen, self.green, self.snake.snake_body[j])
            # Limit to 60 frames per second
            self.clock.tick(2)

            # Go ahead and update the screen with what we've drawn.
            pygame.display.flip()

        self.restart_game()
        # pygame.quit()

    def restart_game(self):
        """ Restarts the game by taking the user back to the menu if they
        press "spacebar"
        """
        restart = True

        while restart:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        self.__init__()  # relaunch game from the title screen

            self.screen.fill(self.green)

            # ------------ Draw labels for game over screen ----------------

            game_over_render = pygame.font.Font('freesansbold.ttf', 75)
            game_over_label = game_over_render.render("Game Over!", 1,
                                                      self.white)

            self.screen.blit(game_over_label, (self.window_size[0] // 7.6,
                                               self.window_size[1] // 2.5))

            score_render = pygame.font.Font('freesansbold.ttf', 16)
            score_label = score_render.render("Final Score: " + str(self.score),
                                              1, self.white)

            self.screen.blit(score_label, (self.window_size[0] // 2.4,
                                           self.window_size[1] // 1.8))

            restart_render = pygame.font.Font('freesansbold.ttf', 16)
            restart_label = restart_render.render("Press spacebar to restart",
                                                  1, self.white)

            self.screen.blit(restart_label, (self.window_size[0] // 2.9,
                                             self.window_size[1] // 1.6))
            pygame.display.update()
            self.clock.tick(15)

    def place_food(self) -> Tuple[int, int]:
        """
        Place food randomly on the grid, not on the snke
        """
        is_valid = False
        row = None
        col = None
        while not is_valid:
            row = randint(1, 15)
            col = randint(1, 15)
            is_valid = type(self.grid.get_item(row, col)) != linked_list._Node
        color = self.red
        rect = pygame.Rect(col * (self.grid_height + self.margin) - 1,
                           row * (self.grid_width + self.margin),
                           self.grid_height, self.grid_width)
        pygame.draw.rect(self.screen, color, rect)
        return row, col


# This main method is currently here to test out the GUI.
# It can be removed once we finish anaconda.py

if __name__ == "__main__":
    app = Application()
    # app.show_title_screen()
