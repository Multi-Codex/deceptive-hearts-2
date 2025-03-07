init python:

    ######
    #
    # IMPORTANT: the following variable defines the path to your layeredimage folder starting from the
    # game folder, so change it according to your own path!! (here, that would be game/mod_assets/MPT/skinny_mc_mpt/...)
    # Basically, only the part before "skinny_mc_mpt" has to change for your needs to find the assets!
    path = "mod_assets/MPT/skinny_mc_mpt/"

    # Of course, you can still change the layeredimage below to your taste, I tried my best to put
    # everything that would go well together, although there aren't that much expressions for that MC.

    # IF YOU WANT EXPLANATIONS ABOUT HOW LAYEREDIMAGES WORK, PLEASE GO TO LINE 53 :)

    ############
    #
    # If you have the original MPT, please cut/paste both skinnymcref functions below in the
    # 'layeredimage_functions.rpy' file, with the others!!
    #
    # Otherwise, leave it as it is.
    #
    # Don't copy that function if you already have the MPT! It's already in layeredimage_functions.rpy
    #
    ############
    def clear_tag(character, target='master'):
        if not isinstance(character, str): 
            raise Exception("'character' argument must be a string.")
        if not character in renpy.get_showing_tags(layer=target, sort=True):
            return
        pose = str(renpy.get_attributes(character, layer=target)[0])
        if not pose:
            return
        renpy.show(character + " " + pose + " refreshattribute", layer=target)
        renpy.show(character, layer=target)

    # Layered image refreshes (copy both functions below if you have the original MPT)
    def skinnymcref(target="master"):
        if not "skinny_mc" in renpy.get_showing_tags(layer=target, sort=True):
            #If not currently showing this sprite, stop function.
            return

        renpy.show("skinny_mc" + " refreshattribute", layer=target)
        renpy.show("skinny_mc", layer=target)

    # Better cleaning, that function resets the current character back to its default pose and expression
    def skinnymcref(target="master"):
        clear_tag("skinny_mc", target)

    
###
#
# EXPLANATIONS
#
# A layered image is a very useful way to show displayables on screen, and those displayables are separated into
# different parts (most of the time, like in this case, the left/right body parts, a face without any expression,
# eyes, mouths...) which, once put together, create a complete image.
#
# A layeredimage is made up of group statements where each one contains attributes, and those attributes are the
# ones we write in our script to show the image. The 'group' order in the layeredimage shows in which order
# the elements will be added to the image, which can be very important in some cases (i.e Yuri's MPT with left body part)
#
# Each group represents a body part and each attribute represents
# one of these body parts (a specific mouth for example). Here is an example with our skinny mc:

    # show skinny_mc happ rup ldown om ce blus at t11

# 'skinny_mc': name of the character (layeredimage)
# 'happ': the mood (happy, but can be anything listed in the group mood below)
# The mood will use some face elements by default that would fit the best (you can still customize everything)
# rup: the right arm (only for us, because it's the character's left arm) is up (as always, take a look in the layeredimage to understand while reading this)
# ldown: the left arm (only for us, because it's the character's right arm) is down
# om: opened mouth (the one used with the 'happ' mood, but as I said, you can change it, using the truncated tags (line 228))
# ce: closed eyes (the ones used with the 'happ' mood (truncated tags line 241))
# blus: blush (a simple sweat drop in that case, but there is a full blushing attribute as well, which is 'blaw')

# Truncated tags are attributes unrelated to the mood you've chosen. That said, you can customize expressions
# (although that could look weird sometimes of course, but as always, truncated tags are mentioned below in comments
# of each group). If we use the example above, putting ce3 isntead of ce for the closed eyes will use these specific
# eyes instead of the default one used with the 'happ' mood. Same goes for basically everything related to the face.
#
#####
#
# IMPORTANT TO NOTE FOR EASE OF USE: the order in which you write the attributes doesn't matter, apart from 
# the layeredimage name, and the mood that still have to be the first ones. Another thing, when you write a mood
# or anything, you don't need to write it again on the next show statement: you can for example write the new mood 
# you want to use, and the current mood will be replaced with that new one.
#
#####

layeredimage skinny_mc turned:


    at [renpy.partial(Flatten, drawable_resolution=False), AutofocusDisplayable(name="skinny_mc turned")]


    always path + "facebase/facebase.png"


    group mood:
        attribute neut default null #default face
        attribute happ null #happy
        attribute angr null #angry
        attribute vang null #very angry
        attribute sad null
        attribute laug null #laughing
        attribute cry null 
        attribute doub null #doubtful
        attribute anxi null #anxious
        attribute pani null #shocked eyes
        attribute shoc null #shocked eyes and cry
        attribute mean null #when mc is a meanie (mischievous smile)
        attribute surp null #surprised


    #Some blushes, even though that character only really have two elements relative to the blush
    group blush:
        attribute nobl default null #nothing
        attribute awkw null #Face blush
        attribute blus null #Simple sweat drop on the cheek
        attribute blaw null #Face blush and sweat drop


    #Left body part
    group left:
        attribute ldown default:
            path + "body/1l.png"
        attribute lup:
            path + "body/2l.png"


    #Right body part
    group right:
        attribute rdown default:
            path + "body/1r.png"
        attribute rhip:
            path + "body/2r.png"


    #images depending of the 'group blush' attributes used above
    group nose:
        #Default noses
        attribute nose default if_any(["awkw"]):
            path + "blush/blush.png"
        attribute nose default if_any(["blus"]):
            path + "blush/sweat_drop.png"
        attribute nose default if_any(["blaw"]):
            path + "blush/blaw.png"

        #All noses - Truncated tags (use them if you wish to personalize the expression with other facial elements)
        attribute n1:
            path + "blush/sweat_drop.png"
        attribute n2:
            path + "blush/blush.png"
        attribute n3:
            path + "blush/blaw.png"
    

    #Eyes 
    group eyes:
        #Default opened eyes depending on mood
        attribute oe default if_any(["neut", "happ", "doub", "laug"]):
            path + "eyes/opened_eyes_1.png"
        attribute oe default if_any(["sad"]):
            path + "eyes/opened_eyes_2.png"
        attribute oe default if_any(["pani", "vang", "mean"]):
            path + "eyes/opened_eyes_3.png"
        attribute oe default if_any(["shoc"]):
            path + "eyes/opened_eyes_4.png"
        attribute oe default if_any(["anxi", "angr", "surp"]):
            path + "eyes/opened_eyes_5.png"
        attribute oe default if_any(["cry"]):
            path + "eyes/opened_eyes_6.png"

        #Default closed eyes depending on mood
        attribute ce if_any(["neut", "doub", "angr", "vang", "pani", "anxi"]):
            path + "eyes/closed_eyes_1.png"
        attribute ce if_any(["sad", "cry", "shoc"]):
            path + "eyes/closed_eyes_2.png"
        attribute ce if_any(["happ", "laug", "mean", "surp"]):
            path + "eyes/closed_eyes_3.png"

        #All eyes - Truncated tags (use them if you wish to personalize the expression with other facial elements)
        #Opened eyes
        attribute oe1:
            path + "eyes/opened_eyes_1.png"
        attribute oe2:
            path + "eyes/opened_eyes_2.png"
        attribute oe3:
            path + "eyes/opened_eyes_3.png"
        attribute oe4:
            path + "eyes/opened_eyes_4.png"
        attribute oe5:
            path + "eyes/opened_eyes_5.png"
        attribute oe6:
            path + "eyes/opened_eyes_6.png"

        #Closed eyes
        attribute ce1:
            path + "eyes/closed_eyes_1.png"
        attribute ce2:
            path + "eyes/closed_eyes_2.png"
        attribute ce3:
            path + "eyes/closed_eyes_3.png"

    
    #Mouths
    group mouth:
        #Opened mouths
        attribute om if_any(["happ", "laug"]):
            path + "mouth/laugh.png"
        attribute om if_any(["cry", "anxi", "shoc", "pani", "surp"]):
            path + "mouth/vsurp.png"
        attribute om if_any(["mean"]):
            path + "mouth/wide_smile.png"
        attribute om if_any(["neut", "sad", "doub"]):
            path + "mouth/open_mouth.png"
        attribute om if_any(["angr", "vang"]):
            path + "mouth/grit_teeth.png"

        #Closed mouths
        attribute cm default if_any(["neut", "happ", "laug"]):
            path + "mouth/smile.png"
        attribute cm default if_any(["sad", "cry", "mean", "anxi", "angr"]):
            path + "mouth/sad.png"
        attribute cm default if_any(["shoc", "pani", "doub", "vang", "surp"]):
            path + "mouth/surp.png"

        #All mouths - Trucated tags (use them if you wish to personalize the expression with other facial elements)
        #Opened mouths
        attribute om1:
            path + "mouth/open_mouth.png"
        attribute om2:
            path + "mouth/laugh.png"
        attribute om3:
            path + "mouth/vsurp.png"
        attribute om4:
            path + "mouth/wide_smile.png"
        attribute om5:
            path + "mouth/grit_teeth.png"
        
        #Closed mouths
        attribute cm1:
            path + "mouth/smile.png"
        attribute cm2:
            path + "mouth/sad.png"
        attribute cm3:
            path + "mouth/surp.png"

    
    #Eyebrows
    group eyebrows:
        
        #Default eyebrows
        attribute brow default if_any(["neut", "doub"]):
            path + "eyebrows/eyebrows_1.png"
        attribute brow default if_any(["sad", "cry", "anxi", "pani"]):
            path + "eyebrows/eyebrows_2.png"
        attribute brow default if_any(["surp", "happ", "laug", "shoc"]):
            path + "eyebrows/eyebrows_3.png"
        attribute brow default if_any(["angr", "vang", "mean"]):
            path + "eyebrows/eyebrows_4.png"

        #All eyebrows - Trucated tags (use them if you wish to personalize the expression with other facial elements)
        attribute brow1:
            path + "eyebrows/eyebrows_1.png"
        attribute brow2:
            path + "eyebrows/eyebrows_2.png"
        attribute brow3:
            path + "eyebrows/eyebrows_3.png"
        attribute brow4:
            path + "eyebrows/eyebrows_4.png"

#This is it :)