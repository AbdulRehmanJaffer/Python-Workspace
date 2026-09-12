#activity 1
"""import cv2

image = cv2.imread('images.jpg')

cv2.namedWindow('Loaded Image', cv2.WINDOW_NORMAL)

cv2.resizeWindow('Loaded Image', 800, 500)

cv2.imshow('Loaded Image', image)

cv2.waitKey(0)
cv2.destroyAllWindows()"""
#activity 2

import cv2

image = cv2.imread('images.jpg')
#to convert it to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#resize the grayscale image to 224x224
resized_image = cv2.resize(gray_image, (224, 224))
# Display the resized grayscale im age in a single window
cv2.imshow('Processed Image', resized_image)
#Wait for key press
key = cv2.waitKey(0)

#Check if the "S" key was pressed (ASCII for "S" is 83)
if key == ord('s'):
    #save the processed image when "S" is pressed
    cv2.imwrite('grayscale_resized_image.jpg', resized_image)

    print("Image saved as grayscale_resized_image.jpg")

else:
    print("Image not Saved")

cv2.destroyAllWindows()

print(f"Processed Image Dimensions: {resized_image.shape}")