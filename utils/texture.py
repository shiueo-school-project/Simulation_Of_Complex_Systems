from utils import image, global_variables
from OpenGL.GL import *

from utils.set_variables import SIM_ASPECT_X, SIM_ASPECT_Y

global texx


def loadTexture(texture: str):
    global texx
    try:
        texx = image.load(texture)
    except IOError as e:
        print("Failed to open texture file: ", texture)

    texxData = list(texx.getdata())
    texxID = glGenTextures(1)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    glBindTexture(GL_TEXTURE_2D, texxID)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_BORDER)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_BORDER)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_BASE_LEVEL, 0)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAX_LEVEL, 0)
    glTexImage2D(
        GL_TEXTURE_2D,
        0,
        GL_RGBA,
        texx.size[0],
        texx.size[1],
        0,
        GL_RGBA,
        GL_UNSIGNED_BYTE,
        texxData,
    )
    texx.close()
    return texxID, texx.size[0], texx.size[1]


def drawImage(centerX: float, centerY: float, textureID, ratio: float):
    ASPECT_X = global_variables.get_var(SIM_ASPECT_X)
    ASPECT_Y = global_variables.get_var(SIM_ASPECT_Y)
    verts = (
        (ratio / ASPECT_X, ratio / ASPECT_Y),
        (ratio / ASPECT_X, -ratio / ASPECT_Y),
        (-ratio / ASPECT_X, -ratio / ASPECT_Y),
        (-ratio / ASPECT_X, ratio / ASPECT_Y),
    )
    texts = ((1, 0), (1, 1), (0, 1), (0, 0))
    surf = (0, 1, 2, 3)

    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, textureID)

    glBegin(GL_QUADS)
    for i in surf:
        glTexCoord2f(texts[i][0], texts[i][1])
        glVertex2f(centerX + verts[i][0], centerY + verts[i][1])
    glEnd()
    glDisable(GL_TEXTURE_2D)
