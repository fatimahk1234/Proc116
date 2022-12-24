import cv2
img=cv2.imread("solar-system.jpg")

text="Mercury"
cv2.putText(img,text,(20,200),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(200,200,200))
cv2.imshow("Displaying the output0",img)
cv2.waitKey(0)

text="Venus"
cv2.putText(img,text,(30,200),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(200,200,100))
cv2.imshow("Displaying the output0",img)
cv2.waitKey(0)

text="Earth"
cv2.putText(img,text,(40,200),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(200,200,100))
cv2.imshow("Displaying the output0",img)
cv2.waitKey(0)

text="Mars"
cv2.putText(img,text,(50,200),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(200,200,100))
cv2.imshow("Displaying the output0",img)
cv2.waitKey(0)

text="Jupiter"
cv2.putText(img,text,(60,200),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(200,200,100))
cv2.imshow("Displaying the output0",img)
cv2.waitKey(0)

text="Saturn"
cv2.putText(img,text,(70,200),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(200,200,100))
cv2.imshow("Displaying the output0",img)
cv2.waitKey(0)

text="Uranus"
cv2.putText(img,text,(80,200),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(200,200,100))
cv2.imshow("Displaying the output0",img)
cv2.waitKey(0)

text="Neptune"
cv2.putText(img,text,(90,200),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(200,200,100))
cv2.imshow("Displaying the output0",img)
cv2.waitKey(0)