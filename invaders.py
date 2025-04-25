from PIL import Image
import random

# Constants
PIXEL_SIZE = 20  # Size of each pixel square
INVADER_SIZE = 5  # 5x5 grid

# Generate a symmetrical 5x5 invader pattern
# Left 3 columns random, right 2 columns mirror left
def generate_invader_pattern():
    pattern = [[0]*INVADER_SIZE for _ in range(INVADER_SIZE)]
    for y in range(INVADER_SIZE):
        for x in range((INVADER_SIZE + 1)//2):  # left half + middle if odd
            val = random.randint(0, 1)
            pattern[y][x] = val
            pattern[y][INVADER_SIZE - 1 - x] = val  # mirror
    return pattern

# Draw the invader pattern to an image
def draw_invader(pattern, pixel_size=PIXEL_SIZE):
    img_size = INVADER_SIZE * pixel_size
    img = Image.new('RGB', (img_size, img_size), 'black')
    pixels = img.load()
    for y in range(INVADER_SIZE):
        for x in range(INVADER_SIZE):
            if pattern[y][x] == 1:
                for py in range(pixel_size):
                    for px in range(pixel_size):
                        pixels[x*pixel_size + px, y*pixel_size + py] = (255, 255, 255)  # white
    return img

# Main function to generate and save multiple invaders
def generate_invaders(count=10, output_prefix='invader'):
    for i in range(count):
        pattern = generate_invader_pattern()
        img = draw_invader(pattern)
        filename = f'{output_prefix}_{i+1}.png'
        img.save(filename)
        print(f'Saved {filename}')

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Generate 8-bit style Space Invader images.')
    parser.add_argument('-n', '--number', type=int, default=10, help='Number of invaders to generate')
    parser.add_argument('-p', '--prefix', type=str, default='invader', help='Output filename prefix')
    args = parser.parse_args()
    generate_invaders(args.number, args.prefix)
