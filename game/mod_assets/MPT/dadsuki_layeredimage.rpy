layeredimage dadsuki turned:

    at [renpy.partial(Flatten, drawable_resolution=False), AutofocusDisplayable(name="dadsuki turned")]

    always "mod_assets/MPT/dadsuki/base.png"

    group outfit:
        
        attribute casual default null
    
    group moods:

        attribute neut default null
        attribute angr null
        attribute anno null
        attribute cry null
        attribute curi null
        attribute dist null
        attribute happ null
        attribute laug null
        attribute nerv null
        attribute shoc null
        attribute sad null
        attribute vang null
        attribute worr null

    group eyes:

        attribute oe default if_any(["neut", "anno", "curi", "happ", "laug", "sad"]):
            "mod_assets/MPT/dadsuki/eyes/e1a.png"
        attribute oe default if_any(["cry"]):
            "mod_assets/MPT/dadsuki/eyes/e1d.png"
        attribute oe default if_any(["nerv", "worr", "dist"]):
            "mod_assets/MPT/dadsuki/eyes/e1b.png"
        attribute oe default if_any(["shoc", "vang", "angr"]):
            "mod_assets/MPT/dadsuki/eyes/e1c.png"

        attribute ce if_any(["neut", "worr", "dist", "anno", "curi", "happ", "laug", "sad", "vang", "nerv", "shoc", "angr"]):
            "mod_assets/MPT/dadsuki/eyes/e2a.png"
        attribute ce if_any(["cry"]):
            "mod_assets/MPT/dadsuki/eyes/e2b.png"

        attribute e1a:
            "mod_assets/MPT/dadsuki/eyes/e1a.png"
        attribute e1b:
            "mod_assets/MPT/dadsuki/eyes/e1b.png"
        attribute e1c:
            "mod_assets/MPT/dadsuki/eyes/e1c.png"
        attribute e1d:
            "mod_assets/MPT/dadsuki/eyes/e1d.png"
        attribute e2a:
            "mod_assets/MPT/dadsuki/eyes/e2a.png"
        attribute e2b:
            "mod_assets/MPT/dadsuki/eyes/e2b.png"

    group brows:

        attribute brows default if_any(["neut", "dist", "happ", "laug", "shoc"]) if_not(["ce"]):
            "mod_assets/MPT/dadsuki/brows/b1a.png"
        attribute brows default if_any(["neut", "dist", "happ", "laug", "shoc"]) if_not(["oe"]):
            "mod_assets/MPT/dadsuki/brows/b1aC.png"

        attribute brows default if_any(["anno", "vang", "angr"]) if_not(["ce"]):
            "mod_assets/MPT/dadsuki/brows/b1b.png"
        attribute brows default if_any(["anno", "vang", "angr"]) if_not(["oe"]):
            "mod_assets/MPT/dadsuki/brows/b1bC.png"

        attribute brows default if_any(["cry", "nerv", "sad", "worr"]) if_not(["ce"]):
            "mod_assets/MPT/dadsuki/brows/b1c.png"
        attribute brows default if_any(["cry", "sad", "nerv", "worr"]) if_not(["oe"]):
            "mod_assets/MPT/dadsuki/brows/b2a.png"

        attribute brows default if_any(["curi"]) if_not(["ce"]):
            "mod_assets/MPT/dadsuki/brows/b1d.png"
        attribute brows default if_any(["curi"]) if_not(["oe"]):
            "mod_assets/MPT/dadsuki/brows/b1dC.png"


        attribute b1a if_not(["b2a", "ce"]):
            "mod_assets/MPT/dadsuki/brows/b1a.png"
        attribute b1aC if_any(["b2a", "ce"]):
            "mod_assets/MPT/dadsuki/brows/b1aC.png"
        
        attribute b1b if_not(["b2a", "ce"]):
            "mod_assets/MPT/dadsuki/brows/b1b.png"
        attribute b1bC if_any(["b2a", "ce"]):
            "mod_assets/MPT/dadsuki/brows/b1bC.png"
        
        attribute b1c:
            "mod_assets/MPT/dadsuki/brows/b1c.png"
        
        attribute b1d if_not(["b2a", "ce"]):
            "mod_assets/MPT/dadsuki/brows/b1d.png"
        attribute b1dC if_any(["b2a", "ce"]):
            "mod_assets/MPT/dadsuki/brows/b1dC.png"

        attribute b2a:
            "mod_assets/MPT/dadsuki/brows/b2a.png"
    
    group mouths:

        attribute cm default if_any(["neut", "worr", "dist", "anno", "cry", "curi", "shoc", "sad", "angr"]):
            "mod_assets/MPT/dadsuki/mouths/ma.png"
        attribute cm default if_any(["happ", "laug", "nerv"]):
            "mod_assets/MPT/dadsuki/mouths/mb.png"
        attribute cm default if_any(["vang"]):
            "mod_assets/MPT/dadsuki/mouths/md.png"

        attribute om if_any(["neut", "worr", "dist", "anno", "cry", "curi", "nerv", "shoc", "sad", "happ", "angr"]):
            "mod_assets/MPT/dadsuki/mouths/mc.png"
        attribute om if_any(["vang", "laug"]):
            "mod_assets/MPT/dadsuki/mouths/me.png"

        attribute ma:
            "mod_assets/MPT/dadsuki/mouths/ma.png"
        attribute mb:
            "mod_assets/MPT/dadsuki/mouths/mb.png"
        attribute mc:
            "mod_assets/MPT/dadsuki/mouths/mc.png"
        attribute md:
            "mod_assets/MPT/dadsuki/mouths/md.png"
        attribute me:
            "mod_assets/MPT/dadsuki/mouths/me.png"

    group chin:
        attribute shave:
            "mod_assets/MPT/dadsuki/clean/Overlay/face_clean.png"
    
    group nose:

        attribute blus:
            "mod_assets/MPT/dadsuki/nose/n1.png"
        
        attribute n1:
            "mod_assets/MPT/dadsuki/nose/n1.png"

    group wink:

        attribute wink:
            "mod_assets/MPT/dadsuki/eyes/e3a.png"
        
        attribute e3a:
            "mod_assets/MPT/dadsuki/eyes/e3a.png"

    group right:
        anchor (0,0) subpixel (True)
        yoffset (-0.5) xoffset(-0.5)

        attribute rdown default if_not(["cross"]):
            "mod_assets/MPT/dadsuki/clothes/1r.png"
        attribute rup if_not(["cross"]):
            "mod_assets/MPT/dadsuki/clothes/2r.png"
        attribute cross:
            "mod_assets/MPT/dadsuki/clothes/3a.png"
    
    group left:
        anchor (0,0) subpixel (True)
        yoffset (-0.5) xoffset(-0.5)

        attribute ldown default if_not(["cross"]):
            "mod_assets/MPT/dadsuki/clothes/1l.png"
        attribute lup if_not(["cross"]):
            "mod_assets/MPT/dadsuki/clothes/2l.png"
        attribute lbott if_not(["cross"]):
            "mod_assets/MPT/dadsuki/clothes/4l.png"



layeredimage dadsuki clean:

    at [renpy.partial(Flatten, drawable_resolution=False), AutofocusDisplayable(name="dadsuki clean")]

    always "mod_assets/MPT/dadsuki/base.png"

    group outfit:
        
        attribute casual default null
    
    group moods:

        attribute neut default null
        attribute angr null
        attribute anno null
        attribute cry null
        attribute curi null
        attribute dist null
        attribute happ null
        attribute laug null
        attribute nerv null
        attribute shoc null
        attribute sad null
        attribute vang null
        attribute worr null

    group eyes:

        attribute oe default if_any(["neut", "anno", "curi", "happ", "laug", "sad"]):
            "mod_assets/MPT/dadsuki/eyes/e1a.png"
        attribute oe default if_any(["cry"]):
            "mod_assets/MPT/dadsuki/eyes/e1d.png"
        attribute oe default if_any(["nerv", "worr", "dist"]):
            "mod_assets/MPT/dadsuki/eyes/e1b.png"
        attribute oe default if_any(["shoc", "vang", "angr"]):
            "mod_assets/MPT/dadsuki/eyes/e1c.png"

        attribute ce if_any(["neut", "worr", "dist", "anno", "curi", "happ", "laug", "sad", "vang", "nerv", "shoc", "angr"]):
            "mod_assets/MPT/dadsuki/eyes/e2a.png"
        attribute ce if_any(["cry"]):
            "mod_assets/MPT/dadsuki/eyes/e2b.png"

        attribute e1a:
            "mod_assets/MPT/dadsuki/eyes/e1a.png"
        attribute e1b:
            "mod_assets/MPT/dadsuki/eyes/e1b.png"
        attribute e1c:
            "mod_assets/MPT/dadsuki/eyes/e1c.png"
        attribute e1d:
            "mod_assets/MPT/dadsuki/eyes/e1d.png"
        attribute e2a:
            "mod_assets/MPT/dadsuki/eyes/e2a.png"
        attribute e2b:
            "mod_assets/MPT/dadsuki/eyes/e2b.png"

    group brows:

        attribute brows default if_any(["neut", "dist", "happ", "laug", "shoc"]) if_not(["ce"]):
            "mod_assets/MPT/dadsuki/brows/b1a.png"
        attribute brows default if_any(["neut", "dist", "happ", "laug", "shoc"]) if_not(["oe"]):
            "mod_assets/MPT/dadsuki/brows/b1aC.png"

        attribute brows default if_any(["anno", "vang", "angr"]) if_not(["ce"]):
            "mod_assets/MPT/dadsuki/brows/b1b.png"
        attribute brows default if_any(["anno", "vang", "angr"]) if_not(["oe"]):
            "mod_assets/MPT/dadsuki/brows/b1bC.png"

        attribute brows default if_any(["cry", "nerv", "sad", "worr"]) if_not(["ce"]):
            "mod_assets/MPT/dadsuki/brows/b1c.png"
        attribute brows default if_any(["cry", "sad", "nerv", "worr"]) if_not(["oe"]):
            "mod_assets/MPT/dadsuki/brows/b2a.png"

        attribute brows default if_any(["curi"]) if_not(["ce"]):
            "mod_assets/MPT/dadsuki/brows/b1d.png"
        attribute brows default if_any(["curi"]) if_not(["oe"]):
            "mod_assets/MPT/dadsuki/brows/b1dC.png"


        attribute b1a if_not(["b2a", "ce"]):
            "mod_assets/MPT/dadsuki/brows/b1a.png"
        attribute b1aC if_any(["b2a", "ce"]):
            "mod_assets/MPT/dadsuki/brows/b1aC.png"
        
        attribute b1b if_not(["b2a", "ce"]):
            "mod_assets/MPT/dadsuki/brows/b1b.png"
        attribute b1bC if_any(["b2a", "ce"]):
            "mod_assets/MPT/dadsuki/brows/b1bC.png"
        
        attribute b1c:
            "mod_assets/MPT/dadsuki/brows/b1c.png"
        
        attribute b1d if_not(["b2a", "ce"]):
            "mod_assets/MPT/dadsuki/brows/b1d.png"
        attribute b1dC if_any(["b2a", "ce"]):
            "mod_assets/MPT/dadsuki/brows/b1dC.png"

        attribute b2a:
            "mod_assets/MPT/dadsuki/brows/b2a.png"
    
    group mouths:

        attribute cm default if_any(["neut", "worr", "dist", "anno", "cry", "curi", "shoc", "sad", "angr"]):
            "mod_assets/MPT/dadsuki/mouths/ma.png"
        attribute cm default if_any(["happ", "laug", "nerv"]):
            "mod_assets/MPT/dadsuki/mouths/mb.png"
        attribute cm default if_any(["vang"]):
            "mod_assets/MPT/dadsuki/mouths/md.png"

        attribute om if_any(["neut", "worr", "dist", "anno", "cry", "curi", "nerv", "shoc", "sad", "happ", "angr"]):
            "mod_assets/MPT/dadsuki/mouths/mc.png"
        attribute om if_any(["vang", "laug"]):
            "mod_assets/MPT/dadsuki/mouths/me.png"

        attribute ma:
            "mod_assets/MPT/dadsuki/mouths/ma.png"
        attribute mb:
            "mod_assets/MPT/dadsuki/mouths/mb.png"
        attribute mc:
            "mod_assets/MPT/dadsuki/mouths/mc.png"
        attribute md:
            "mod_assets/MPT/dadsuki/mouths/md.png"
        attribute me:
            "mod_assets/MPT/dadsuki/mouths/me.png"


    group chin:
        attribute shave:
            "mod_assets/MPT/dadsuki/clean/Overlay/face_clean.png"
    
    group nose:

        attribute blus:
            "mod_assets/MPT/dadsuki/nose/n1.png"
        
        attribute n1:
            "mod_assets/MPT/dadsuki/nose/n1.png"

    group wink:

        attribute wink:
            "mod_assets/MPT/dadsuki/eyes/e3a.png"
        
        attribute e3a:
            "mod_assets/MPT/dadsuki/eyes/e3a.png"

    group right:
        anchor (0,0) subpixel (True)
        yoffset (-0.5) xoffset(-0.5)

        attribute rdown default if_not(["cross"]):
            "mod_assets/MPT/dadsuki/clean/1r.png"
        attribute rup if_not(["cross"]):
            "mod_assets/MPT/dadsuki/clean/2r.png"
        attribute cross:
            "mod_assets/MPT/dadsuki/clean/3.png"
    
    group left:
        anchor (0,0) subpixel (True)
        yoffset (-0.5) xoffset(-0.5)

        attribute ldown default if_not(["cross"]):
            "mod_assets/MPT/dadsuki/clean/1l.png"
        attribute lup if_not(["cross"]):
            "mod_assets/MPT/dadsuki/clean/2l.png"
        attribute lbott if_not(["cross"]):
            "mod_assets/MPT/dadsuki/clean/4l.png"

    group tie:
        attribute tie if_not(["cross"]):
            "mod_assets/MPT/dadsuki/clean/Overlay/Tie-a.png"
        attribute loosetie if_not(["cross"]):
            "mod_assets/MPT/dadsuki/clean/Overlay/Tie-b.png"
        attribute tie if_any(["cross"]):
            "mod_assets/MPT/dadsuki/clean/Overlay/3-Tie-a.png"
        attribute loosetie if_any(["cross"]):
            "mod_assets/MPT/dadsuki/clean/Overlay/3-Tie-b.png"
        attribute tie if_any(["lup"]):
            "mod_assets/MPT/dadsuki/clean/Overlay/lup.png"
        attribute loosetie if_any(["lup"]):
            "mod_assets/MPT/dadsuki/clean/Overlay/lup.png"



layeredimage dadsuki reversed:

    at [renpy.partial(Flatten, drawable_resolution=False), AutofocusDisplayable(name="dadsuki reversed")]

    always "mod_assets/MPT/dadsuki/reversed/base.png"

    group outfit:
        
        attribute casual default null
    
    group moods:

        attribute neut default null
        attribute angr null
        attribute anno null
        attribute cry null
        attribute curi null
        attribute dist null
        attribute happ null
        attribute laug null
        attribute nerv null
        attribute shoc null
        attribute sad null
        attribute vang null
        attribute worr null

    group eyes:

        attribute oe default if_any(["neut", "anno", "curi", "happ", "laug", "sad"]):
            "mod_assets/MPT/dadsuki/reversed/eyes/e1a.png"
        attribute oe default if_any(["cry"]):
            "mod_assets/MPT/dadsuki/reversed/eyes/e1d.png"
        attribute oe default if_any(["nerv", "worr", "dist"]):
            "mod_assets/MPT/dadsuki/reversed/eyes/e1b.png"
        attribute oe default if_any(["shoc", "vang", "angr"]):
            "mod_assets/MPT/dadsuki/reversed/eyes/e1c.png"

        attribute ce if_any(["neut", "worr", "dist", "anno", "curi", "happ", "laug", "sad", "vang", "angr", "nerv", "shoc"]):
            "mod_assets/MPT/dadsuki/reversed/eyes/e2a.png"
        attribute ce if_any(["cry"]):
            "mod_assets/MPT/dadsuki/reversed/eyes/e2b.png"

        attribute e1a:
            "mod_assets/MPT/dadsuki/reversed/eyes/e1a.png"
        attribute e1b:
            "mod_assets/MPT/dadsuki/reversed/eyes/e1b.png"
        attribute e1c:
            "mod_assets/MPT/dadsuki/reversed/eyes/e1c.png"
        attribute e1d:
            "mod_assets/MPT/dadsuki/reversed/eyes/e1d.png"
        attribute e2a:
            "mod_assets/MPT/dadsuki/reversed/eyes/e2a.png"
        attribute e2b:
            "mod_assets/MPT/dadsuki/reversed/eyes/e2b.png"

    group brows:

        attribute brows default if_any(["neut", "dist", "happ", "laug", "shoc"]) if_not(["ce"]):
            "mod_assets/MPT/dadsuki/reversed/brows/b1a.png"
        attribute brows default if_any(["neut", "dist", "happ", "laug", "shoc"]) if_not(["oe"]):
            "mod_assets/MPT/dadsuki/reversed/brows/b1aC.png"

        attribute brows default if_any(["anno", "vang", "angr"]) if_not(["ce"]):
            "mod_assets/MPT/dadsuki/reversed/brows/b1b.png"
        attribute brows default if_any(["anno", "vang", "angr"]) if_not(["oe"]):
            "mod_assets/MPT/dadsuki/reversed/brows/b1bC.png"

        attribute brows default if_any(["cry", "nerv", "sad", "worr"]) if_not(["ce"]):
            "mod_assets/MPT/dadsuki/reversed/brows/b1c.png"
        attribute brows default if_any(["cry", "sad", "nerv", "worr"]) if_not(["oe"]):
            "mod_assets/MPT/dadsuki/reversed/brows/b2a.png"

        attribute brows default if_any(["curi"]) if_not(["ce"]):
            "mod_assets/MPT/dadsuki/reversed/brows/b1d.png"
        attribute brows default if_any(["curi"]) if_not(["oe"]):
            "mod_assets/MPT/dadsuki/reversed/brows/b1dC.png"


        attribute b1a if_not(["b2a", "ce"]):
            "mod_assets/MPT/dadsuki/reversed/brows/b1a.png"
        attribute b1aC if_any(["b2a", "ce"]):
            "mod_assets/MPT/dadsuki/reversed/brows/b1aC.png"
        
        attribute b1b if_not(["b2a", "ce"]):
            "mod_assets/MPT/dadsuki/reversed/brows/b1b.png"
        attribute b1bC if_any(["b2a", "ce"]):
            "mod_assets/MPT/dadsuki/reversed/brows/b1bC.png"
        
        attribute b1c:
            "mod_assets/MPT/dadsuki/reversed/brows/b1c.png"
        
        attribute b1d if_not(["b2a", "ce"]):
            "mod_assets/MPT/dadsuki/reversed/brows/b1d.png"
        attribute b1dC if_any(["b2a", "ce"]):
            "mod_assets/MPT/dadsuki/reversed/brows/b1dC.png"

        attribute b2a:
            "mod_assets/MPT/dadsuki/reversed/brows/b2a.png"
    
    group mouths:

        attribute cm default if_any(["neut", "worr", "dist", "anno", "cry", "curi", "shoc", "sad", "angr"]):
            "mod_assets/MPT/dadsuki/reversed/mouths/ma.png"
        attribute cm default if_any(["happ", "laug", "nerv"]):
            "mod_assets/MPT/dadsuki/reversed/mouths/mb.png"
        attribute cm default if_any(["vang"]):
            "mod_assets/MPT/dadsuki/reversed/mouths/md.png"

        attribute om if_any(["neut", "worr", "dist", "anno", "cry", "curi", "nerv", "shoc", "sad", "happ", "angr"]):
            "mod_assets/MPT/dadsuki/reversed/mouths/mc.png"
        attribute om if_any(["vang", "laug"]):
            "mod_assets/MPT/dadsuki/reversed/mouths/me.png"

        attribute ma:
            "mod_assets/MPT/dadsuki/reversed/mouths/ma.png"
        attribute mb:
            "mod_assets/MPT/dadsuki/reversed/mouths/mb.png"
        attribute mc:
            "mod_assets/MPT/dadsuki/reversed/mouths/mc.png"
        attribute md:
            "mod_assets/MPT/dadsuki/reversed/mouths/md.png"
        attribute me:
            "mod_assets/MPT/dadsuki/reversed/mouths/me.png"

    group chin:
        attribute shave:
            "mod_assets/MPT/dadsuki/reversed/clean/Overlay/face_clean.png"
    
    group nose:

        attribute blus:
            "mod_assets/MPT/dadsuki/reversed/nose/n1.png"
        
        attribute n1:
            "mod_assets/MPT/dadsuki/reversed/nose/n1.png"

    group wink:

        attribute wink:
            "mod_assets/MPT/dadsuki/reversed/eyes/e3a.png"
        
        attribute e3a:
            "mod_assets/MPT/dadsuki/reversed/eyes/e3a.png"

    group right:
        anchor (0,0) subpixel (True)
        yoffset (-0.5) xoffset(-0.5)

        attribute rdown default if_not(["cross"]):
            "mod_assets/MPT/dadsuki/reversed/clothes/1r.png"
        attribute rup if_not(["cross"]):
            "mod_assets/MPT/dadsuki/reversed/clothes/2r.png"
        attribute cross:
            "mod_assets/MPT/dadsuki/reversed/clothes/3a.png"
    
    group left:
        anchor (0,0) subpixel (True)
        yoffset (-0.5) xoffset(-0.5)

        attribute ldown default if_not(["cross"]):
            "mod_assets/MPT/dadsuki/reversed/clothes/1l.png"
        attribute lup if_not(["cross"]):
            "mod_assets/MPT/dadsuki/reversed/clothes/2l.png"
        attribute lbott if_not(["cross"]):
            "mod_assets/MPT/dadsuki/reversed/clothes/4l.png"


layeredimage dadsuki cleanreversed:

    at [renpy.partial(Flatten, drawable_resolution=False), AutofocusDisplayable(name="dadsuki cleanreversed")]

    always "mod_assets/MPT/dadsuki/reversed/base.png"

    group outfit:
        
        attribute casual default null
    
    group moods:

        attribute neut default null
        attribute angr null
        attribute anno null
        attribute cry null
        attribute curi null
        attribute dist null
        attribute happ null
        attribute laug null
        attribute nerv null
        attribute shoc null
        attribute sad null
        attribute vang null
        attribute worr null

    group eyes:

        attribute oe default if_any(["neut", "anno", "curi", "happ", "laug", "sad"]):
            "mod_assets/MPT/dadsuki/reversed/eyes/e1a.png"
        attribute oe default if_any(["cry"]):
            "mod_assets/MPT/dadsuki/reversed/eyes/e1d.png"
        attribute oe default if_any(["nerv", "worr", "dist"]):
            "mod_assets/MPT/dadsuki/reversed/eyes/e1b.png"
        attribute oe default if_any(["shoc", "vang", "angr"]):
            "mod_assets/MPT/dadsuki/reversed/eyes/e1c.png"

        attribute ce if_any(["neut", "worr", "dist", "anno", "curi", "happ", "laug", "sad", "vang", "angr", "nerv", "shoc"]):
            "mod_assets/MPT/dadsuki/reversed/eyes/e2a.png"
        attribute ce if_any(["cry"]):
            "mod_assets/MPT/dadsuki/reversed/eyes/e2b.png"

        attribute e1a:
            "mod_assets/MPT/dadsuki/reversed/eyes/e1a.png"
        attribute e1b:
            "mod_assets/MPT/dadsuki/reversed/eyes/e1b.png"
        attribute e1c:
            "mod_assets/MPT/dadsuki/reversed/eyes/e1c.png"
        attribute e1d:
            "mod_assets/MPT/dadsuki/reversed/eyes/e1d.png"
        attribute e2a:
            "mod_assets/MPT/dadsuki/reversed/eyes/e2a.png"
        attribute e2b:
            "mod_assets/MPT/dadsuki/reversed/eyes/e2b.png"

    group brows:

        attribute brows default if_any(["neut", "dist", "happ", "laug", "shoc"]) if_not(["ce"]):
            "mod_assets/MPT/dadsuki/reversed/brows/b1a.png"
        attribute brows default if_any(["neut", "dist", "happ", "laug", "shoc"]) if_not(["oe"]):
            "mod_assets/MPT/dadsuki/reversed/brows/b1aC.png"

        attribute brows default if_any(["anno", "vang", "angr"]) if_not(["ce"]):
            "mod_assets/MPT/dadsuki/reversed/brows/b1b.png"
        attribute brows default if_any(["anno", "vang", "angr"]) if_not(["oe"]):
            "mod_assets/MPT/dadsuki/reversed/brows/b1bC.png"

        attribute brows default if_any(["cry", "nerv", "sad", "worr"]) if_not(["ce"]):
            "mod_assets/MPT/dadsuki/reversed/brows/b1c.png"
        attribute brows default if_any(["cry", "sad", "nerv", "worr"]) if_not(["oe"]):
            "mod_assets/MPT/dadsuki/reversed/brows/b2a.png"

        attribute brows default if_any(["curi"]) if_not(["ce"]):
            "mod_assets/MPT/dadsuki/reversed/brows/b1d.png"
        attribute brows default if_any(["curi"]) if_not(["oe"]):
            "mod_assets/MPT/dadsuki/reversed/brows/b1dC.png"


        attribute b1a if_not(["b2a", "ce"]):
            "mod_assets/MPT/dadsuki/reversed/brows/b1a.png"
        attribute b1aC if_any(["b2a", "ce"]):
            "mod_assets/MPT/dadsuki/reversed/brows/b1aC.png"
        
        attribute b1b if_not(["b2a", "ce"]):
            "mod_assets/MPT/dadsuki/reversed/brows/b1b.png"
        attribute b1bC if_any(["b2a", "ce"]):
            "mod_assets/MPT/dadsuki/reversed/brows/b1bC.png"
        
        attribute b1c:
            "mod_assets/MPT/dadsuki/reversed/brows/b1c.png"
        
        attribute b1d if_not(["b2a", "ce"]):
            "mod_assets/MPT/dadsuki/reversed/brows/b1d.png"
        attribute b1dC if_any(["b2a", "ce"]):
            "mod_assets/MPT/dadsuki/reversed/brows/b1dC.png"

        attribute b2a:
            "mod_assets/MPT/dadsuki/reversed/brows/b2a.png"
    
    group mouths:

        attribute cm default if_any(["neut", "worr", "dist", "anno", "cry", "curi", "shoc", "sad", "angr"]):
            "mod_assets/MPT/dadsuki/reversed/mouths/ma.png"
        attribute cm default if_any(["happ", "laug", "nerv"]):
            "mod_assets/MPT/dadsuki/reversed/mouths/mb.png"
        attribute cm default if_any(["vang"]):
            "mod_assets/MPT/dadsuki/reversed/mouths/md.png"

        attribute om if_any(["neut", "worr", "dist", "anno", "cry", "curi", "nerv", "shoc", "sad", "happ", "angr"]):
            "mod_assets/MPT/dadsuki/reversed/mouths/mc.png"
        attribute om if_any(["vang", "laug"]):
            "mod_assets/MPT/dadsuki/reversed/mouths/me.png"

        attribute ma:
            "mod_assets/MPT/dadsuki/reversed/mouths/ma.png"
        attribute mb:
            "mod_assets/MPT/dadsuki/reversed/mouths/mb.png"
        attribute mc:
            "mod_assets/MPT/dadsuki/reversed/mouths/mc.png"
        attribute md:
            "mod_assets/MPT/dadsuki/reversed/mouths/md.png"
        attribute me:
            "mod_assets/MPT/dadsuki/reversed/mouths/me.png"

    group chin:
        attribute shave:
            "mod_assets/MPT/dadsuki/reversed/clean/Overlay/face_clean.png"
    
    group nose:

        attribute blus:
            "mod_assets/MPT/dadsuki/reversed/nose/n1.png"
        
        attribute n1:
            "mod_assets/MPT/dadsuki/reversed/nose/n1.png"

    group wink:

        attribute wink:
            "mod_assets/MPT/dadsuki/reversed/eyes/e3a.png"
        
        attribute e3a:
            "mod_assets/MPT/dadsuki/reversed/eyes/e3a.png"

    group right:
        anchor (0,0) subpixel (True)
        yoffset (-0.5) xoffset(-0.5)

        attribute rdown default if_not(["cross"]):
            "mod_assets/MPT/dadsuki/reversed/clean/1r.png"
        attribute rup if_not(["cross"]):
            "mod_assets/MPT/dadsuki/reversed/clean/2r.png"
        attribute cross:
            "mod_assets/MPT/dadsuki/reversed/clean/3.png"
    
    group left:
        anchor (0,0) subpixel (True)
        yoffset (-0.5) xoffset(-0.5)

        attribute ldown default if_not(["cross"]):
            "mod_assets/MPT/dadsuki/reversed/clean/1l.png"
        attribute lup if_not(["cross"]):
            "mod_assets/MPT/dadsuki/reversed/clean/2l.png"
        attribute lbott if_not(["cross"]):
            "mod_assets/MPT/dadsuki/reversed/clean/4l.png"


    group tie:
        attribute tie if_not(["cross"]):
            "mod_assets/MPT/dadsuki/reversed/clean/Overlay/Tie-a.png"
        attribute loosetie if_not(["cross"]):
            "mod_assets/MPT/dadsuki/reversed/clean/Overlay/Tie-b.png"
        attribute tie if_any(["cross"]):
            "mod_assets/MPT/dadsuki/reversed/clean/Overlay/3-Tie-a.png"
        attribute loosetie if_any(["cross"]):
            "mod_assets/MPT/dadsuki/reversed/clean/Overlay/3-Tie-b.png"
        attribute tie if_any(["lup"]):
            "mod_assets/MPT/dadsuki/reversed/clean/Overlay/lup.png"
        attribute loosetie if_any(["lup"]):
            "mod_assets/MPT/dadsuki/reversed/clean/Overlay/lup.png"


init python:
    #Layered image refreshes
    def dadsukiref(target="master"):
        if not "dadsuki" in renpy.get_showing_tags(layer=target, sort=True):
            #If not currently showing this sprite, stop function.
            return
        pose = str(renpy.get_attributes("dadsuki",layer=target)[0])
        if pose == "":
            #Nope out if there's no actual pose here.
            return
        renpy.show("dadsuki " + pose + " refreshattribute",layer=target)
        renpy.show("dadsuki",layer=target)
