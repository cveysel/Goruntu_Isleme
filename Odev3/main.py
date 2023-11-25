import cv2
import matplotlib.pyplot as plt


foto = cv2.imread("pirinc2.jpg",0)
foto_boyut = cv2.resize(foto, (500, 700))
#cv2.imshow("pirinc", foto_boyut)
#cv2.waitKey(0)

esikleme = cv2.inRange(foto_boyut, 70, 257)
cv2.imshow("esikleme",esikleme)
cv2.waitKey()

blur = cv2.GaussianBlur(esikleme, (11, 11), 0)
plt.imshow(blur, cmap='gray')

canny = cv2.Canny(blur, 30, 150, 3)
plt.imshow(canny, cmap='gray')

dilated = cv2.dilate(canny, (1, 1), iterations=0)
plt.imshow(dilated, cmap='gray')

(cnt, hierarchy) = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
rgb = cv2.cvtColor(esikleme, cv2.COLOR_BGR2RGB)
cv2.drawContours(rgb, cnt, -1, (0, 255, 0), 2)

plt.imshow(rgb)

print("Resimdeki pirinç sayısı : ", len(cnt))
