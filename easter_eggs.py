"""
The Anaconda: A Game

=== Module Description ===
This module is a compilation of all the easter eggs players can activate
during the game.

To add any additional easter eggs, just add a new class in this module
corresponding to the easter egg.
"""

import pygame
import random


class CreditsEgg:
    """
    This class runs the credits easter eggs where random characters appear
    on the screen where once in a while, it'll display an author's name.

    === Attributes ===
    window_size:
        size of game window
    clock:
        manage how quickly the window refreshes
    characters:
        string of all letters and numbers
    author_names:
        list of all author names that contributed to the project
        bhavik, chris, dhaval, mark, and stanley: Main game programmers
        hillary: Sprites designer
    selected_author: current author to draw on screen
    """

    def __init__(self):
        pygame.init()
        self.window_size = [590, 590]
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode(self.window_size)

        self.characters = "abcdefghijklmnopqrstuvwxyz1234567890"
        self.author_names = ["bhavik", "chris", "dhaval", "hillary", "mark",
                             "stanley"]
        self.selected_author = ""

        self.white = (255, 255, 255)
        self.black = (0, 0, 0)

        self.render = pygame.font.Font('freesansbold.ttf', 16)

        self.credits_egg()

    def credits_egg(self):
        """ Display the credits for Anaconda
        """
        y = 0
        x = 0

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            # if there's a selected author, draw that author character
            # by character
            if self.draw_author():

                label = self.render.render("" + self.get_author_char(), 1,
                                           self.white)

            else:
                label = self.render.render("" + self.characters[
                    random.randint(0, len(self.characters) - 1)], 1,
                                           self.white)

            self.screen.blit(label, (x, y))
            y += 20

            if y >= self.window_size[1]:
                x += 20
                y = 0

            if x >= self.window_size[0]:
                # restart once it reaches the end of the screen
                self.screen.fill(self.black)
                y = 0
                x = 0

            pygame.display.update()
            self.clock.tick(15)

    def get_author_char(self):
        """ Return a character from the selected author's name at each pass.
        Each time a character is taken, slice the string so that the same
        character doesn't get printed again.
        """

        print(self.selected_author)
        char = self.selected_author[0]
        self.selected_author = self.selected_author[1:]
        return char

    def draw_author(self):
        """ Return a boolean which represents whether to continue drawing
        an author's name or not.
        """
        if self.selected_author != "":
            return True

        elif random.randint(0, 500) == 10:  # chance of drawing an author
            self.selected_author = self.author_names[
                random.randint(0, len(self.author_names) - 1)]
            return True

        return False
