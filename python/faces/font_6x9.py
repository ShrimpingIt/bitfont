from bitfont import BitFont
font = BitFont(
	height = 9,
	pixBytes = bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00^\x00\x00\x00\x00\xc0\x01\x00\x07\x00\x00\xa0\xf0\x87\xc2\x1f\n\x00L$\xfd\x97D\x06\x80\x802\x12\x90\x98\x02\xc2F\x92$6\xa0\x00\x00\x00\xe0\x00\x00\x00\x00\x00\x00\xf0\x11\x04\x00\x00\x00\x00\x82\xf8\x00\x00@\x05\x07\x04\x1cT\x00@\x80\xc0\x07\x02\x04\x00\x00\x00\x80\x04\x07\x00\x00\x04\x08\x10 @\x00\x00\x00\x00\x180\x00\x00\x00\x00\x03\x01\x81\x01\x00\x00x\x08\x11\xc2\x03\x00\x00"~\x80\x00\x00\x00\x80\x88\x18)L\x00\x00\x10\xa2\xc4\x89\x0c\x000P\x90\xf0\x03\x02\x00\x00\'J\x94\xc8\x00\x00\x80\x87\x12%0\x00\x00\x10 F\x82\x03\x00\x00h(QB\x03\x00\x00\x06R\xa4\xf0\x00\x00\x00\x00\x1b6\x00\x00\x00\x00\xc0\x92\x1d\x00\x00\x10P\xa0 B\x04\x00\n\x14(P\xa0\x00@\x84\x08\n\x14\x10\x00\x00\x10\x90%\x81\x01\x00<\x84h\xb1\x82\x00\x00\x1e\n\x12(\xe0\x01\xe0G\x89\x12%4\x00\x00\xe0!D\x08\t\x00\x00\xfc\x08\x11\xc2\x03\x00\x00?J\x94\x08\x01\x00\xc0\x8f\x02\x05\x02\x00\x00\xe0!D\n\r\x00\x00\xfc @\xe0\x07\x00\x00!~\x84\x00\x00\x00\x02\x88\x10\x1f\x02\x00\x00\xf0\x83\x80\x82\x18\x00\x00\xfc\x00\x01\x02\x04\x80\x1f\x02\x18\x08\xf8\x01\x00\xc0\x0f\x01\x04~\x00\xf0\x10"D\x08\x0f\x00\x00\xfcH\x90\xc0\x00\x00\x00\x1eR\xc4\xf0\x02\x00\xc0\x8f\x04\tl\x00\x00 \xa1D\n\t\x00\x02\x04\xf8\x11 \x00\x00\x00\x1f@\x80\xf8\x00\x00\xc0\x03\x1c8\x1e\x00\xf8\x01\x81\x01\x84\x1f\x00BH` !\x04\x80\x01\x04p\x10\x18\x00\x00@\x8c\x14%F\x00\x00\xf0#D\x08\x00\x00\x00\x0c \x80\x00\x06\x00\x00!B\xfc\x00\x00\x80\x80\x80\x00\x02\x08\x00\x00\x04\x08\x10 @\x00\x00\x00\x08 \x00\x00\x00\x00\x18H\x90\xe0\x01\x00\xc0\x0f\x12$0\x00\x00\x80\x81\x04\t\x12\x00\x00` A\xe2\x07\x00\x00\x18h\xb0@\x01\x00\x00\x02\x1f\t\x04\x00\x00\x80\x81\x14)<\x00\x00\xfc @\x00\x07\x00\x00$z\x80\x00\x00\x00\x00\x10B}\x00\x00\x00\xf0\x03\x01\x05\x10\x00\x00\x84\xf8\x01\x02\x00\x00\x1e\x040\x10\xc0\x01\x00\x00\x0f\x02\x04p\x00\x00\x80\x81\x04\t\x0c\x00\x00\xf0#A\x02\x03\x00\x00\x18H\x90\xe0\x07\x00\x00\x0f\x04\x04\x10\x00\x00\x80\x82\x05\r\n\x00\x00\x10\xf8@\x02\x02\x00\x00\x1c@\x80\xe0\x01\x00\x00\x03\x180\x18\x00\xe0\x00\x02\x03\x08\x0e\x00\x00\x90\xc0\x80\x81\x04\x00\x00\\@\x81\xe2\x03\x00\x00\t\x1a,H\x00\x00@`#\x08\x00\x00\x00\x00\xf8\x03\x00\x00\x00\x80 6\x10\x00\x00\x00\x00\x01\x01\x04\x04\x00\x00'),
	endCols = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96, 102, 108, 114, 120, 126, 132, 138, 144, 150, 156, 162, 168, 174, 180, 186, 192, 198, 204, 210, 216, 222, 228, 234, 240, 246, 252, 258, 264, 270, 276, 282, 288, 294, 300, 306, 312, 318, 324, 330, 336, 342, 348, 354, 360, 366, 372, 378, 384, 390, 396, 402, 408, 414, 420, 426, 432, 438, 444, 450, 456, 462, 468, 474, 480, 486, 492, 498, 504, 510, 516, 522, 528, 534, 540, 546, 552, 558, 564, 570]
)