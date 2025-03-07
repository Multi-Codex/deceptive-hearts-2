init python:

    #If you need to change the path of Elyssa's MPT folder,
    #change the 'base_path' variable!
    base_path = "mod_assets/MPT/Elyssa_MPT/" #Base path to the MPT folder
    outfit_path = base_path + "outfits/" #Path to the outfits folder
    expressions_path = base_path + "expressions/" #Path to the expressions folder

image elyssa_blink:
    alpha 0.0
    renpy.random.randint(20, 100)*0.1
    choice:
        alpha 1.0
        expressions_path + "eyes/e2a.png"
        0.015
        expressions_path + "eyes/e2b.png"
        0.035
        expressions_path + "eyes/e2a.png"
        0.015
    choice:
        alpha 1.0
        expressions_path + "eyes/e2a.png"
        0.015
        expressions_path + "eyes/e2b.png"
        0.065
        expressions_path + "eyes/e2a.png"
        0.015
    choice:
        alpha 1.0
        expressions_path + "eyes/e2a.png"
        0.015
        expressions_path + "eyes/e2b.png"
        0.095
        expressions_path + "eyes/e2a.png"
        0.015
    choice:
        alpha 1.0
        expressions_path + "eyes/e2a.png"
        0.015
        expressions_path + "eyes/e2b.png"
        0.035
        expressions_path + "eyes/e2a.png"
        0.015
        alpha 0.0
        0.15
        alpha 1.0
        expressions_path + "eyes/e2a.png"
        0.015
        expressions_path + "eyes/e2b.png"
        0.035
        expressions_path + "eyes/e2a.png"
        0.015
    repeat

layeredimage elyssa turned:

    #better quality of the sprite
    at renpy.partial(Flatten, drawable_resolution=False)

    always expressions_path + "facebase.png" #always the same face

    #outfits
    group outfit:
        #uniform
        attribute uniform default null
        #casual (purple shirt and blue jeans)
        attribute casual null
        #green vest around the waist
        attribute green_vest_waistline null
        #green vest worn
        attribute green_vest null
        #laboratory outfit
        attribute lab null
        #white shirt
        attribute white_shirt null

    group mood: 
        attribute neut default null #neutral
        attribute angr null #angry
        attribute anno null #annoyed
        attribute cry null  #crying
        attribute curi null #curious
        attribute dist null #distant
        attribute doub null #doubtful
        attribute flus null #flustered
        attribute happ null #happy
        attribute laug null #laughing
        attribute lsur null #surprised (lightly)
        attribute nerv null #nervous
        attribute pani null #panicked
        attribute pout null #pouting
        attribute sad null  #sad
        attribute vsur null #surprised (very)
        attribute worr null #worried
    
    #nose
    group blush:
        attribute nobl default null #default nose. Same than the facebase
        attribute blus null #blush
        attribute awkw null #awkward
        attribute blaw null #blush + awkward

    group left:
        anchor (0,0) subpixel (True)

        #uniform
        attribute ldown default if_any(["uniform"]):
            outfit_path + "uniform/ldown.png"
        attribute lhip if_any(["uniform"]):
            outfit_path + "uniform/lhip.png"

        #casual
        attribute ldown default if_any(["casual"]):
            outfit_path + "casual/ldown.png"
        attribute lup if_any(["casual"]):
            outfit_path + "casual/lup.png"
        attribute lpoint if_any(["casual"]):
            outfit_path + "casual/lpoint.png"

        #green vest
        attribute ldown default if_any(["green_vest"]):
            outfit_path + "green_vest/ldown.png"
        attribute lhip if_any(["green_vest"]):
            outfit_path + "green_vest/lhip.png"
        
        #green vest around the waist
        attribute ldown default if_any(["green_vest_waistline"]):
            outfit_path + "green_vest_waistline/waistline_ldown.png"
        attribute lhip if_any(["green_vest_waistline"]):
            outfit_path + "green_vest_waistline/waistline_lhip.png"

        #laboratory
        attribute ldown default if_any(["lab"]):
            outfit_path + "lab/ldown.png"
        attribute lup if_any(["lab"]):
            outfit_path + "lab/lup.png"
        attribute lpoint if_any(["lab"]):
            outfit_path + "lab/lpoint.png"

        #white shirt
        attribute ldown default if_any(["white_shirt"]):
            outfit_path + "white_shirt/ldown.png"
        attribute lhip if_any(["white_shirt"]):
            outfit_path + "white_shirt/lhip.png"

        
    group right:
        anchor (0,0) subpixel (True)
        
        attribute rdown default if_any(["uniform"]):
            outfit_path + "uniform/rdown.png"
        attribute rhip if_any(["uniform"]):
            outfit_path + "uniform/rhip.png"
        attribute rpen if_any(["uniform"]):
            outfit_path + "uniform/rpen.png"

        #casual
        attribute rdown default if_any(["casual"]):
            outfit_path + "casual/rdown.png"
        attribute rup if_any(["casual"]):
            outfit_path + "casual/rup.png"

        #green vest
        attribute rdown default if_any(["green_vest"]):
            outfit_path + "green_vest/rdown.png"
        attribute rhip if_any(["green_vest"]):
            outfit_path + "green_vest/rhip.png"
        attribute rpen if_any(["green_vest"]):
            outfit_path + "green_vest/rpen.png"
        
        #green vest around the waist
        attribute rdown default if_any(["green_vest_waistline"]):
            outfit_path + "green_vest_waistline/waistline_rdown.png"
        attribute rhip if_any(["green_vest_waistline"]):
            outfit_path + "green_vest_waistline/waistline_rhip.png"
        attribute rpen if_any(["green_vest_waistline"]):
            outfit_path + "green_vest_waistline/waistline_rpen.png"

        #laboratory
        attribute rdown default if_any(["lab"]):
            outfit_path + "lab/rdown.png"
        attribute rup if_any(["lab"]):
            outfit_path + "lab/rup.png"
        attribute rhip if_any(["lab"]):
            outfit_path + "lab/rhip.png"

        #white shirt
        attribute rdown default if_any(["white_shirt"]):
            outfit_path + "white_shirt/rdown.png"
        attribute rhip if_any(["white_shirt"]):
            outfit_path + "white_shirt/rhip.png"
        attribute rpen if_any(["white_shirt"]):
            outfit_path + "white_shirt/rpen.png"
        attribute rup if_any(["white_shirt"]):
            outfit_path + "white_shirt/rup.png"

    group nose:

        attribute nose default if_any(["nobl"]): #default
            expressions_path + "nose/default.png"
        attribute nose default if_any(["awkw"]): #awkward
            expressions_path + "nose/awkw.png"
        attribute nose default if_any(["blus"]): #blush
            expressions_path + "nose/blus.png"
        attribute nose default if_any(["blaw"]): #blush + awkward
            expressions_path + "nose/blaw.png"
    
        #Truncated tags
        attribute n1:
            expressions_path + "nose/default.png"
        attribute n2:
            expressions_path + "nose/awkw.png"
        attribute n3:
            expressions_path + "nose/blus.png"
        attribute n4:
            expressions_path + "nose/blaw.png"

    group mouth:

        #Closed mouths
        attribute cm default if_any(["happ", "laug"]):
            expressions_path + "mouths/m1a.png"
        attribute cm default if_any(["neut", "angr", "sad"]):
            expressions_path + "mouths/m1b.png"
        attribute cm default if_any(["curi", "flus", "lsur", "nerv"]):
            expressions_path + "mouths/m1c.png"
        attribute cm default if_any(["doub", "dist", "cry"]):
            expressions_path + "mouths/m1d.png"
        attribute cm default if_any(["pani", "pout", "vsur", "worr"]):
            expressions_path + "mouths/m1e.png"
        attribute cm default if_any(["anno"]):
            expressions_path + "mouths/m2h.png"

        #Opened mouths
        attribute om if_any(["happ", "laug"]):
            expressions_path + "mouths/m2a.png"
        attribute om if_any(["lsur"]):
            expressions_path + "mouths/m2b.png"
        attribute om if_any(["cry"]):
            expressions_path + "mouths/m2c.png"
        attribute om if_any(["neut", "curi", "worr"]):
            expressions_path + "mouths/m2d.png"
        attribute om if_any(["dist", "doub", "pout", "sad"]):
            expressions_path + "mouths/m2e.png"
        attribute om if_any(["vsur"]):
            expressions_path + "mouths/m2f.png"
        attribute om if_any(["pani"]):
            expressions_path + "mouths/m2g.png"
        attribute om if_any(["anno"]):
            expressions_path + "mouths/m2h.png"
        attribute om if_any(["angr"]):
            expressions_path + "mouths/m2i.png"
        attribute om if_any(["flus", "nerv"]):
            expressions_path + "mouths/m2j.png"

        #Truncated tags
        attribute m1a:
            expressions_path + "mouths/m1a.png"
        attribute m1b:
            expressions_path + "mouths/m1b.png"
        attribute m1c:
            expressions_path + "mouths/m1c.png"
        attribute m1d:
            expressions_path + "mouths/m1d.png"
        attribute m1e:
            expressions_path + "mouths/m1e.png"
        attribute m2a:
            expressions_path + "mouths/m2a.png"
        attribute m2b:
            expressions_path + "mouths/m2b.png"
        attribute m2c:
            expressions_path + "mouths/m2c.png"
        attribute m2d:
            expressions_path + "mouths/m2d.png"
        attribute m2e:
            expressions_path + "mouths/m2e.png"
        attribute m2f:
            expressions_path + "mouths/m2f.png"
        attribute m2g:
            expressions_path + "mouths/m2g.png"
        attribute m2h:
            expressions_path + "mouths/m2h.png"
        attribute m2i:
            expressions_path + "mouths/m2i.png"
        attribute m2j:
            expressions_path + "mouths/m2j.png"

    #This group allows you to potentially add flowing tears to Elyssa's face.
    #Just use the attribute 'tears' when showing her.
    #BE AWARE THAT IT'S NOT BEEN TESTED ON ALL THE POSSIBLE EYES COMBINATIONS!
    #If needed, ask me for some quick edits to add to your code :D
    group tears:
        attribute no_tears default null
        attribute tears if_not(["e2c", "e3a", "e3b"]): #avoid using on those >_< eyes and one eye blink
            expressions_path + "tears.png"

    #eyes
    group eyes:
        #Opened eyes
        attribute oe default if_any(["neut", "anno", "curi", "doub", "happ", "laug",
                                    "lsur", "worr"]):
            expressions_path + "eyes/e1a.png"
        attribute oe default if_any(["angr", "vsur"]):
            expressions_path + "eyes/e1b.png"
        attribute oe default if_any(["pani"]):
            expressions_path + "eyes/e1c.png"
        attribute oe default if_any(["dist", "flus", "nerv", "pout", "sad"]):
            expressions_path + "eyes/e1d.png"
        attribute oe default if_any(["cry"]):
            expressions_path + "eyes/e1e.png"

        #Closed eyes
        attribute ce if_any(["neut", "angr", "anno", "dist", "doub", "pout", "sad", "worr"]):
            expressions_path + "eyes/e2a.png"
        attribute ce if_any(["curi", "flus", "happ", "laug", "lsur", "nerv"]):
            expressions_path + "eyes/e2b.png"
        attribute ce if_any(["pani", "vsur"]):
            expressions_path + "eyes/e2c.png"
        attribute ce if_any(["cry"]):
            expressions_path + "eyes/e2d.png"
        
        #Truncated tags (for customization)
        #Opened eyes
        attribute e1a:
            expressions_path + "eyes/e1a.png"
        attribute e1b:
            expressions_path + "eyes/e1b.png"
        attribute e1c:
            expressions_path + "eyes/e1c.png"
        attribute e1d:
            expressions_path + "eyes/e1d.png"
        attribute e1e:
            expressions_path + "eyes/e1e.png"

        #Closed eyes
        attribute e2a:
            expressions_path + "eyes/e2a.png"
        attribute e2b:
            expressions_path + "eyes/e2b.png"
        attribute e2c:
            expressions_path + "eyes/e2c.png"
        attribute e2d:
            expressions_path + "eyes/e2d.png"
        
        #Left eye blink (from our POV)
        attribute e3a:
            expressions_path + "eyes/e3a.png"
        #Right eye blink (from our POV)
        attribute e3b:
            expressions_path + "eyes/e3b.png"

    #Blinking group, enabled by default. If you want to completely
    #disable it, remove the 'default' keyword from the 'blink' attribute
    #and write the other one like that 'attribute no_blink default null',
    #or simply use the attribute 'no_blink' in your code.
    group blink:
        attribute no_blink null
        #Not displayed if closed eyes
        attribute blink default if_not(["ce", "e2a", "e2b", "e2c", "e2d", "e3a", "e3b"]):
            "elyssa_blink"

    #Eyebrows
    group eyebrows:
        attribute brow default if_any(["neut", "dist"]): #normal ones
            expressions_path + "eyebrows/ba.png"
        attribute brow default if_any(["happ", "laug", "vsur", "pani"]): #surprised
            expressions_path + "eyebrows/bb.png"
        attribute brow default if_any(["curi", "nerv", "worr"]): #worried
            expressions_path + "eyebrows/bc.png"
        attribute brow default if_any(["anno", "angr"]): #furrowed
            expressions_path + "eyebrows/bd.png"
        attribute brow default if_any(["doub"]): #doubtful
            expressions_path + "eyebrows/be.png"
        attribute brow default if_any(["cry", "flus", "sad"]): #sad
            expressions_path + "eyebrows/bf.png"
        attribute brow default if_any(["lsur", "pout"]): #straight eyebrows
            expressions_path + "eyebrows/bg.png"

        #Truncated tags (for customization)
        attribute ba:
            expressions_path + "eyebrows/ba.png"
        attribute bb:
            expressions_path + "eyebrows/bb.png"
        attribute bc:
            expressions_path + "eyebrows/bc.png"
        attribute bd:
            expressions_path + "eyebrows/bd.png"
        attribute be:
            expressions_path + "eyebrows/be.png"
        attribute bf:
            expressions_path + "eyebrows/bf.png"
        attribute bg:
            expressions_path + "eyebrows/bg.png"

    #Group to add the glasses to Elyssa. Default doesn't have them.
    group accessories:
        attribute no_glasses default null
        attribute glasses:
            expressions_path + "glasses.png"
        

#Crossed arms of Elyssa (easier to make another layeredimage for this pose)
layeredimage elyssa cross:

    #better quality of the sprite
    at renpy.partial(Flatten, drawable_resolution=False)

    always expressions_path + "facebase.png" #always the same face

    #outfits
    group outfit:
        #uniform
        attribute uniform default null
        #casual (purple shirt and blue jeans)
        attribute casual null
        #green vest around the waist
        attribute green_vest_waistline null
        #green vest worn
        attribute green_vest null
        #laboratory outfit
        attribute lab null
        #white shirt
        attribute white_shirt null

    group mood: 
        attribute neut default null #neutral
        attribute angr null #angry
        attribute anno null #annoyed
        attribute cry null  #crying
        attribute curi null #curious
        attribute dist null #distant
        attribute doub null #doubtful
        attribute flus null #flustered
        attribute happ null #happy
        attribute laug null #laughing
        attribute lsur null #surprised (lightly)
        attribute nerv null #nervous
        attribute pani null #panicked
        attribute pout null #pouting
        attribute sad null  #sad
        attribute vsur null #surprised (very)
        attribute worr null #worried
    
    #nose
    group blush:
        attribute nobl default null #default nose. Same than the facebase
        attribute blus null #blush
        attribute awkw null #awkward
        attribute blaw null #blush + awkward

    group center:
        attribute center default if_any(["uniform"]):
            outfit_path + "uniform/crossed.png"
        attribute center default if_any(["casual"]):
            outfit_path + "casual/crossed.png"
        attribute center default if_any(["green_vest"]):
            outfit_path + "green_vest/crossed.png"
        attribute center default if_any(["green_vest_waistline"]):
            outfit_path + "green_vest_waistline/waistline_crossed.png"
        attribute center default if_any(["lab"]):
            outfit_path + "lab/crossed.png"
        attribute center default if_any(["white_shirt"]):
            outfit_path + "white_shirt/crossed.png"

    group nose:

        attribute nose default if_any(["nobl"]): #default
            expressions_path + "nose/default.png"
        attribute nose default if_any(["awkw"]): #awkward
            expressions_path + "nose/awkw.png"
        attribute nose default if_any(["blus"]): #blush
            expressions_path + "nose/blus.png"
        attribute nose default if_any(["blaw"]): #blush + awkward
            expressions_path + "nose/blaw.png"
    
        #Truncated tags
        attribute n1:
            expressions_path + "nose/default.png"
        attribute n2:
            expressions_path + "nose/awkw.png"
        attribute n3:
            expressions_path + "nose/blus.png"
        attribute n4:
            expressions_path + "nose/blaw.png"

    group mouth:

        #Closed mouths
        attribute cm default if_any(["happ", "laug"]):
            expressions_path + "mouths/m1a.png"
        attribute cm default if_any(["neut", "angr", "sad"]):
            expressions_path + "mouths/m1b.png"
        attribute cm default if_any(["curi", "flus", "lsur", "nerv"]):
            expressions_path + "mouths/m1c.png"
        attribute cm default if_any(["doub", "dist", "cry"]):
            expressions_path + "mouths/m1d.png"
        attribute cm default if_any(["pani", "pout", "vsur", "worr"]):
            expressions_path + "mouths/m1e.png"
        attribute cm default if_any(["anno"]):
            expressions_path + "mouths/m2h.png"

        #Opened mouths
        attribute om if_any(["happ", "laug"]):
            expressions_path + "mouths/m2a.png"
        attribute om if_any(["lsur"]):
            expressions_path + "mouths/m2b.png"
        attribute om if_any(["cry"]):
            expressions_path + "mouths/m2c.png"
        attribute om if_any(["neut", "curi", "worr"]):
            expressions_path + "mouths/m2d.png"
        attribute om if_any(["dist", "doub", "pout", "sad"]):
            expressions_path + "mouths/m2e.png"
        attribute om if_any(["vsur"]):
            expressions_path + "mouths/m2f.png"
        attribute om if_any(["pani"]):
            expressions_path + "mouths/m2g.png"
        attribute om if_any(["anno"]):
            expressions_path + "mouths/m2h.png"
        attribute om if_any(["angr"]):
            expressions_path + "mouths/m2i.png"
        attribute om if_any(["flus", "nerv"]):
            expressions_path + "mouths/m2j.png"

        #Truncated tags
        attribute m1a:
            expressions_path + "mouths/m1a.png"
        attribute m1b:
            expressions_path + "mouths/m1b.png"
        attribute m1c:
            expressions_path + "mouths/m1c.png"
        attribute m1d:
            expressions_path + "mouths/m1d.png"
        attribute m1e:
            expressions_path + "mouths/m1e.png"
        attribute m2a:
            expressions_path + "mouths/m2a.png"
        attribute m2b:
            expressions_path + "mouths/m2b.png"
        attribute m2c:
            expressions_path + "mouths/m2c.png"
        attribute m2d:
            expressions_path + "mouths/m2d.png"
        attribute m2e:
            expressions_path + "mouths/m2e.png"
        attribute m2f:
            expressions_path + "mouths/m2f.png"
        attribute m2g:
            expressions_path + "mouths/m2g.png"
        attribute m2h:
            expressions_path + "mouths/m2h.png"
        attribute m2i:
            expressions_path + "mouths/m2i.png"
        attribute m2j:
            expressions_path + "mouths/m2j.png"

    #This group allows you to potentially add flowing tears to Elyssa's face.
    #Just use the attribute 'tears' when showing her.
    #BE AWARE THAT IT'S NOT BEEN TESTED ON ALL THE POSSIBLE EYES COMBINATIONS!
    #If needed, ask me for some quick edits to add to your code :D
    group tears:
        attribute no_tears default null
        attribute tears if_not(["e2c"]): #avoid using on those >_< eyes
            expressions_path + "tears.png"

    #eyes
    group eyes:
        #Opened eyes
        attribute oe default if_any(["neut", "anno", "curi", "doub", "happ", "laug",
                                    "lsur", "worr"]):
            expressions_path + "eyes/e1a.png"
        attribute oe default if_any(["angr", "vsur"]):
            expressions_path + "eyes/e1b.png"
        attribute oe default if_any(["pani"]):
            expressions_path + "eyes/e1c.png"
        attribute oe default if_any(["dist", "flus", "nerv", "pout", "sad"]):
            expressions_path + "eyes/e1d.png"
        attribute oe default if_any(["cry"]):
            expressions_path + "eyes/e1e.png"

        #Closed eyes
        attribute ce if_any(["neut", "angr", "anno", "dist", "doub", "pout", "sad", "worr"]):
            expressions_path + "eyes/e2a.png"
        attribute ce if_any(["curi", "flus", "happ", "laug", "lsur", "nerv"]):
            expressions_path + "eyes/e2b.png"
        attribute ce if_any(["pani", "vsur"]):
            expressions_path + "eyes/e2c.png"
        attribute ce if_any(["cry"]):
            expressions_path + "eyes/e2d.png"
        
        #Truncated tags (for customization)
        #Opened eyes
        attribute e1a:
            expressions_path + "eyes/e1a.png"
        attribute e1b:
            expressions_path + "eyes/e1b.png"
        attribute e1c:
            expressions_path + "eyes/e1c.png"
        attribute e1d:
            expressions_path + "eyes/e1d.png"
        attribute e1e:
            expressions_path + "eyes/e1e.png"

        #Closed eyes
        attribute e2a:
            expressions_path + "eyes/e2a.png"
        attribute e2b:
            expressions_path + "eyes/e2b.png"
        attribute e2c:
            expressions_path + "eyes/e2c.png"
        attribute e2d:
            expressions_path + "eyes/e2d.png"
        
        #Left eye blink (from our POV)
        attribute e3a:
            expressions_path + "eyes/e3a.png"
        #Right eye blink (from our POV)
        attribute e3b:
            expressions_path + "eyes/e3b.png"

    #Blinking group, enabled by default. If you want to completely
    #disable it, remove the 'default' keyword from the 'blink' attribute
    #and write the other one like that 'attribute no_blink default null',
    #or simply use the attribute 'no_blink' in your code.
    group blink:
        attribute no_blink null
        #Not displayed if closed eyes
        attribute blink default if_not(["ce", "e2a", "e2b", "e2c", "e2d", "e3a", "e3b"]):
            "elyssa_blink"

    #Eyebrows
    group eyebrows:
        attribute brow default if_any(["neut", "dist"]): #normal ones
            expressions_path + "eyebrows/ba.png"
        attribute brow default if_any(["happ", "laug", "vsur", "pani"]): #surprised
            expressions_path + "eyebrows/bb.png"
        attribute brow default if_any(["curi", "nerv", "worr"]): #worried
            expressions_path + "eyebrows/bc.png"
        attribute brow default if_any(["anno", "angr"]): #furrowed
            expressions_path + "eyebrows/bd.png"
        attribute brow default if_any(["doub"]): #doubtful
            expressions_path + "eyebrows/be.png"
        attribute brow default if_any(["cry", "flus", "sad"]): #sad
            expressions_path + "eyebrows/bf.png"
        attribute brow default if_any(["lsur", "pout"]): #straight eyebrows
            expressions_path + "eyebrows/bg.png"

        #Truncated tags (for customization)
        attribute ba:
            expressions_path + "eyebrows/ba.png"
        attribute bb:
            expressions_path + "eyebrows/bb.png"
        attribute bc:
            expressions_path + "eyebrows/bc.png"
        attribute bd:
            expressions_path + "eyebrows/bd.png"
        attribute be:
            expressions_path + "eyebrows/be.png"
        attribute bf:
            expressions_path + "eyebrows/bf.png"
        attribute bg:
            expressions_path + "eyebrows/bg.png"

    #Group to add the glasses to Elyssa. Default doesn't have them.
    group accessories:
        attribute no_glasses default null
        attribute glasses:
            expressions_path + "glasses.png"