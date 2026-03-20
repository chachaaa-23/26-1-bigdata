import os

from PIL import Image
from PIL import ImageDraw

# Open one image file in this folder.
base_dir = os.path.dirname(__file__)
input_path = os.path.join(base_dir, "sample.jpg")
generated_dir = os.path.join(base_dir, "_generated")
output_path = os.path.join(generated_dir, "sample_with_circle.jpg")

os.makedirs(generated_dir, exist_ok=True)

# the original image first.
image = Image.open(input_path)

# Draw one red circle on the image.
draw = ImageDraw.Draw(image)
draw.ellipse((140, 140, 380, 380), outline="red", width=6) #원본 복제 저장ㅇㅇ

# Save and show the edited image.
image.save(output_path)

print(input_path)
print(output_path)
