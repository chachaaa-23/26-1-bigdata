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


# Rotate an image to the right.
def rotate_right(pixels):
    height = len(pixels)
    width = len(pixels[0])
    rotated = []

    for x in range(width):
        row = []

        for y in range(height - 1, -1, -1):
            row.append(pixels[y][x])

        rotated.append(row)

    return rotated


# Change a color image into grayscale.
def to_gray(pixels):
    gray_pixels = []

    for row in pixels:
        new_row = []

        for red, green, blue in row:
            gray = (red + green + blue) // 3
            new_row.append((gray, gray, gray))

        gray_pixels.append(new_row)

    return gray_pixels


base_dir = os.path.dirname(__file__)
generated_dir = os.path.join(base_dir, "_generated")
image_path = os.path.join(generated_dir, "test.ppm")

os.makedirs(generated_dir, exist_ok=True)

# Make a small sample image.
pixels = [
    [(255, 0, 0), (255, 200, 0), (255, 255, 0), (0, 200, 0)],
    [(255, 150, 150), (255, 255, 255), (150, 255, 150), (150, 200, 255)],
    [(0, 150, 255), (0, 0, 255), (100, 0, 200), (200, 0, 200)],
    [(80, 80, 80), (140, 140, 140), (200, 200, 200), (0, 0, 0)],
]

save_ppm(image_path, pixels)

# Crop part of the image and save it.
cropped_pixels = [row[1:3] for row in pixels[1:3]]
save_ppm(os.path.join(generated_dir, "img_cropped.ppm"), cropped_pixels)

# Rotate, flip, and convert the image.
rotated_pixels = rotate_right(pixels)
save_ppm(os.path.join(generated_dir, "img_rotated.ppm"), rotated_pixels)

flipped_pixels = [row[::-1] for row in pixels]
save_ppm(os.path.join(generated_dir, "img_flipped.ppm"), flipped_pixels)

gray_pixels = to_gray(pixels)
save_ppm(os.path.join(generated_dir, "img_gray.ppm"), gray_pixels)

# Read and change one pixel.
pixel_value = pixels[1][1]
print(pixel_value)

pixels[1][1] = (255, 0, 0)
save_ppm(os.path.join(generated_dir, "img_pixel_changed.ppm"), pixels)
