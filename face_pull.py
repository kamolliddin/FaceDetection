from PIL import Image
import face_recognition

image = face_recognition.load_image_file('./img/known/Kamoliddin.jpeg')
face_locations = face_recognition.face_locations(image)

for face in face_locations:
	top, right, bottom, left = face
	face_image = image[top:bottom, left:right]
	pil_image = Image.fromarray(face_image)
	pil_image.save(f'{top}.jpg')
