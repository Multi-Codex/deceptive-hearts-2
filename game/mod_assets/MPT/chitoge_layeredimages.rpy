layeredimage chitoge turned:
    at [renpy.partial(Flatten, drawable_resolution=False), AutofocusDisplayable(name="chitoge turned")]

    always:


        "mod_assets/MPT/chitoge/facebase.png"

    group outfit:
        attribute uniform default null

    group left:
        anchor (0,0) subpixel (True)
        yoffset (-0.5) xoffset(-0.5)
        attribute lbehind default if_any(["uniform"]):
            "mod_assets/MPT/chitoge/uniform/lbehind.png"
        attribute lup if_any(["uniform"]):
            "mod_assets/MPT/chitoge/uniform/lup.png"
        
    group right:
        anchor (0,0) subpixel (True)
        yoffset (-1.0) xoffset(-1.0)
        attribute rhip default if_any(["uniform"]):
            "mod_assets/MPT/chitoge/uniform/rhip.png"
        attribute rhold if_any(["uniform"]):
            "mod_assets/MPT/chitoge/uniform/rhold.png"
        
    group nose:
        attribute na default null
        attribute nb:
            "mod_assets/MPT/chitoge/nose_b.png" # sweat drop

    group mouth:
        attribute ma default:
            "mod_assets/MPT/chitoge/mouth_a.png" # smiling
        attribute mb:
            "mod_assets/MPT/chitoge/mouth_b.png" # talking + smiling
        attribute mc:
            "mod_assets/MPT/chitoge/mouth_c.png" # big ass smile
        attribute md:
            "mod_assets/MPT/chitoge/mouth_d.png" # closed mouth -> _
        attribute me:
            "mod_assets/MPT/chitoge/mouth_e.png" # neutral + talking
        attribute mf:
            "mod_assets/MPT/chitoge/mouth_f.png" # open mouth (surprised)
        attribute mg:
            "mod_assets/MPT/chitoge/mouth_g.png" # ^ but showing teeth (angry?)
        attribute mh:
            "mod_assets/MPT/chitoge/mouth_h.png" # crazy bitch
        
    group eyes:
        attribute ea default:
            "mod_assets/MPT/chitoge/eye_a.png" # neutral
        attribute eb:
            "mod_assets/MPT/chitoge/eye_b.png" # "oy really now?" / distant
        attribute ec:
            "mod_assets/MPT/chitoge/eye_c.png" # looking left
        attribute ed:
            "mod_assets/MPT/chitoge/eye_d.png" # ^ + distant
        attribute ee:
            "mod_assets/MPT/chitoge/eye_e.png" # closed
        attribute ef:
            "mod_assets/MPT/chitoge/eye_f.png" # closed + happy
        attribute eg:
            "mod_assets/MPT/chitoge/eye_g.png" # crying
        attribute eh:
            "mod_assets/MPT/chitoge/eye_h.png" # crying + closed
        
    group eyebrows:
        attribute ba default:
            "mod_assets/MPT/chitoge/eyebrow_a.png" # neutral
        attribute bb:
            "mod_assets/MPT/chitoge/eyebrow_b.png" # serious / angry
        attribute bc:
            "mod_assets/MPT/chitoge/eyebrow_c.png" # sad
    
        