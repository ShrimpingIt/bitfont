from bitfont import BitFont
font = BitFont(
	height = 13,
	pixBytes = bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0\xc2\x03\x00\x00\x00\x00\x00\x00\x00\x00p\x00\x00\x00\x008\x00\x00\x00\x00\x80\x00t\xe0\x03P\x00:\xf0\x01\x08\x00\x00\x00\x00@\xc0\x08\xe4\xc3\'\x90\x03\x02\x00\x00\x00\x06!P\x02$\x01R \x04\x03\x00\x00\x00\x00`\x00\x128\x82,P\x06$\x01\x00\x00\x00\x00\x00\x00\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x98\x81@\x08\x00\x00\x00\x00\x00\x00\x00\x00\x10\x02\x81\x19\xc0\x00\x00\x00\x00\x00\x00(@\x03p\x00\x16\xa0\x00\x10\x00\x00\x00\x00\x08\x00\x078\x00\x04\x80\x00\x00\x00\x00\x00\x00\x00\x00 \x00\x03`\x00\x04\x00\x00\x00\x00\x00\x08\x00\x01 \x00\x04\x80\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x07@\x00\x00\x00\x00\x00\x00\x06 \x00\x02 \x00\x04@\x00\x04`\x00\x80\x01N \x10\x02B \x10\x03\x1c\x00\x00\x00\x00\x80@\x10\xc4\xc3G\x00\x08\x00\x00\x00\x00\x06\xa3\x10\x12BBD\x88\x08\x0e\x00\x00\x00\x82\x80\x10\x10"BF(\x07\x03\x00\x00\x00\x000\x00\x05\x90\x00q\x90\x03O\x00\x00\x00\x02\x8cp\x11\x12BBH\x061\x00\x00\x80\x03\x8e \x11"BD\x08\x07\x02\x00\x00\x00\x80\xc0\x10\x06"@\x02(\x00\x03\x00\x00\x80\x03\x8f\x10\x11"BD\x88\x07\x0e\x00\x00\x00\x00\x87\x10\x11"B$H\x03\x1e\x00\x00\x00\x00\x00\x00\x10\x10\x07G@\x00\x00\x00\x00\x00\x00\x00\x01\x18\x10\x03\'@\x00\x00\x00\x00\x00\x00\x18\x80\x04\x08\x81@\x08\x00\x00\x00\x00\x00\x01$\x80\x04\x90\x00\x12@\x02\x08\x00\x00\x00\x00\x80\x10\x08\x84\x00\t\xc0\x00\x00\x00\x00\x00\x00\x02 \x00\xc2B\x04H\x00\x06\x00\x00\x80\x03\x8f\x10\x12\xa2BRH\x01>\x00\x00\x80\x07\x1e \x02B@\x08\x10\x0f\x1c\x00\x00\x80\x87\x8f\x10\x11"B,P\x02\x04\x00\x00\x80\x03\x8f\x10\x10\x02B@\x08\x04\x02\x00\x00\x80\x87\x8f\x10\x10\x02B \x10\x03\x1c\x00\x00\x80\x87\x8f\x10\x11"BD\x08\x08\x01\x00\x00\x80\x87\x0f\x10\x01"@\x04\x08\x00\x01\x00\x00\x80\x03\x8f\x10\x10BB(\x08\x0f\x02\x00\x00\x80\x87\x0f\x00\x01 \x00\x04\x80\x0f\x0f\x00\x00\x00\x00\x80\x10\x10\xc2\xc3G\x08\x08\x01\x00\x00\x00\x02\x80\x00\x10\x02B8\xf8\x00\x01\x00\x00\x80\x87\x0f\x00\x03\x90\x00!\x10\x08\x01\x00\x00\x00\x00\xf0\xf0\x11\x00\x02@\x00\x08\x00\x01\x00\x80\x87\x0f@\x00\x10\x00\x04@\x00\xe4\xe1\x03\x80\x87\x0f@\x00\x10\x00\x0c\x00\x0f\x1f\x00\x00\x80\x03\x8f\x10\x10\x02B@\x08\x07\x1e\x00\x00\x80\x87\x0f\x10\x01"@\x04\x88\x00\x0e\x00\x00\xc0\x03\x87\x10\x14\x02C@\x88\x17\x0e\x00\x00\x80\x87\x0f\x10\x03\xa2@$\x88\x08\x0e\x00\x00\x00\x02\x87\x10\x11"BD\x08\x07\x02\x00\x00\x04\x80\x00\x10\x1e>@\x00\x08\x00\x01\x00\x00\xc0\x83\x87\x00\x10\x00\x02@\x80\x07\x0f\x00\x00\x1c\x00|\x00\x10\x80\x01\x0c`\x00\x03\x00\x00\x80\x83\x8f\x00\x08\xc0\x00$\x00\x08\xe0\xe0\x03\x00\x86!@\x020\x00\x0c@\x02\x84a\x00\x0c\x00\x02\x80\x1c`\x00\x02 \x00\x03\x00\x00\x00\x86\xa0\x10\x12"BB(\x08\x03\x00\x00\x00\x00\xf0\xf0\x11\x02B@\x08\x00\x00\x00\x00\x00\x80\x01@\x00\x10\x00\x0c\x00\x02\x80\x01\x00\x00\x00\x80\x10\x10\x02Bx\xf8\x00\x00\x00\x00\x00\x00\x02 \x00\x02\x80\x00 \x00\x00\x00\x00\x00\x08\x00\x01 \x00\x04\x80\x00\x10\x00\x02\x00\x00\x00\x00\x00\x00\x01@\x00\x00\x00\x00\x00\x00\x00\x03\x90\x80\x12P\x02*@\x0f\x10\x00\x00\x00\x87_\x00\x11\x10\x02B@\x060\x00\x00\x80\x03\x88\x80\x10\x10\x02B@\x04\x10\x00\x00\x80\x03\x88\x80\x10\x10\x02"\x80\x0f\x0f\x00\x00\x00\x03\x98\x80\x12P\x02J@\x05\x10\x00\x00\x00\x00\xe8\xe0\x03"@\x04\x88\x00\x02\x00\x00\x80\n\xa8\x82T\x90\nJ\x81\x10\x08\x00\x00\x00\x07\x1e0\x01\x10\x00\x02@\x0e0\x00\x00\x00\x00\x80\x00\x10\x90\x83N\x00\x08\x00\x00\x00\x00\x00\x80\x01@\x00\x08\x00A\x1e:\x00\x00\x00\x00\xe0\xf0\x03@\x00\x14\x80\x04\x08\x01\x00\x00\x00\x80\x00\x10\xc2\xc3G\x00\x08\x00\x00\x00\x00\x07\x1c\x80\x00\x90\x01\x0c@\x00\xc8\x01\x06\x00\x07\x1c\x00\x01\x10\x00\x02@\x0e0\x00\x00\x00\x03\x98\x80\x10\x10\x02B@\x060\x00\x00\x00\x18\xe0\x80\x07 \x01"@\x04H\x00\x06\x80\x01H\x80\x08\x10\x01\x92\x81\x0f\x18\x00\x00\x00\x00\xe4\x00\x03\x10\x00\x02@\x00\x10\x00\x00\x00\x02\x88\x80\x12\x90\x02R@\x04\x10\x00\x00\x00\x00t\xe0\x11\x10\x02B@\x04\x00\x00\x00\x00\x00`\x80\x13\x00\x02@\x00\x068\x01\x00\x00\x00|\x00\x10\x80\x01\x08\xc0\x00\x00\x00\x00\x80\x03\x8c\x00\x08\xc0\x00 \x00\x08\xe0\x00\x03\x00\x04D\x00\x05\xc0\x00(\x80\x08\x08\x00\x00\x80\tL\x02H\x00\t\x10\x01\x1f\x18\x00\x00\x00\x04\xc4\x80\x14P\x02J\xc0\x08\x08\x00\x00\x00\x00h`\x13\x12B@\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\xc3\x07\x00\x00\x00\x00\x00\x00\x00\x80\x10\x10BB6\xb0\x00\x00\x00\x00\x00\x00\x03\x10\x00\x04\x00\x01\x18\x00\x00\x00\x00'),
	endCols = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160, 168, 176, 184, 192, 200, 208, 216, 224, 232, 240, 248, 256, 264, 272, 280, 288, 296, 304, 312, 320, 328, 336, 344, 352, 360, 368, 376, 384, 392, 400, 408, 416, 424, 432, 440, 448, 456, 464, 472, 480, 488, 496, 504, 512, 520, 528, 536, 544, 552, 560, 568, 576, 584, 592, 600, 608, 616, 624, 632, 640, 648, 656, 664, 672, 680, 688, 696, 704, 712, 720, 728, 736, 744, 752, 760]
)