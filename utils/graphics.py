from utils import global_variables
import glfw

from utils.set_variables import GRAPHICS_FPS_LIMITER


def set_fps_limit(fps: int):
    last = global_variables.get_var(name=GRAPHICS_FPS_LIMITER)
    while glfw.get_time() <= last + 1 / fps:
        pass
    global_variables.set_var(name=GRAPHICS_FPS_LIMITER, value=last + 1 / fps)
