   
import cv2  
import random
import numpy as np
import io
import discord
import tempfile

def draw_circle(image_path: str, mask_path: str = None) -> None:
    image = cv2.imread(image_path)
    mask = cv2.imread(mask_path)

    # Transform pixels into single values
    mask = mask.sum(axis=2) > 0
    
    # List of white pixels
    valid_points = np.array(np.where(mask))

    # Get random coordinates
    index = random.randrange(0, valid_points.shape[1])
    x = valid_points[1, index]
    y = valid_points[0, index]
    center_coordinates = (x, y)

    # Circle properties
    radius = int(1 / 30 * image.shape[0])
    color = (255, 255, 224)
    thickness = 8

    # Draw circle
    image = cv2.circle(image, center_coordinates, radius, color, thickness)

    # Send file
    with tempfile.NamedTemporaryFile(suffix='.png') as tmp:
        cv2.imwrite(tmp.name, image)
        image_file = discord.File(tmp.name)
        return image_file