from utils import global_variables
import glfw

SIM_ASPECT_X = "SIM_GRAPHICS_ASPECT_X"
SIM_ASPECT_Y = "SIM_GRAPHICS_ASPECT_Y"
GRAPHICS_FPS_LIMITER = "SIM_FPS_RATE_LIMITER_TIME_VAR"
APPLY = "SIM_APPLY"
RESOURCES_X_POS = "RESOUUUUURCES_X"
RESOURCES_Y_POS = "RESOUUUUURCES_Y"
A_X_POS = "AAAAAAAPOS_X"
A_Y_POS = "AAAAAAAPOS_Y"
A_X_RETURN = "AAAAAAAAAAXY_RETURN"
A_Y_RETURN = "AAAAAAAAAAAAAAAAAAAAAY_RETURN"

B_X_POS = "BBBBBBBBBBBBBBBB_POS_X"
B_Y_POS = "BBBBBBBBBBBBBBBBBBBBB_POS_Y"
B_X_RETURN = "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB_X_RETURN"
B_Y_RETURN = "BBBBBBBBBBBBBBBBBBBBBBB_Y_RETURN"

def setvar():
    global_variables.set_var(name=SIM_ASPECT_X, value=16)
    global_variables.set_var(name=SIM_ASPECT_Y, value=9)
    global_variables.set_var(name=GRAPHICS_FPS_LIMITER, value=glfw.get_time())
    global_variables.set_var(name=APPLY, value=False)
    global_variables.set_var(name=RESOURCES_X_POS, value="")
    global_variables.set_var(name=RESOURCES_Y_POS, value="")
    global_variables.set_var(name=A_X_POS, value="")
    global_variables.set_var(name=A_Y_POS, value="")
    global_variables.set_var(name=A_X_RETURN, value="")
    global_variables.set_var(name=A_Y_RETURN, value="")
    global_variables.set_var(name=B_X_POS, value="")
    global_variables.set_var(name=B_Y_POS, value="")
    global_variables.set_var(name=B_X_RETURN, value="")
    global_variables.set_var(name=B_Y_RETURN, value="")
