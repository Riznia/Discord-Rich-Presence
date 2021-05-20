from pypresence import Presence
import time

client_id = 'client_token here'
CRP = Presence(client_id)
CRP.connect()

#   ===================================================================================================================================================
#   =       ========================================  =======       ==============  =======       =====================================================
#   =  ====  =======================================  =======  ====  =============  =======  ====  ====================================================
#   =  ====  =======================================  =======  ====  =============  =======  ====  ====================================================
#   =  ====  ==  ===   ====   ====   ===  =   ======  =======  ===   ==  ===   ===  =======  ====  ==  =   ====   ====   ====   ===  = ====   ====   ==
#   =  ====  ======  =  ==  =  ==     ==    =  ===    =======      ========  =  ==    =====       ===    =  ==  =  ==  =  ==  =  ==     ==  =  ==  =  =
#   =  ====  ==  ===  ====  =====  =  ==  =======  =  =======  ====  ==  ==  =====  =  ====  ========  =======     ===  ====     ==  =  ==  =====     =
#   =  ====  ==  ====  ===  =====  =  ==  =======  =  =======  ====  ==  ==  =====  =  ====  ========  =======  =======  ===  =====  =  ==  =====  ====
#   =  ====  ==  ==  =  ==  =  ==  =  ==  =======  =  =======  ====  ==  ==  =  ==  =  ====  ========  =======  =  ==  =  ==  =  ==  =  ==  =  ==  =  =
#   =       ===  ===   ====   ====   ===  ========    =======  ====  ==  ===   ===  =  ====  ========  ========   ====   ====   ===  =  ===   ====   ==
#   =================================================================================================================================================== 


CRP.update(
    details="This is a detail text.",
    state="Text that goes directly below the details.",
    large_image = "Please enter the specified image name value after registering the image in Rich Presence Art Asset.",
    large_text="This is the text displayed when hovering over a large image of the mouse cursor.",
    small_image="Please enter the specified image name value after registering the image in Rich Presence Art Asset.",
    small_text="This is the text that is visible when hovering over the mouse cursor in a small image.",
    start=time.time(),

    buttons = [
        {"label": "1st label", "url": " "},
        {"label": "2nd lable", "url": " "}
    ]
)

input()