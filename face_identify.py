import face_recognition
from PIL import Image, ImageDraw

image_1 = face_recognition.load_image_file('./img/known/Barack Obama.jpg')
image_encoding_1 = face_recognition.face_encodings(image_1)[0]

image_2 = face_recognition.load_image_file('./img/known/Bill Gates.jpg')
image_encoding_2 = face_recognition.face_encodings(image_2)[0]

image_3 = face_recognition.load_image_file('./img/known/Donald Trump.jpg')
image_encoding_3 = face_recognition.face_encodings(image_3)[0]

image_4 = face_recognition.load_image_file('./img/known/Elon Musk.jpg')
image_encoding_4 = face_recognition.face_encodings(image_4)[0]

image_5 = face_recognition.load_image_file('./img/known/Michael Jordan.jpg')
image_encoding_5 = face_recognition.face_encodings(image_5)[0]

image_6 = face_recognition.load_image_file('./img/known/Steve Jobs.jpg')
image_encoding_6 = face_recognition.face_encodings(image_6)[0]


known_face_encodings = [
	image_encoding_1, image_encoding_2, image_encoding_3, image_encoding_4, image_encoding_5, image_encoding_6
]

known_face_names = [
	"Barack Obama","Bill Gates","Donald Trump","Elon Musk","Michael Jordan","Steve Jobs"
]

test_image = face_recognition.load_image_file('./img/groups/bill-steve-elon.jpg')

face_locations = face_recognition.face_locations(test_image)
face_encodings = face_recognition.face_encodings(test_image, face_locations)


pil_image = Image.fromarray(test_image)
draw = ImageDraw.Draw(pil_image)

for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
	matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

	name = "Unknown Person"

	if True in matches:
		first_match_index = matches.index(True)
		name = known_face_names[first_match_index]

	draw.rectangle(((left, top), (right, bottom)), outline=(0,0,255))
	text_width, text_height = draw.textsize(name)
	draw.rectangle(((left, bottom-text_height-10),(right,bottom)), fill=(0,0,255), outline=(0,0,0))
	draw.text((left + 6,bottom-text_height-5), name, fill=(255,255,255,255))

del draw

pil_image.show()

