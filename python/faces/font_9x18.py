from bitfont import BitFont
font = BitFont(
	height = 18,
	pixBytes = bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0\xcf\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0\x01\x00\x00\x00\x00\x00x\x00\x00\x00\x00\x00\x00 \x01\x80\x04\xc0\xff\x00H\x00 \x01\xf0?\x00\x12\x00H\x00\x00\x00\x00\x00\x00C\x00\x12\x02\x88\x08\xf0\x7f\x80\x88\x00B\x02\x10\x06\x00\x00\x00\x00\x00\x06\x02$\x06`\x04\x00\x0c\x00\x88\x01\x18\t\x10\x18\x00\x00\x00\x00\x008\x07\x10#@\x8c\x00N\x01\x00\x02\x00\x14\x00\x88\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\x0300 \x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08@\xc0\xc0\x00\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x88\x00@\x01\x00\x02\x00\x7f\x00 \x00@\x01\x80\x08\x00\x00\x00\x00\x00\x00\x02\x00\x08\x00 \x00\xf0\x07\x00\x02\x00\x08\x00 \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xb0\x00\xc0\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00 \x00\x80\x00\x00\x02\x00\x08\x00 \x00\x80\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00 \x00`\x00@\x00\xc0\x00\x80\x00\x80\x01\x00\x01\x00\x00\x00\x00\x00\x00?\x00\x02\x01\x04\x08\x10 @\x80\x00\x02\x01\xf0\x03\x00\x00\x00\x00\x00\x08\x02\x10\x08  \xc0\xff\x00\x00\x02\x00\x08\x00 \x00\x00\x00\x00\x00\x10\x08 0@\xa0\x00A\x02\x84\x08 !\x00\x83\x00\x00\x00\x00\x00\x10\x10@\x80\x00\x01\x02D\x08\x90!@I\x00\xc3\x00\x00\x00\x00\x00\x00\x18\x00P\x00 \x01@\x04\x80\x10\x00\xff\x03\x00\x01\x00\x00\x00\x00\x00\x1f\x01D\x08\x10!@\x84\x00\x11\x02\x84\x04\x10\x0c\x00\x00\x00\x00\x00\xf0\x03 \x12@\x84\x00\x11\x02D\x08\x10\x12\x000\x00\x00\x00\x00\x00\x10\x00@\x00\x00\x01\x00\x04\x0f\x10\x03@\x03\x00\x03\x00\x00\x00\x00\x00\x001\x00*\x01D\x08\x10!@\x84\x00*\x01\x10\x03\x00\x00\x00\x00\x00\x0c\x00H\x08\x10"@\x88\x00!\x02H\x04\xc0\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x03`\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00`,\x80q\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00 \x00@\x01\x80\x08\x00A\x00\x02\x02\x00\x00\x00\x00\x00\x00\x00\x90\x00@\x02\x00\t\x00$\x00\x90\x00@\x02\x00\t\x00\x00\x00\x00\x00\x00\x00  \x00A\x00\x88\x00@\x01\x00\x02\x00\x00\x00\x00\x00\x00\x00@\x00\x80\x00\x00\x01\x00\x04\x0b\x10\x02\x80\x04\x00\x0c\x00\x00\x00\x00\x00\x00?\x00\x02\x01\xe4\tP(@\xbf\x00\x82\x02\xf0\x01\x00\x00\x00\x00\x00\x80\x03\xc0\x01\xe0\x02@\x08\x00.\x00\xc0\x01\x008\x00\x00\x00\x00\x00\xfc\x0f\x10!@\x84\x00\x11\x02D\x08\xa0\x12\x001\x00\x00\x00\x00\x00\xc0\x0f\x80@\x00\x01\x02\x04\x08\x10 @\x80\x00\x02\x01\x00\x00\x00\x00\xc0\xff\x00\x01\x02\x04\x08\x10 @\x80\x00\x02\x01\xf0\x03\x00\x00\x00\x00\x00\xff\x03D\x08\x10!@\x84\x00\x11\x02\x04\x08\x10 \x00\x00\x00\x00\x00\xfc\x0f\x10\x01@\x04\x00\x11\x00D\x00\x10\x00@\x00\x00\x00\x00\x00\x00\xc0\x0f\x80@\x00\x01\x02\x04\x08\x10"\x80H\x00\xe4\x00\x00\x00\x00\x00\xc0\xff\x00\x10\x00@\x00\x00\x01\x00\x04\x00\x10\x00\xfc\x0f\x00\x00\x00\x00\x00\x00\x00\x04\x08\x10 \xc0\xff\x00\x01\x02\x04\x08\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00 @\x80\x00\x01\x02\xfc\x07\x10\x00@\x00\x00\x00\x00\x00\x00\xf0?\x00\x08\x00\x10\x00\xa0\x00@\x04\x80 \x00\x01\x03\x00\x00\x00\x00\xc0\xff\x00\x00\x02\x00\x08\x00 \x00\x80\x00\x00\x02\x00\x08\x00\x00\x00\x00\x00\xff\x03\x10\x00\x80\x00\x00\x04\x00\x08\x00\x10\x00\xf0?\x00\x00\x00\x00\x00\xfc\x0f@\x00\x00\x02\x00\x10\x00\x80\x00\x00\x04\xc0\xff\x00\x00\x00\x00\x00\xe0\x1f@\x80\x00\x01\x02\x04\x08\x10 @\x80\x00\xfe\x01\x00\x00\x00\x00\xc0\xff\x00!\x00\x84\x00\x10\x02@\x08\x00\x12\x000\x00\x00\x00\x00\x00\x00\xfc\x00\x08\x04\x10 @\x80\x00\x81\x02\x08\x04\xc0/\x00\x00\x01\x00\x00\xfc\x0f\x10\x02@\x08\x00a\x00\x84\x02 \x11\x00\x83\x00\x00\x00\x00\x00\xe0\x10@\x84\x00\x11\x02D\x08\x10!@\x84\x00\xe2\x01\x00\x00\x00\x00@\x00\x00\x01\x00\x04\x00\xf0?@\x00\x00\x01\x00\x04\x00\x00\x00\x00\x00\x00\xff\x00\x00\x04\x00 \x00\x80\x00\x00\x02\x00\x04\xf0\x0f\x00\x00\x00\x00\x00\x1c\x00\x80\x03\x00p\x00\x00\x02\x00\x07\x80\x03\xc0\x01\x00\x00\x00\x00\x00\xf0\x1f\x00\x80\x00\x00\x01\xc0\x03\x00\x10\x00\x80\x00\xff\x01\x00\x00\x00\x00\xc0\xc0\x00\x84\x00 \x01\x00\x03\x00\x12\x00\x84\x00\x0c\x0c\x00\x00\x00\x00\x00\x03\x00\x10\x00\x80\x00\x00\xfc\x00\x08\x00\x10\x000\x00\x00\x00\x00\x00\x00\x04\x0e\x10$@\x88\x00\x11\x02$\x08P \xc0\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xff\x07\x02\x10\x08@ \x00\x01\x00\x00\x00\x00\x00\x00@\x00\x00\x06\x00 \x00\x00\x03\x00\x10\x00\x80\x01\x00\x08\x00\x00\x00\x00\x00\x00\x00\x02\x10\x08@ \x00\x81\xff\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00 \x00@\x00\x80\x00\x00\x01\x00\x08\x00@\x00\x00\x02\x00\x00\x00\x00\x10\x00@\x00\x00\x01\x00\x04\x00\x10\x00@\x00\x00\x01\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\x00\x04\x00 \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x01 \t\x80$\x00\x92\x00H\x02 \x05\x00?\x00\x00\x00\x00\x00\xfc\x0f\x00\x11\x00\x82\x00\x08\x02 \x08\x80 \x00|\x00\x00\x00\x00\x00\x00\x1f\x00\x82\x00\x08\x02 \x08\x80 \x00\x82\x00\x10\x01\x00\x00\x00\x00\x00|\x00\x08\x02 \x08\x80 \x00\x82\x00\x10\x01\xfc\x0f\x00\x00\x00\x00\x00\xf0\x01 \t\x80$\x00\x92\x00H\x02 \t\x00\x17\x00\x00\x00\x00\x00\x80\x00\x00\x02\x80\xff\x00!\x00\x84\x00\x10\x00\x80\x01\x00\x00\x00\x00\x00\x00\xd7\x00\xa2\x04\x88\x12 J\x80(\x01\x9c\x04\x08\x0c\x00\x00\x00\x00\xc0\xff\x00\x10\x00 \x00\x80\x00\x00\x02\x00\x08\x00\xc0\x0f\x00\x00\x00\x00\x00\x00\x00 \x08\x90 @\xfe\x00\x00\x02\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\x00\x04\x08\x10$@\x90\xff\x00\x00\x00\x00\x00\x00\x00\xf0?\x00 \x00@\x00\x80\x01\x00\t\x00B\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x01\x02\x04\x08\xf0?\x00\x80\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\xf8\x03 \x00\x80\x00\x00|\x00\x08\x00 \x00\x00?\x00\x00\x00\x00\x00\xe0\x0f\x00\x01\x00\x02\x00\x08\x00 \x00\x80\x00\x00\xfc\x00\x00\x00\x00\x00\x00\x1f\x00\x82\x00\x08\x02 \x08\x80 \x00\x82\x00\xf0\x01\x00\x00\x00\x00\x00\xfe\x07\x10\x01 \x08\x80 \x00\x82\x00\x10\x01\x80\x03\x00\x00\x00\x00\x00\xe0\x00@\x04\x80 \x00\x82\x00\x08\x02@\x04\x80\xff\x01\x00\x00\x00\x00 \x00\x00?\x00\x04\x00\x08\x00 \x00\x80\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x13\x00\x92\x00H\x02 \t\x80$\x00\x92\x00\x90\x01\x00\x00\x00\x00\x00\x02\x00\x08\x00\xf8\x07\x80 \x00\x82\x00\x08\x02\x00\x04\x00\x00\x00\x00\x00\xf8\x01\x00\x08\x00 \x00\x80\x00\x00\x02\x00\x04\x80?\x00\x00\x00\x00\x00`\x00\x00\x06\x00`\x00\x00\x02\x00\x06\x00\x06\x00\x06\x00\x00\x00\x00\x00\x80\x1f\x00\x80\x00\x00\x01\x80\x03\x00\x10\x00\x80\x00\xf8\x01\x00\x00\x00\x00\x00\x82\x00\x10\x01\x80\x02\x00\x04\x00(\x00\x10\x01 \x08\x00\x00\x00\x00\x00\x00\x08`@\x00\x0e\x01\xc0\x03\x00\x03\x80\x03\x80\x01\x00\x00\x00\x00\x00 \x08\x800\x00\xa2\x00H\x02\xa0\x08\x80!\x00\x82\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x10\x00\xbc\x07\x08  \x80\x80\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf8\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\x02\x02\x08\x08 \xc0{\x00\x10\x00@\x00\x00\x00\x00\x00\x00\x00\x00\x18\x00\x10\x00@\x00\x00\x02\x00\x10\x00@\x00\xc0\x00\x00\x00\x00'),
	endCols = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 108, 117, 126, 135, 144, 153, 162, 171, 180, 189, 198, 207, 216, 225, 234, 243, 252, 261, 270, 279, 288, 297, 306, 315, 324, 333, 342, 351, 360, 369, 378, 387, 396, 405, 414, 423, 432, 441, 450, 459, 468, 477, 486, 495, 504, 513, 522, 531, 540, 549, 558, 567, 576, 585, 594, 603, 612, 621, 630, 639, 648, 657, 666, 675, 684, 693, 702, 711, 720, 729, 738, 747, 756, 765, 774, 783, 792, 801, 810, 819, 828, 837, 846, 855]
)