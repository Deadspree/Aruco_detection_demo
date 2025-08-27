import cv2
import numpy as np
import matplotlib.pyplot as plt

# Define the dictionary we want to use
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)

# Generate a marker
marker_id = 23
marker_size = 200  # Size in pixels
marker_image = cv2.aruco.generateImageMarker(aruco_dict, marker_id, marker_size)

# Add a white border around the marker
border_size = 20  # pixels
marker_with_border = cv2.copyMakeBorder(
    marker_image,
    border_size, border_size, border_size, border_size,
    cv2.BORDER_CONSTANT,
    value=255  # white
)

# Save and display
cv2.imwrite('marker_23_border.png', marker_with_border)

plt.imshow(marker_with_border, cmap='gray', interpolation='nearest')
plt.axis('off')
plt.title(f'ArUco Marker {marker_id} with White Border')
plt.show()
