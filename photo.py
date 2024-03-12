import cv2 as cv


img = cv.imread('photo2.jpeg', cv.IMREAD_GRAYSCALE)
cv.imshow('photo2', img)
cv.waitKey(0)
cv.imwrite('new_photo.jpg', img)

print("Высота:" + str(img.shape[0]))
print("Ширина:" + str(img.shape[1]))
# print("Количество каналов:" + str(img.shape[2]))

(b, g, r) = img[0, 0]
print("Красный: {}, Зелёный: {}, Синий: {}".format(r, g, b))


# ВОЗВРАЩАЕТ ЧБ ФОТО