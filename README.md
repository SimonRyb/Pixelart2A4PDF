# Pixelart2A4PDF
Program for extracting pixels from an image and adding it to an A4 PDF to be able to be printed, aswell as a program for downscaling an image

# Dependencies
The brogram uses the libaries:
  - PIL
  - reportlab
  
# Example
## Step 1: Choose image and downscale
Decide on a image to downscale, or if you have a pixelated image you can go directly to step 2. The image beeing used will be:
![input_image_star](https://user-images.githubusercontent.com/98055937/222794677-053debc2-56e2-4940-9ecf-f5f2dd5fb663.JPG)
Using the program "Pixelateimage.py" you go into the code and change line #9 where the input image is beeing defined. Importat to know is that the image and the program has to be situated within the same folder to just be able to write the name of the image, otherwise the path also has to be declared. Line #6 can be used to change how much the image is beeing downcaled. 

Using the image above the resulting image became:
![output_image](https://user-images.githubusercontent.com/98055937/222794820-7acd015a-ab54-468f-9cbb-76590e50c786.jpg)


