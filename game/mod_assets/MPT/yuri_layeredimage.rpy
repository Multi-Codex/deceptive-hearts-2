init python: ###ADD THIS BLOCK
    path = "mod_assets/MPT/yuri_swimsuit_MPT/" # I added this so that you can easily change the path of the swimsuit folder 
                                                # once and for all instead of doing this for each attribute.


layeredimage yuri turned:

    ###EDIT the 'at Flatten' line so that you have this one. If you don't even have that said line, just add it.
    ###It will make it so that Natsuki's sprite renders better on screen, as well as avoiding the vertical 'line'
    ###issue that happens sometimes.
    at renpy.partial(Flatten, drawable_resolution=False)
    
    
    group outfit: 
        attribute uniform default null
        attribute casual null
        ###ADD
        attribute swimsuit null
    
    ###ADD THOSE TWO LINES AFTER THE 'group outfit' AND REMOVE THE 'always' statement before the 'group outfit'
    always "mod_assets/MPT/yuri/yuri_turned_facebase.png" if_not(["swimsuit"])
    always path + "facebase.png" if_any(["swimsuit"])


    
    group mood: 
        attribute neut default null 
        attribute angr null 
        attribute anno null 
        attribute cry null  
        attribute curi null 
        attribute dist null 
        attribute doub null 
        attribute flus null 
        attribute happ null 
        attribute laug null 
        attribute lsur null 
        attribute nerv null 
        attribute pani null 
        attribute pout null 
        attribute sad null  
        attribute sedu null 
        attribute shoc null 
        attribute vang null 
        attribute vsur null 
        attribute worr null 
        attribute yand null 
    
    
    
    group blush: 
        attribute nobl default null 
        attribute awkw null 
        attribute blus null 
        attribute blaw null 
    
    
    
    group left:
        subpixel (True)
        yoffset (-0.5)
        xoffset (0.5)
        attribute ldown default if_any(["uniform"]):
            "mod_assets/MPT/yuri/yuri_turned_uniform_left_down.png"
        attribute lup if_any(["rup","rcut"]) if_all(["uniform"]):
            "mod_assets/MPT/yuri/yuri_turned_uniform_left_up.png"

        attribute ldown default if_any(["casual"]):
            "mod_assets/MPT/yuri/yuri_turned_casual_left_down.png"
        attribute lup if_any(["rup","rcut"]) if_all(["casual"]):
            "mod_assets/MPT/yuri/yuri_turned_casual_left_up.png"
    
    
    
    group right:
        subpixel (True)
        yoffset (-0.5)
        attribute rdown default if_any(["uniform"]):
            "mod_assets/MPT/yuri/yuri_turned_uniform_right_down.png"
        attribute rup if_any(["uniform"]):
            "mod_assets/MPT/yuri/yuri_turned_uniform_right_up.png"
        attribute rcut if_any(["uniform"]):
            "mod_assets/MPT/yuri/yuri_turned_uniform_right_cut.png"
        
        
        attribute rdown default if_any(["casual"]):
            "mod_assets/MPT/yuri/yuri_turned_casual_right_down.png"
        attribute rup if_any(["casual"]):
            "mod_assets/MPT/yuri/yuri_turned_casual_right_up.png"
    
    
    
    group left:
        subpixel (True)
        yoffset (-0.5)
        xoffset (0.5)
        attribute lup if_not(["rup","rcut"]) if_all(["uniform"]):
            "mod_assets/MPT/yuri/yuri_turned_uniform_left_up.png"
        
        attribute lup if_not(["rup","rcut"]) if_all(["casual"]):
            "mod_assets/MPT/yuri/yuri_turned_casual_left_up.png"
    
    
    ###ADD THIS GROUP BELOW
    group body:
        subpixel (True)
        yoffset (-0.5)
        #SWIMSUIT
        attribute swimsuit_turned default if_any(["swimsuit"]):
            path + "body/1f.png"
    

    
    group nose:
        
        anchor (0,0) subpixel (True)
        
        attribute nose default if_any(["nobl"]):
            "mod_assets/MPT/yuri/yuri_turned_nose_n1.png"
        attribute nose default if_any(["awkw"]):
            "mod_assets/MPT/yuri/yuri_turned_nose_n2.png"
        attribute nose default if_any(["blus"]):
            "mod_assets/MPT/yuri/yuri_turned_nose_n3.png"
        attribute nose default if_any(["blaw"]):
            "mod_assets/MPT/yuri/yuri_turned_nose_n4.png"
        
        
        attribute n1:
            "mod_assets/MPT/yuri/yuri_turned_nose_n1.png"
        attribute n2:
            "mod_assets/MPT/yuri/yuri_turned_nose_n2.png"
        attribute n3:
            "mod_assets/MPT/yuri/yuri_turned_nose_n3.png"
        attribute n4:
            "mod_assets/MPT/yuri/yuri_turned_nose_n4.png"
    
    
    
    group mouth:
        
        anchor (0,0) subpixel (True)

        attribute cm default if_any(["happ","laug"]):
            "mod_assets/MPT/yuri/yuri_turned_mouth_ma.png"
        attribute cm default if_any(["neut","lsur","worr"]):
            "mod_assets/MPT/yuri/yuri_turned_mouth_md.png"#
        attribute cm default if_any(["sedu"]):
            "mod_assets/MPT/yuri/yuri_turned_mouth_me.png"
        attribute cm default if_any(["pout","curi"]):
            "mod_assets/MPT/yuri/yuri_turned_mouth_mf.png"
        attribute cm default if_any(["shoc"]):
            "mod_assets/MPT/yuri/yuri_turned_mouth_mg.png"
        attribute cm default if_any(["dist","anno","vsur","sad","angr","cry","doub"]):
            "mod_assets/MPT/yuri/yuri_turned_mouth_mj.png"
        attribute cm default if_any(["nerv","flus"]):
            "mod_assets/MPT/yuri/yuri_turned_mouth_mk.png"
        attribute cm default if_any(["vang","pani"]):
            "mod_assets/MPT/yuri/yuri_turned_mouth_mm.png"
        attribute cm default if_any(["yand"]):
            "mod_assets/MPT/yuri/yuri_turned_mouth_mo.png"

        attribute om if_any(["happ"]):
            "mod_assets/MPT/yuri/yuri_turned_mouth_mb.png"
        attribute om if_any(["laug","nerv","yand"]):
            "mod_assets/MPT/yuri/yuri_turned_mouth_mc.png"
        attribute om if_any(["worr","pout"]):
            "mod_assets/MPT/yuri/yuri_turned_mouth_me.png"
        attribute om if_any(["sedu"]):
            "mod_assets/MPT/yuri/yuri_turned_mouth_mf.png"
        attribute om if_any(["dist","lsur","angr","cry"]):
            "mod_assets/MPT/yuri/yuri_turned_mouth_mg.png"
        attribute om if_any(["neut","anno","vsur","curi"]):
            "mod_assets/MPT/yuri/yuri_turned_mouth_mh.png"
        attribute om if_any(["flus","doub"]):
            "mod_assets/MPT/yuri/yuri_turned_mouth_mi.png"
        attribute om if_any(["sad"]):
            "mod_assets/MPT/yuri/yuri_turned_mouth_mk.png"
        attribute om if_any(["vang","shoc","pani"]):
            "mod_assets/MPT/yuri/yuri_turned_mouth_ml.png"
        

        attribute ma:
            "mod_assets/MPT/yuri/yuri_turned_mouth_ma.png"
        attribute mb:
            "mod_assets/MPT/yuri/yuri_turned_mouth_mb.png"
        attribute mc:
            "mod_assets/MPT/yuri/yuri_turned_mouth_mc.png"
        attribute md:
            "mod_assets/MPT/yuri/yuri_turned_mouth_md.png"
        attribute me:
            "mod_assets/MPT/yuri/yuri_turned_mouth_me.png"
        attribute mf:
            "mod_assets/MPT/yuri/yuri_turned_mouth_mf.png"
        attribute mg:
            "mod_assets/MPT/yuri/yuri_turned_mouth_mg.png"
        attribute mh:
            "mod_assets/MPT/yuri/yuri_turned_mouth_mh.png"
        attribute mi:
            "mod_assets/MPT/yuri/yuri_turned_mouth_mi.png"
        attribute mj:
            "mod_assets/MPT/yuri/yuri_turned_mouth_mj.png"
        attribute mk:
            "mod_assets/MPT/yuri/yuri_turned_mouth_mk.png"
        attribute ml:
            "mod_assets/MPT/yuri/yuri_turned_mouth_ml.png"
        attribute mm:
            "mod_assets/MPT/yuri/yuri_turned_mouth_mm.png"
        attribute mn:
            "mod_assets/MPT/yuri/yuri_turned_mouth_mn.png"
        attribute mo:
            "mod_assets/MPT/yuri/yuri_turned_mouth_mo.png"
        attribute mp:
            "mod_assets/MPT/yuri/yuri_turned_mouth_mp.png"
        attribute mq:
            "mod_assets/MPT/yuri/yuri_turned_mouth_mq.png"
        attribute mr:
            "mod_assets/MPT/yuri/yuri_turned_mouth_mr.png"
    
    
    
    group eyes:
        
        anchor (0,0) subpixel (True)

        attribute oe default if_any(["neut","sedu"]):
            "mod_assets/MPT/yuri/yuri_turned_eyes_e1a.png"
        attribute oe default if_any(["dist","worr"]):
            "mod_assets/MPT/yuri/yuri_turned_eyes_e1b.png"
        attribute oe default if_any(["happ","angr","pout","curi"]):
            "mod_assets/MPT/yuri/yuri_turned_eyes_e1d.png"
        attribute oe default if_any(["cry"]):
            "mod_assets/MPT/yuri/yuri_turned_eyes_e1h.png"
        attribute oe default if_any(["lsur","vang"]):
            "mod_assets/MPT/yuri/yuri_turned_eyes_e2a.png"
        attribute oe default if_any(["anno","flus","laug","sad"]):
            "mod_assets/MPT/yuri/yuri_turned_eyes_e2b.png"
        attribute oe default if_any(["nerv","doub"]):
            "mod_assets/MPT/yuri/yuri_turned_eyes_e2c.png"
        attribute oe default if_any(["shoc","pani","vsur"]):
            "mod_assets/MPT/yuri/yuri_turned_eyes_e2d.png"
        attribute oe default if_any(["yand"]):
            "mod_assets/MPT/yuri/yuri_turned_eyes_e3a.png"

        attribute ce if_any(["dist","anno","vang","flus","lsur","shoc","vsur","worr","sad","angr","nerv","curi","doub"]):
            "mod_assets/MPT/yuri/yuri_turned_eyes_e4a.png"
        attribute ce if_any(["neut","happ","yand","pani","laug","sedu","pout"]):
            "mod_assets/MPT/yuri/yuri_turned_eyes_e4b.png"
        attribute ce if_any(["cry"]):
            "mod_assets/MPT/yuri/yuri_turned_eyes_e4e.png"
        

        attribute e1a:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e1a.png"
        attribute e1b:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e1b.png"
        attribute e1c:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e1c.png"
        attribute e1d:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e1d.png"
        attribute e1e:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e1e.png"
        attribute e1f:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e1f.png"
        attribute e1g:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e1g.png"
        attribute e1h:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e1h.png"
        attribute e2a:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e2a.png"
        attribute e2b:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e2b.png"
        attribute e2c:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e2c.png"
        attribute e2d:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e2d.png"
        attribute e3a:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e3a.png"
        attribute e3b:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e3b.png"
        attribute e4a:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e4a.png"
        attribute e4b:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e4b.png"
        attribute e4c:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e4c.png"
        attribute e4d:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e4d.png"
        attribute e4e:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e4e.png"
        attribute e0a:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e0a.png"
        attribute e0b:
            "mod_assets/MPT/yuri/yuri_turned_eyes_e0b.png"
        attribute ela:
            "mod_assets/MPT/yuri/yuri_turned_eyes_ela.png"
        attribute elb:
            "mod_assets/MPT/yuri/yuri_turned_eyes_elb.png"

        ###ADD THIS EXTRA ATTRIBUTE IF YOU WANNA USE THE EXTRA EYES
        ###THAT ARE IN THE FOLDER.
        ###EXAMPLE: show yuri turned swimsuit happ eyes1 at t11
        attribute eyes1:
            path + "eyes1.png"
    
    
    
    group eyebrows:
        
        anchor (0,0) subpixel (True)
        
        attribute brow default if_any(["neut"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b1a.png"
        attribute brow default if_any(["flus","lsur","laug"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b1b.png"
        attribute brow default if_any(["dist","sedu"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b1c.png"
        attribute brow default if_any(["anno"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b1d.png"
        attribute brow default if_any(["vang","angr"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b1e.png"
        attribute brow default if_any(["curi","doub"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b1f.png"
        attribute brow default if_any(["happ"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b2a.png"
        attribute brow default if_any(["worr","sad","nerv","cry"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b2b.png"
        attribute brow default if_any(["yand","shoc","vsur","pani"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b2c.png"
        attribute brow default if_any(["pout"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b3b.png"
        

        attribute b1a:
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b1a.png"
        attribute b1b:
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b1b.png"
        attribute b1c if_not(["e0b","e2d","e3a","e3b","shoc","pani","vsur","yand"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b1c.png"
        attribute b1d if_not(["e0b","e2d","e3a","e3b","shoc","pani","vsur","yand"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b1d.png"
        attribute b1e if_not(["e0b","e2d","e3a","e3b","shoc","pani","vsur","yand"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b1e.png"
        attribute b1f:
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b1f.png"
        attribute b2a:
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b2a.png"
        attribute b2b if_not(["e0b","e2d","e3a","e3b","shoc","pani","vsur","yand"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b2b.png"
        attribute b2c:
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b2c.png"
        attribute b3a if_not(["e0b","e2d","e3a","e3b","shoc","pani","vsur","yand"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b3a.png"
        attribute b3b if_not(["e0b","e2d","e3a","e3b","shoc","pani","vsur","yand"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b3b.png"
        attribute b3c:
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b3c.png"
        
        
        attribute b1c if_any(["shoc","pani","vsur","yand"]) if_all(["ce"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b1c.png"
        attribute b1d if_any(["shoc","pani","vsur","yand"]) if_all(["ce"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b1d.png"
        attribute b1e if_any(["shoc","pani","vsur","yand"]) if_all(["ce"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b1e.png"
        attribute b2b if_any(["shoc","pani","vsur","yand"]) if_all(["ce"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b2b.png"
        attribute b3a if_any(["shoc","pani","vsur","yand"]) if_all(["ce"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b3a.png"
        attribute b3b if_any(["shoc","pani","vsur","yand"]) if_all(["ce"]):
            "mod_assets/MPT/yuri/yuri_turned_eyebrows_b3b.png"
    
    
    
    group special:
        
        anchor (0,0) subpixel (True)
        
        attribute s_scream:
            "mod_assets/MPT/yuri/yuri_turned_special_scream.png"



layeredimage yuri shy:

    at renpy.partial(Flatten, drawable_resolution=False)

    group outfit:
        
        anchor (0,0) subpixel (True)
        attribute uniform default:
            "mod_assets/MPT/yuri/yuri_shy_uniform_bodybase.png"
        attribute casual:
            "mod_assets/MPT/yuri/yuri_shy_casual_bodybase.png"

        ###ADD THIS ATTRIBUTE
        attribute swimsuit:
            xoffset 9
            path + "body/2f.png"

    ###ADD THOSE TWO 'always' statements and remove the one before the 'group outfit'
    always "mod_assets/MPT/yuri/yuri_shy_facebase.png" if_not(["swimsuit"])
    always:
        xoffset 9
        path + "shy_facebase.png" if_any(["swimsuit"])

    
    group mood: 
        attribute neut default null 
        attribute angr null 
        attribute happ null 
        attribute sad null
    
    
    
    group blush:
        attribute nobl default null
        attribute awkw null 
        attribute blus null 
        attribute blaw null 
        attribute bful null 
    
    
    group nose:
        
        anchor (0,0) subpixel (True)

        attribute nose default if_any(["nobl"]):
            "mod_assets/MPT/yuri/yuri_shy_nose_n1.png"
        attribute nose default if_any(["awkw"]):
            "mod_assets/MPT/yuri/yuri_shy_nose_n2.png"
        attribute nose default if_any(["blus"]):
            "mod_assets/MPT/yuri/yuri_shy_nose_n3.png"
        attribute nose default if_any(["blaw"]):
            "mod_assets/MPT/yuri/yuri_shy_nose_n4.png"
        attribute nose default if_any(["bful"]):
            "mod_assets/MPT/yuri/yuri_shy_nose_n5.png"
        

        attribute n1:
            "mod_assets/MPT/yuri/yuri_shy_nose_n1.png"
        attribute n2:
            "mod_assets/MPT/yuri/yuri_shy_nose_n2.png"
        attribute n3:
            "mod_assets/MPT/yuri/yuri_shy_nose_n3.png"
        attribute n4:
            "mod_assets/MPT/yuri/yuri_shy_nose_n4.png"
        attribute n5:
            "mod_assets/MPT/yuri/yuri_shy_nose_n5.png"
    
    
    
    group mouth:
        
        anchor (0,0) subpixel (True)

        attribute cm default if_any(["neut"]):
            "mod_assets/MPT/yuri/yuri_shy_mouth_m1.png"
        attribute cm default if_any(["angr","sad"]):
            "mod_assets/MPT/yuri/yuri_shy_mouth_m2.png"
        attribute cm default if_any(["happ"]):
            "mod_assets/MPT/yuri/yuri_shy_mouth_m3.png"

        attribute om:
            "mod_assets/MPT/yuri/yuri_shy_mouth_m4.png"

        attribute m1:
            "mod_assets/MPT/yuri/yuri_shy_mouth_m1.png"
        attribute m2:
            "mod_assets/MPT/yuri/yuri_shy_mouth_m2.png"
        attribute m3:
            "mod_assets/MPT/yuri/yuri_shy_mouth_m3.png"
        attribute m4:
            "mod_assets/MPT/yuri/yuri_shy_mouth_m4.png"
    
    
    
    group eyes if_not(["n5","bful"]): 
        
        anchor (0,0) subpixel (True)

        attribute oe default if_any(["happ"]):
            "mod_assets/MPT/yuri/yuri_shy_eyes_e1.png"
        attribute oe default if_any(["neut"]):
            "mod_assets/MPT/yuri/yuri_shy_eyes_e2.png"
        attribute oe default if_any(["angr"]):
            "mod_assets/MPT/yuri/yuri_shy_eyes_e3.png"
        attribute oe default if_any(["sad"]):
            "mod_assets/MPT/yuri/yuri_shy_eyes_e4.png"

        attribute ce if_any(["angr","neut","happ"]):
            "mod_assets/MPT/yuri/yuri_shy_eyes_e5.png"
        attribute ce if_any(["sad"]):
            "mod_assets/MPT/yuri/yuri_shy_eyes_e6.png"
        

        attribute e1:
            "mod_assets/MPT/yuri/yuri_shy_eyes_e1.png"
        attribute e2:
            "mod_assets/MPT/yuri/yuri_shy_eyes_e2.png"
        attribute e3:
            "mod_assets/MPT/yuri/yuri_shy_eyes_e3.png"
        attribute e4:
            "mod_assets/MPT/yuri/yuri_shy_eyes_e4.png"
        attribute e5:
            "mod_assets/MPT/yuri/yuri_shy_eyes_e5.png"
        attribute e6:
            "mod_assets/MPT/yuri/yuri_shy_eyes_e6.png"
    
    
    
    group eyebrows if_not(["n5","bful"]):
        
        anchor (0,0) subpixel (True)
        
        attribute brow default if_any(["happ"]):
            "mod_assets/MPT/yuri/yuri_shy_eyebrows_b1.png"
        attribute brow default if_any(["neut","sad"]):
            "mod_assets/MPT/yuri/yuri_shy_eyebrows_b2.png"
        attribute brow default if_any(["angr"]):
            "mod_assets/MPT/yuri/yuri_shy_eyebrows_b3.png"
        
        attribute b1:
            "mod_assets/MPT/yuri/yuri_shy_eyebrows_b1.png"
        attribute b2:
            "mod_assets/MPT/yuri/yuri_shy_eyebrows_b2.png"
        attribute b3:
            "mod_assets/MPT/yuri/yuri_shy_eyebrows_b3.png"



