import cv2

filename = r'C:\Users\ASUS\Desktop\couple.jpg'
# 取自https://www.dailymercury.com.au/news/couple-forced-apart-due-to-virus-rules/3986568/

face_cascade = cv2.CascadeClassifier(
    r'C:\Users\ASUS\Anaconda3\pkgs\libopencv-3.4.1-h875b8b8_3\Library\etc\haarcascades\haarcascade_frontalface_default.xml')

img = cv2.imread(filename)

faces = face_cascade.detectMultiScale(img, 1.05, 3, cv2.CASCADE_SCALE_IMAGE, (100, 100), (400, 400))
for (x, y, h, w) in faces:
    img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
cv2.namedWindow('faces Detected!')
cv2.imshow('faces Detected!', img)
cv2.imwrite('faces.jpg', img)
cv2.waitKey(0)
