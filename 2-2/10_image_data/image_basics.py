import os

# Save pixels as a simple PPM image file.
def save_ppm(image_path, pixels):
    height = len(pixels)
    width = len(pixels[0])

    with open(image_path, "w", encoding="utf-8") as f:
        f.write("P3\n")
        f.write(f"{width} {height}\n")
        f.write("255\n")

        for row in pixels:
            values = []

            for red, green, blue in row:
                values.append(f"{red} {green} {blue}")

            f.write(" ".join(values) + "\n")


# Load pixels from a simple PPM image file.
def load_ppm(image_path):
    with open(image_path, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    width, height = map(int, lines[1].split())
    numbers = list(map(int, " ".join(lines[3:]).split()))
    pixels = []
    index = 0

    for _ in range(height):
        row = []

        for _ in range(width):
            row.append(tuple(numbers[index:index + 3]))
            index += 3

        pixels.append(row)

    return pixels


# Make a smaller image by skipping every other pixel.
def resize_half(pixels):
    return [row[::2] for row in pixels[::2]]


base_dir = os.path.dirname(__file__)
generated_dir = os.path.join(base_dir, "_generated")
image_path = os.path.join(generated_dir, "test.ppm")
save_path = os.path.join(generated_dir, "test_copy.ppm")
resized_path = os.path.join(generated_dir, "test_small.ppm")

os.makedirs(generated_dir, exist_ok=True)

# Make a small sample image.
pixels = [
    [(255, 0, 0), (255, 200, 0), (255, 255, 0), (0, 200, 0)],
    [(255, 150, 150), (255, 255, 255), (150, 255, 150), (150, 200, 255)],
    [(0, 150, 255), (0, 0, 255), (100, 0, 200), (200, 0, 200)],
    [(80, 80, 80), (140, 140, 140), (200, 200, 200), (0, 0, 0)],
]

save_ppm(image_path, pixels)

# Load the image again and save a copy.
loaded_pixels = load_ppm(image_path)
save_ppm(save_path, loaded_pixels)

# Print the image size.
print((len(loaded_pixels[0]), len(loaded_pixels)))

# Make a smaller copy of the image.
small_pixels = resize_half(loaded_pixels)
save_ppm(resized_path, small_pixels)
