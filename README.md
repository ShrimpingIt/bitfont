# bitfont

Renderer-agnostic pixel fonts for python3, sourced by @olikraus for u8g2, 
ported by @ShrimpingIt 

Implement a function with the signature ```plot(x,y)``` 
to use this bitfont library in your preferred rendering environment.

To run a test render using PIL (Pillow Fork), install pillow from pip3
then try cd-ing to the repository's ```python``` folder in a console 
and run...

```python -m render.pillow```

You should find bitmap-rendered file ```pillow.png``` in the 
python/render folder.

Edit the run() function in python/render/pillow.py to change the configuration 
of the test render.

P.S. See original bdf typefaces at https://github.com/cefn/u8g2/tree/master/tools/font/bdf
