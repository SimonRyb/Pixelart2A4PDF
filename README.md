# Pixelart2A4PDF
Program for extracting pixels from an image and adding it to an A4 PDF to be able to be printed, aswell as a program for downscaling an image

# Dependencies
The program uses the libaries:
  - PIL
  - reportlab
  
 These can be installed by running the following commands in a terminal:
 '''
 pip install PIL
 pip install reportlab
 '''
  
# Example
## Step 1: Choose image and downscale
Decide on a image to downscale, or if you have a pixelated image you can go directly to step 2. The image beeing used will be:
![input_image_star](https://user-images.githubusercontent.com/98055937/222794677-053debc2-56e2-4940-9ecf-f5f2dd5fb663.JPG)
Using the program "Pixelateimage.py" you go into the code and change line #9 where the input image is beeing defined. Importat to know is that the image and the program has to be situated within the same folder to just be able to write the name of the image, otherwise the path also has to be declared. Line #6 can be used to change how much the image is beeing downcaled. 

Using the image above the resulting image became: <br />

![output_image](https://user-images.githubusercontent.com/98055937/222794820-7acd015a-ab54-468f-9cbb-76590e50c786.jpg)

## Step 2: Create PDF
After the pixelated image is created the program "CreatePDF" can be used to extract the pixels from the pixelated image and put them in a A4 PDF to be able to be printed. Where in the code the input and output has to be defined. There are predetermined parameters for the size of the squares that represent the pixels, aswell as how many are beeing printed on each line, these parameters can be changed within the code.

Using the pixaled image from above the reulting PDF looks like: <br />
<img width="339" alt="Screenshot 2023-03-03 at 19 15 22" src="https://user-images.githubusercontent.com/98055937/222796685-c98a0983-d811-481f-b48e-bfc69e811ef8.png">

## Step 3: Print
The PDF can now be printed, the squares can then be cut out and the circles within each square can then be cut out with a hole punch. An example with another image is shown bellow, where the squares were joined with 3d printed clips: <br />
![IMG_7064](https://user-images.githubusercontent.com/98055937/222799324-b5e5531a-2429-4f28-a221-3974332e4562.jpg)
