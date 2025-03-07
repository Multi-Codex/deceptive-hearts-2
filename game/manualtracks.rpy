
init python:    
    ## Manual Soundtracks Options
    #     name - The songs' name [REQUIRED]
    #     author - The songs' artist [REQUIRED]
    #     path - The path to the song [REQUIRED]
    #     album - The songs' album
    #     albumartist - The song' album artist
    #     composer - The songs' composer (person who made the music piece)
    #     genre - The songs' genre
    #     description - The song' description/comment
    #     cover_art - The path to the songs' cover art or 'False'
    #                 (without quotes) if this song has no cover art [REQUIRED]
    #     unlocked = 'True' (without quotes) for unlocked or 
    #                renpy.seen_audio("path/to/song") for True/False 
    #                determination

    leave_table_two = soundtrack(
        name = "Leave the Table v2",
        author = "MGT",
        path = "mod_assets/music/leavethetablev2.mp3",
        description = "Please leave this table.",
        cover_art = False
    )     
    manualDefineList.append(leave_table_two)

    holy_bread = soundtrack(
        name = "Holy Bread",
        author = "Suno AI Model",
        path = "mod_assets/music/Holy_Bread.mp3",
        description = "Garlic bread is life.",
        cover_art = False
    )     
    manualDefineList.append(holy_bread)

    freezy_flame = soundtrack(
        name = "Freezy Flame Galaxy",
        author = "Qumu",
        path = "mod_assets/music/freeze.mp3",
        description = "Christmas in DDMC.",
        cover_art = False
    )     
    manualDefineList.append(freezy_flame)

    leave_table = soundtrack(
        name = "Leave the Table",
        author = "MGT",
        path = "mod_assets/music/leavethetable.mp3",
        description = "Leave this table.",
        cover_art = False
    )     
    manualDefineList.append(leave_table)

    water_edge = soundtrack(
        name = "Water's Edge",
        author = "LumaTVM",
        path = "mod_assets/music/DDMC_Track_Series_Waters_Edge.mp3",
        description = "Water edging.",
        cover_art = False
    )     
    manualDefineList.append(water_edge)

    everything = soundtrack(
        name = "Everything in It's Right Place",
        author = "Wretched Team",
        path = "mod_assets/music/eiirp.ogg",
        description = "Two colors in my head.",
        cover_art = False
    )     
    manualDefineList.append(everything)

    cooling = soundtrack(
        name = "Cooling",
        author = "Wretched Team",
        path = "mod_assets/music/cooling.ogg",
        description = "I'm cold.",
        cover_art = False
    )     
    manualDefineList.append(cooling)

    lobarap = soundtrack(
        name = "Lobarap",
        author = "Wretched Team",
        path = "mod_assets/music/lobarap.ogg",
        description = "Menacing.",
        cover_art = False
    )     
    manualDefineList.append(lobarap)

    fulstop = soundtrack(
        name = "Ful Stop",
        author = "Wretched Team",
        path = "mod_assets/music/fulstop.ogg",
        description = "You really messed up everything.",
        cover_art = False
    )     
    manualDefineList.append(fulstop)

    mps = soundtrack(
        name = "Motion Picture Soundtrack",
        author = "Wretched Team",
        path = "mod_assets/music/motionpicturesoundtrack.ogg",
        description = "I can hear the bells.",
        cover_art = False
    )     
    manualDefineList.append(mps)

    doom = soundtrack(
        name = "E1M1 Remix",
        author = "Hydra Boss",
        path = "mod_assets/music/e1m1.mp3",
        description = "Rip and tear until it is done.",
        cover_art = False
    )     
    manualDefineList.append(doom)

    hope = soundtrack(
        name = "There's Always Hope!",
        author = "cpcantimark",
        path = "mod_assets/music/hope.mp3",
        description = "My food got violated.",
        cover_art = False
    )     
    manualDefineList.append(hope)

    nohope = soundtrack(
        name = "There's Never Hope",
        author = "cpcantimark",
        path = "mod_assets/music/hope.mp3",
        description = "Ruh roh raggy.",
        cover_art = False
    )     
    manualDefineList.append(nohope)

    salvation = soundtrack(
        name = "White Salvation",
        author = "cpcantimark",
        path = "mod_assets/music/whitesalvation.mp3",
        description = "How chill.",
        cover_art = False
    )     
    manualDefineList.append(salvation)

    nuhuh = soundtrack(
        name = "Nuh Uh",
        author = "cpcantimark",
        path = "mod_assets/music/nuhuh.ogg",
        description = "Final boss music.",
        cover_art = False
    )     
    manualDefineList.append(nuhuh)

    justsayori = soundtrack(
        name = "Just Sayori",
        author = "Jan Hehr",
        path = "mod_assets/music/justsayori.ogg",
        description = "The case is afoot.",
        cover_art = False
    )     
    manualDefineList.append(justsayori)

    istill = soundtrack(
        name = "I Still Love You Remix",
        author = "TritraSerpifeu",
        path = "mod_assets/music/istill.mp3",
        description = "My final moments.",
        cover_art = False
    )     
    manualDefineList.append(istill)

    inferno = soundtrack(
        name = "Inferno",
        author = "K-PSZH",
        path = "mod_assets/music/Inferno.ogg",
        description = "Let them go.",
        cover_art = False
    )     
    manualDefineList.append(inferno)

    entropy = soundtrack(
        name = "Entropy",
        author = "Empyre",
        path = "mod_assets/music/Entropy.ogg",
        description = "Forgive him.",
        cover_art = False
    )     
    manualDefineList.append(entropy)

    gh = soundtrack(
        name = "golden hour",
        author = "John Rod Dondoyano",
        path = "mod_assets/music/gh.mp3",
        description = "Roll credits.",
        cover_art = False
    )     
    manualDefineList.append(gh)

    thickofit = soundtrack(
        name = "Thick of It",
        author = "TensuraEdogawa",
        path = "mod_assets/music/thickofit.ogg",
        description = "From the screen.",
        cover_art = False
    )     
    manualDefineList.append(thickofit)

    ## Example

    # poem_panic = soundtrack(
    #     name = "Poem Panic",
    #     path = "bgm/example.ogg",
    #     author = "Dan Salvato",
    #     description = "Example",
    #     unlocked = renpy.seen_audio("bgm/example.ogg")
    # )
    # manualDefineList.append(poem_panic)