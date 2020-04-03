import pygame
import tensorflow as tf
from tensorflow import keras
import numpy as np




data = keras.datasets.mnist
(train_images, train_labels), (test_images, test_labels) = data.load_data()


train_images = train_images/255.0
test_images = test_images/255.0
train_images = train_images//0.51
test_images = test_images//0.51

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28,28)),
    keras.layers.Dense(128, activation="relu"),
    keras.layers.Dense(10, activation="softmax")
    ])

model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
model.fit(train_images, train_labels, epochs=9)




width = 280
height = 280
win = pygame.display.set_mode((width, height))
canvasList = []
for x in range(0, height // 10):
    canvasList.append([])
    for y in range(0, width // 10):
        canvasList[x].append(0)
canvasList_old = canvasList
pygame.display.set_caption("Canvas")
whiteColour = (255, 255, 255)
blackColour = (0, 0, 0)
win.fill(whiteColour)
pygame.display.flip()
def predict():
    prediction = model.predict([canvasList])
    prediction = np.argmax(prediction[0])
    print(prediction)

def neighbours(win, x, y):

    if x == 0:
        draw(win, blackColour, x, y)
        draw(win, blackColour, x+10, y)
    elif x >= 270:
        draw(win, blackColour, x-10, y)
        draw(win, blackColour, x, y)
    elif x > 0:
        draw(win, blackColour, x - 10, y)
        draw(win, blackColour, x, y)
        draw(win, blackColour, x + 10, y)


def rndLower(num, nearest=10):
    p = num // 10
    dif = num - p * 10
    return num - dif
def draw(win, colour, x, y):
    pygame.draw.rect(win, colour, [x, y, 10, 10])
    canvasList[y//10][x//10] = 1

    pygame.display.update()

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif pygame.mouse.get_pressed()[0]:
                (mouseX, mouseY) = pygame.mouse.get_pos()
                mouseX = rndLower(mouseX)
                mouseY = rndLower(mouseY)
                neighbours(win, mouseX, mouseY)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    predict()

main()