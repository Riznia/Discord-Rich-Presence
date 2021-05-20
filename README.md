# Discord-Rich-Presence [ENG & KR]

========================================================

[KR]
                
    step1,해당 Discord-Rich-Presence 를 사용할려면, py파일과 배치파일을 다운로드 받아주세요.

    step2, https://discord.com/developers/applications/ 에서 봇을 만들어주세요.

    봇 이름은 원하는 것으로 해주세요.(Ex, 만약 Discord로 정했다면 파일 실행 후 게임활동에는 "Discord 하는중" 으로 뜨게 됩니다.

    디스코드_게임_활동_메세지_커스텀_[KR].py에 대한 부가적인 추가 설명 입니다. 

    client_id = '봇 토큰을 여기다가 입력해주세요.' #봇 토큰을 입력해주시면 됩니다.

    details="세부 텍스트 텍스트 입니다." #게임 활동 밑에 들어가는 텍스트 입니다.
    
    state="세부 텍스트 아래에 들어가는 텍스트입니다.", #텍스트 그대로 세부 텍스트 밑에 들어가는 텍스트 입니다.
    
    large_image = "Rich Presence Art에서 이미지 등록을 한 후, 등록한 이미지의 이름값을 입력 해주세요.", 
    
    large_text="large_image에 마우스 커서를 놓을경우 보이는 텍스트 입니다.",
    
    small_image="Rich Presence Art에서 이미지 등록을 한 후, 등록한 이미지의 이름값을 입력 해주세요.",
    
    small_text="small_image에 마우스 커서를 놓을경우 보이는 텍스트 입니다.",
    
        start=time.time(), #게임 실행한 시간을 출력 해줍니다.
        
    buttons = [
    
        {"label": "1st label", "url": " "}, #지정할 만한 url이 없을경우 "https://discord.com/developers/applications/자신의 봇토큰/information"을 입력 하고 넣으셔도 무방합니다.
        
        {"label": "2nd lable", "url": " "}
        
    ]
    
    )

    step3,문의가 있을경우 댓글로 남겨주세요.

========================================================

There may be a mistranslation in English.


[ENG]

    Step1, If you want to use the Discord-Rich-Presence, please download the py file and batch file.
    
    Step2, make a bot at https://discord.com/developers/applications/.
    Please name the bot as you want. (Ex, if you choose Discord, it will appear as "Discording" in the game activity after running the file.)
    Discode_Game_Activity_Message_Custom_[KR].This is an additional explanation of py.
    
    Client_id = 'Enter the bot token here' #Enter the bot token.
    ~
    details="This is detail text." #This is the text that goes underneath the game activity.
    state="This is the text that goes underneath the detail text," #Text is the text that goes under the detail text as it is.
    large_image = "After registering the image in Rich Presence Art, please enter the name value of the registered image."
    large_text="text visible when mouse cursor is placed on large_image,"
    After registering the image in small_image="Rich Presence Art, please enter the name value of the registered image.",
    small_text="text visible when mouse cursor is placed on a small_image,"
    
    start=time.time(), #This will print out the game run time.
    
    buttons = [
    {"label": "1st label", "url": "}, #If you don't have a specifiable url, you can enter and insert your own botoken/information at https://discord.com/developers/applications/.
    {"label": "2nd lable", "url": " "}
    ]
    )
    Step3. If you have any questions, please leave a comment.
