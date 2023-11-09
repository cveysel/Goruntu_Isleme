import cv2

foto = cv2.imread("download.jpg",flags=0)

cv2.imshow("ragnar",foto)
cv2.waitKey()

histogram =[0 for x in range(0,256)]

for j in range (len(foto[:,0])) :
    for i in range(len(foto[0,:])):
        histogram[foto[j,i]] += 1

print(histogram)
