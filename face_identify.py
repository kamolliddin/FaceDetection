import face_recognition
from PIL import Image, ImageDraw
import os
from os import listdir
from os.path import isfile, join

files = [f for f in listdir('./img/known') if isfile(join('./img/known', f))]
images = list()
face_names = list()
for file in files:
	filename, file_extension = os.path.splitext(file)
	if file_extension in ['.jpeg','.jpg','.png']:
		images.append(file)
		face_names.append(filename)

images_to_recognize = list()
image_encodings = list()

for image_name in images:
	image = face_recognition.load_image_file(f'./img/known/{image_name}')
	images_to_recognize.append(image)
	image_encodings.append(face_recognition.face_encodings(image)[0])

for image_name in images:

	test_image = face_recognition.load_image_file(f'./img/unknown/{image_name}')
	face_locations = face_recognition.face_locations(test_image)
	face_encodings = face_recognition.face_encodings(test_image, face_locations)

	pil_image = Image.fromarray(test_image)
	draw = ImageDraw.Draw(pil_image)

	for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
		matches = face_recognition.compare_faces(image_encodings, face_encoding)

		name = "Unknown Person"

		if True in matches:
			first_match_index = matches.index(True)
			name = face_names[first_match_index]

		draw.rectangle(((left, top), (right, bottom)), outline=(0,0,255))
		text_width, text_height = draw.textsize(name)
		draw.rectangle(((left, bottom-text_height-10),(right,bottom)), fill=(0,0,255), outline=(0,0,0))
		draw.text((left + 6,bottom-text_height-5), name, fill=(255,255,255,255))

	del draw
	pil_image.show()



