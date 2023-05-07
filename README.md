# Dalgona Squid Game 🔺⭐🔴

## Python implementation of the Dalgona Game using hand tracking from MediaPipe

This project was built to show some use cases for computer vision (including hand landmarks and gamification) using
OpenCV. It's a simple game that you play using the camera of your computer and your fingers to control/cut the cookie.  
You can leave the cutting area (black line) once, then you crack the cookie, if the user leaves again, GAME OVER!

There are three types of shapes/images: square, circle and star 
![square](https://user-images.githubusercontent.com/121193399/236656378-7a0c917d-d2fd-42da-8e5a-31ba9c3f49f2.png)
![circle](https://user-images.githubusercontent.com/121193399/236656370-f79d69d2-3320-4f24-aed3-507c440a82c6.png)
![star](https://user-images.githubusercontent.com/121193399/236656382-fb5edbe7-37f2-423a-88dd-1e21ccf567f1.png)

It is necessary to identify where the user can cut or not, so you will need to draw the marks in each image or use 
the following ones (*you can make the game harder by drawing the marks closer to the black line*):
![square_mark](https://user-images.githubusercontent.com/121193399/236657590-36967142-5e20-4f9e-8dc6-ae709b1e015b.png)
![circle_mark](https://user-images.githubusercontent.com/121193399/236657582-8156854c-81ea-45f4-b539-6f16b65870c6.png)
![star_mark](https://user-images.githubusercontent.com/121193399/236657576-3bcf799f-79e6-4f24-acce-60103b246d9e.png)

And we also have the cracked images to identify when the user leave the cutting area:
![square_crack](https://user-images.githubusercontent.com/121193399/236657753-daa5c0b3-46c2-45d1-bb0f-ddc79fc84d7a.png)
![circle_crack](https://user-images.githubusercontent.com/121193399/236657761-237060b2-9e10-475a-8838-3f40ffd59829.png)
![star_crack](https://user-images.githubusercontent.com/121193399/236657762-d358a01c-d62d-4fb4-8bcb-5bd2eff8449f.png)

Important Libraries:
* OpenCV - read and resize images, acess camera...
* CVZone - insert text (game interface)
* MediaPipe - detect and track hands/fingers
* Playsound - play some sounds that have been used (that's not essential)

## User Instructions

**Note:** If your computer doesn't have an in-built webcam, certain changes need to be done in the code.  
The code at line 53 in main.py will have to be changed from:

   *cap = cv2.VideoCapture(0)*
   
   to 
   
   *cap = cv2.VideoCapture(1)*

This will hopefully allow the external camera to work.

## Authors
* Bernardo Aires de Oliveira
  * https://www.linkedin.com/in/bernardoaires/
* Daniel Machado Pedrozo
    * https://www.linkedin.com/in/daniel-machado-pedrozo-9357b6244/
* Luís Ricardo Lima
* Marcelo Henrique Alves
  * https://www.linkedin.com/in/marcelo-henrique-alves-pereira-sobrinho-7bb0711b8/
