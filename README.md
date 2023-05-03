# Dalgona Squid Game 🔺⭐🔴

## Python implementation of the Dalgona Game using hand tracking from MediaPipe

This project was built to show some use cases for computer vision (including hand landmarks and gamification) using
OpenCV. It's a simple game that you play using the camera of your computer and your fingers to control/cut the cookie.

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