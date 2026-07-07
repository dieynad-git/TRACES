#!/usr/bin/env python3
"""
    Trace un buffer autour des points d'intéret dans nos captures Strava
"""
import cv2
import matplotlib.pyplot as plt
from math import sqrt 


# Lire la capture
img = cv2.imread("Capture_point2.png")
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #Sans cette ligne les couleurs sont inversees en temre de rouge et bleu


plt.figure(figsize=(20, 20))
plt.imshow(img_rgb)
plt.axis("off")
plt.title("Déterminer le nb de pixels de l'échelle")
zoom = plt.ginput(1)

points = plt.ginput(2) # Pour selectionner les 2 extremites de la barre d'echelle

centre = plt.ginput(1) 

plt.close()


print(points)
print(centre)

(x1, y1), (x2, y2) = points
longueur_pixels = sqrt((x2 - x1)**2 + (y2 - y1)**2)

rayon_pixels = 600 * longueur_pixels/100
print("Rayon du buffer en pixels : ", rayon_pixels)

(x_centre, y_centre) = centre[0]
cv2.circle(img, (int(x_centre), 
                 int(y_centre)), 
                 int(rayon_pixels), (0, 0, 255), 3)

cv2.imwrite("buffer_point2.png", img)