import cv2

img = cv2.imread("elsa.jpeg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Gambar elsa Original", img)
cv2.imshow("Gambar elsa Grayscale", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()