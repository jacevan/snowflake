import time
import random
import board
import neopixel

# adjust these based on your project
NUM_PIXELS = 42
PIXELS_PER_BRANCH = 7

# color variables
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# global neopixel instance
pixels = neopixel.NeoPixel(board.D18, NUM_PIXELS)

# fill a branch (0-6) a specific color
def fill_branch(branch, color):
  start = branch * PIXELS_PER_BRANCH
  finish = start + PIXELS_PER_BRANCH
  pixels[start:finish] = [color] * PIXELS_PER_BRANCH

# fill all the pixels
def fill_all(color):
  pixels[:] = [color] * NUM_PIXELS

if __name__ == "__main__":
  while True:
    # create random branch indexes
    branches = [0, 1, 2, 3, 4, 5]
    random.shuffle(branches)

    # restart all LEDs to WHITE
    # go through random indexes
    # and light up branches to blue  
    fill_all(WHITE)
    time.sleep(0.5)
    for i in branches:
      fill_branch(branches[i], BLUE)
      time.sleep(0.5)