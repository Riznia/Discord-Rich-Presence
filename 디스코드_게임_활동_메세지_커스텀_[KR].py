from pypresence import Presence
import time

client_id = '봇 토큰을 여기다가 입력해주세요.'
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
    details="세부 텍스트 텍스트 입니다.",
    state="세부 텍스트 아래에 들어가는 텍스트입니다.",
    large_image = "Rich Presence Art에서 이미지 등록을 한 후, 등록한 이미지의 이름값을 입력 해주세요.",
    large_text="large_image에 마우스 커서를 놓을경우 보이는 텍스트 입니다.",
    small_image="Rich Presence Art에서 이미지 등록을 한 후, 등록한 이미지의 이름값을 입력 해주세요.",
    small_text="small_image에 마우스 커서를 놓을경우 보이는 텍스트 입니다.",
    start=time.time(),

    buttons = [
        {"label": "1st label", "url": " "},
        {"label": "2nd lable", "url": " "}
    ]
)

input()
