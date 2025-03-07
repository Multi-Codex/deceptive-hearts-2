layeredimage miyuki turned:
    at [renpy.partial(Flatten, drawable_resolution=False), AutofocusDisplayable(name="miyuki turned")]

    #####
    # If you're using Autofocus, uncomment the lines below and comment/remove the 'at renpy.partial(Flatten, drawable_resolution=False)' above
    #####
    #at AutofocusDisplayable(name="miyuki")
    #
    #group autofocus_coloring:
    #    attribute day default null
    #    attribute dawn null
    #    attribute sunset null
    #    attribute evening null
    #    attribute night null

    always:
        subpixel True
        anchor (0.0, 0.0)
        yoffset 0.55

        "mod_assets/MPT/miyuki/facebase.png"

    group outfit:
        attribute uniform default null
        attribute winter null

    group left:
        attribute ldown default if_any(["uniform"]):
            "mod_assets/MPT/miyuki/outfits/uniform_ldown.png"
        attribute lbehind if_any(["uniform"]):
            "mod_assets/MPT/miyuki/outfits/uniform_lbehind.png"
        attribute lup if_any(["uniform"]):
            "mod_assets/MPT/miyuki/outfits/uniform_lup.png"
        attribute lup2 if_any(["uniform"]): # those two are the same image
            "mod_assets/MPT/miyuki/outfits/uniform_lup2.png"
        attribute peace if_any(["uniform"]):# but i defined them in 2 != ways cause why not
            "mod_assets/MPT/miyuki/outfits/uniform_lup2.png"
        attribute ldown default if_any(["winter"]):
            "mod_assets/MPT/miyuki/winter/1.png"
        attribute lbehind if_any(["winter"]):
            "mod_assets/MPT/miyuki/winter/3.png"
        attribute lup if_any(["winter"]):
            "mod_assets/MPT/miyuki/winter/2.png"
        attribute peace if_any(["winter"]):# but i defined them in 2 != ways cause why not
            "mod_assets/MPT/miyuki/winter/2a.png"
        
    group right:
        attribute rhip default if_any(["uniform"]):
            "mod_assets/MPT/miyuki/outfits/uniform_rhip.png"
        attribute rhold if_any(["uniform"]):
            "mod_assets/MPT/miyuki/outfits/uniform_rhold.png"
        
    group nose:
        attribute na default null
        attribute nb:
            "mod_assets/MPT/miyuki/nose_b.png" # sweat drop
        attribute nc:
            "mod_assets/MPT/miyuki/nose_c.png" # blush
        attribute nd:
            "mod_assets/MPT/miyuki/nose_d.png" # blush + sweat drop

    group mouth:
        attribute ma default:
            "mod_assets/MPT/miyuki/mouth_a.png" # smiling
        attribute mb:
            "mod_assets/MPT/miyuki/mouth_b.png" # talking + smiling
        attribute mc:
            "mod_assets/MPT/miyuki/mouth_c.png" # big ass smile
        attribute md:
            "mod_assets/MPT/miyuki/mouth_d.png" # closed mouth -> _
        attribute me:
            "mod_assets/MPT/miyuki/mouth_e.png" # neutral + talking
        attribute mf:
            "mod_assets/MPT/miyuki/mouth_f.png" # open mouth (surprised)
        attribute mg:
            "mod_assets/MPT/miyuki/mouth_g.png" # ^ but showing teeth (angry?)
        attribute mh:
            "mod_assets/MPT/miyuki/mouth_h.png" # crazy bitch
        
    group eyes:
        attribute ea default:
            "mod_assets/MPT/miyuki/eyes_a.png" # neutral
        attribute eb:
            "mod_assets/MPT/miyuki/eyes_b.png" # "oy really now?" / distant
        attribute ec:
            "mod_assets/MPT/miyuki/eyes_c.png" # looking left
        attribute ed:
            "mod_assets/MPT/miyuki/eyes_d.png" # ^ + distant
        attribute ee:
            "mod_assets/MPT/miyuki/eyes_e.png" # closed
        attribute ef:
            "mod_assets/MPT/miyuki/eyes_f.png" # closed + happy
        attribute eg:
            "mod_assets/MPT/miyuki/eyes_g.png" # crying
        attribute eh:
            "mod_assets/MPT/miyuki/eyes_h.png" # crying + closed
        attribute ei:
            "mod_assets/MPT/miyuki/eyes_i.png" # surprised / crazy
        
    group eyebrows:
        attribute ba default:
            "mod_assets/MPT/miyuki/eyebrows_a.png" # neutral
        attribute bb:
            "mod_assets/MPT/miyuki/eyebrows_b.png" # serious / angry
        attribute bc:
            "mod_assets/MPT/miyuki/eyebrows_c.png" # raised eyebrow *vine boom*
        attribute bd:
            "mod_assets/MPT/miyuki/eyebrows_d.png" # surprised
        attribute be:
            "mod_assets/MPT/miyuki/eyebrows_e.png" # sad
    
    group shadow:
        attribute shadow default null
        attribute shadow if_all(["uniform", "rhold"]):
            "mod_assets/MPT/miyuki/outfits/uniform_shadow.png"
        