import playsound as ps
import mediapipe as mp
import cvzone as cvz
import pygame as pg
import numpy as np
import cv2 as cv
import random
import time


width, height = 1280, 720


def main():
    names_mark = ["Images/circle_mark.png", "Images/square_mark.png", "Images/star_mark.png"]

    names = ["Images/circle.png", "Images/square.png", "Images/star.png", "Images/circle_crack.png",
             "Images/square_crack.png", "Images/star_crack.png"]

    num_form = random.randint(0, 2)

    start = False

    pg.init()

    line = cont_line = error = 0

    cookie_img = cv.imread(names_mark[num_form])

    cookie_img_exit = cv.imread(names[num_form])

    cookie_img_exit_crack = cv.imread(names[num_form + 3])

    blood_img = cv.imread("Images/blood.png")

    blood_img = cv.resize(blood_img, (1280, 720))

    mat_mark = np.zeros((1280, 720), dtype=int)

    for x in range(0, 1280):
        for y in range(0, 720):
            if ((cookie_img[y][x][0] == 0) and (cookie_img[y][x][1] == 0) and (cookie_img[y][x][2] == 0)):
                mat_mark[x][y] = 1
                line += 1

    line -= 100
    print(mat_mark)
    y_middle_finger = 0
    x_indicador = 0
    y_indicador = 0
    positions = {}

    timestart = time.time()
    totaltime = 200

    cap = cv.VideoCapture(0)
    cap.set(3, 1280)
    cap.set(4, 720)

    mpHands = mp.solutions.hands
    hands = mpHands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.80,
                          min_tracking_confidence=0.80)
    mpDraw = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles

    while True:

        if cv.waitKey(1) == ord('q'):
            break

        sucess, frame = cap.read()
        frame = cv.flip(frame, 1)

        imgRGB = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        results = hands.process(imgRGB)

        if time.time() - timestart < totaltime and cont_line <= line and error < 2:

            if results.multi_hand_landmarks:

                for handLms in results.multi_hand_landmarks:

                    for id, lm in enumerate(handLms.landmark):

                        cx, cy = int(lm.x * width), int(lm.y * height)
                        positions[id] = (cx, cy)

                        if id == 12:
                            y_middle_finger = cy

                        elif id == 8:
                            x_indicador = cx
                            y_indicador = cy

                        if (y_middle_finger - y_indicador) >= 30:

                            if (mat_mark[x_indicador][y_indicador] == 1):
                                for i in range(-10, 10):
                                    for j in range(-10, 10):
                                        if (mat_mark[x_indicador + j][y_indicador + i] == 1):
                                            start = True
                                            mat_mark[x_indicador + j][y_indicador + i] = 2
                                            cv.line(cookie_img_exit, (x_indicador + j, y_indicador + i),
                                                    (x_indicador + j, y_indicador + i), (0, 255, 0), 1)
                                            cv.line(cookie_img_exit_crack, (x_indicador + j, y_indicador + i),
                                                    (x_indicador + j, y_indicador + i), (0, 255, 0), 1, )
                                            cont_line += 1

                            elif (mat_mark[x_indicador][y_indicador] == 2):
                                start = True

                            elif ((cookie_img[y_indicador][x_indicador][0] == 0) and (
                                    cookie_img[y_indicador][x_indicador][1] == 0) and (
                                          cookie_img[y_indicador][x_indicador][2] == 255) and start == True):
                                ps.playsound('Sounds/crack.wav', False)
                                cookie_img_exit = cookie_img_exit_crack
                                start = False
                                error += 1

                            cv.circle(frame, (x_indicador, y_indicador), 8, (0, 0, 255), -1)

            exit = cv.addWeighted(frame, 0.2, cookie_img_exit, 0.8, 0)
            cvz.putTextRect(exit, f'{int(totaltime - (time.time() - timestart))}', [1080, 75], colorR=(0, 0, 0),
                            scale=3, offset=20)
            cv.imshow("Dalgona", exit)

        elif cont_line > line:
            ps.playsound("Sounds/win.mp3", False)
            exit = cv.addWeighted(frame, 0.2, cookie_img_exit, 0.8, 0)
            cvz.putTextRect(exit, f'YOU WIN', (480, 400), scale=5, colorR=(32, 165, 218), offset=30, thickness=7)
            cv.imshow("Dalgona", exit)
            if cv.waitKey(0) == ord('q'):
                break

        else:
            ps.playsound("Sounds/gum_shot.wav", False)
            exit = cv.addWeighted(frame, 0.2, blood_img, 0.8, 0)
            cvz.putTextRect(exit, f'GAME OVER', (400, 400), scale=5, colorR=(0, 0, 0), offset=30, thickness=7)
            cv.imshow("Dalgona", exit)
            if cv.waitKey(0) == ord('q'):
                break

    cap.release()
    cv.destroyAllWindows()
    exit()


if __name__ == '__main__':
    main()
