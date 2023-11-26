import cv2
import matplotlib.pyplot as plt

foto = cv2.imread("pirinc2.jpg",0)
foto_boyut = cv2.resize(foto, (500, 700))
#cv2.imshow("pirinc", foto_boyut)
#cv2.waitKey(0)

esikleme = cv2.inRange(foto_boyut, 70, 257)
cv2.imshow("esikleme",esikleme)
cv2.waitKey()

(cnt, hierarchy) = cv2.findContours(esikleme, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
rgb = cv2.cvtColor(esikleme, cv2.COLOR_BGR2RGB)
cv2.drawContours(rgb, cnt, -1, (0, 255, 0), 2)

plt.imshow(rgb)

print("resimdeki pirinç sayısı : ", len(cnt))





