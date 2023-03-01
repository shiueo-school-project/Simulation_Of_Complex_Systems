import math

import glfw

from utils import texture, global_variables
from utils.set_variables import APPLY, RESOURCES_X_POS, RESOURCES_Y_POS, A_X_POS, A_Y_POS, A_X_RETURN, A_Y_RETURN, \
    B_X_POS, B_Y_POS


def draw(white_box, red_box, blue_box, green_box):
    if global_variables.get_var(APPLY):
        Resource_X = list(map(float, global_variables.get_var(RESOURCES_X_POS).split()))
        Resource_Y = list(map(float, global_variables.get_var(RESOURCES_Y_POS).split()))
        # print(Resource_X, Resource_Y)
        for i in range(len(Resource_X)):
            texture.drawImage(
                centerX=Resource_X[i],
                centerY=Resource_Y[i],
                textureID=green_box,
                ratio=0.1,
            )

        A_X = list(map(float, global_variables.get_var(A_X_POS).split()))
        A_Y = list(map(float, global_variables.get_var(A_Y_POS).split()))
        # print(A_X, A_Y)

        for j in range(len(A_X)):
            texture.drawImage(
                centerX=A_X[j],
                centerY=A_Y[j],
                textureID=white_box,
                ratio=0.1,
            )

        B_X = list(map(float, global_variables.get_var(B_X_POS).split()))
        B_Y = list(map(float, global_variables.get_var(B_Y_POS).split()))
        # print(B_X, B_Y)
        print(len(A_X))

        for j in range(len(B_X)):
            texture.drawImage(
                centerX=B_X[j],
                centerY=B_Y[j],
                textureID=red_box,
                ratio=0.1,
            )
    else:
        pass

def sans(white_box, red_box, blue_box, green_box):
    if global_variables.get_var(APPLY):
        Resource_X = list(map(float, global_variables.get_var(RESOURCES_X_POS).split()))
        Resource_Y = list(map(float, global_variables.get_var(RESOURCES_Y_POS).split()))
        #print(Resource_X, Resource_Y)
        for i in range(len(Resource_X)):
            texture.drawImage(
                centerX=Resource_X[i],
                centerY=Resource_Y[i],
                textureID=green_box,
                ratio=0.1,
            )

        A_X = list(map(float, global_variables.get_var(A_X_POS).split()))
        A_Y = list(map(float, global_variables.get_var(A_Y_POS).split()))
        #print(A_X, A_Y)

        for j in range(len(A_X)):
            texture.drawImage(
                centerX=A_X[j],
                centerY=A_Y[j],
                textureID=white_box,
                ratio=0.1,
            )

        B_X = list(map(float, global_variables.get_var(B_X_POS).split()))
        B_Y = list(map(float, global_variables.get_var(B_Y_POS).split()))
        #print(B_X, B_Y)
        print(len(A_X))

        for j in range(len(B_X)):
            texture.drawImage(
                centerX=B_X[j],
                centerY=B_Y[j],
                textureID=red_box,
                ratio=0.1,
            )
    else:
        pass