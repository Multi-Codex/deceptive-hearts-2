
#Because of how amy's faces are able to interchange across poses - unlike everyone else - her logic and coding is different.  First off, to try and cut down on having definitions repeated and in so many places across the script, the first block of code here are a bunch of in-between image definitions that the rest of the definitions use below.  This was done so that if something needed to be changed in the file path/structure/whatnot, there is *one* place to fix it, and not 2 or more.
#The tags used for the image definitions themselves are referenced later in this doc, where they're necessary to be used.  Since the tags themselves are short enough and unique enough in name, if changes need to be enacted on *those* parts of the code, a find/replace will be quicker to do.

#First block is for the "forward" face attributes:

image amy_ff_n1:
    "mod_assets/MPT/amy/amy_turned_nose_n1.png"
image amy_ff_n2:
    "mod_assets/MPT/amy/amy_turned_nose_n2.png"
image amy_ff_n3:
    "mod_assets/MPT/amy/amy_turned_nose_n3.png"
image amy_ff_n4:
    "mod_assets/MPT/amy/amy_turned_nose_n4.png"



image amy_ff_ma:
    "mod_assets/MPT/amy/amy_turned_mouth_ma.png"
image amy_ff_mb:
    "mod_assets/MPT/amy/amy_turned_mouth_mb.png"
image amy_ff_mc:
    "mod_assets/MPT/amy/amy_turned_mouth_mc.png"
image amy_ff_md:
    "mod_assets/MPT/amy/amy_turned_mouth_md.png"
image amy_ff_me:
    "mod_assets/MPT/amy/amy_turned_mouth_me.png"
image amy_ff_mf:
    "mod_assets/MPT/amy/amy_turned_mouth_mf.png"
image amy_ff_mg:
    "mod_assets/MPT/amy/amy_turned_mouth_mg.png"
image amy_ff_mh:
    "mod_assets/MPT/amy/amy_turned_mouth_mh.png"
image amy_ff_mi:
    "mod_assets/MPT/amy/amy_turned_mouth_mi.png"
image amy_ff_mj:
    "mod_assets/MPT/amy/amy_turned_mouth_mj.png"
image amy_ff_mk:
    "mod_assets/MPT/amy/amy_turned_mouth_mk.png"
image amy_ff_ml:
    "mod_assets/MPT/amy/amy_turned_mouth_ml.png"

image amy_ff_e1a:
    "mod_assets/MPT/amy/amy_turned_eyes_e1a.png"
image amy_ff_e1b:
    "mod_assets/MPT/amy/amy_turned_eyes_e1b.png"
image amy_ff_e1c:
    "mod_assets/MPT/amy/amy_turned_eyes_e1c.png"
image amy_ff_e1d:
    "mod_assets/MPT/amy/amy_turned_eyes_e1d.png"
image amy_ff_e1e:
    "mod_assets/MPT/amy/amy_turned_eyes_e1e.png"
image amy_ff_e1f:
    "mod_assets/MPT/amy/amy_turned_eyes_e1f.png"
image amy_ff_e1g:
    "mod_assets/MPT/amy/amy_turned_eyes_e1g.png"
image amy_ff_e1h:
    "mod_assets/MPT/amy/amy_turned_eyes_e1h.png"
image amy_ff_e1i:
    "mod_assets/MPT/amy/amy_turned_eyes_e1i.png"
image amy_ff_e1j:
    "mod_assets/MPT/amy/amy_turned_eyes_e1j.png"
image amy_ff_e1k:
    "mod_assets/MPT/amy/amy_turned_eyes_e1k.png"



image amy_ff_b1a:
    "mod_assets/MPT/amy/amy_turned_eyebrows_b1a.png"
image amy_ff_b1b:
    "mod_assets/MPT/amy/amy_turned_eyebrows_b1b.png"
image amy_ff_b1c:
    "mod_assets/MPT/amy/amy_turned_eyebrows_b1c.png"
image amy_ff_b1d:
    "mod_assets/MPT/amy/amy_turned_eyebrows_b1d.png"
image amy_ff_b1e:
    "mod_assets/MPT/amy/amy_turned_eyebrows_b1e.png"

layeredimage amy turned:

    at [renpy.partial(Flatten, drawable_resolution=False)]
    
    
    
    group outfit:
        attribute uniform default null
        attribute casual null
    
    
    
    group mood: #Mood determines what the defaults images are for the following attributes:
        #"oe", "ce", "om", "cm", "brow".
        #By changing what the "mood" attribute is, you can easily switch between premade sets of expressions that work well together, speeding up your workflow.
        #Additionally, you can add in any new ones as you like.
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
        attribute sedu null #seductive
        attribute shoc null #shocked
        attribute vang null #VERY angry
        attribute vsur null #surprised (very)
        attribute worr null #worried
        attribute yand null #yandere
        #attribute xxxx null #xxxx #Do you want to define a new mood?  Here, have a template!
    
    
    
    group blush: #state of her nose/blush.
        attribute nobl default null #no blush or tear drop.
        attribute awkw null #awkward.  defaults for n
        attribute blus null #blushing.  defaults for n
        attribute blaw null #blushing AND awkward.  defaults for n
        attribute bful null #full face blush.  Currently only works on the side face.
    
    
    

    
    
    
    group head: #This needs to render above her body for her "turned" pose.
        
        anchor (0,0) subpixel (True)
        
        attribute ff default:
            "mod_assets/MPT/amy/amy_turned_facebase.png"
    
    
    #######First set of definitions is for amy's "Forward" face.
  
    group mouth if_all(["ff"]):
        
        anchor (0,0) subpixel (True)
        
        ###Default Closed Mouths:
        attribute cm default if_any(["happ","sedu","nerv","laug","yand"]):
            "amy_ff_ma"
        attribute cm default if_any(["neut","anno","worr","sad","angr","vsur","dist","doub"]):
            "amy_ff_md"
        attribute cm default if_any(["pout","curi","flus","lsur","shoc"]):
            "amy_ff_me"
        attribute cm default if_any(["vang","pani","cry"]):
            "amy_ff_mi"
        attribute cm default if_any(["yand"]):
            "amy_ff_mk"
        
        ###Default Open Mouths:
        attribute om if_any(["sedu","nerv"]):
            "amy_ff_mb"
        attribute om if_any(["happ","laug"]):
            "amy_ff_mc"
        attribute om if_any(["anno","lsur","neut","curi"]):
            "amy_ff_mg"
        attribute om if_any(["sad","dist","pout","worr"]):
            "amy_ff_mh"
        attribute om if_any(["doub","angr","vsur","flus","shoc","cry","awkw"]):
            "amy_ff_mf"
        attribute om if_any(["vang","pani"]):
            "amy_ff_mj"
        attribute om if_any(["yand"]):
            "amy_ff_ml"
        
        ###All mouths - truncated tags:
        attribute ma:
            "amy_ff_ma"
        attribute mb:
            "amy_ff_mb"
        attribute mc:
            "amy_ff_mc"
        attribute md:
            "amy_ff_md"
        attribute me:
            "amy_ff_me"
        attribute mf:
            "amy_ff_mf"
        attribute mg:
            "amy_ff_mg"
        attribute mh:
            "amy_ff_mh"
        attribute mi:
            "amy_ff_mi"
        attribute mj:
            "amy_ff_mj"
        attribute mk:
            "amy_ff_mk"
        attribute ml:
            "amy_ff_ml"
    
    
    
    group eyes if_all(["ff"]):
        
        anchor (0,0) subpixel (True)
        
        ###Default Opened eyes:
        attribute oe default if_any(["neut","happ","laug","pout","curi","lsur"]):
            "amy_ff_e1a"
        attribute oe default if_any(["sad","worr","flus"]):
            "amy_ff_e1b"
        attribute oe default if_any(["dist"]):
            "amy_ff_e1c"
        attribute oe default if_any(["anno","sedu","doub"]):
            "amy_ff_e1d"
        attribute oe default if_any(["cry"]):
            "amy_ff_e1i"
        attribute oe default if_any(["angr","nerv"]):
            "amy_ff_e1e"
        attribute oe default if_any(["vang","vsur","pani","shoc","yand"]):
            "amy_ff_e1f"

        ###Default Closed eyes:
        attribute ce if_any(["sad","worr","anno","angr","vang","flus","dist","sedu","nerv","doub","curi","lsur","neut"]):
            "amy_ff_e1g"
        attribute ce if_any(["happ","laug","yand","pout","vsur"]):
            "amy_ff_e1h"
        attribute ce if_any(["shoc","pani"]):
            "amy_ff_e1h"
        attribute ce if_any(["cry"]):
            "amy_ff_e1g"
        
        
        ###All eyes - truncated tags:
        attribute e1a:
            "amy_ff_e1a"
        attribute e1b:
            "amy_ff_e1b"
        attribute e1c:
            "amy_ff_e1c"
        attribute e1d:
            "amy_ff_e1d"
        attribute e1e:
            "amy_ff_e1e"
        attribute e1f:
            "amy_ff_e1f"
        attribute e1g:
            "amy_ff_e1g"
        attribute e1h:
            "amy_ff_e1h"
        attribute e1i:
            "amy_ff_e1i"
        attribute e1j:
            "amy_ff_e1j"
        attribute e1k:
            "amy_ff_e1k"
    
    group nose if_all(["ff"]):
        
        anchor (0,0) subpixel (True)
        
        ###Default nose/blush
        attribute nose default if_any(["nobl"]):
            "amy_ff_n1"
        attribute nose if_any(["awkw","pani","worr","nerv"]):
            "amy_ff_n3"
        attribute nose if_any(["blus","sedu"]):
            "amy_ff_n2"
        attribute nose if_any(["blaw","flus"]):
            "amy_ff_n4"
        
        
        
        ###All noses - truncated tags:
        attribute n1:
            "amy_ff_n1"
        attribute n2:
            "amy_ff_n2"
        attribute n3:
            "amy_ff_n3"
        attribute n4:
            "amy_ff_n4"



    group eyebrows if_all(["ff"]) if_not(["fta","fs"]): #eyebrows.
        
        anchor (0,0) subpixel (True)
        
        #Default Eyebrows:
        attribute brow default if_any(["neut","sedu"]):
            "amy_ff_b1a"
        attribute brow default if_any(["sad","pani","flus","pout","nerv","cry","dist"]):
            "amy_ff_b1d"
        attribute brow default if_any(["happ","worr","shoc","vsur","curi"]):
            "amy_ff_b1b"
        attribute brow default if_any(["curi","doub","worr"]):
            "amy_ff_b1c"
        attribute brow default if_any(["lsur"]):
            "amy_ff_b1b"
        attribute brow default if_any(["angr","anno","vang"]):
            "amy_ff_b1e"        
    
    
    
    
    group eyebrows if_all(["ff"]) if_not(["fta","fs"]):
        
        anchor (0,0) subpixel (True)
        
        ###All eyebrows - truncated tags:
        attribute b1a:
            "amy_ff_b1a"
        attribute b1b:
            "amy_ff_b1b"
        attribute b1c:
            "amy_ff_b1c"
        attribute b1d:
            "amy_ff_b1d"
        attribute b1e:
            "amy_ff_b1e"
    
    
    
    #This group is intentionally last on this list, so it will render over top of every other thing on the face.
    group broken if_all(["ff"]) if_not(["fta","fs"]):
        
        anchor (0,0) subpixel (True)
        
        attribute br1a:
            "mod_assets/MPT/amy/amy_broken_1a.png"
        attribute br1b:
            "mod_assets/MPT/amy/amy_broken_1b.png"
        attribute br1c:
            "mod_assets/MPT/amy/amy_broken_1c.png"
        attribute br1d:
            "mod_assets/MPT/amy/amy_broken_1d.png"


    group left: #Left arm.
        anchor (0,0) subpixel (True)
        yoffset (-0.5)
        attribute ldown default if_any(["uniform"]):
            "mod_assets/MPT/amy/amy_turned_uniform_left_down.png"
        attribute ldown default if_any(["casual"]):
            "mod_assets/MPT/amy/amy_turned_casual_left_down.png"
        attribute lback if_any(["uniform"]):
            "mod_assets/MPT/amy/amy_turned_uniform_left_back.png"
        attribute lback if_any(["casual"]):
            "mod_assets/MPT/amy/amy_turned_casual_left_back.png"
        attribute lneck if_any(["uniform"]):
            "mod_assets/MPT/amy/amy_turned_uniform_left_neck.png"
        attribute lneck if_any(["casual"]):
            "mod_assets/MPT/amy/amy_turned_casual_left_neck.png"
        attribute lspecs if_any(["uniform"]):
            "mod_assets/MPT/amy/amy_turned_uniform_left_specs.png"
        attribute lspecs if_any(["casual"]):
            "mod_assets/MPT/amy/amy_turned_casual_left_specs.png"        
    
    
    
    group right: #right half of her body.
        anchor (0,0) subpixel (True)
        yoffset (-0.5)
        attribute rdown default if_any(["uniform"]):
            "mod_assets/MPT/amy/amy_turned_uniform_right_down.png"
        attribute rdown default if_any(["casual"]):
            "mod_assets/MPT/amy/amy_turned_casual_right_down.png"
        attribute rback if_any(["uniform"]):
            "mod_assets/MPT/amy/amy_turned_uniform_right_back.png"
        attribute rback if_any(["casual"]):
            "mod_assets/MPT/amy/amy_turned_casual_right_back.png"
    
layeredimage amy cross:
    
    at [renpy.partial(Flatten, drawable_resolution=False)]
    
    group outfit:
        attribute uniform default null
        attribute casual null
    
    
    
    group mood: #Mood determines what the defaults images are for the following attributes:
        #"oe", "ce", "om", "cm", "brow".
        #By changing what the "mood" attribute is, you can easily switch between premade sets of expressions that work well together, speeding up your workflow.
        #Additionally, you can add in any new ones as you like.
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
        attribute sedu null #seductive
        attribute shoc null #shocked
        attribute vang null #VERY angry
        attribute vsur null #surprised (very)
        attribute worr null #worried
        attribute yand null #yandere
        #attribute xxxx null #xxxx #Do you want to define a new mood?  Here, have a template!
    
    
    
    group blush: #state of her nose/blush.
        attribute nobl default null #no blush or tear drop.
        attribute awkw null #awkward.  defaults for n
        attribute blus null #blushing.  defaults for n
        attribute blaw null #blushing AND awkward.  defaults for n
        attribute bful null #full face blush.  Currently only works on the side face.
    
    
    
    group body: #The body.
        anchor (0,0) subpixel (True)
        yoffset (-0.5)
        attribute up default if_any(["uniform"]):
            "mod_assets/MPT/amy/amy_cross_uniform_up.png"   
        attribute up default if_any(["casual"]):
            "mod_assets/MPT/amy/amy_cross_casual_up.png"      
        attribute down if_any(["uniform"]):
            "mod_assets/MPT/amy/amy_cross_uniform_down.png"  
        attribute down if_any(["casual"]):
            "mod_assets/MPT/amy/amy_cross_casual_down.png"              

    group head: #This needs to render above her body for her "turned" pose.
        
        anchor (0,0) subpixel (True)
        
        attribute ff default:
            "mod_assets/MPT/amy/amy_turned_facebase.png"
    
    
    #######First set of definitions is for amy's "Forward" face.
    
    
    
    group mouth if_all(["ff"]):
        
        anchor (0,0) subpixel (True)
        
        ###Default Closed Mouths:
        attribute cm default if_any(["happ","sedu","nerv","laug","yand"]):
            "amy_ff_ma"
        attribute cm default if_any(["neut","anno","worr","sad","angr","vsur","dist","doub"]):
            "amy_ff_md"
        attribute cm default if_any(["pout","curi","flus","lsur","shoc"]):
            "amy_ff_me"
        attribute cm default if_any(["vang","pani","cry"]):
            "amy_ff_mi"
        attribute cm default if_any(["yand"]):
            "amy_ff_mk"
        
        ###Default Open Mouths:
        attribute om if_any(["sedu","nerv"]):
            "amy_ff_mb"
        attribute om if_any(["happ","laug"]):
            "amy_ff_mc"
        attribute om if_any(["anno","lsur","neut","curi"]):
            "amy_ff_mg"
        attribute om if_any(["sad","dist","pout","worr"]):
            "amy_ff_mh"
        attribute om if_any(["doub","angr","vsur","flus","shoc","cry","awkw"]):
            "amy_ff_mf"
        attribute om if_any(["vang","pani"]):
            "amy_ff_mj"
        attribute om if_any(["yand"]):
            "amy_ff_ml"
        
        ###All mouths - truncated tags:
        attribute ma:
            "amy_ff_ma"
        attribute mb:
            "amy_ff_mb"
        attribute mc:
            "amy_ff_mc"
        attribute md:
            "amy_ff_md"
        attribute me:
            "amy_ff_me"
        attribute mf:
            "amy_ff_mf"
        attribute mg:
            "amy_ff_mg"
        attribute mh:
            "amy_ff_mh"
        attribute mi:
            "amy_ff_mi"
        attribute mj:
            "amy_ff_mj"
        attribute mk:
            "amy_ff_mk"
        attribute ml:
            "amy_ff_ml"
    
    
    
    group eyes if_all(["ff"]):
        
        anchor (0,0) subpixel (True)
        
        ###Default Opened eyes:
        attribute oe default if_any(["neut","happ","laug","pout","curi","lsur"]):
            "amy_ff_e1a"
        attribute oe default if_any(["sad","worr","flus"]):
            "amy_ff_e1b"
        attribute oe default if_any(["dist"]):
            "amy_ff_e1c"
        attribute oe default if_any(["anno","sedu","doub"]):
            "amy_ff_e1d"
        attribute oe default if_any(["cry"]):
            "amy_ff_e1i"
        attribute oe default if_any(["angr","nerv"]):
            "amy_ff_e1e"
        attribute oe default if_any(["vang","vsur","pani","shoc","yand"]):
            "amy_ff_e1f"

        ###Default Closed eyes:
        attribute ce if_any(["sad","worr","anno","angr","vang","flus","dist","sedu","nerv","doub","curi","lsur","neut"]):
            "amy_ff_e1g"
        attribute ce if_any(["happ","laug","yand","pout","vsur"]):
            "amy_ff_e1h"
        attribute ce if_any(["shoc","pani"]):
            "amy_ff_e1h"
        attribute ce if_any(["cry"]):
            "amy_ff_e1g"
        
        
        ###All eyes - truncated tags:
        attribute e1a:
            "amy_ff_e1a"
        attribute e1b:
            "amy_ff_e1b"
        attribute e1c:
            "amy_ff_e1c"
        attribute e1d:
            "amy_ff_e1d"
        attribute e1e:
            "amy_ff_e1e"
        attribute e1f:
            "amy_ff_e1f"
        attribute e1g:
            "amy_ff_e1g"
        attribute e1h:
            "amy_ff_e1h"
        attribute e1i:
            "amy_ff_e1i"
        attribute e1j:
            "amy_ff_e1j"
        attribute e1k:
            "amy_ff_e1k"
    
    group nose if_all(["ff"]):
        
        anchor (0,0) subpixel (True)
        
        ###Default nose/blush
        attribute nose default if_any(["nobl"]):
            "amy_ff_n1"
        attribute nose if_any(["awkw","pani","worr","nerv"]):
            "amy_ff_n3"
        attribute nose if_any(["blus","sedu"]):
            "amy_ff_n2"
        attribute nose if_any(["blaw","flus"]):
            "amy_ff_n4"
        
        
        
        ###All noses - truncated tags:
        attribute n1:
            "amy_ff_n1"
        attribute n2:
            "amy_ff_n2"
        attribute n3:
            "amy_ff_n3"
        attribute n4:
            "amy_ff_n4"



    group eyebrows if_all(["ff"]) if_not(["fta","fs"]): #eyebrows.
        
        anchor (0,0) subpixel (True)
        
        #Default Eyebrows:
        attribute brow default if_any(["neut","sedu"]):
            "amy_ff_b1a"
        attribute brow default if_any(["sad","pani","flus","pout","nerv","cry","dist"]):
            "amy_ff_b1d"
        attribute brow default if_any(["happ","worr","shoc","vsur","curi"]):
            "amy_ff_b1b"
        attribute brow default if_any(["curi","doub","worr"]):
            "amy_ff_b1c"
        attribute brow default if_any(["lsur"]):
            "amy_ff_b1b"
        attribute brow default if_any(["angr","anno","vang"]):
            "amy_ff_b1e"        
    
    
    
    
    group eyebrows if_all(["ff"]) if_not(["fta","fs"]):
        
        anchor (0,0) subpixel (True)
        
        ###All eyebrows - truncated tags:
        attribute b1a:
            "amy_ff_b1a"
        attribute b1b:
            "amy_ff_b1b"
        attribute b1c:
            "amy_ff_b1c"
        attribute b1d:
            "amy_ff_b1d"
        attribute b1e:
            "amy_ff_b1e"
    
    
    
    #This group is intentionally last on this list, so it will render over top of every other thing on the face.
    group broken if_all(["ff"]) if_not(["fta","fs"]):
        
        anchor (0,0) subpixel (True)
        
        attribute br1a:
            "mod_assets/MPT/amy/amy_broken_1a.png"
        attribute br1b:
            "mod_assets/MPT/amy/amy_broken_1b.png"
        attribute br1c:
            "mod_assets/MPT/amy/amy_broken_1c.png"
        attribute br1d:
            "mod_assets/MPT/amy/amy_broken_1d.png"