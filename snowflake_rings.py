import time
import board
import neopixel

NUM_PIXELS = 42

INNER_RING = [0, 6, 7, 13, 14, 20, 21, 27, 28, 34, 35, 41]
MID_RING = [1, 5, 8, 12, 15, 19, 22, 26, 29, 33, 36, 40]
OUTER_RING = [2, 3, 4, 9, 10, 11, 16, 17, 18, 23, 24, 25, 30, 31, 32, 37, 38, 39]

pixels = neopixel.NeoPixel(board.D18, NUM_PIXELS)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
colors = [RED, GREEN, BLUE]

def fill_ring(RING, color):
  for i in RING:
    pixels[i] = color
  # pixels.show()

def fill_inner_ring(color):
  fill_ring(INNER_RING, color)

def fill_mid_ring(color):
  fill_ring(MID_RING, color)

def fill_outer_ring(color):
  fill_ring(OUTER_RING, color)

# fill all
def fill_all(color):
  # for i in range(50):
  pixels[:] = [color] * NUM_PIXELS

if __name__ == "__main__":
  while True:
  #   for i in range(6):
  #     fill_branch(i, (255, 255, 255))
  #     time.sleep(0.05)
  #     turn_off()
    
    fill_all(BLUE)
    fill_inner_ring(WHITE)
    time.sleep(0.25)
    fill_mid_ring(WHITE)
    time.sleep(0.25)
    fill_outer_ring(WHITE)
    time.sleep(0.25)