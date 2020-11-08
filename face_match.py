import face_recognition

image = face_recognition.load_image_file('./img/known/Bill Gates.jpg')
image_encoding = face_recognition.face_encodings(image)[0]

image_unknown = face_recognition.load_image_file('./img/unknown/d-trump.jpg')
image_unknown_encoding = face_recognition.face_encodings(image_unknown)[0]

results = face_recognition.compare_faces([image_encoding], image_unknown_encoding )

if results[0]:
	print('This is Bill gates')
else:
	print('This is not Bill gates')