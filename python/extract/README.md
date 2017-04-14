This folder can be used to process .bdf files into .py modules containing a single bitfont, full alphabet pngs or per-character pngs for a typeface.

First, the pilfont utility from PIL (Pillow Fork) should be used to generate .pil and .pbm files extracting the typefaces into a PIL-compatible format, and they should be placed in this folder.

If you cd to the python folder in this repository and run python -m extract a font_XXX.py file containing a python BitFont will be authored in the 'faces' folder, providing rendering logic for that font.

These font_XXX.py files can be used in projects to plot the typefaces using an arbitrary x,y renderer.
