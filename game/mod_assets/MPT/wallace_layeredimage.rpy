init python:

    path = "mod_assets/MPT/wallace_reborn_MPT/" ### Global path to the folder of Wallace's MPT
                                                ### That way, you can change it easily without replacing everything!


layeredimage wallace forward: #Front-facing Wallace

    at renpy.partial(Flatten, drawable_resolution=False)

    always path + "facebases/facebase.png"

    group outfit: # 2 outfits: normal uniform and a dark remake of it

        attribute uniform default null
        attribute casual null

    group mood: #Mood determines what the defaults images are for the following attributes:
                #"oe", "ce", "om", "cm", "brow".
        attribute neut default null #neutral
        attribute angr null #angry
        attribute anno null #annoyed
        attribute curi null #curious
        attribute dist null #distant 
        attribute doub null #doubtful
        attribute flus null #flustered
        attribute happ null #happy
        attribute laug null #laughing
        attribute lsur null #surprised (lightly)
        attribute nerv null #nervous
        attribute pout null #pouting
        attribute sad null  #sad
        attribute shoc null #shocked
        attribute vsur null #surprised (very)
        attribute vang null #angry (very)
        attribute worr null #worried
        attribute yand null #yandere 

    group blush:
        attribute nobl default null #default, no blush
        attribute awkw null #sweat drop
        attribute blus null #slight blush
        attribute blaw null #sweat drop + slight blush
        attribute bful null #full face blush.
        attribute bful_cover null #If you want the full face blush to cover the face, except the mouth

    group left: #left arm
        attribute ldown default if_any(["uniform"]):
            path + "body/1l.png"
        attribute ldown default if_any(["casual"]):
            path + "body/1bl.png"
        attribute lhip if_any(["uniform"]):
            path + "body/2l.png"
        attribute lhip if_any(["casual"]):
            path + "body/2bl.png"

    group right: #right arm
        attribute rdown default if_any(["uniform"]):
            path + "body/1r.png"
        attribute rdown default if_any(["casual"]):
            path + "body/1br.png"
        attribute rhip if_any(["uniform"]):
            path + "body/2r.png"
        attribute rhip if_any(["casual"]):
            path + "body/2br.png"


    group nose: #default blushes

        anchor (0,0) subpixel (True)

        attribute nose default if_any(["nobl"]) null #no blush default

        attribute nose default if_any(["awkw"]): #awkward
            path + "nose_forward/awkw.png"
        attribute nose default if_any(["blus"]): #blushing
            path + "nose_forward/blus.png"
        attribute nose default if_any(["blaw"]): #blushing + awkward
            path + "nose_forward/blaw.png"
        attribute nose default if_any(["bful"]): #full face blush
            path + "nose_forward/bful.png"

        ###Truncated tags (use if you want custom expressions)
        attribute n1:
            path + "nose_forward/awkw.png"
        attribute n2:
            path + "nose_forward/blus.png"
        attribute n3:
            path + "nose_forward/blaw.png"
        attribute n4:
            path + "nose_forward/bful.png"

    ###Mouth
    group mouth:

        anchor (0,0) subpixel (True)

        ###Closed mouths
        attribute cm default if_any(["happ", "laug", "yand"]): #smiling
            path + "mouth_forward/m1a.png"
        attribute cm default if_any(["neut", "anno", "angr", "dist", "doub", "pout", "sad", "shoc", "vsur", "worr"]): #not smiling
            path + "mouth_forward/m1b.png"
        attribute cm default if_any(["curi", "lsur", "flus", "nerv", "vang"]): #barely opened
            path + "mouth_forward/m2b.png"

        ###Opened mouths
        attribute om if_any(["happ", "laug", "yand", "flus", "neut", "lsur", "nerv"]): #talking/smiling
            path + "mouth_forward/m2a.png"
        attribute om if_any(["anno", "dist", "pout", "sad", "curi"]): #barely opened
            path + "mouth_forward/m2b.png"
        attribute om if_any(["angr", "shoc", "vsur", "doub", "worr", "vang"]): #angry
            path + "mouth_forward/m2c.png"

        ###Truncated tags (use if you want custom expressions)
        attribute ma:
            path + "mouth_forward/m1a.png"
        attribute mb:
            path + "mouth_forward/m1b.png"
        attribute mc:
            path + "mouth_forward/m2a.png"
        attribute md:
            path + "mouth_forward/m2b.png"
        attribute me:
            path + "mouth_forward/m2c.png"


    ###Eyes
    group eyes:

        anchor (0,0) subpixel (True)

        ###Opened eyes
        attribute oe default if_any(["neut", "angr", "lsur", "anno"]):  #neutral eyes
            path + "eyes_forward/e1a.png"
        attribute oe default if_any(["happ", "laug", "curi", "vsur", "worr"]): #wide open eyes
            path + "eyes_forward/e1b.png"
        attribute oe default if_any(["doub", "dist", "pout"]): #side eyes
            path + "eyes_forward/e1c.png"
        attribute oe default if_any(["sad", "flus", "nerv"]): #wide open side eyes
            path + "eyes_forward/e1d.png"
        attribute oe default if_any(["yand", "vang", "shoc"]): #yandere/very angry eyes
            path + "eyes_forward/e1e.png"

        ###Closed eyes
        attribute ce if_any(["neut", "angr", "anno", "worr", "doub",
                            "dist", "pout", "sad", "nerv", "vang", "shoc"]): #'sad' closed eyes
            path + "eyes_forward/e2a.png"
        attribute ce if_any(["happ", "lsur", "vsur", "laug", "curi", "flus", "yand"]): #'happy' closed eyes
            path + "eyes_forward/e2b.png"

        ###Truncated tags (use if you want custom expressions)
        ##Opened eyes
        attribute e1a:
            path + "eyes_forward/e1a.png"
        attribute e1b:
            path + "eyes_forward/e1b.png"
        attribute e1c:
            path + "eyes_forward/e1c.png"
        attribute e1d:
            path + "eyes_forward/e1d.png"
        attribute e1e:
            path + "eyes_forward/e1e.png"

        ##Closed eyes
        attribute e2a:
            path + "eyes_forward/e2a.png"
        attribute e2b:
            path + "eyes_forward/e2b.png"


    ###Eyebrows
    group eyebrows:

        anchor (0,0) subpixel (True)

        attribute brow default if_any(["neut", "lsur", "dist"]): #normal eyebrows
            path + "eyebrows_forward/ba.png"
        attribute brow default if_any(["happ", "laug", "vsur", "yand", "curi"]): #raised eyebrows
            path + "eyebrows_forward/bb.png"
        attribute brow default if_any(["angr", "vang", "anno", "pout", "doub"]): #frowning eyebrows
            path + "eyebrows_forward/bc.png"
        attribute brow default if_any(["worr", "sad", "nerv", "shoc", "flus"]): #worried/sad eyebrows
            path + "eyebrows_forward/bd.png"

        ###Truncated tags (use if you want custom expressions)
        attribute ba:
            path + "eyebrows_forward/ba.png"
        attribute bb:
            path + "eyebrows_forward/bb.png"
        attribute bc:
            path + "eyebrows_forward/bc.png"
        attribute bd:
            path + "eyebrows_forward/bd.png"
        

    group blush_full: ##This group is the last of the layeredimage in order for the full face blush
                        #to cover the face entirely, except the mouth

        attribute nose default if_any(["bful_cover"]):
            path + "nose_forward/bful.png"



layeredimage wallace turned: #Wallace with his head turned a bit

    at renpy.partial(Flatten, drawable_resolution=False)

    group outfit: # 2 outfits: normal uniform and a dark remake of it

        attribute uniform default null
        attribute casual null

    group mood: #Mood determines what the defaults images are for the following attributes:
                #"oe", "ce", "om", "cm", "brow".
        attribute neut default null #neutral
        attribute angr null #angry
        attribute anno null #annoyed
        attribute curi null #curious
        attribute dist null #distant 
        attribute doub null #doubtful
        attribute flus null #flustered
        attribute happ null #happy
        attribute laug null #laughing
        attribute lsur null #surprised (lightly)
        attribute nerv null #nervous
        attribute pout null #pouting
        attribute sad null  #sad
        attribute shoc null #shocked
        attribute vsur null #surprised (very)
        attribute vang null #angry (very)
        attribute worr null #worried
        attribute yand null #yandere 

    group blush:
        attribute nobl default null #default, no blush
        attribute awkw null #sweat drop
        attribute blus null #slight blush
        attribute blaw null #sweat drop + slight blush
        attribute bful null #full face blush.
        attribute bful_cover null #If you want the full face blush to cover the face, except the mouth

    group left: #left arm
        attribute ldown default if_any(["uniform"]):
            path + "body/1l.png"
        attribute ldown default if_any(["casual"]):
            path + "body/1bl.png"
        attribute lhip if_any(["uniform"]):
            path + "body/2l.png"
        attribute lhip if_any(["casual"]):
            path + "body/2bl.png"

    group right: #right arm
        attribute rdown default if_any(["uniform"]):
            path + "body/1r.png"
        attribute rdown default if_any(["casual"]):
            path + "body/1br.png"
        attribute rhip if_any(["uniform"]):
            path + "body/2r.png"
        attribute rhip if_any(["casual"]):
            path + "body/2br.png"


    ###His head is added after his body in order for the sprite to look good.
    ###If his head was added before his body, it'd look like his throat's been cut or something
    always path + "facebases/facebase_side.png"


    group nose: #default blushes

        anchor (0,0) subpixel (True)

        attribute nose default if_any(["nobl"]) null #no blush default

        attribute nose default if_any(["awkw"]): #awkward
            path + "nose_side/awkw.png"
        attribute nose default if_any(["blus"]): #blushing
            path + "nose_side/blus.png"
        attribute nose default if_any(["blaw"]): #blushing + awkward
            path + "nose_side/blaw.png"
        attribute nose default if_any(["bful"]): #full face blush
            path + "nose_side/bful.png"

        ###Truncated tags (use if you want custom expressions)
        attribute n1:
            path + "nose_side/awkw.png"
        attribute n2:
            path + "nose_side/blus.png"
        attribute n3:
            path + "nose_side/blaw.png"
        attribute n4:
            path + "nose_side/bful.png"

    ###Mouth
    group mouth:

        anchor (0,0) subpixel (True)

        ###Closed mouths
        attribute cm default if_any(["happ", "laug", "yand", "flus"]): #smiling
            path + "mouth_side/m1a.png"
        attribute cm default if_any(["neut", "lsur", "curi", "anno", "angr", "dist", "doub", "pout"]): #neutral
            path + "mouth_side/m1b.png"
        attribute cm default if_any(["sad", "nerv", "vang", "shoc", "worr", "vsur"]): #not smiling
            path + "mouth_side/m1c.png"

        ###Opened mouths
        attribute om if_any(["happ", "laug", "yand", "flus", "neut", "lsur", "nerv"]): #talking/smiling
            path + "mouth_side/m2a.png"
        attribute om if_any(["anno", "dist", "pout", "sad", "curi"]): #barely opened
            path + "mouth_side/m2b.png"
        attribute om if_any(["angr", "shoc", "vsur", "doub", "worr", "vang"]): #angry
            path + "mouth_side/m2c.png"

        ###Truncated tags (use if you want custom expressions)
        attribute ma:
            path + "mouth_side/m1a.png"
        attribute mb:
            path + "mouth_side/m1b.png"
        attribute mc:
            path + "mouth_side/m2a.png"
        attribute md:
            path + "mouth_side/m2b.png"
        attribute me:
            path + "mouth_side/m2c.png"


    ###Eyes
    group eyes:

        anchor (0,0) subpixel (True)

        ###Opened eyes
        attribute oe default if_any(["neut", "angr", "lsur", "anno"]):  #neutral eyes
            path + "eyes_side/e1a.png"
        attribute oe default if_any(["happ", "laug", "curi", "vsur", "worr"]): #wide open eyes
            path + "eyes_side/e1b.png"
        attribute oe default if_any(["doub", "dist", "pout"]): #side eyes
            path + "eyes_side/e1c.png"
        attribute oe default if_any(["sad", "flus", "nerv"]): #wide open side eyes
            path + "eyes_side/e1d.png"
        attribute oe default if_any(["yand", "vang", "shoc"]): #yandere/very angry eyes
            path + "eyes_side/e1e.png"

        ###Closed eyes
        attribute ce if_any(["neut", "angr", "anno", "worr", "doub",
                            "dist", "pout", "sad", "nerv", "vang", "shoc"]): #'sad' closed eyes
            path + "eyes_side/e2a.png"
        attribute ce if_any(["happ", "lsur", "vsur", "laug", "curi", "flus", "yand"]): #'happy' closed eyes
            path + "eyes_side/e2b.png"

        ###Truncated tags (use if you want custom expressions)
        ##Opened eyes
        attribute e1a:
            path + "eyes_side/e1a.png"
        attribute e1b:
            path + "eyes_side/e1b.png"
        attribute e1c:
            path + "eyes_side/e1c.png"
        attribute e1d:
            path + "eyes_side/e1d.png"
        attribute e1e:
            path + "eyes_side/e1e.png"

        ##Closed eyes
        attribute e2a:
            path + "eyes_side/e2a.png"
        attribute e2b:
            path + "eyes_side/e2b.png"


    ###Eyebrows
    group eyebrows:

        anchor (0,0) subpixel (True)

        attribute brow default if_any(["neut", "lsur", "dist"]): #normal eyebrows
            path + "eyebrows_side/ba.png"
        attribute brow default if_any(["happ", "laug", "vsur", "yand", "curi"]): #raised eyebrows
            path + "eyebrows_side/bb.png"
        attribute brow default if_any(["vang", "anno", "pout"]): #heavily furrowed eyebrows
            path + "eyebrows_side/bc.png"
        attribute brow default if_any(["angr", "doub"]): #slightly frowning eyebrows
            path + "eyebrows_side/bd.png"
        attribute brow default if_any(["worr", "sad", "nerv", "shoc", "flus"]): #worried/sad eyebrows
            path + "eyebrows_side/be.png"

        ###Truncated tags (use if you want custom expressions)
        attribute ba:
            path + "eyebrows_side/ba.png"
        attribute bb:
            path + "eyebrows_side/bb.png"
        attribute bc:
            path + "eyebrows_side/bc.png"
        attribute bd:
            path + "eyebrows_side/bd.png"
        attribute be:
            path + "eyebrows_side/be.png"
        

    group blush_full: ##This group is the last of the layeredimage in order for the full face blush
                        #to cover the face entirely, except the mouth

        attribute nose default if_any(["bful_cover"]):
            path + "nose_side/bful.png"