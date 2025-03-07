## definitions.rpy

# This file defines important stuff for DDLC and your mod!

# This variable declares if the mod is a demo or not.
# Leftover from DDLC.
define persistent.demo = False

# This variable declares whether the mod is in the 'steamapps' folder.
define persistent.steam = ("steamapps" in config.basedir.lower())

# This variable declares whether Developer Mode is on or off in the mod.
define config.developer = False

# This python statement starts singleton to make sure only one copy of the mod
# is running.


init -3 python:
    ## Dynamic Super Position (DSP)
    # DSP is a feature in where the game upscales the positions of assets 
    # with higher resolutions (1080p).
    # This is just simple division from Adobe, implemented in Python.
    def dsp(orig_val):
        ceil = not isinstance(orig_val, float)
        dsp_scale = config.screen_width / 1280.0 
        if ceil: return math.ceil(orig_val * dsp_scale)
        # since `absolute * float` -> `float`
        # we wanna keep the same type
        return type(orig_val)(orig_val * dsp_scale)
    
    # This makes evaluating the value faster
    renpy.pure(dsp)

    ## Dynamic Super Resolution
    # DSR is a feature in where the game upscales asset sizes to higher
    # resolutions (1080p) and sends back a modified transform.
    # (Recommend that you just make higher res assets than upscale lower res ones)
    def dsr(path):
        img_bounds = renpy.image_size(path)
        return Transform(path, size=(dsp(img_bounds[0]), dsp(img_bounds[1])))

## Android Gestures (provided by Tulkas)
## These gestures allow players to access different settings using the touch screen.
# Swipe Up - Saves
# Swipe Down - Hide Dialogue Box
# Swipe Left - History
# Swipe Right - Skip Dialogue
define config.gestures = { "n" : 'game_menu', "s" : "hide_windows", "e" : 'toggle_skip', "w" : "history" }

# This init python statement sets up the functions, keymaps and channels
# for the game.
init python:
    ## More Android Gestures
    # This variable makes a keymap for the history screen.
    if renpy.android:
        config.underlay.append(renpy.Keymap(history = ShowMenu("history"))) 

        # These commented variables sets all keybinds from Rollback to History.
        # config.keymap["rollback"] = []
        # config.keymap["history"] = [ 'K_PAGEUP', 'repeat_K_PAGEUP', 'K_AC_BACK', 'mousedown_4' ]

    # These variable declarations adjusts the mapping for certain actions in-game.
    config.keymap['game_menu'].remove('mouseup_3')
    config.keymap['hide_windows'].append('mouseup_3')
    config.keymap['self_voicing'] = []
    config.keymap['clipboard_voicing'] = []
    config.keymap['toggle_skip'] = []

    # This variable declaration registers the music poem channel for the poem sharing music.
    renpy.music.register_channel("music_poem", mixer="music", tight=True)
    
    # This function gets the postition of the music playing in a given channel.
    def get_pos(channel='music'):
        pos = renpy.music.get_pos(channel=channel)
        if pos: return pos
        return 0

    # This function deletes all the saves made in the mod.
    def delete_all_saves():
        for savegame in renpy.list_saved_games(fast=True):
            renpy.unlink_save(savegame)

    # This function deletes a given character name from the characters folder.
    def delete_character(name):
        if renpy.android:
            try: os.remove(os.environ['ANDROID_PUBLIC'] + "/characters/" + name + ".chr")
            except: pass
        else:
            try: os.remove(config.basedir + "/characters/" + name + ".chr")
            except: pass

    # These functions restores all the character CHR files to the characters folder 
    # given the playthrough number in the mod and list of characters to restore.
    def restore_character(names):
        if not isinstance(names, list):
            raise Exception("'names' parameter must be a list. Example: [\"monika\", \"sayori\"].")

        for x in names:
            if renpy.android:
                try: renpy.file(os.environ['ANDROID_PUBLIC'] + "/characters/" + x + ".chr")
                except: open(os.environ['ANDROID_PUBLIC'] + "/characters/" + x + ".chr", "wb").write(renpy.file("chrs/" + x + ".chr").read())
            else:
                try: renpy.file(config.basedir + "/characters/" + x + ".chr")
                except: open(config.basedir + "/characters/" + x + ".chr", "wb").write(renpy.file("chrs/" + x + ".chr").read())

    def restore_all_characters():
        if persistent.playthrough == 0:
            restore_character(["monika", "sayori", "natsuki", "yuri"])
        elif persistent.playthrough == 1 or persistent.playthrough == 2:
            restore_character(["monika", "natsuki", "yuri"])
        elif persistent.playthrough == 3:
            restore_character(["monika"])
        else:
            restore_character(["sayori", "natsuki", "yuri"])
    
    # This function is obsolete as all characters now restores only
    # relevant characters to the characters folder.
    def restore_relevant_characters():
        restore_all_characters()

    # This function pauses the time for a certain amount of time or indefinite.
    def pause(time=None):
        global _windows_hidden

        if not time:
            _windows_hidden = True
            renpy.ui.saybehavior(afm=" ")
            renpy.ui.interact(mouse='pause', type='pause', roll_forward=None)
            _windows_hidden = False
            return
        if time <= 0: return
        _windows_hidden = True
        renpy.pause(time)
        _windows_hidden = False

## Music
# This section declares the music available to be played in the mod.
# Syntax:
#   audio. - This tells Ren'Py this is a audio variable.
#   t1 - This tells Ren'Py the label of the music/sound file being declared.
#   <loop 22.073> - This tells Ren'Py to loop the music/sound to this position when the song completes.
#   "bgm/1.ogg" - This tells Ren'Py the path of the music/sound file to use.
# Example: 
#   define audio.t2 = "bgm/2.ogg"

define audio.t1 = "<loop 22.073>bgm/1.ogg" # Doki Doki Literature Club! - Main Theme
define audio.t2 = "<loop 4.499>bgm/2.ogg" # Ohayou Sayori! - Sayori Theme
define audio.t2g = "bgm/2g.ogg"
define audio.t2g2 = "<from 4.499 loop 4.499>bgm/2.ogg"
define audio.t2g3 = "<loop 4.492>bgm/2g2.ogg"
define audio.t3 = "<loop 4.618>bgm/3.ogg" # Main Theme - In Game 
define audio.t3g = "<to 15.255>bgm/3g.ogg"
define audio.t3g2 = "<from 15.255 loop 4.618>bgm/3.ogg"
define audio.t3g3 = "<loop 4.618>bgm/3g2.ogg"
define audio.t3m = "<loop 4.618>bgm/3.ogg"
define audio.t4 = "<loop 19.451>bgm/4.ogg" # Dreams of Love and Literature - Poem Game Theme
define audio.t4g = "<loop 1.000>bgm/4g.ogg"
define audio.t5 = "<loop 4.444>bgm/5.ogg" # Okay Everyone! - Sharing Poems Theme

define audio.tmonika = "<loop 4.444>bgm/5_monika.ogg" # Okay Everyone! (Monika)
define audio.tsayori = "<loop 4.444>bgm/5_sayori.ogg" # Okay Everyone! (Sayori)
define audio.tnatsuki = "<loop 4.444>bgm/5_natsuki.ogg" # Okay Everyone! (Natsuki)
define audio.tyuri = "<loop 4.444>bgm/5_yuri.ogg" # Okay Everyone! (Yuri)

define audio.t5b = "<loop 4.444>bgm/5.ogg"
define audio.t5c = "<loop 4.444>bgm/5.ogg"
define audio.t6 = "<loop 10.893>bgm/6.ogg" # Play With Me - Yuri/Natsuki Theme
define audio.t6g = "<loop 10.893>bgm/6g.ogg"
define audio.t6r = "<to 39.817 loop 0>bgm/6r.ogg"
define audio.t6s = "<loop 43.572>bgm/6s.ogg"
define audio.t7 = "<loop 2.291>bgm/7.ogg" # Poem Panic - Argument Theme
define audio.t7a = "<loop 4.316 to 12.453>bgm/7.ogg"
define audio.t7g = "<loop 31.880>bgm/7g.ogg"
define audio.t8 = "<loop 9.938>bgm/8.ogg" # Daijoubu! - Argument Resolved Theme
define audio.t9 = "<loop 3.172>bgm/9.ogg" # My Feelings - Emotional Theme
define audio.t9g = "<loop 1.532>bgm/9g.ogg" # My Feelings but 207% Speed
define audio.t10 = "<loop 5.861>bgm/10.ogg" # My Confession - Sayori Confession Theme
define audio.t10y = "<loop 0>bgm/10-yuri.ogg"
define audio.td = "<loop 36.782>bgm/d.ogg"

define audio.m1 = "<loop 0>bgm/m1.ogg" # Just Monika. - Just Monika.
define audio.mend = "<loop 6.424>bgm/monika-end.ogg" # I Still Love You - Monika Post-Delete Theme

define audio.ghostmenu = "<loop 0>bgm/ghostmenu.ogg"
define audio.g1 = "<loop 0>bgm/g1.ogg"
define audio.g2 = "<loop 0>bgm/g2.ogg"
define audio.hb = "<loop 0>bgm/heartbeat.ogg"

define audio.closet_open = "sfx/closet-open.ogg"
define audio.closet_close = "sfx/closet-close.ogg"
define audio.page_turn = "sfx/pageflip.ogg"
define audio.fall = "sfx/fall.ogg"

#custom shit
define audio.water = "mod_assets/music/DDMC_Track_Series_Waters_Edge.mp3"
define audio.shiveria = "mod_assets/music/shiveria.mp3"
define audio.cooling = "<loop 21.454>mod_assets/music/cooling.ogg"
define audio.lobarap = "<loop 2.507>mod_assets/music/lobarap.ogg"
define audio.e1m1 = "mod_assets/music/e1m1.mp3"
define audio.finale = "mod_assets/music/finale.ogg"
define audio.hope = "mod_assets/music/hope.mp3"
define audio.fulstop = "mod_assets/music/fulstop.ogg"
define audio.nohope = "mod_assets/music/nohope.mp3"
define audio.justsayori = "mod_assets/music/justsayori.ogg"
define audio.whitesalv = "mod_assets/music/whitesalvation.mp3"
define audio.freeze = "mod_assets/music/freeze.mp3"
define audio.istill = "mod_assets/music/istill.mp3"
define audio.mps = "mod_assets/music/motionpicturesoundtrack.ogg"
define audio.iris = "mod_assets/music/Iris.mp3"
define audio.eiirp1 = "<from 0 to 56.129 loop 46.452>mod_assets/music/eiirp.ogg"
define audio.eiirp2 = "<from 56.129 to 147.347 loop 80.081>mod_assets/music/eiirp.ogg"
define audio.eiirp3 = "<from 147.347 to 268.798 loop 147.347>mod_assets/music/eiirp.ogg"
define audio.inferno = "mod_assets/music/Inferno.ogg"
define audio.nuhuh = "mod_assets/music/nuhuh.ogg"
define audio.entropy = "mod_assets/music/Entropy.ogg"

#sfx
define audio.transsay = "mod_assets/music/transition_s.ogg"
define audio.transnat = "mod_assets/music/transition_n.ogg"
define audio.transyuri = "mod_assets/music/transition_y.ogg"
define audio.transmoni = "mod_assets/music/transition_m.ogg"
define audio.portal = "mod_assets/music/portal.mp3"
define audio.portal_disappear = "mod_assets/music/disappear.mp3"
define audio.gun = "mod_assets/music/gun.mp3"
define audio.pipe = "mod_assets/music/mp.mp3"
define audio.beam = "mod_assets/music/beam.mp3"
define audio.rope = "mod_assets/music/rope.mp3"


#CUSTOM IMAGES

image portal = "mod_assets/portal.png"

## Backgrounds
# This section declares the backgrounds available to be shown in the mod.
# To define a new color background, declare a new image statement like in this example:
#     image blue = "X" where X is your color hex i.e. '#158353'
# To define a new background, declare a new image statement like this instead:
#     image bg bathroom = "mod_assets/bathroom.png" 

# Statc background
init python:
    def capture_images(prefix, filt):
        for file in filter(filt, renpy.list_files()):
            renpy.image(" ".join([prefix, os.path.splitext(os.path.split(file)[1])[0]]), file)

    capture_images("bg", lambda x: x.startswith("mod_assets/bg/"))
    
    print(renpy.display.image.list_images())

# DOOM Transition

transform move_down(delay_time):
    ypos 0
    pause delay_time
    linear 3.0 ypos renpy.config.screen_height + 100

default my_BG = "mod_assets/bg/corridor.png"

screen screen_melt:
    zorder 1000

    # Create 640 vertical slices & move 'em.
    for i in range(640):
        add my_BG crop (i * (renpy.config.screen_width // 640), 0, renpy.config.screen_width // 640, renpy.config.screen_height) xpos i * (renpy.config.screen_width // 640) ypos 0 at move_down(renpy.random.uniform(0, 0.2))

image black = "#000000"
image dark = "#000000e4"
image darkred = "#110000c8"
image white = "#ffffff"
image splash = "bg/splash.png"
image end:
    truecenter
    "gui/end.png"

image bg residential_day = "bg/residential.png" # Start of DDLC BG
image bg class_day = "bg/class.png" # The classroom BG
image bg corridor = "bg/corridor.png" # The hallway BG
image bg club_day = "bg/club.png" # The club BG
image bg club_day2: # Glitched Club BG
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg/club-skill.png"

image bg closet = "bg/closet.png" # The closet BG
image bg bedroom = "bg/bedroom.png" # MC's Room BG
image bg sayori_bedroom = "bg/sayori_bedroom.png" # Sayori's Room BG
image bg house = "bg/house.png" # Sayori's House BG
image bg kitchen = "bg/kitchen.png" # MC's Kitchen BG

image bg notebook = "bg/notebook.png" # Poem Game Notebook Scene
image bg notebook-glitch = "bg/notebook-glitch.png" # Glitched Poem Game BG

# This image shows a glitched screen during Act 2 poem sharing with Yuri.
image bg glitch = LiveTile("bg/glitch.jpg")

# This image transform shows a glitched scene effect
# during Act 3 when we delete Monika.
image glitch_color:
    ytile 3
    zoom 2.5
    parallel:
        "bg/glitch-red.png"
        0.1
        "bg/glitch-green.png"
        0.1
        "bg/glitch-blue.png"
        0.1
        repeat
    parallel:
        yoffset 720
        linear 0.5 yoffset 0
        repeat
    parallel:
        choice:
            xoffset 0
        choice:
            xoffset 10
        choice:
            xoffset 20
        choice:
            xoffset 35
        choice:
            xoffset -10
        choice:
            xoffset -20
        choice:
            xoffset -30
        0.01
        repeat
    parallel:
        alpha 0.6
        linear 0.15 alpha 0.1
        0.2
        alpha 0.6
        linear 0.15 alpha 0.1
        0.2
        alpha 0.7
        linear 0.45 alpha 0

# This image transform shows another glitched scene effect
# during Act 3 when we delete Monika.
image glitch_color2:
    ytile 3
    zoom 2.5
    parallel:
        "bg/glitch-red.png"
        0.1
        "bg/glitch-green.png"
        0.1
        "bg/glitch-blue.png"
        0.1
        repeat
    parallel:
        yoffset 720
        linear 0.5 yoffset 0
        repeat
    parallel:
        choice:
            xoffset 0
        choice:
            xoffset 10
        choice:
            xoffset 20
        choice:
            xoffset 35
        choice:
            xoffset -10
        choice:
            xoffset -20
        choice:
            xoffset -30
        0.01
        repeat
    parallel:
        alpha 0.7
        linear 0.45 alpha 0

# Characters
# This is where the characters bodies and faces are defined in the mod.
# They are defined by a left half, a right half and their head.
# To define a new image, declare a new image statement like in this example:
#     image sayori 1ca = Composite((960, 960), (0, 0), "mod_assets/sayori/1cl.png", (0, 0), "mod_assets/sayori/1cr.png", (0, 0), "sayori/a.png")

# Sayori's Character Definitions
image sayori 1 = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 1a = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 1b = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/b.png")
image sayori 1c = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/c.png")
image sayori 1d = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/d.png")
image sayori 1e = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/e.png")
image sayori 1f = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/f.png")
image sayori 1g = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/g.png")
image sayori 1h = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/h.png")
image sayori 1i = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/i.png")
image sayori 1j = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/j.png")
image sayori 1k = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/k.png")
image sayori 1l = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/l.png")
image sayori 1m = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/m.png")
image sayori 1n = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/n.png")
image sayori 1o = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/o.png")
image sayori 1p = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/p.png")
image sayori 1q = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/q.png")
image sayori 1r = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/r.png")
image sayori 1s = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/s.png")
image sayori 1t = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/t.png")
image sayori 1u = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/u.png")
image sayori 1v = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/v.png")
image sayori 1w = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/w.png")
image sayori 1x = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/x.png")
image sayori 1y = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/y.png")

image sayori 2 = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 2a = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 2b = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/b.png")
image sayori 2c = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/c.png")
image sayori 2d = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/d.png")
image sayori 2e = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/e.png")
image sayori 2f = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/f.png")
image sayori 2g = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/g.png")
image sayori 2h = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/h.png")
image sayori 2i = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/i.png")
image sayori 2j = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/j.png")
image sayori 2k = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/k.png")
image sayori 2l = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/l.png")
image sayori 2m = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/m.png")
image sayori 2n = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/n.png")
image sayori 2o = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/o.png")
image sayori 2p = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/p.png")
image sayori 2q = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/q.png")
image sayori 2r = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/r.png")
image sayori 2s = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/s.png")
image sayori 2t = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/t.png")
image sayori 2u = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/u.png")
image sayori 2v = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/v.png")
image sayori 2w = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/w.png")
image sayori 2x = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/x.png")
image sayori 2y = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/y.png")

image sayori 3 = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 3a = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 3b = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/b.png")
image sayori 3c = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/c.png")
image sayori 3d = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/d.png")
image sayori 3e = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/e.png")
image sayori 3f = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/f.png")
image sayori 3g = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/g.png")
image sayori 3h = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/h.png")
image sayori 3i = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/i.png")
image sayori 3j = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/j.png")
image sayori 3k = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/k.png")
image sayori 3l = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/l.png")
image sayori 3m = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/m.png")
image sayori 3n = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/n.png")
image sayori 3o = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/o.png")
image sayori 3p = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/p.png")
image sayori 3q = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/q.png")
image sayori 3r = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/r.png")
image sayori 3s = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/s.png")
image sayori 3t = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/t.png")
image sayori 3u = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/u.png")
image sayori 3v = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/v.png")
image sayori 3w = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/w.png")
image sayori 3x = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/x.png")
image sayori 3y = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/y.png")

image sayori 4 = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 4a = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 4b = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/b.png")
image sayori 4c = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/c.png")
image sayori 4d = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/d.png")
image sayori 4e = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/e.png")
image sayori 4f = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/f.png")
image sayori 4g = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/g.png")
image sayori 4h = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/h.png")
image sayori 4i = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/i.png")
image sayori 4j = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/j.png")
image sayori 4k = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/k.png")
image sayori 4l = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/l.png")
image sayori 4m = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/m.png")
image sayori 4n = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/n.png")
image sayori 4o = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/o.png")
image sayori 4p = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/p.png")
image sayori 4q = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/q.png")
image sayori 4r = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/r.png")
image sayori 4s = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/s.png")
image sayori 4t = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/t.png")
image sayori 4u = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/u.png")
image sayori 4v = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/v.png")
image sayori 4w = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/w.png")
image sayori 4x = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/x.png")
image sayori 4y = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/y.png")

image sayori 5 = im.Composite((960, 960), (0, 0), "sayori/3a.png")
image sayori 5a = im.Composite((960, 960), (0, 0), "sayori/3a.png")
image sayori 5b = im.Composite((960, 960), (0, 0), "sayori/3b.png")
image sayori 5c = im.Composite((960, 960), (0, 0), "sayori/3c.png")
image sayori 5d = im.Composite((960, 960), (0, 0), "sayori/3d.png")

# Sayori in her Casual Outfit [Day 4]
image sayori 1ba = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/a.png")
image sayori 1bb = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/b.png")
image sayori 1bc = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/c.png")
image sayori 1bd = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/d.png")
image sayori 1be = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/e.png")
image sayori 1bf = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/f.png")
image sayori 1bg = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/g.png")
image sayori 1bh = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/h.png")
image sayori 1bi = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/i.png")
image sayori 1bj = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/j.png")
image sayori 1bk = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/k.png")
image sayori 1bl = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/l.png")
image sayori 1bm = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/m.png")
image sayori 1bn = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/n.png")
image sayori 1bo = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/o.png")
image sayori 1bp = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/p.png")
image sayori 1bq = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/q.png")
image sayori 1br = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/r.png")
image sayori 1bs = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/s.png")
image sayori 1bt = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/t.png")
image sayori 1bu = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/u.png")
image sayori 1bv = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/v.png")
image sayori 1bw = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/w.png")
image sayori 1bx = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/x.png")
image sayori 1by = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/y.png")

image sayori 2ba = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/a.png")
image sayori 2bb = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/b.png")
image sayori 2bc = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/c.png")
image sayori 2bd = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/d.png")
image sayori 2be = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/e.png")
image sayori 2bf = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/f.png")
image sayori 2bg = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/g.png")
image sayori 2bh = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/h.png")
image sayori 2bi = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/i.png")
image sayori 2bj = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/j.png")
image sayori 2bk = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/k.png")
image sayori 2bl = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/l.png")
image sayori 2bm = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/m.png")
image sayori 2bn = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/n.png")
image sayori 2bo = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/o.png")
image sayori 2bp = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/p.png")
image sayori 2bq = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/q.png")
image sayori 2br = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/r.png")
image sayori 2bs = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/s.png")
image sayori 2bt = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/t.png")
image sayori 2bu = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/u.png")
image sayori 2bv = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/v.png")
image sayori 2bw = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/w.png")
image sayori 2bx = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/x.png")
image sayori 2by = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/y.png")

image sayori 3ba = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/a.png")
image sayori 3bb = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/b.png")
image sayori 3bc = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/c.png")
image sayori 3bd = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/d.png")
image sayori 3be = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/e.png")
image sayori 3bf = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/f.png")
image sayori 3bg = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/g.png")
image sayori 3bh = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/h.png")
image sayori 3bi = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/i.png")
image sayori 3bj = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/j.png")
image sayori 3bk = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/k.png")
image sayori 3bl = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/l.png")
image sayori 3bm = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/m.png")
image sayori 3bn = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/n.png")
image sayori 3bo = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/o.png")
image sayori 3bp = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/p.png")
image sayori 3bq = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/q.png")
image sayori 3br = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/r.png")
image sayori 3bs = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/s.png")
image sayori 3bt = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/t.png")
image sayori 3bu = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/u.png")
image sayori 3bv = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/v.png")
image sayori 3bw = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/w.png")
image sayori 3bx = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/x.png")
image sayori 3by = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/y.png")

image sayori 4ba = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/a.png")
image sayori 4bb = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/b.png")
image sayori 4bc = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/c.png")
image sayori 4bd = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/d.png")
image sayori 4be = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/e.png")
image sayori 4bf = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/f.png")
image sayori 4bg = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/g.png")
image sayori 4bh = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/h.png")
image sayori 4bi = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/i.png")
image sayori 4bj = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/j.png")
image sayori 4bk = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/k.png")
image sayori 4bl = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/l.png")
image sayori 4bm = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/m.png")
image sayori 4bn = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/n.png")
image sayori 4bo = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/o.png")
image sayori 4bp = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/p.png")
image sayori 4bq = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/q.png")
image sayori 4br = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/r.png")
image sayori 4bs = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/s.png")
image sayori 4bt = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/t.png")
image sayori 4bu = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/u.png")
image sayori 4bv = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/v.png")
image sayori 4bw = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/w.png")
image sayori 4bx = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/x.png")
image sayori 4by = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/y.png")

# This image shows a glitched Sayori sprite during Act 2.
image sayori glitch:
    "sayori/glitch1.png"
    pause 0.01666
    "sayori/glitch2.png"
    pause 0.01666
    repeat

# Natsuki's Character Definitions
image natsuki 11 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 1a = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/a.png")
image natsuki 1b = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/b.png")
image natsuki 1c = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/c.png")
image natsuki 1d = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/d.png")
image natsuki 1e = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/e.png")
image natsuki 1f = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/f.png")
image natsuki 1g = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/g.png")
image natsuki 1h = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/h.png")
image natsuki 1i = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/i.png")
image natsuki 1j = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/j.png")
image natsuki 1k = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/k.png")
image natsuki 1l = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/l.png")
image natsuki 1m = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/m.png")
image natsuki 1n = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/n.png")
image natsuki 1o = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/o.png")
image natsuki 1p = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/p.png")
image natsuki 1q = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/q.png")
image natsuki 1r = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/r.png")
image natsuki 1s = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/s.png")
image natsuki 1t = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/t.png")
image natsuki 1u = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/u.png")
image natsuki 1v = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/v.png")
image natsuki 1w = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/w.png")
image natsuki 1x = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/x.png")
image natsuki 1y = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/y.png")
image natsuki 1z = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/z.png")

image natsuki 21 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 2a = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/a.png")
image natsuki 2b = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/b.png")
image natsuki 2c = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/c.png")
image natsuki 2d = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/d.png")
image natsuki 2e = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/e.png")
image natsuki 2f = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/f.png")
image natsuki 2g = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/g.png")
image natsuki 2h = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/h.png")
image natsuki 2i = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/i.png")
image natsuki 2j = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/j.png")
image natsuki 2k = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/k.png")
image natsuki 2l = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/l.png")
image natsuki 2m = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/m.png")
image natsuki 2n = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/n.png")
image natsuki 2o = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/o.png")
image natsuki 2p = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/p.png")
image natsuki 2q = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/q.png")
image natsuki 2r = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/r.png")
image natsuki 2s = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/s.png")
image natsuki 2t = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/t.png")
image natsuki 2u = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/u.png")
image natsuki 2v = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/v.png")
image natsuki 2w = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/w.png")
image natsuki 2x = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/x.png")
image natsuki 2y = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/y.png")
image natsuki 2z = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/z.png")

image natsuki 31 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 3a = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/a.png")
image natsuki 3b = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/b.png")
image natsuki 3c = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/c.png")
image natsuki 3d = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/d.png")
image natsuki 3e = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/e.png")
image natsuki 3f = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/f.png")
image natsuki 3g = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/g.png")
image natsuki 3h = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/h.png")
image natsuki 3i = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/i.png")
image natsuki 3j = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/j.png")
image natsuki 3k = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/k.png")
image natsuki 3l = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/l.png")
image natsuki 3m = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/m.png")
image natsuki 3n = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/n.png")
image natsuki 3o = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/o.png")
image natsuki 3p = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/p.png")
image natsuki 3q = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/q.png")
image natsuki 3r = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/r.png")
image natsuki 3s = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/s.png")
image natsuki 3t = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/t.png")
image natsuki 3u = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/u.png")
image natsuki 3v = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/v.png")
image natsuki 3w = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/w.png")
image natsuki 3x = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/x.png")
image natsuki 3y = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/y.png")
image natsuki 3z = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/z.png")

image natsuki 41 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 4a = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/a.png")
image natsuki 4b = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/b.png")
image natsuki 4c = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/c.png")
image natsuki 4d = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/d.png")
image natsuki 4e = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/e.png")
image natsuki 4f = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/f.png")
image natsuki 4g = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/g.png")
image natsuki 4h = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/h.png")
image natsuki 4i = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/i.png")
image natsuki 4j = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/j.png")
image natsuki 4k = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/k.png")
image natsuki 4l = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/l.png")
image natsuki 4m = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/m.png")
image natsuki 4n = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/n.png")
image natsuki 4o = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/o.png")
image natsuki 4p = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/p.png")
image natsuki 4q = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/q.png")
image natsuki 4r = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/r.png")
image natsuki 4s = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/s.png")
image natsuki 4t = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/t.png")
image natsuki 4u = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/u.png")
image natsuki 4v = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/v.png")
image natsuki 4w = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/w.png")
image natsuki 4x = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/x.png")
image natsuki 4y = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/y.png")
image natsuki 4z = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/z.png")

image natsuki 12 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2t.png")
image natsuki 12a = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2ta.png")
image natsuki 12b = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tb.png")
image natsuki 12c = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tc.png")
image natsuki 12d = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2td.png")
image natsuki 12e = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2te.png")
image natsuki 12f = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tf.png")
image natsuki 12g = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tg.png")
image natsuki 12h = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2th.png")
image natsuki 12i = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2ti.png")

image natsuki 42 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2t.png")
image natsuki 42a = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2ta.png")
image natsuki 42b = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tb.png")
image natsuki 42c = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tc.png")
image natsuki 42d = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2td.png")
image natsuki 42e = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2te.png")
image natsuki 42f = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tf.png")
image natsuki 42g = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tg.png")
image natsuki 42h = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2th.png")
image natsuki 42i = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2ti.png")

image natsuki 51 = im.Composite((960, 960), (18, 22), "natsuki/1t.png", (0, 0), "natsuki/3.png")
image natsuki 5a = im.Composite((960, 960), (18, 22), "natsuki/a.png", (0, 0), "natsuki/3.png")
image natsuki 5b = im.Composite((960, 960), (18, 22), "natsuki/b.png", (0, 0), "natsuki/3.png")
image natsuki 5c = im.Composite((960, 960), (18, 22), "natsuki/c.png", (0, 0), "natsuki/3.png")
image natsuki 5d = im.Composite((960, 960), (18, 22), "natsuki/d.png", (0, 0), "natsuki/3.png")
image natsuki 5e = im.Composite((960, 960), (18, 22), "natsuki/e.png", (0, 0), "natsuki/3.png")
image natsuki 5f = im.Composite((960, 960), (18, 22), "natsuki/f.png", (0, 0), "natsuki/3.png")
image natsuki 5g = im.Composite((960, 960), (18, 22), "natsuki/g.png", (0, 0), "natsuki/3.png")
image natsuki 5h = im.Composite((960, 960), (18, 22), "natsuki/h.png", (0, 0), "natsuki/3.png")
image natsuki 5i = im.Composite((960, 960), (18, 22), "natsuki/i.png", (0, 0), "natsuki/3.png")
image natsuki 5j = im.Composite((960, 960), (18, 22), "natsuki/j.png", (0, 0), "natsuki/3.png")
image natsuki 5k = im.Composite((960, 960), (18, 22), "natsuki/k.png", (0, 0), "natsuki/3.png")
image natsuki 5l = im.Composite((960, 960), (18, 22), "natsuki/l.png", (0, 0), "natsuki/3.png")
image natsuki 5m = im.Composite((960, 960), (18, 22), "natsuki/m.png", (0, 0), "natsuki/3.png")
image natsuki 5n = im.Composite((960, 960), (18, 22), "natsuki/n.png", (0, 0), "natsuki/3.png")
image natsuki 5o = im.Composite((960, 960), (18, 22), "natsuki/o.png", (0, 0), "natsuki/3.png")
image natsuki 5p = im.Composite((960, 960), (18, 22), "natsuki/p.png", (0, 0), "natsuki/3.png")
image natsuki 5q = im.Composite((960, 960), (18, 22), "natsuki/q.png", (0, 0), "natsuki/3.png")
image natsuki 5r = im.Composite((960, 960), (18, 22), "natsuki/r.png", (0, 0), "natsuki/3.png")
image natsuki 5s = im.Composite((960, 960), (18, 22), "natsuki/s.png", (0, 0), "natsuki/3.png")
image natsuki 5t = im.Composite((960, 960), (18, 22), "natsuki/t.png", (0, 0), "natsuki/3.png")
image natsuki 5u = im.Composite((960, 960), (18, 22), "natsuki/u.png", (0, 0), "natsuki/3.png")
image natsuki 5v = im.Composite((960, 960), (18, 22), "natsuki/v.png", (0, 0), "natsuki/3.png")
image natsuki 5w = im.Composite((960, 960), (18, 22), "natsuki/w.png", (0, 0), "natsuki/3.png")
image natsuki 5x = im.Composite((960, 960), (18, 22), "natsuki/x.png", (0, 0), "natsuki/3.png")
image natsuki 5y = im.Composite((960, 960), (18, 22), "natsuki/y.png", (0, 0), "natsuki/3.png")
image natsuki 5z = im.Composite((960, 960), (18, 22), "natsuki/z.png", (0, 0), "natsuki/3.png")

# Natsuki in her casual outfit [Day 4 - Natsuki Route]
image natsuki 1ba = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/a.png")
image natsuki 1bb = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/b.png")
image natsuki 1bc = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/c.png")
image natsuki 1bd = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/d.png")
image natsuki 1be = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/e.png")
image natsuki 1bf = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/f.png")
image natsuki 1bg = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/g.png")
image natsuki 1bh = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/h.png")
image natsuki 1bi = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/i.png")
image natsuki 1bj = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/j.png")
image natsuki 1bk = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/k.png")
image natsuki 1bl = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/l.png")
image natsuki 1bm = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/m.png")
image natsuki 1bn = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/n.png")
image natsuki 1bo = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/o.png")
image natsuki 1bp = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/p.png")
image natsuki 1bq = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/q.png")
image natsuki 1br = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/r.png")
image natsuki 1bs = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/s.png")
image natsuki 1bt = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/t.png")
image natsuki 1bu = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/u.png")
image natsuki 1bv = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/v.png")
image natsuki 1bw = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/w.png")
image natsuki 1bx = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/x.png")
image natsuki 1by = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/y.png")
image natsuki 1bz = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/z.png")

image natsuki 2ba = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/a.png")
image natsuki 2bb = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/b.png")
image natsuki 2bc = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/c.png")
image natsuki 2bd = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/d.png")
image natsuki 2be = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/e.png")
image natsuki 2bf = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/f.png")
image natsuki 2bg = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/g.png")
image natsuki 2bh = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/h.png")
image natsuki 2bi = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/i.png")
image natsuki 2bj = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/j.png")
image natsuki 2bk = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/k.png")
image natsuki 2bl = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/l.png")
image natsuki 2bm = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/m.png")
image natsuki 2bn = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/n.png")
image natsuki 2bo = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/o.png")
image natsuki 2bp = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/p.png")
image natsuki 2bq = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/q.png")
image natsuki 2br = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/r.png")
image natsuki 2bs = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/s.png")
image natsuki 2bt = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/t.png")
image natsuki 2bu = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/u.png")
image natsuki 2bv = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/v.png")
image natsuki 2bw = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/w.png")
image natsuki 2bx = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/x.png")
image natsuki 2by = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/y.png")
image natsuki 2bz = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/z.png")

image natsuki 3ba = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/a.png")
image natsuki 3bb = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/b.png")
image natsuki 3bc = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/c.png")
image natsuki 3bd = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/d.png")
image natsuki 3be = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/e.png")
image natsuki 3bf = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/f.png")
image natsuki 3bg = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/g.png")
image natsuki 3bh = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/h.png")
image natsuki 3bi = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/i.png")
image natsuki 3bj = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/j.png")
image natsuki 3bk = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/k.png")
image natsuki 3bl = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/l.png")
image natsuki 3bm = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/m.png")
image natsuki 3bn = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/n.png")
image natsuki 3bo = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/o.png")
image natsuki 3bp = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/p.png")
image natsuki 3bq = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/q.png")
image natsuki 3br = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/r.png")
image natsuki 3bs = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/s.png")
image natsuki 3bt = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/t.png")
image natsuki 3bu = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/u.png")
image natsuki 3bv = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/v.png")
image natsuki 3bw = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/w.png")
image natsuki 3bx = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/x.png")
image natsuki 3by = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/y.png")
image natsuki 3bz = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/z.png")

image natsuki 4ba = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/a.png")
image natsuki 4bb = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/b.png")
image natsuki 4bc = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/c.png")
image natsuki 4bd = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/d.png")
image natsuki 4be = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/e.png")
image natsuki 4bf = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/f.png")
image natsuki 4bg = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/g.png")
image natsuki 4bh = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/h.png")
image natsuki 4bi = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/i.png")
image natsuki 4bj = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/j.png")
image natsuki 4bk = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/k.png")
image natsuki 4bl = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/l.png")
image natsuki 4bm = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/m.png")
image natsuki 4bn = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/n.png")
image natsuki 4bo = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/o.png")
image natsuki 4bp = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/p.png")
image natsuki 4bq = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/q.png")
image natsuki 4br = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/r.png")
image natsuki 4bs = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/s.png")
image natsuki 4bt = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/t.png")
image natsuki 4bu = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/u.png")
image natsuki 4bv = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/v.png")
image natsuki 4bw = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/w.png")
image natsuki 4bx = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/x.png")
image natsuki 4by = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/y.png")
image natsuki 4bz = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/z.png")

image natsuki 12ba = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bta.png")
image natsuki 12bb = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btb.png")
image natsuki 12bc = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btc.png")
image natsuki 12bd = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btd.png")
image natsuki 12be = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bte.png")
image natsuki 12bf = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btf.png")
image natsuki 12bg = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btg.png")
image natsuki 12bh = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bth.png")
image natsuki 12bi = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bti.png")

image natsuki 42ba = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bta.png")
image natsuki 42bb = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btb.png")
image natsuki 42bc = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btc.png")
image natsuki 42bd = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btd.png")
image natsuki 42be = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bte.png")
image natsuki 42bf = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btf.png")
image natsuki 42bg = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btg.png")
image natsuki 42bh = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bth.png")
image natsuki 42bi = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bti.png")

image natsuki 5ba = im.Composite((960, 960), (18, 22), "natsuki/a.png", (0, 0), "natsuki/3b.png")
image natsuki 5bb = im.Composite((960, 960), (18, 22), "natsuki/b.png", (0, 0), "natsuki/3b.png")
image natsuki 5bc = im.Composite((960, 960), (18, 22), "natsuki/c.png", (0, 0), "natsuki/3b.png")
image natsuki 5bd = im.Composite((960, 960), (18, 22), "natsuki/d.png", (0, 0), "natsuki/3b.png")
image natsuki 5be = im.Composite((960, 960), (18, 22), "natsuki/e.png", (0, 0), "natsuki/3b.png")
image natsuki 5bf = im.Composite((960, 960), (18, 22), "natsuki/f.png", (0, 0), "natsuki/3b.png")
image natsuki 5bg = im.Composite((960, 960), (18, 22), "natsuki/g.png", (0, 0), "natsuki/3b.png")
image natsuki 5bh = im.Composite((960, 960), (18, 22), "natsuki/h.png", (0, 0), "natsuki/3b.png")
image natsuki 5bi = im.Composite((960, 960), (18, 22), "natsuki/i.png", (0, 0), "natsuki/3b.png")
image natsuki 5bj = im.Composite((960, 960), (18, 22), "natsuki/j.png", (0, 0), "natsuki/3b.png")
image natsuki 5bk = im.Composite((960, 960), (18, 22), "natsuki/k.png", (0, 0), "natsuki/3b.png")
image natsuki 5bl = im.Composite((960, 960), (18, 22), "natsuki/l.png", (0, 0), "natsuki/3b.png")
image natsuki 5bm = im.Composite((960, 960), (18, 22), "natsuki/m.png", (0, 0), "natsuki/3b.png")
image natsuki 5bn = im.Composite((960, 960), (18, 22), "natsuki/n.png", (0, 0), "natsuki/3b.png")
image natsuki 5bo = im.Composite((960, 960), (18, 22), "natsuki/o.png", (0, 0), "natsuki/3b.png")
image natsuki 5bp = im.Composite((960, 960), (18, 22), "natsuki/p.png", (0, 0), "natsuki/3b.png")
image natsuki 5bq = im.Composite((960, 960), (18, 22), "natsuki/q.png", (0, 0), "natsuki/3b.png")
image natsuki 5br = im.Composite((960, 960), (18, 22), "natsuki/r.png", (0, 0), "natsuki/3b.png")
image natsuki 5bs = im.Composite((960, 960), (18, 22), "natsuki/s.png", (0, 0), "natsuki/3b.png")
image natsuki 5bt = im.Composite((960, 960), (18, 22), "natsuki/t.png", (0, 0), "natsuki/3b.png")
image natsuki 5bu = im.Composite((960, 960), (18, 22), "natsuki/u.png", (0, 0), "natsuki/3b.png")
image natsuki 5bv = im.Composite((960, 960), (18, 22), "natsuki/v.png", (0, 0), "natsuki/3b.png")
image natsuki 5bw = im.Composite((960, 960), (18, 22), "natsuki/w.png", (0, 0), "natsuki/3b.png")
image natsuki 5bx = im.Composite((960, 960), (18, 22), "natsuki/x.png", (0, 0), "natsuki/3b.png")
image natsuki 5by = im.Composite((960, 960), (18, 22), "natsuki/y.png", (0, 0), "natsuki/3b.png")
image natsuki 5bz = im.Composite((960, 960), (18, 22), "natsuki/z.png", (0, 0), "natsuki/3b.png")

# These image definitions are left-overs of certain Natsuki expressions 
# found in the original 1.0 release of DDLC.
image natsuki 1 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 2 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 3 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 4 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 5 = im.Composite((960, 960), (18, 22), "natsuki/1t.png", (0, 0), "natsuki/3.png")

# This image shows the realistic mouth on Natsuki on a random playthrough
# of Act 2.
image natsuki mouth = im.Composite((960, 960), (0, 0), "natsuki/0.png", (390, 340), "n_rects_mouth", (480, 334), "n_rects_mouth")

# This image shows black rectangles on Natsuki on a random playthrough
# of Act 2.
image n_rects_mouth:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    size (20, 25)

# This image transform makes the realistic mouth move on Natsuki's face
# on a random playthrough of Act 2.
image n_moving_mouth:
    "images/natsuki/mouth.png"
    pos (615, 305)
    xanchor 0.5 yanchor 0.5
    parallel:
        choice:
            ease 0.10 yzoom 0.2
        choice:
            ease 0.05 yzoom 0.2
        choice:
            ease 0.075 yzoom 0.2
        pass
        choice:
            0.02
        choice:
            0.04
        choice:
            0.06
        choice:
            0.08
        pass
        choice:
            ease 0.10 yzoom 1
        choice:
            ease 0.05 yzoom 1
        choice:
            ease 0.075 yzoom 1
        pass
        choice:
            0.02
        choice:
            0.04
        choice:
            0.06
        choice:
            0.08
        repeat
    parallel:
        choice:
            0.2
        choice:
            0.4
        choice:
            0.6
        ease 0.2 xzoom 0.4
        ease 0.2 xzoom 0.8
        repeat

# These images show the Natsuki ghost sprite shown in the poemgame of 
# Act 2.
image natsuki_ghost_blood:
    "#00000000"
    "natsuki/ghost_blood.png" with ImageDissolve("images/menu/wipedown.png", 80.0, ramplen=4, alpha=True)
    pos (620,320) zoom 0.80

image natsuki ghost_base:
    "natsuki/ghost1.png"
image natsuki ghost1:
    "natsuki 11"
    "natsuki ghost_base" with Dissolve(20.0, alpha=True)
image natsuki ghost2 = Image("natsuki/ghost2.png")
image natsuki ghost3 = Image("natsuki/ghost3.png")
image natsuki ghost4:
    "natsuki ghost3"
    parallel:
        easeout 0.25 zoom 4.5 yoffset 1200
    parallel:
        ease 0.025 xoffset -20
        ease 0.025 xoffset 20
        repeat
    0.25
    "black"

# This image makes Natsuki's sprite glitch up for a bit before
# returning to normal.
image natsuki glitch1:
    "natsuki/glitch1.png"
    zoom 1.25
    block:
        yoffset 300 xoffset 100 ytile 2
        linear 0.15 yoffset 200
        repeat
    time 0.75
    yoffset 0 zoom 1 xoffset 0 ytile 1
    "natsuki 4e"

image natsuki scream = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/scream.png")
image natsuki vomit = "natsuki/vomit.png"

# These images declare alterative eyes for Natsuki on a random playthrough of
# Act 2.
image n_blackeyes = "images/natsuki/blackeyes.png"
image n_eye = "images/natsuki/eye.png"

# Yuri's Character Definitions
# Note: Sprites with a 'y' in the middle are Yuri's Yandere Sprites.
image yuri 1 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/a.png")
image yuri 2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png")
image yuri 3 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png")
image yuri 4 = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/a2.png")

image yuri 1a = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/a.png")
image yuri 1b = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/b.png")
image yuri 1c = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/c.png")
image yuri 1d = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/d.png")
image yuri 1e = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/e.png")
image yuri 1f = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/f.png")
image yuri 1g = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/g.png")
image yuri 1h = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/h.png")
image yuri 1i = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/i.png")
image yuri 1j = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/j.png")
image yuri 1k = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/k.png")
image yuri 1l = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/l.png")
image yuri 1m = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/m.png")
image yuri 1n = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/n.png")
image yuri 1o = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/o.png")
image yuri 1p = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/p.png")
image yuri 1q = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/q.png")
image yuri 1r = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/r.png")
image yuri 1s = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/s.png")
image yuri 1t = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/t.png")
image yuri 1u = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/u.png")
image yuri 1v = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/v.png")
image yuri 1w = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/w.png")

image yuri 1y1 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y1.png")
image yuri 1y2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y2.png")
image yuri 1y3 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y3.png")
image yuri 1y4 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y4.png")
image yuri 1y5 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y5.png")
image yuri 1y6 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y6.png")
image yuri 1y7 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y7.png")

image yuri 2a = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png")
image yuri 2b = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/b.png")
image yuri 2c = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/c.png")
image yuri 2d = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/d.png")
image yuri 2e = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/e.png")
image yuri 2f = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/f.png")
image yuri 2g = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/g.png")
image yuri 2h = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/h.png")
image yuri 2i = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/i.png")
image yuri 2j = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/j.png")
image yuri 2k = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/k.png")
image yuri 2l = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/l.png")
image yuri 2m = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/m.png")
image yuri 2n = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/n.png")
image yuri 2o = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/o.png")
image yuri 2p = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/p.png")
image yuri 2q = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/q.png")
image yuri 2r = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/r.png")
image yuri 2s = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/s.png")
image yuri 2t = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/t.png")
image yuri 2u = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/u.png")
image yuri 2v = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/v.png")
image yuri 2w = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/w.png")

image yuri 2y1 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y1.png")
image yuri 2y2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y2.png")
image yuri 2y3 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y3.png")
image yuri 2y4 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y4.png")
image yuri 2y5 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y5.png")
image yuri 2y6 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y6.png")
image yuri 2y7 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y7.png")

image yuri 3a = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png")
image yuri 3b = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/b.png")
image yuri 3c = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/c.png")
image yuri 3d = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/d.png")
image yuri 3e = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/e.png")
image yuri 3f = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/f.png")
image yuri 3g = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/g.png")
image yuri 3h = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/h.png")
image yuri 3i = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/i.png")
image yuri 3j = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/j.png")
image yuri 3k = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/k.png")
image yuri 3l = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/l.png")
image yuri 3m = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/m.png")
image yuri 3n = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/n.png")
image yuri 3o = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/o.png")
image yuri 3p = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/p.png")
image yuri 3q = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/q.png")
image yuri 3r = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/r.png")
image yuri 3s = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/s.png")
image yuri 3t = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/t.png")
image yuri 3u = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/u.png")
image yuri 3v = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/v.png")
image yuri 3w = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/w.png")

image yuri 3y1 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y1.png")
image yuri 3y2 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y2.png")
image yuri 3y3 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y3.png")
image yuri 3y4 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y4.png")
image yuri 3y5 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y5.png")
image yuri 3y6 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y6.png")
image yuri 3y7 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y7.png")

image yuri 4a = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/a2.png")
image yuri 4b = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/b2.png")
image yuri 4c = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/c2.png")
image yuri 4d = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/d2.png")
image yuri 4e = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/e2.png")

# Yuri in her casual outfit [Day 4 - Yuri Route]
image yuri 1ba = im.Composite((960, 960), (0, 0), "yuri/a.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bb = im.Composite((960, 960), (0, 0), "yuri/b.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bc = im.Composite((960, 960), (0, 0), "yuri/c.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bd = im.Composite((960, 960), (0, 0), "yuri/d.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1be = im.Composite((960, 960), (0, 0), "yuri/e.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bf = im.Composite((960, 960), (0, 0), "yuri/f.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bg = im.Composite((960, 960), (0, 0), "yuri/g.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bh = im.Composite((960, 960), (0, 0), "yuri/h.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bi = im.Composite((960, 960), (0, 0), "yuri/i.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bj = im.Composite((960, 960), (0, 0), "yuri/j.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bk = im.Composite((960, 960), (0, 0), "yuri/k.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bl = im.Composite((960, 960), (0, 0), "yuri/l.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bm = im.Composite((960, 960), (0, 0), "yuri/m.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bn = im.Composite((960, 960), (0, 0), "yuri/n.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bo = im.Composite((960, 960), (0, 0), "yuri/o.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bp = im.Composite((960, 960), (0, 0), "yuri/p.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bq = im.Composite((960, 960), (0, 0), "yuri/q.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1br = im.Composite((960, 960), (0, 0), "yuri/r.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bs = im.Composite((960, 960), (0, 0), "yuri/s.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bt = im.Composite((960, 960), (0, 0), "yuri/t.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bu = im.Composite((960, 960), (0, 0), "yuri/u.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bv = im.Composite((960, 960), (0, 0), "yuri/v.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bw = im.Composite((960, 960), (0, 0), "yuri/w.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")

image yuri 2ba = im.Composite((960, 960), (0, 0), "yuri/a.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bb = im.Composite((960, 960), (0, 0), "yuri/b.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bc = im.Composite((960, 960), (0, 0), "yuri/c.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bd = im.Composite((960, 960), (0, 0), "yuri/d.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2be = im.Composite((960, 960), (0, 0), "yuri/e.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bf = im.Composite((960, 960), (0, 0), "yuri/f.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bg = im.Composite((960, 960), (0, 0), "yuri/g.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bh = im.Composite((960, 960), (0, 0), "yuri/h.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bi = im.Composite((960, 960), (0, 0), "yuri/i.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bj = im.Composite((960, 960), (0, 0), "yuri/j.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bk = im.Composite((960, 960), (0, 0), "yuri/k.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bl = im.Composite((960, 960), (0, 0), "yuri/l.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bm = im.Composite((960, 960), (0, 0), "yuri/m.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bn = im.Composite((960, 960), (0, 0), "yuri/n.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bo = im.Composite((960, 960), (0, 0), "yuri/o.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bp = im.Composite((960, 960), (0, 0), "yuri/p.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bq = im.Composite((960, 960), (0, 0), "yuri/q.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2br = im.Composite((960, 960), (0, 0), "yuri/r.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bs = im.Composite((960, 960), (0, 0), "yuri/s.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bt = im.Composite((960, 960), (0, 0), "yuri/t.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bu = im.Composite((960, 960), (0, 0), "yuri/u.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bv = im.Composite((960, 960), (0, 0), "yuri/v.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bw = im.Composite((960, 960), (0, 0), "yuri/w.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")

image yuri 3ba = im.Composite((960, 960), (0, 0), "yuri/a.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bb = im.Composite((960, 960), (0, 0), "yuri/b.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bc = im.Composite((960, 960), (0, 0), "yuri/c.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bd = im.Composite((960, 960), (0, 0), "yuri/d.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3be = im.Composite((960, 960), (0, 0), "yuri/e.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bf = im.Composite((960, 960), (0, 0), "yuri/f.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bg = im.Composite((960, 960), (0, 0), "yuri/g.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bh = im.Composite((960, 960), (0, 0), "yuri/h.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bi = im.Composite((960, 960), (0, 0), "yuri/i.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bj = im.Composite((960, 960), (0, 0), "yuri/j.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bk = im.Composite((960, 960), (0, 0), "yuri/k.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bl = im.Composite((960, 960), (0, 0), "yuri/l.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bm = im.Composite((960, 960), (0, 0), "yuri/m.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bn = im.Composite((960, 960), (0, 0), "yuri/n.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bo = im.Composite((960, 960), (0, 0), "yuri/o.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bp = im.Composite((960, 960), (0, 0), "yuri/p.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bq = im.Composite((960, 960), (0, 0), "yuri/q.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3br = im.Composite((960, 960), (0, 0), "yuri/r.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bs = im.Composite((960, 960), (0, 0), "yuri/s.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bt = im.Composite((960, 960), (0, 0), "yuri/t.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bu = im.Composite((960, 960), (0, 0), "yuri/u.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bv = im.Composite((960, 960), (0, 0), "yuri/v.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bw = im.Composite((960, 960), (0, 0), "yuri/w.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")

image yuri 4ba = im.Composite((960, 960), (0, 0), "yuri/a2.png", (0, 0), "yuri/3b.png")
image yuri 4bb = im.Composite((960, 960), (0, 0), "yuri/b2.png", (0, 0), "yuri/3b.png")
image yuri 4bc = im.Composite((960, 960), (0, 0), "yuri/c2.png", (0, 0), "yuri/3b.png")
image yuri 4bd = im.Composite((960, 960), (0, 0), "yuri/d2.png", (0, 0), "yuri/3b.png")
image yuri 4be = im.Composite((960, 960), (0, 0), "yuri/e2.png", (0, 0), "yuri/3b.png")

# This image shows the looping Yuri glitched head in Act 2.
image y_glitch_head:
    "images/yuri/za.png"
    0.15
    "images/yuri/zb.png"
    0.15
    "images/yuri/zc.png"
    0.15
    "images/yuri/zd.png"
    0.15
    repeat

# These images shows Yuri stabbing herself at the end of Act 2 in six stages.
image yuri stab_1 = "yuri/stab/1.png"
image yuri stab_2 = "yuri/stab/2.png"
image yuri stab_3 = "yuri/stab/3.png"
image yuri stab_4 = "yuri/stab/4.png"
image yuri stab_5 = "yuri/stab/5.png"
image yuri stab_6 = im.Composite((960,960), (0, 0), "yuri/stab/6-mask.png", (0, 0), "yuri stab_6_eyes", (0, 0), "yuri/stab/6.png")

# This image transform animates Yuri's eyes on her 6th stabbing in Act 2.
image yuri stab_6_eyes:
    "yuri/stab/6-eyes.png"
    subpixel True
    parallel:
        choice:
            xoffset 0.5
        choice:
            xoffset 0
        choice:
            xoffset -0.5
        0.2
        repeat
    parallel:
        choice:
            yoffset 0.5
        choice:
            yoffset 0
        choice:
            yoffset -0.5
        0.2
        repeat
    parallel:
        2.05
        easeout 1.0 yoffset -15
        linear 10 yoffset -15

# These images shows Yuri with a offcenter right eye moving slowing away
# from her face.
image yuri oneeye = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/oneeye.png", (0, 0), "yuri oneeye2")
image yuri oneeye2:
    "yuri/oneeye2.png"
    subpixel True
    pause 5.0
    linear 60 xoffset -50 yoffset 20

# These images show a glitched Yuri during Act 2.
image yuri glitch:
    "yuri/glitch1.png"
    pause 0.1
    "yuri/glitch2.png"
    pause 0.1
    "yuri/glitch3.png"
    pause 0.1
    "yuri/glitch4.png"
    pause 0.1
    "yuri/glitch5.png"
    pause 0.1
    repeat
image yuri glitch2:
    "yuri/0a.png"
    pause 0.1
    "yuri/0b.png"
    pause 0.5
    "yuri/0a.png"
    pause 0.3
    "yuri/0b.png"
    pause 0.3
    "yuri 1"

# These image declarations show Yuri's moving eyes in Act 2.
image yuri eyes = im.Composite((1280, 720), (0, 0), "yuri/eyes1.png", (0, 0), "yuripupils")

# This image shows the base of Yuri's sprite as her eyes move.
image yuri eyes_base = "yuri/eyes1.png"

# This image shows Yuri's realistic moving eyes during Act 2.
image yuripupils:
    "yuri/eyes2.png"
    yuripupils_move

image yuri cuts = "yuri/cuts.png"

# This image shows another glitched Yuri from Act 2. 
image yuri dragon:
    "yuri 3"
    0.25
    parallel:
        "yuri/dragon1.png"
        0.01
        "yuri/dragon2.png"
        0.01
        repeat
    parallel:
        0.01
        choice:
            xoffset -1
            xoffset -2
            xoffset -5
            xoffset -6
            xoffset -9
            xoffset -10
        0.01
        xoffset 0
        repeat
    time 0.55
    xoffset 0
    "yuri 3"

# Monika's Character Definitions
image monika 1 = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
image monika 2 = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png")
image monika 3 = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
image monika 4 = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png")
image monika 5 = im.Composite((960, 960), (0, 0), "monika/3a.png")

image monika 1a = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
image monika 1b = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/b.png")
image monika 1c = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/c.png")
image monika 1d = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/d.png")
image monika 1e = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/e.png")
image monika 1f = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/f.png")
image monika 1g = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/g.png")
image monika 1h = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/h.png")
image monika 1i = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/i.png")
image monika 1j = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/j.png")
image monika 1k = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/k.png")
image monika 1l = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/l.png")
image monika 1m = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/m.png")
image monika 1n = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/n.png")
image monika 1o = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/o.png")
image monika 1p = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/p.png")
image monika 1q = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/q.png")
image monika 1r = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/r.png")

image monika 2a = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png")
image monika 2b = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/b.png")
image monika 2c = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/c.png")
image monika 2d = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/d.png")
image monika 2e = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/e.png")
image monika 2f = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/f.png")
image monika 2g = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/g.png")
image monika 2h = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/h.png")
image monika 2i = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/i.png")
image monika 2j = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/j.png")
image monika 2k = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/k.png")
image monika 2l = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/l.png")
image monika 2m = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/m.png")
image monika 2n = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/n.png")
image monika 2o = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/o.png")
image monika 2p = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/p.png")
image monika 2q = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/q.png")
image monika 2r = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/r.png")

image monika 3a = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
image monika 3b = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/b.png")
image monika 3c = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/c.png")
image monika 3d = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/d.png")
image monika 3e = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/e.png")
image monika 3f = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/f.png")
image monika 3g = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/g.png")
image monika 3h = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/h.png")
image monika 3i = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/i.png")
image monika 3j = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/j.png")
image monika 3k = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/k.png")
image monika 3l = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/l.png")
image monika 3m = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/m.png")
image monika 3n = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/n.png")
image monika 3o = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/o.png")
image monika 3p = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/p.png")
image monika 3q = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/q.png")
image monika 3r = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/r.png")

image monika 4a = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png")
image monika 4b = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/b.png")
image monika 4c = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/c.png")
image monika 4d = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/d.png")
image monika 4e = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/e.png")
image monika 4f = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/f.png")
image monika 4g = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/g.png")
image monika 4h = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/h.png")
image monika 4i = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/i.png")
image monika 4j = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/j.png")
image monika 4k = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/k.png")
image monika 4l = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/l.png")
image monika 4m = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/m.png")
image monika 4n = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/n.png")
image monika 4o = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/o.png")
image monika 4p = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/p.png")
image monika 4q = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/q.png")
image monika 4r = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/r.png")

image monika 5a = im.Composite((960, 960), (0, 0), "monika/3a.png")
image monika 5b = im.Composite((960, 960), (0, 0), "monika/3b.png")

# This image transform shows a glitched Monika during a special poem.
image monika g1:
    "monika/g1.png"
    xoffset 35 yoffset 55
    parallel:
        zoom 1.00
        linear 0.10 zoom 1.03
        repeat
    parallel:
        xoffset 35
        0.20
        xoffset 0
        0.05
        xoffset -10
        0.05
        xoffset 0
        0.05
        xoffset -80
        0.05
        repeat
    time 1.25
    xoffset 0 yoffset 0 zoom 1.00
    "monika 3"

# This image transform shows Monika being glitched as she is 
# deleted in Act 3.
image monika g2:
    block:
        choice:
            "monika/g2.png"
        choice:
            "monika/g3.png"
        choice:
            "monika/g4.png"
    block:
        choice:
            pause 0.05
        choice:
            pause 0.1
        choice:
            pause 0.15
        choice:
            pause 0.2
    repeat

##Custom Character Defs

image kryo 1 = im.Composite((960, 960), (0, 0), "mod_assets/kryo/Body/1.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")

image kryo 1a = im.Composite((960, 960), (0, 0), "mod_assets/kryo/Body/1.png", (0, 0), "mod_assets/Kryo/Expressions/a.png")
image kryo 1a1 = im.Composite((960, 960), (0, 0), "mod_assets/kryo/Body/1.png", (0, 0), "mod_assets/Kryo/Expressions/a1.png")
image kryo 1a30 = im.Composite((960, 960), (0, 0), "mod_assets/kryo/Body/1.png", (0, 0), "mod_assets/Kryo/Expressions/a30.png")
image kryo 1b = im.Composite((960, 960), (0, 0), "mod_assets/kryo/Body/1.png", (0, 0), "mod_assets/Kryo/Expressions/b.png")
image kryo 1b1 = im.Composite((960, 960), (0, 0), "mod_assets/kryo/Body/1.png", (0, 0), "mod_assets/Kryo/Expressions/b1.png")
image kryo 1c = im.Composite((960, 960), (0, 0), "mod_assets/kryo/Body/1.png", (0, 0), "mod_assets/Kryo/Expressions/c.png")
image kryo 1c1 = im.Composite((960, 960), (0, 0), "mod_assets/kryo/Body/1.png", (0, 0), "mod_assets/Kryo/Expressions/c1.png")
image kryo 1d = im.Composite((960, 960), (0, 0), "mod_assets/kryo/Body/1.png", (0, 0), "mod_assets/Kryo/Expressions/d.png")
image kryo 1e = im.Composite((960, 960), (0, 0), "mod_assets/kryo/Body/1.png", (0, 0), "mod_assets/Kryo/Expressions/e.png")
image kryo 1f = im.Composite((960, 960), (0, 0), "mod_assets/kryo/Body/1.png", (0, 0), "mod_assets/Kryo/Expressions/f.png")
image kryo 1g = im.Composite((960, 960), (0, 0), "mod_assets/kryo/Body/1.png", (0, 0), "mod_assets/Kryo/Expressions/g.png")
image kryo 1h = im.Composite((960, 960), (0, 0), "mod_assets/kryo/Body/1.png", (0, 0), "mod_assets/Kryo/Expressions/h.png")
image kryo 1i = im.Composite((960, 960), (0, 0), "mod_assets/kryo/Body/1.png", (0, 0), "mod_assets/Kryo/Expressions/i.png")
image kryo 1j = im.Composite((960, 960), (0, 0), "mod_assets/kryo/Body/1.png", (0, 0), "mod_assets/Kryo/Expressions/j.png")
image kryo 1k = im.Composite((960, 960), (0, 0), "mod_assets/kryo/Body/1.png", (0, 0), "mod_assets/Kryo/Expressions/k.png")
image kryo 1l = im.Composite((960, 960), (0, 0), "mod_assets/kryo/Body/1.png", (0, 0), "mod_assets/Kryo/Expressions/l.png")
image kryo 1m = im.Composite((960, 960), (0, 0), "mod_assets/kryo/Body/1.png", (0, 0), "mod_assets/Kryo/Expressions/m.png")
image kryo 1n = im.Composite((960, 960), (0, 0), "mod_assets/kryo/Body/1.png", (0, 0), "mod_assets/Kryo/Expressions/n.png")
image kryo 1o = im.Composite((960, 960), (0, 0), "mod_assets/kryo/Body/1.png", (0, 0), "mod_assets/Kryo/Expressions/o.png")
image kryo 1p = im.Composite((960, 960), (0, 0), "mod_assets/kryo/Body/1.png", (0, 0), "mod_assets/Kryo/Expressions/p.png")
image kryo 1q = im.Composite((960, 960), (0, 0), "mod_assets/kryo/Body/1.png", (0, 0), "mod_assets/Kryo/Expressions/q.png")
image kryo 1r = im.Composite((960, 960), (0, 0), "mod_assets/kryo/Body/1.png", (0, 0), "mod_assets/Kryo/Expressions/r.png")
image kryo 1s = im.Composite((960, 960), (0, 0), "mod_assets/kryo/Body/1.png", (0, 0), "mod_assets/Kryo/Expressions/s.png")
image kryo 1t = im.Composite((960, 960), (0, 0), "mod_assets/kryo/Body/1.png", (0, 0), "mod_assets/Kryo/Expressions/t.png")
image kryo 1u = im.Composite((960, 960), (0, 0), "mod_assets/kryo/Body/1.png", (0, 0), "mod_assets/Kryo/Expressions/u.png")
image kryo 1v = im.Composite((960, 960), (0, 0), "mod_assets/kryo/Body/1.png", (0, 0), "mod_assets/Kryo/Expressions/v.png")
image kryo 1w = im.Composite((960, 960), (0, 0), "mod_assets/kryo/Body/1.png", (0, 0), "mod_assets/Kryo/Expressions/w.png")
image kryo 1x = im.Composite((960, 960), (0, 0), "mod_assets/kryo/Body/1.png", (0, 0), "mod_assets/Kryo/Expressions/x.png")
image kryo 1y = im.Composite((960, 960), (0, 0), "mod_assets/kryo/Body/1.png", (0, 0), "mod_assets/Kryo/Expressions/y.png")
image kryo 1z = im.Composite((960, 960), (0, 0), "mod_assets/kryo/Body/1.png", (0, 0), "mod_assets/Kryo/Expressions/z.png")

image david 1a = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/1l.png", (0, 0), "mod_assets/david/Poses/1r.png", (0, 0), "mod_assets/david/Expressions/1.png")
image david 1b = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/1l.png", (0, 0), "mod_assets/david/Poses/1r.png", (0, 0), "mod_assets/david/Expressions/2.png")
image david 1c = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/1l.png", (0, 0), "mod_assets/david/Poses/1r.png", (0, 0), "mod_assets/david/Expressions/3.png")
image david 1d = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/1l.png", (0, 0), "mod_assets/david/Poses/1r.png", (0, 0), "mod_assets/david/Expressions/4.png")
image david 1e = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/1l.png", (0, 0), "mod_assets/david/Poses/1r.png", (0, 0), "mod_assets/david/Expressions/5.png")
image david 1f = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/1l.png", (0, 0), "mod_assets/david/Poses/1r.png", (0, 0), "mod_assets/david/Expressions/6.png")
image david 1g = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/1l.png", (0, 0), "mod_assets/david/Poses/1r.png", (0, 0), "mod_assets/david/Expressions/7.png")
image david 1h = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/1l.png", (0, 0), "mod_assets/david/Poses/1r.png", (0, 0), "mod_assets/david/Expressions/8.png")
image david 1i = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/1l.png", (0, 0), "mod_assets/david/Poses/1r.png", (0, 0), "mod_assets/david/Expressions/9.png")
image david 1j = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/1l.png", (0, 0), "mod_assets/david/Poses/1r.png", (0, 0), "mod_assets/david/Expressions/10.png")
image david 1k = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/1l.png", (0, 0), "mod_assets/david/Poses/1r.png", (0, 0), "mod_assets/david/Expressions/11.png")
image david 1l = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/1l.png", (0, 0), "mod_assets/david/Poses/1r.png", (0, 0), "mod_assets/david/Expressions/12.png")
image david 1m = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/1l.png", (0, 0), "mod_assets/david/Poses/1r.png", (0, 0), "mod_assets/david/Expressions/13a.png")
image david 1n = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/1l.png", (0, 0), "mod_assets/david/Poses/1r.png", (0, 0), "mod_assets/david/Expressions/13b.png")
image david 1o = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/1l.png", (0, 0), "mod_assets/david/Poses/1r.png", (0, 0), "mod_assets/david/Expressions/14.png")
image david 1p = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/1l.png", (0, 0), "mod_assets/david/Poses/1r.png", (0, 0), "mod_assets/david/Expressions/15.png")
image david 1q = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/1l.png", (0, 0), "mod_assets/david/Poses/1r.png", (0, 0), "mod_assets/david/Expressions/16.png")
image david 1r = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/1l.png", (0, 0), "mod_assets/david/Poses/1r.png", (0, 0), "mod_assets/david/Expressions/17a.png")
image david 1s = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/1l.png", (0, 0), "mod_assets/david/Poses/1r.png", (0, 0), "mod_assets/david/Expressions/17b.png")
image david 1t = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/1l.png", (0, 0), "mod_assets/david/Poses/1r.png", (0, 0), "mod_assets/david/Expressions/18.png")
image david 1u = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/1l.png", (0, 0), "mod_assets/david/Poses/1r.png", (0, 0), "mod_assets/david/Expressions/19.png")
image david 1v = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/1l.png", (0, 0), "mod_assets/david/Poses/1r.png", (0, 0), "mod_assets/david/Expressions/20.png")

image david 2a = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/1l.png", (0, 0), "mod_assets/david/Poses/2r.png", (0, 0), "mod_assets/david/Expressions/1.png")
image david 2b = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/1l.png", (0, 0), "mod_assets/david/Poses/2r.png", (0, 0), "mod_assets/david/Expressions/2.png")
image david 2c = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/1l.png", (0, 0), "mod_assets/david/Poses/2r.png", (0, 0), "mod_assets/david/Expressions/3.png")
image david 2d = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/1l.png", (0, 0), "mod_assets/david/Poses/2r.png", (0, 0), "mod_assets/david/Expressions/4.png")
image david 2e = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/1l.png", (0, 0), "mod_assets/david/Poses/2r.png", (0, 0), "mod_assets/david/Expressions/5.png")
image david 2f = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/1l.png", (0, 0), "mod_assets/david/Poses/2r.png", (0, 0), "mod_assets/david/Expressions/6.png")
image david 2g = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/1l.png", (0, 0), "mod_assets/david/Poses/2r.png", (0, 0), "mod_assets/david/Expressions/7.png")
image david 2h = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/1l.png", (0, 0), "mod_assets/david/Poses/2r.png", (0, 0), "mod_assets/david/Expressions/8.png")
image david 2i = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/1l.png", (0, 0), "mod_assets/david/Poses/2r.png", (0, 0), "mod_assets/david/Expressions/9.png")
image david 2j = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/1l.png", (0, 0), "mod_assets/david/Poses/2r.png", (0, 0), "mod_assets/david/Expressions/10.png")
image david 2k = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/1l.png", (0, 0), "mod_assets/david/Poses/2r.png", (0, 0), "mod_assets/david/Expressions/11.png")
image david 2l = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/1l.png", (0, 0), "mod_assets/david/Poses/2r.png", (0, 0), "mod_assets/david/Expressions/12.png")
image david 2m = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/1l.png", (0, 0), "mod_assets/david/Poses/2r.png", (0, 0), "mod_assets/david/Expressions/13a.png")
image david 2n = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/1l.png", (0, 0), "mod_assets/david/Poses/2r.png", (0, 0), "mod_assets/david/Expressions/13b.png")
image david 2o = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/1l.png", (0, 0), "mod_assets/david/Poses/2r.png", (0, 0), "mod_assets/david/Expressions/14.png")
image david 2p = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/1l.png", (0, 0), "mod_assets/david/Poses/2r.png", (0, 0), "mod_assets/david/Expressions/15.png")
image david 2q = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/1l.png", (0, 0), "mod_assets/david/Poses/2r.png", (0, 0), "mod_assets/david/Expressions/16.png")
image david 2r = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/1l.png", (0, 0), "mod_assets/david/Poses/2r.png", (0, 0), "mod_assets/david/Expressions/17a.png")
image david 2s = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/1l.png", (0, 0), "mod_assets/david/Poses/2r.png", (0, 0), "mod_assets/david/Expressions/17b.png")
image david 2t = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/1l.png", (0, 0), "mod_assets/david/Poses/2r.png", (0, 0), "mod_assets/david/Expressions/18.png")
image david 2u = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/1l.png", (0, 0), "mod_assets/david/Poses/2r.png", (0, 0), "mod_assets/david/Expressions/19.png")
image david 2v = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/1l.png", (0, 0), "mod_assets/david/Poses/2r.png", (0, 0), "mod_assets/david/Expressions/20.png")

image david 3a = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/2l.png", (0, 0), "mod_assets/david/Poses/1r.png", (0, 0), "mod_assets/david/Expressions/1.png")
image david 3b = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/2l.png", (0, 0), "mod_assets/david/Poses/1r.png", (0, 0), "mod_assets/david/Expressions/2.png")
image david 3c = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/2l.png", (0, 0), "mod_assets/david/Poses/1r.png", (0, 0), "mod_assets/david/Expressions/3.png")
image david 3d = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/2l.png", (0, 0), "mod_assets/david/Poses/1r.png", (0, 0), "mod_assets/david/Expressions/4.png")
image david 3e = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/2l.png", (0, 0), "mod_assets/david/Poses/1r.png", (0, 0), "mod_assets/david/Expressions/5.png")
image david 3f = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/2l.png", (0, 0), "mod_assets/david/Poses/1r.png", (0, 0), "mod_assets/david/Expressions/6.png")
image david 3g = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/2l.png", (0, 0), "mod_assets/david/Poses/1r.png", (0, 0), "mod_assets/david/Expressions/7.png")
image david 3h = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/2l.png", (0, 0), "mod_assets/david/Poses/1r.png", (0, 0), "mod_assets/david/Expressions/8.png")
image david 3i = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/2l.png", (0, 0), "mod_assets/david/Poses/1r.png", (0, 0), "mod_assets/david/Expressions/9.png")
image david 3j = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/2l.png", (0, 0), "mod_assets/david/Poses/1r.png", (0, 0), "mod_assets/david/Expressions/10.png")
image david 3k = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/2l.png", (0, 0), "mod_assets/david/Poses/1r.png", (0, 0), "mod_assets/david/Expressions/11.png")
image david 3l = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/2l.png", (0, 0), "mod_assets/david/Poses/1r.png", (0, 0), "mod_assets/david/Expressions/12.png")
image david 3m = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/2l.png", (0, 0), "mod_assets/david/Poses/1r.png", (0, 0), "mod_assets/david/Expressions/13a.png")
image david 3n = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/2l.png", (0, 0), "mod_assets/david/Poses/1r.png", (0, 0), "mod_assets/david/Expressions/13b.png")
image david 3o = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/2l.png", (0, 0), "mod_assets/david/Poses/1r.png", (0, 0), "mod_assets/david/Expressions/14.png")
image david 3p = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/2l.png", (0, 0), "mod_assets/david/Poses/1r.png", (0, 0), "mod_assets/david/Expressions/15.png")
image david 3q = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/2l.png", (0, 0), "mod_assets/david/Poses/1r.png", (0, 0), "mod_assets/david/Expressions/16.png")
image david 3r = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/2l.png", (0, 0), "mod_assets/david/Poses/1r.png", (0, 0), "mod_assets/david/Expressions/17a.png")
image david 3s = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/2l.png", (0, 0), "mod_assets/david/Poses/1r.png", (0, 0), "mod_assets/david/Expressions/17b.png")
image david 3t = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/2l.png", (0, 0), "mod_assets/david/Poses/1r.png", (0, 0), "mod_assets/david/Expressions/18.png")
image david 3u = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/2l.png", (0, 0), "mod_assets/david/Poses/1r.png", (0, 0), "mod_assets/david/Expressions/19.png")
image david 3v = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/2l.png", (0, 0), "mod_assets/david/Poses/1r.png", (0, 0), "mod_assets/david/Expressions/20.png")

image david 4a = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/2l.png", (0, 0), "mod_assets/david/Poses/2r.png", (0, 0), "mod_assets/david/Expressions/1.png")
image david 4b = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/2l.png", (0, 0), "mod_assets/david/Poses/2r.png", (0, 0), "mod_assets/david/Expressions/2.png")
image david 4c = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/2l.png", (0, 0), "mod_assets/david/Poses/2r.png", (0, 0), "mod_assets/david/Expressions/3.png")
image david 4d = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/2l.png", (0, 0), "mod_assets/david/Poses/2r.png", (0, 0), "mod_assets/david/Expressions/4.png")
image david 4e = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/2l.png", (0, 0), "mod_assets/david/Poses/2r.png", (0, 0), "mod_assets/david/Expressions/5.png")
image david 4f = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/2l.png", (0, 0), "mod_assets/david/Poses/2r.png", (0, 0), "mod_assets/david/Expressions/6.png")
image david 4g = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/2l.png", (0, 0), "mod_assets/david/Poses/2r.png", (0, 0), "mod_assets/david/Expressions/7.png")
image david 4h = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/2l.png", (0, 0), "mod_assets/david/Poses/2r.png", (0, 0), "mod_assets/david/Expressions/8.png")
image david 4i = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/2l.png", (0, 0), "mod_assets/david/Poses/2r.png", (0, 0), "mod_assets/david/Expressions/9.png")
image david 4j = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/2l.png", (0, 0), "mod_assets/david/Poses/2r.png", (0, 0), "mod_assets/david/Expressions/10.png")
image david 4k = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/2l.png", (0, 0), "mod_assets/david/Poses/2r.png", (0, 0), "mod_assets/david/Expressions/11.png")
image david 4l = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/2l.png", (0, 0), "mod_assets/david/Poses/2r.png", (0, 0), "mod_assets/david/Expressions/12.png")
image david 4m = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/2l.png", (0, 0), "mod_assets/david/Poses/2r.png", (0, 0), "mod_assets/david/Expressions/13a.png")
image david 4n = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/2l.png", (0, 0), "mod_assets/david/Poses/2r.png", (0, 0), "mod_assets/david/Expressions/13b.png")
image david 4o = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/2l.png", (0, 0), "mod_assets/david/Poses/2r.png", (0, 0), "mod_assets/david/Expressions/14.png")
image david 4p = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/2l.png", (0, 0), "mod_assets/david/Poses/2r.png", (0, 0), "mod_assets/david/Expressions/15.png")
image david 4q = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/2l.png", (0, 0), "mod_assets/david/Poses/2r.png", (0, 0), "mod_assets/david/Expressions/16.png")
image david 4r = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/2l.png", (0, 0), "mod_assets/david/Poses/2r.png", (0, 0), "mod_assets/david/Expressions/17a.png")
image david 4s = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/2l.png", (0, 0), "mod_assets/david/Poses/2r.png", (0, 0), "mod_assets/david/Expressions/17b.png")
image david 4t = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/2l.png", (0, 0), "mod_assets/david/Poses/2r.png", (0, 0), "mod_assets/david/Expressions/18.png")
image david 4u = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/2l.png", (0, 0), "mod_assets/david/Poses/2r.png", (0, 0), "mod_assets/david/Expressions/19.png")
image david 4v = im.Composite((960, 960), (0, 0), "mod_assets/david/Poses/2l.png", (0, 0), "mod_assets/david/Poses/2r.png", (0, 0), "mod_assets/david/Expressions/20.png")

image soverytired 1a = im.Composite((960, 960), (0, 0), "mod_assets/soverytired/svt.png")
image soverytired 1b = im.Composite((900, 900), (0, 0), "mod_assets/soverytired/svtold.png")

image dpmc 1a = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1.png", (0, 0), "mod_assets/dpmc/a.png")
image dpmc 1b = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1.png", (0, 0), "mod_assets/dpmc/b.png")
image dpmc 1c = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1.png", (0, 0), "mod_assets/dpmc/c.png")
image dpmc 1c1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1.png", (0, 0), "mod_assets/dpmc/c1.png")
image dpmc 1d = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1.png", (0, 0), "mod_assets/dpmc/d.png")
image dpmc 1d1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1.png", (0, 0), "mod_assets/dpmc/d1.png")
image dpmc 1e = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1.png", (0, 0), "mod_assets/dpmc/e.png")
image dpmc 1e1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1.png", (0, 0), "mod_assets/dpmc/e1.png")
image dpmc 1f = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1.png", (0, 0), "mod_assets/dpmc/f.png")
image dpmc 1f1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1.png", (0, 0), "mod_assets/dpmc/f1.png")
image dpmc 1g = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1.png", (0, 0), "mod_assets/dpmc/g.png")
image dpmc 1g1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1.png", (0, 0), "mod_assets/dpmc/g1.png")
image dpmc 1h = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1.png", (0, 0), "mod_assets/dpmc/h.png")
image dpmc 1h1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1.png", (0, 0), "mod_assets/dpmc/h1.png")
image dpmc 1i = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1.png", (0, 0), "mod_assets/dpmc/i.png")
image dpmc 1j = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1.png", (0, 0), "mod_assets/dpmc/j.png")
image dpmc 1j1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1.png", (0, 0), "mod_assets/dpmc/j1.png")
image dpmc 1k = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1.png", (0, 0), "mod_assets/dpmc/k.png")
image dpmc 1k1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1.png", (0, 0), "mod_assets/dpmc/k1.png")
image dpmc 1l = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1.png", (0, 0), "mod_assets/dpmc/l.png")
image dpmc 1l1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1.png", (0, 0), "mod_assets/dpmc/l1.png")
image dpmc 1m = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1.png", (0, 0), "mod_assets/dpmc/m.png")
image dpmc 1m1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1.png", (0, 0), "mod_assets/dpmc/m1.png")
image dpmc 1n = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1.png", (0, 0), "mod_assets/dpmc/n.png")
image dpmc 1o = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1.png", (0, 0), "mod_assets/dpmc/o.png")
image dpmc 1p = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1.png", (0, 0), "mod_assets/dpmc/p.png")
image dpmc 1q = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1.png", (0, 0), "mod_assets/dpmc/q.png")
image dpmc 1r = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1.png", (0, 0), "mod_assets/dpmc/r.png")
image dpmc 1r1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1.png", (0, 0), "mod_assets/dpmc/r1.png")
image dpmc 1r3 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1.png", (0, 0), "mod_assets/dpmc/r3.png")
image dpmc 1s = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1.png", (0, 0), "mod_assets/dpmc/s.png")
image dpmc 1s1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1.png", (0, 0), "mod_assets/dpmc/s1.png")
image dpmc 1s2 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1.png", (0, 0), "mod_assets/dpmc/s2.png")
image dpmc 1t = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1.png", (0, 0), "mod_assets/dpmc/t.png")
image dpmc 1t1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1.png", (0, 0), "mod_assets/dpmc/a.png")
image dpmc 1u = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1.png", (0, 0), "mod_assets/dpmc/u.png")
image dpmc 1u1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1.png", (0, 0), "mod_assets/dpmc/u1.png")
image dpmc 1v = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1.png", (0, 0), "mod_assets/dpmc/v.png")
image dpmc 1v1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1.png", (0, 0), "mod_assets/dpmc/a.png")
image dpmc 1w = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1.png", (0, 0), "mod_assets/dpmc/w.png")
image dpmc 1w1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1.png", (0, 0), "mod_assets/dpmc/w1.png")
image dpmc 1w2 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1.png", (0, 0), "mod_assets/dpmc/w2.png")
image dpmc 1x = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1.png", (0, 0), "mod_assets/dpmc/x.png")
image dpmc 1x1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1.png", (0, 0), "mod_assets/dpmc/x1.png")
image dpmc 1x2 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1.png", (0, 0), "mod_assets/dpmc/x2.png")
image dpmc 1y = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1.png", (0, 0), "mod_assets/dpmc/y.png")
image dpmc 1y1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1.png", (0, 0), "mod_assets/dpmc/y1.png")
image dpmc 1z = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1.png", (0, 0), "mod_assets/dpmc/z.png")
image dpmc 1z1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1.png", (0, 0), "mod_assets/dpmc/z1.png")
image dpmc 1z2 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1.png", (0, 0), "mod_assets/dpmc/z3.png")
image dpmc 1za = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1.png", (0, 0), "mod_assets/dpmc/za.png")
image dpmc 1za1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1.png", (0, 0), "mod_assets/dpmc/za1.png")
image dpmc 1za2 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1.png", (0, 0), "mod_assets/dpmc/za2.png")
image dpmc 1zb = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1.png", (0, 0), "mod_assets/dpmc/zb.png")
image dpmc 1zb1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1.png", (0, 0), "mod_assets/dpmc/zb1.png")
image dpmc 1zb2 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1.png", (0, 0), "mod_assets/dpmc/zb2.png")
image dpmc 1zc1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1.png", (0, 0), "mod_assets/dpmc/zc1.png")
image dpmc 1zc2 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1.png", (0, 0), "mod_assets/dpmc/zc2.png")
image dpmc 1zd = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1.png", (0, 0), "mod_assets/dpmc/zd.png")
image dpmc 1zd1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1.png", (0, 0), "mod_assets/dpmc/zd1.png")
image dpmc 1zd2 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1.png", (0, 0), "mod_assets/dpmc/zd2.png")
image dpmc 1ze = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1.png", (0, 0), "mod_assets/dpmc/ze.png")
image dpmc 1ze1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1.png", (0, 0), "mod_assets/dpmc/ze1.png")
image dpmc 1ze2 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1.png", (0, 0), "mod_assets/dpmc/ze2.png")

image dpmc 2a = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2.png", (0, 0), "mod_assets/dpmc/a.png")
image dpmc 2b = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2.png", (0, 0), "mod_assets/dpmc/b.png")
image dpmc 2c = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2.png", (0, 0), "mod_assets/dpmc/c.png")
image dpmc 2c1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2.png", (0, 0), "mod_assets/dpmc/c1.png")
image dpmc 2d = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2.png", (0, 0), "mod_assets/dpmc/d.png")
image dpmc 2d1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2.png", (0, 0), "mod_assets/dpmc/d1.png")
image dpmc 2e = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2.png", (0, 0), "mod_assets/dpmc/e.png")
image dpmc 2e1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2.png", (0, 0), "mod_assets/dpmc/e1.png")
image dpmc 2f = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2.png", (0, 0), "mod_assets/dpmc/f.png")
image dpmc 2f1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2.png", (0, 0), "mod_assets/dpmc/f1.png")
image dpmc 2g = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2.png", (0, 0), "mod_assets/dpmc/g.png")
image dpmc 2g1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2.png", (0, 0), "mod_assets/dpmc/g1.png")
image dpmc 2h = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2.png", (0, 0), "mod_assets/dpmc/h.png")
image dpmc 2h1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2.png", (0, 0), "mod_assets/dpmc/h1.png")
image dpmc 2i = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2.png", (0, 0), "mod_assets/dpmc/i.png")
image dpmc 2j = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2.png", (0, 0), "mod_assets/dpmc/j.png")
image dpmc 2j1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2.png", (0, 0), "mod_assets/dpmc/j1.png")
image dpmc 2k = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2.png", (0, 0), "mod_assets/dpmc/k.png")
image dpmc 2k1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2.png", (0, 0), "mod_assets/dpmc/k1.png")
image dpmc 2l = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2.png", (0, 0), "mod_assets/dpmc/l.png")
image dpmc 2l1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2.png", (0, 0), "mod_assets/dpmc/l1.png")
image dpmc 2m = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2.png", (0, 0), "mod_assets/dpmc/m.png")
image dpmc 2m1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2.png", (0, 0), "mod_assets/dpmc/m1.png")
image dpmc 2n = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2.png", (0, 0), "mod_assets/dpmc/n.png")
image dpmc 2o = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2.png", (0, 0), "mod_assets/dpmc/o.png")
image dpmc 2p = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2.png", (0, 0), "mod_assets/dpmc/p.png")
image dpmc 2q = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2.png", (0, 0), "mod_assets/dpmc/q.png")
image dpmc 2r = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2.png", (0, 0), "mod_assets/dpmc/r.png")
image dpmc 2r1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2.png", (0, 0), "mod_assets/dpmc/r1.png")
image dpmc 2r3 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2.png", (0, 0), "mod_assets/dpmc/r3.png")
image dpmc 2s = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2.png", (0, 0), "mod_assets/dpmc/s.png")
image dpmc 2s1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2.png", (0, 0), "mod_assets/dpmc/s1.png")
image dpmc 2s2 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2.png", (0, 0), "mod_assets/dpmc/s2.png")
image dpmc 2t = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2.png", (0, 0), "mod_assets/dpmc/t.png")
image dpmc 2t1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2.png", (0, 0), "mod_assets/dpmc/a.png")
image dpmc 2u = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2.png", (0, 0), "mod_assets/dpmc/u.png")
image dpmc 2u1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2.png", (0, 0), "mod_assets/dpmc/u1.png")
image dpmc 2v = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2.png", (0, 0), "mod_assets/dpmc/v.png")
image dpmc 2v1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2.png", (0, 0), "mod_assets/dpmc/a.png")
image dpmc 2w = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2.png", (0, 0), "mod_assets/dpmc/w.png")
image dpmc 2w1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2.png", (0, 0), "mod_assets/dpmc/w1.png")
image dpmc 2w2 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2.png", (0, 0), "mod_assets/dpmc/w2.png")
image dpmc 2x = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2.png", (0, 0), "mod_assets/dpmc/x.png")
image dpmc 2x1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2.png", (0, 0), "mod_assets/dpmc/x1.png")
image dpmc 2x2 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2.png", (0, 0), "mod_assets/dpmc/x2.png")
image dpmc 2y = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2.png", (0, 0), "mod_assets/dpmc/y.png")
image dpmc 2y1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2.png", (0, 0), "mod_assets/dpmc/y1.png")
image dpmc 2z = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2.png", (0, 0), "mod_assets/dpmc/z.png")
image dpmc 2z1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2.png", (0, 0), "mod_assets/dpmc/z1.png")
image dpmc 2z2 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2.png", (0, 0), "mod_assets/dpmc/z3.png")
image dpmc 2za = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2.png", (0, 0), "mod_assets/dpmc/za.png")
image dpmc 2za1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2.png", (0, 0), "mod_assets/dpmc/za1.png")
image dpmc 2za2 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2.png", (0, 0), "mod_assets/dpmc/za2.png")
image dpmc 2zb = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2.png", (0, 0), "mod_assets/dpmc/zb.png")
image dpmc 2zb1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2.png", (0, 0), "mod_assets/dpmc/zb1.png")
image dpmc 2zb2 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2.png", (0, 0), "mod_assets/dpmc/zb2.png")
image dpmc 2zc1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2.png", (0, 0), "mod_assets/dpmc/zc1.png")
image dpmc 2zc2 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2.png", (0, 0), "mod_assets/dpmc/zc2.png")
image dpmc 2zd = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2.png", (0, 0), "mod_assets/dpmc/zd.png")
image dpmc 2zd1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2.png", (0, 0), "mod_assets/dpmc/zd1.png")
image dpmc 2zd2 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2.png", (0, 0), "mod_assets/dpmc/zd2.png")
image dpmc 2ze = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2.png", (0, 0), "mod_assets/dpmc/ze.png")
image dpmc 2ze1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2.png", (0, 0), "mod_assets/dpmc/ze1.png")
image dpmc 2ze2 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2.png", (0, 0), "mod_assets/dpmc/ze2.png")

image dpmc 3a = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/3.png", (0, 0), "mod_assets/dpmc/a1.png")
image dpmc 3e = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/3.png", (0, 0), "mod_assets/dpmc/e2.png")
image dpmc 3i = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/3.png", (0, 0), "mod_assets/dpmc/i1.png")
image dpmc 3n = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/3.png", (0, 0), "mod_assets/dpmc/n1.png")
image dpmc 3r = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/3.png", (0, 0), "mod_assets/dpmc/r2.png")
image dpmc 3s = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/3.png", (0, 0), "mod_assets/dpmc/r4.png")

image dpmc 1yan1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1.png", (0, 0), "mod_assets/dpmc/yan1.png")
image dpmc 1yan2 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1.png", (0, 0), "mod_assets/dpmc/yan2.png")
image dpmc 1yan3 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1.png", (0, 0), "mod_assets/dpmc/yan3.png")
image dpmc 1yan4 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1.png", (0, 0), "mod_assets/dpmc/yan4.png")
image dpmc 1yan5 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1.png", (0, 0), "mod_assets/dpmc/yan5.png")
image dpmc 1yan6 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1.png", (0, 0), "mod_assets/dpmc/yan6.png")
image dpmc 1yan7 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1.png", (0, 0), "mod_assets/dpmc/yan7.png")
image dpmc 1yan8 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1.png", (0, 0), "mod_assets/dpmc/yan8.png")

image dpmc 2yan1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2.png", (0, 0), "mod_assets/dpmc/yan1.png")
image dpmc 2yan2 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2.png", (0, 0), "mod_assets/dpmc/yan2.png")
image dpmc 2yan3 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2.png", (0, 0), "mod_assets/dpmc/yan3.png")
image dpmc 2yan4 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2.png", (0, 0), "mod_assets/dpmc/yan4.png")
image dpmc 2yan5 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2.png", (0, 0), "mod_assets/dpmc/yan5.png")
image dpmc 2yan6 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2.png", (0, 0), "mod_assets/dpmc/yan6.png")
image dpmc 2yan7 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2.png", (0, 0), "mod_assets/dpmc/yan7.png")
image dpmc 2yan8 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2.png", (0, 0), "mod_assets/dpmc/yan8.png")

image dpmc glitch1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1.png", (0, 0), "mod_assets/dpmc/glitch1.png")
image dpmc glitch2 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1.png", (0, 0), "mod_assets/dpmc/glitch2.png")
image dpmc glitch3 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1.png", (0, 0), "mod_assets/dpmc/glitch3.png")


image dpmc 1ba = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1b.png", (0, 0), "mod_assets/dpmc/a.png")
image dpmc 1bb = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1b.png", (0, 0), "mod_assets/dpmc/b.png")
image dpmc 1bc = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1b.png", (0, 0), "mod_assets/dpmc/c.png")
image dpmc 1bc1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1b.png", (0, 0), "mod_assets/dpmc/c1.png")
image dpmc 1bd = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1b.png", (0, 0), "mod_assets/dpmc/d.png")
image dpmc 1bd1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1b.png", (0, 0), "mod_assets/dpmc/d1.png")
image dpmc 1be = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1b.png", (0, 0), "mod_assets/dpmc/e.png")
image dpmc 1be1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1b.png", (0, 0), "mod_assets/dpmc/e1.png")
image dpmc 1bf = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1b.png", (0, 0), "mod_assets/dpmc/f.png")
image dpmc 1bf1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1b.png", (0, 0), "mod_assets/dpmc/f1.png")
image dpmc 1bg = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1b.png", (0, 0), "mod_assets/dpmc/g.png")
image dpmc 1bg1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1b.png", (0, 0), "mod_assets/dpmc/g1.png")
image dpmc 1bh = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1b.png", (0, 0), "mod_assets/dpmc/h.png")
image dpmc 1bh1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1b.png", (0, 0), "mod_assets/dpmc/h1.png")
image dpmc 1bi = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1b.png", (0, 0), "mod_assets/dpmc/i.png")
image dpmc 1bj = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1b.png", (0, 0), "mod_assets/dpmc/j.png")
image dpmc 1bj1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1b.png", (0, 0), "mod_assets/dpmc/j1.png")
image dpmc 1bk = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1b.png", (0, 0), "mod_assets/dpmc/k.png")
image dpmc 1bk1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1b.png", (0, 0), "mod_assets/dpmc/k1.png")
image dpmc 1bl = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1b.png", (0, 0), "mod_assets/dpmc/l.png")
image dpmc 1bl1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1b.png", (0, 0), "mod_assets/dpmc/l1.png")
image dpmc 1bm = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1b.png", (0, 0), "mod_assets/dpmc/m.png")
image dpmc 1bm1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1b.png", (0, 0), "mod_assets/dpmc/m1.png")
image dpmc 1bn = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1b.png", (0, 0), "mod_assets/dpmc/n.png")
image dpmc 1bo = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1b.png", (0, 0), "mod_assets/dpmc/o.png")
image dpmc 1bp = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1b.png", (0, 0), "mod_assets/dpmc/p.png")
image dpmc 1bq = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1b.png", (0, 0), "mod_assets/dpmc/q.png")
image dpmc 1br = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1b.png", (0, 0), "mod_assets/dpmc/r.png")
image dpmc 1br1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1b.png", (0, 0), "mod_assets/dpmc/r1.png")
image dpmc 1br3 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1b.png", (0, 0), "mod_assets/dpmc/r3.png")
image dpmc 1bs = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1b.png", (0, 0), "mod_assets/dpmc/s.png")
image dpmc 1bs1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1b.png", (0, 0), "mod_assets/dpmc/s1.png")
image dpmc 1bs2 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1b.png", (0, 0), "mod_assets/dpmc/s2.png")
image dpmc 1bt = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1b.png", (0, 0), "mod_assets/dpmc/t.png")
image dpmc 1bt1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1b.png", (0, 0), "mod_assets/dpmc/a.png")
image dpmc 1bu = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1b.png", (0, 0), "mod_assets/dpmc/u.png")
image dpmc 1bu1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1b.png", (0, 0), "mod_assets/dpmc/u1.png")
image dpmc 1bv = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1b.png", (0, 0), "mod_assets/dpmc/v.png")
image dpmc 1bv1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1b.png", (0, 0), "mod_assets/dpmc/a.png")
image dpmc 1bw = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1b.png", (0, 0), "mod_assets/dpmc/w.png")
image dpmc 1bw1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1b.png", (0, 0), "mod_assets/dpmc/w1.png")
image dpmc 1bw2 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1b.png", (0, 0), "mod_assets/dpmc/w2.png")
image dpmc 1bx = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1b.png", (0, 0), "mod_assets/dpmc/x.png")
image dpmc 1bx1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1b.png", (0, 0), "mod_assets/dpmc/x1.png")
image dpmc 1bx2 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1b.png", (0, 0), "mod_assets/dpmc/x2.png")
image dpmc 1by = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1b.png", (0, 0), "mod_assets/dpmc/y.png")
image dpmc 1by1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1b.png", (0, 0), "mod_assets/dpmc/y1.png")
image dpmc 1bz = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1b.png", (0, 0), "mod_assets/dpmc/z.png")
image dpmc 1bz1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1b.png", (0, 0), "mod_assets/dpmc/z1.png")
image dpmc 1bz2 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1b.png", (0, 0), "mod_assets/dpmc/z3.png")
image dpmc 1bza = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1b.png", (0, 0), "mod_assets/dpmc/za.png")
image dpmc 1bza1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1b.png", (0, 0), "mod_assets/dpmc/za1.png")
image dpmc 1bza2 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1b.png", (0, 0), "mod_assets/dpmc/za2.png")
image dpmc 1bzb = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1b.png", (0, 0), "mod_assets/dpmc/zb.png")
image dpmc 1bzb1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1b.png", (0, 0), "mod_assets/dpmc/zb1.png")
image dpmc 1bzb2 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1b.png", (0, 0), "mod_assets/dpmc/zb2.png")
image dpmc 1bzc1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1b.png", (0, 0), "mod_assets/dpmc/zc1.png")
image dpmc 1bzc2 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1b.png", (0, 0), "mod_assets/dpmc/zc2.png")
image dpmc 1bzd = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1b.png", (0, 0), "mod_assets/dpmc/zd.png")
image dpmc 1bzd1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1b.png", (0, 0), "mod_assets/dpmc/zd1.png")
image dpmc 1bzd2 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1b.png", (0, 0), "mod_assets/dpmc/zd2.png")
image dpmc 1bze = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1b.png", (0, 0), "mod_assets/dpmc/ze.png")
image dpmc 1bze1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1b.png", (0, 0), "mod_assets/dpmc/ze1.png")
image dpmc 1bze2 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/1b.png", (0, 0), "mod_assets/dpmc/ze2.png")

image dpmc 2ba = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2b.png", (0, 0), "mod_assets/dpmc/a.png")
image dpmc 2bb = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2b.png", (0, 0), "mod_assets/dpmc/b.png")
image dpmc 2bc = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2b.png", (0, 0), "mod_assets/dpmc/c.png")
image dpmc 2bc1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2b.png", (0, 0), "mod_assets/dpmc/c1.png")
image dpmc 2bd = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2b.png", (0, 0), "mod_assets/dpmc/d.png")
image dpmc 2bd1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2b.png", (0, 0), "mod_assets/dpmc/d1.png")
image dpmc 2be = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2b.png", (0, 0), "mod_assets/dpmc/e.png")
image dpmc 2be1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2b.png", (0, 0), "mod_assets/dpmc/e1.png")
image dpmc 2bf = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2b.png", (0, 0), "mod_assets/dpmc/f.png")
image dpmc 2bf1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2b.png", (0, 0), "mod_assets/dpmc/f1.png")
image dpmc 2bg = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2b.png", (0, 0), "mod_assets/dpmc/g.png")
image dpmc 2bg1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2b.png", (0, 0), "mod_assets/dpmc/g1.png")
image dpmc 2bh = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2b.png", (0, 0), "mod_assets/dpmc/h.png")
image dpmc 2bh1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2b.png", (0, 0), "mod_assets/dpmc/h1.png")
image dpmc 2bi = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2b.png", (0, 0), "mod_assets/dpmc/i.png")
image dpmc 2bj = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2b.png", (0, 0), "mod_assets/dpmc/j.png")
image dpmc 2bj1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2b.png", (0, 0), "mod_assets/dpmc/j1.png")
image dpmc 2bk = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2b.png", (0, 0), "mod_assets/dpmc/k.png")
image dpmc 2bk1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2b.png", (0, 0), "mod_assets/dpmc/k1.png")
image dpmc 2bl = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2b.png", (0, 0), "mod_assets/dpmc/l.png")
image dpmc 2bl1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2b.png", (0, 0), "mod_assets/dpmc/l1.png")
image dpmc 2bm = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2b.png", (0, 0), "mod_assets/dpmc/m.png")
image dpmc 2bm1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2b.png", (0, 0), "mod_assets/dpmc/m1.png")
image dpmc 2bn = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2b.png", (0, 0), "mod_assets/dpmc/n.png")
image dpmc 2bo = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2b.png", (0, 0), "mod_assets/dpmc/o.png")
image dpmc 2bp = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2b.png", (0, 0), "mod_assets/dpmc/p.png")
image dpmc 2bq = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2b.png", (0, 0), "mod_assets/dpmc/q.png")
image dpmc 2br = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2b.png", (0, 0), "mod_assets/dpmc/r.png")
image dpmc 2br1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2b.png", (0, 0), "mod_assets/dpmc/r1.png")
image dpmc 2br3 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2b.png", (0, 0), "mod_assets/dpmc/r3.png")
image dpmc 2bs = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2b.png", (0, 0), "mod_assets/dpmc/s.png")
image dpmc 2bs1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2b.png", (0, 0), "mod_assets/dpmc/s1.png")
image dpmc 2bs2 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2b.png", (0, 0), "mod_assets/dpmc/s2.png")
image dpmc 2bt = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2b.png", (0, 0), "mod_assets/dpmc/t.png")
image dpmc 2bt1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2b.png", (0, 0), "mod_assets/dpmc/a.png")
image dpmc 2bu = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2b.png", (0, 0), "mod_assets/dpmc/u.png")
image dpmc 2bu1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2b.png", (0, 0), "mod_assets/dpmc/u1.png")
image dpmc 2bv = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2b.png", (0, 0), "mod_assets/dpmc/v.png")
image dpmc 2bv1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2b.png", (0, 0), "mod_assets/dpmc/a.png")
image dpmc 2bw = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2b.png", (0, 0), "mod_assets/dpmc/w.png")
image dpmc 2bw1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2b.png", (0, 0), "mod_assets/dpmc/w1.png")
image dpmc 2bw2 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2b.png", (0, 0), "mod_assets/dpmc/w2.png")
image dpmc 2bx = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2b.png", (0, 0), "mod_assets/dpmc/x.png")
image dpmc 2bx1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2b.png", (0, 0), "mod_assets/dpmc/x1.png")
image dpmc 2bx2 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2b.png", (0, 0), "mod_assets/dpmc/x2.png")
image dpmc 2by = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2b.png", (0, 0), "mod_assets/dpmc/y.png")
image dpmc 2by1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2b.png", (0, 0), "mod_assets/dpmc/y1.png")
image dpmc 2bz = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2b.png", (0, 0), "mod_assets/dpmc/z.png")
image dpmc 2bz1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2b.png", (0, 0), "mod_assets/dpmc/z1.png")
image dpmc 2bz2 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2b.png", (0, 0), "mod_assets/dpmc/z3.png")
image dpmc 2bza = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2b.png", (0, 0), "mod_assets/dpmc/za.png")
image dpmc 2bza1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2b.png", (0, 0), "mod_assets/dpmc/za1.png")
image dpmc 2bza2 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2b.png", (0, 0), "mod_assets/dpmc/za2.png")
image dpmc 2bzb = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2b.png", (0, 0), "mod_assets/dpmc/zb.png")
image dpmc 2bzb1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2b.png", (0, 0), "mod_assets/dpmc/zb1.png")
image dpmc 2bzb2 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2b.png", (0, 0), "mod_assets/dpmc/zb2.png")
image dpmc 2bzc1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2b.png", (0, 0), "mod_assets/dpmc/zc1.png")
image dpmc 2bzc2 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2b.png", (0, 0), "mod_assets/dpmc/zc2.png")
image dpmc 2bzd = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2b.png", (0, 0), "mod_assets/dpmc/zd.png")
image dpmc 2bzd1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2b.png", (0, 0), "mod_assets/dpmc/zd1.png")
image dpmc 2bzd2 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2b.png", (0, 0), "mod_assets/dpmc/zd2.png")
image dpmc 2bze = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2b.png", (0, 0), "mod_assets/dpmc/ze.png")
image dpmc 2bze1 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2b.png", (0, 0), "mod_assets/dpmc/ze1.png")
image dpmc 2bze2 = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/2b.png", (0, 0), "mod_assets/dpmc/ze2.png")

image dpmc 3ba = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/3b.png", (0, 0), "mod_assets/dpmc/a1.png")
image dpmc 3be = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/3b.png", (0, 0), "mod_assets/dpmc/e2.png")
image dpmc 3bi = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/3b.png", (0, 0), "mod_assets/dpmc/i1.png")
image dpmc 3bn = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/3b.png", (0, 0), "mod_assets/dpmc/n1.png")
image dpmc 3br = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/3b.png", (0, 0), "mod_assets/dpmc/r2.png")
image dpmc 3bs = im.Composite((960, 960), (0, 0), "mod_assets/dpmc/3b.png", (0, 0), "mod_assets/dpmc/r4.png")

image doomslayer 1a = im.Composite((360, 675), (0, 0), "mod_assets/doomslayer/1a.png")

image amana 1 = im.Composite((960, 960), (0, 0), "mod_assets/amana/0a.png", (0, 0), "mod_assets/amana/a.png")
image amana 2 = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/a.png")
image amana 3 = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/a.png")
image amana 4 = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/a.png")
image amana 5 = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/a.png")
image amana 6 = im.Composite((960, 960), (0, 0), "mod_assets/amana/3.png", (0, 0), "mod_assets/amana/a.png")

image amana 1a = im.Composite((960, 960), (0, 0), "mod_assets/amana/0a.png", (0, 0), "mod_assets/amana/a.png")
image amana 1a2 = im.Composite((960, 960), (0, 0), "mod_assets/amana/0a.png", (0, 0), "mod_assets/amana/a2.png")
image amana 1b = im.Composite((960, 960), (0, 0), "mod_assets/amana/0a.png", (0, 0), "mod_assets/amana/b.png")
image amana 1b2 = im.Composite((960, 960), (0, 0), "mod_assets/amana/0a.png", (0, 0), "mod_assets/amana/b2.png")
image amana 1c = im.Composite((960, 960), (0, 0), "mod_assets/amana/0a.png", (0, 0), "mod_assets/amana/c.png")
image amana 1c2 = im.Composite((960, 960), (0, 0), "mod_assets/amana/0a.png", (0, 0), "mod_assets/amana/c2.png")
image amana 1d = im.Composite((960, 960), (0, 0), "mod_assets/amana/0a.png", (0, 0), "mod_assets/amana/d.png")
image amana 1d2 = im.Composite((960, 960), (0, 0), "mod_assets/amana/0a.png", (0, 0), "mod_assets/amana/d2.png")
image amana 1e = im.Composite((960, 960), (0, 0), "mod_assets/amana/0a.png", (0, 0), "mod_assets/amana/e.png")
image amana 1e2 = im.Composite((960, 960), (0, 0), "mod_assets/amana/0a.png", (0, 0), "mod_assets/amana/e2.png")
image amana 1f = im.Composite((960, 960), (0, 0), "mod_assets/amana/0a.png", (0, 0), "mod_assets/amana/f.png")
image amana 1g = im.Composite((960, 960), (0, 0), "mod_assets/amana/0a.png", (0, 0), "mod_assets/amana/g.png")
image amana 1h = im.Composite((960, 960), (0, 0), "mod_assets/amana/0a.png", (0, 0), "mod_assets/amana/h.png")
image amana 1h2 = im.Composite((960, 960), (0, 0), "mod_assets/amana/0a.png", (0, 0), "mod_assets/amana/hisui.png")
image amana 1i = im.Composite((960, 960), (0, 0), "mod_assets/amana/0a.png", (0, 0), "mod_assets/amana/i.png")
image amana 1j = im.Composite((960, 960), (0, 0), "mod_assets/amana/0a.png", (0, 0), "mod_assets/amana/j.png")
image amana 1k = im.Composite((960, 960), (0, 0), "mod_assets/amana/0a.png", (0, 0), "mod_assets/amana/k.png")
image amana 1l = im.Composite((960, 960), (0, 0), "mod_assets/amana/0a.png", (0, 0), "mod_assets/amana/l.png")
image amana 1m = im.Composite((960, 960), (0, 0), "mod_assets/amana/0a.png", (0, 0), "mod_assets/amana/m.png")
image amana 1n = im.Composite((960, 960), (0, 0), "mod_assets/amana/0a.png", (0, 0), "mod_assets/amana/n.png")
image amana 1o = im.Composite((960, 960), (0, 0), "mod_assets/amana/0a.png", (0, 0), "mod_assets/amana/o.png")
image amana 1p = im.Composite((960, 960), (0, 0), "mod_assets/amana/0a.png", (0, 0), "mod_assets/amana/p.png")
image amana 1q = im.Composite((960, 960), (0, 0), "mod_assets/amana/0a.png", (0, 0), "mod_assets/amana/q.png")
image amana 1r = im.Composite((960, 960), (0, 0), "mod_assets/amana/0a.png", (0, 0), "mod_assets/amana/r.png")
image amana 1s = im.Composite((960, 960), (0, 0), "mod_assets/amana/0a.png", (0, 0), "mod_assets/amana/s.png")
image amana 1t = im.Composite((960, 960), (0, 0), "mod_assets/amana/0a.png", (0, 0), "mod_assets/amana/t.png")
image amana 1u = im.Composite((960, 960), (0, 0), "mod_assets/amana/0a.png", (0, 0), "mod_assets/amana/u.png")
image amana 1v = im.Composite((960, 960), (0, 0), "mod_assets/amana/0a.png", (0, 0), "mod_assets/amana/v.png")
image amana 1w = im.Composite((960, 960), (0, 0), "mod_assets/amana/0a.png", (0, 0), "mod_assets/amana/w.png")
image amana 1x = im.Composite((960, 960), (0, 0), "mod_assets/amana/0a.png", (0, 0), "mod_assets/amana/x.png")
image amana 1y = im.Composite((960, 960), (0, 0), "mod_assets/amana/0a.png", (0, 0), "mod_assets/amana/y.png")
image amana 1y1 = im.Composite((960, 960), (0, 0), "mod_assets/amana/0a.png", (0, 0), "mod_assets/amana/y1.png")
image amana 1y2 = im.Composite((960, 960), (0, 0), "mod_assets/amana/0a.png", (0, 0), "mod_assets/amana/y2.png")
image amana 1y3 = im.Composite((960, 960), (0, 0), "mod_assets/amana/0a.png", (0, 0), "mod_assets/amana/y3.png")
image amana 1y4 = im.Composite((960, 960), (0, 0), "mod_assets/amana/0a.png", (0, 0), "mod_assets/amana/y4.png")
image amana 1y5 = im.Composite((960, 960), (0, 0), "mod_assets/amana/0a.png", (0, 0), "mod_assets/amana/y5.png")
image amana 1y6 = im.Composite((960, 960), (0, 0), "mod_assets/amana/0a.png", (0, 0), "mod_assets/amana/y6.png")
image amana 1y7 = im.Composite((960, 960), (0, 0), "mod_assets/amana/0a.png", (0, 0), "mod_assets/amana/y7.png")
image amana 1z1 = im.Composite((960, 960), (0, 0), "mod_assets/amana/0a.png", (0, 0), "mod_assets/amana/za.png")
image amana 1z2 = im.Composite((960, 960), (0, 0), "mod_assets/amana/0a.png", (0, 0), "mod_assets/amana/zb.png")
image amana 1z3 = im.Composite((960, 960), (0, 0), "mod_assets/amana/0a.png", (0, 0), "mod_assets/amana/zc.png")
image amana 1z4 = im.Composite((960, 960), (0, 0), "mod_assets/amana/0a.png", (0, 0), "mod_assets/amana/zd.png")

image amana 2a = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/a.png")
image amana 2a2 = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/a2.png")
image amana 2b = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/b.png")
image amana 2b2 = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/b2.png")
image amana 2c = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/c.png")
image amana 2c2 = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/c2.png")
image amana 2d = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/d.png")
image amana 2d2 = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/d2.png")
image amana 2e = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/e.png")
image amana 2e2 = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/e2.png")
image amana 2f = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/f.png")
image amana 2g = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/g.png")
image amana 2h = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/h.png")
image amana 2h2 = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/hisui.png")
image amana 2i = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/i.png")
image amana 2j = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/j.png")
image amana 2k = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/k.png")
image amana 2l = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/l.png")
image amana 2m = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/m.png")
image amana 2n = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/n.png")
image amana 2o = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/o.png")
image amana 2p = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/p.png")
image amana 2q = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/q.png")
image amana 2r = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/r.png")
image amana 2s = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/s.png")
image amana 2t = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/t.png")
image amana 2u = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/u.png")
image amana 2v = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/v.png")
image amana 2w = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/w.png")
image amana 2x = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/x.png")
image amana 2y = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/y.png")
image amana 2y1 = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/y1.png")
image amana 2y2 = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/y2.png")
image amana 2y3 = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/y3.png")
image amana 2y4 = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/y4.png")
image amana 2y5 = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/y5.png")
image amana 2y6 = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/y6.png")
image amana 2y7 = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/y7.png")
image amana 2z1 = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/za.png")
image amana 2z2 = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/zb.png")
image amana 2z3 = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/zc.png")
image amana 2z4 = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/zd.png")

image amana 3a = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/a.png")
image amana 3a2 = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/a2.png")
image amana 3b = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/b.png")
image amana 3b2 = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/b2.png")
image amana 3c = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/c.png")
image amana 3c2 = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/c2.png")
image amana 3d = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/d.png")
image amana 3d2 = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/d2.png")
image amana 3e = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/e.png")
image amana 3e2 = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/e2.png")
image amana 3f = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/f.png")
image amana 3g = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/g.png")
image amana 3h = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/h.png")
image amana 3h2 = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/hisui.png")
image amana 3i = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/i.png")
image amana 3j = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/j.png")
image amana 3k = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/k.png")
image amana 3l = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/l.png")
image amana 3m = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/m.png")
image amana 3n = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/n.png")
image amana 3o = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/o.png")
image amana 3p = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/p.png")
image amana 3q = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/q.png")
image amana 3r = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/r.png")
image amana 3s = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/s.png")
image amana 3t = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/t.png")
image amana 3u = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/u.png")
image amana 3v = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/v.png")
image amana 3w = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/w.png")
image amana 3x = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/x.png")
image amana 3y = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/y.png")
image amana 3y1 = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/y1.png")
image amana 3y2 = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/y2.png")
image amana 3y3 = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/y3.png")
image amana 3y4 = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/y4.png")
image amana 3y5 = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/y5.png")
image amana 3y6 = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/y6.png")
image amana 3y7 = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/y7.png")
image amana 3z1 = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/za.png")
image amana 3z2 = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/zb.png")
image amana 3z3 = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/zc.png")
image amana 3z4 = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/1r.png", (0, 0), "mod_assets/amana/zd.png")

image amana 4a = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/a.png")
image amana 4a2 = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/a2.png")
image amana 4b = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/b.png")
image amana 4b2 = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/b2.png")
image amana 4c = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/c.png")
image amana 4c2 = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/c2.png")
image amana 4d = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/d.png")
image amana 4d2 = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/d2.png")
image amana 4e = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/e.png")
image amana 4e2 = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/e2.png")
image amana 4f = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/f.png")
image amana 4g = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/g.png")
image amana 4h = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/h.png")
image amana 4h2 = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/hisui.png")
image amana 4i = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/i.png")
image amana 4j = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/j.png")
image amana 4k = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/k.png")
image amana 4l = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/l.png")
image amana 4m = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/m.png")
image amana 4n = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/n.png")
image amana 4o = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/o.png")
image amana 4p = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/p.png")
image amana 4q = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/q.png")
image amana 4r = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/r.png")
image amana 4s = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/s.png")
image amana 4t = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/t.png")
image amana 4u = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/u.png")
image amana 4v = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/v.png")
image amana 4w = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/w.png")
image amana 4x = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/x.png")
image amana 4y = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/y.png")
image amana 4y1 = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/y1.png")
image amana 4y2 = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/y2.png")
image amana 4y3 = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/y3.png")
image amana 4y4 = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/y4.png")
image amana 4y5 = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/y5.png")
image amana 4y6 = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/y6.png")
image amana 4y7 = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/y7.png")
image amana 4z1 = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/za.png")
image amana 4z2 = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/zb.png")
image amana 4z3 = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/zc.png")
image amana 4z4 = im.Composite((960, 960), (0, 0), "mod_assets/amana/1l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/zd.png")

image amana 5a = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/a.png")
image amana 5a2 = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/a2.png")
image amana 5b = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/b.png")
image amana 5b2 = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/b2.png")
image amana 5c = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/c.png")
image amana 5c2 = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/c2.png")
image amana 5d = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/d.png")
image amana 5d2 = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/d2.png")
image amana 5e = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/e.png")
image amana 5e2 = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/e2.png")
image amana 5f = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/f.png")
image amana 5g = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/g.png")
image amana 5h = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/h.png")
image amana 5h2 = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/hisui.png")
image amana 5i = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/i.png")
image amana 5j = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/j.png")
image amana 5k = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/k.png")
image amana 5l = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/l.png")
image amana 5m = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/m.png")
image amana 5n = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/n.png")
image amana 5o = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/o.png")
image amana 5p = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/p.png")
image amana 5q = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/q.png")
image amana 5r = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/r.png")
image amana 5s = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/s.png")
image amana 5t = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/t.png")
image amana 5u = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/u.png")
image amana 5v = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/v.png")
image amana 5w = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/w.png")
image amana 5x = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/x.png")
image amana 5y = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/y.png")
image amana 5y1 = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/y1.png")
image amana 5y2 = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/y2.png")
image amana 5y3 = im.Composite((960, 960), (0, 0), "mod_assets/amana/l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/y3.png")
image amana 5y4 = im.Composite((960, 960), (0, 0), "mod_assets/amana/21l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/y4.png")
image amana 5y5 = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/y5.png")
image amana 5y6 = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/y6.png")
image amana 5y7 = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/y7.png")
image amana 5z1 = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/za.png")
image amana 5z2 = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/zb.png")
image amana 5z3 = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/zc.png")
image amana 5z4 = im.Composite((960, 960), (0, 0), "mod_assets/amana/2l.png", (0, 0), "mod_assets/amana/2r.png", (0, 0), "mod_assets/amana/zd.png")

image amana 6a = im.Composite((960, 960), (0, 0), "mod_assets/amana/3.png", (0, 0), "mod_assets/amana/a.png")
image amana 6a2 = im.Composite((960, 960), (0, 0), "mod_assets/amana/3.png", (0, 0), "mod_assets/amana/a2.png")
image amana 6b = im.Composite((960, 960), (0, 0), "mod_assets/amana/3.png", (0, 0), "mod_assets/amana/b.png")
image amana 6b2 = im.Composite((960, 960), (0, 0), "mod_assets/amana/3.png", (0, 0), "mod_assets/amana/b2.png")
image amana 6c = im.Composite((960, 960), (0, 0), "mod_assets/amana/3.png", (0, 0), "mod_assets/amana/c.png")
image amana 6c2 = im.Composite((960, 960), (0, 0), "mod_assets/amana/3.png", (0, 0), "mod_assets/amana/c2.png")
image amana 6d = im.Composite((960, 960), (0, 0), "mod_assets/amana/3.png", (0, 0), "mod_assets/amana/d.png")
image amana 6d2 = im.Composite((960, 960), (0, 0), "mod_assets/amana/3.png", (0, 0), "mod_assets/amana/d2.png")
image amana 6e = im.Composite((960, 960), (0, 0), "mod_assets/amana/3.png", (0, 0), "mod_assets/amana/e.png")
image amana 6e2 = im.Composite((960, 960), (0, 0), "mod_assets/amana/3.png", (0, 0), "mod_assets/amana/e2.png")
image amana 6f = im.Composite((960, 960), (0, 0), "mod_assets/amana/3.png", (0, 0), "mod_assets/amana/f.png")
image amana 6g = im.Composite((960, 960), (0, 0), "mod_assets/amana/3.png", (0, 0), "mod_assets/amana/g.png")
image amana 6h = im.Composite((960, 960), (0, 0), "mod_assets/amana/3.png", (0, 0), "mod_assets/amana/h.png")
image amana 6h2 = im.Composite((960, 960), (0, 0), "mod_assets/amana/3.png", (0, 0), "mod_assets/amana/hisui.png")
image amana 6i = im.Composite((960, 960), (0, 0), "mod_assets/amana/3.png", (0, 0), "mod_assets/amana/i.png")
image amana 6j = im.Composite((960, 960), (0, 0), "mod_assets/amana/3.png", (0, 0), "mod_assets/amana/j.png")
image amana 6k = im.Composite((960, 960), (0, 0), "mod_assets/amana/3.png", (0, 0), "mod_assets/amana/k.png")
image amana 6l = im.Composite((960, 960), (0, 0), "mod_assets/amana/3.png", (0, 0), "mod_assets/amana/l.png")
image amana 6m = im.Composite((960, 960), (0, 0), "mod_assets/amana/3.png", (0, 0), "mod_assets/amana/m.png")
image amana 6n = im.Composite((960, 960), (0, 0), "mod_assets/amana/3.png", (0, 0), "mod_assets/amana/n.png")
image amana 6o = im.Composite((960, 960), (0, 0), "mod_assets/amana/3.png", (0, 0), "mod_assets/amana/o.png")
image amana 6p = im.Composite((960, 960), (0, 0), "mod_assets/amana/3.png", (0, 0), "mod_assets/amana/p.png")
image amana 6q = im.Composite((960, 960), (0, 0), "mod_assets/amana/3.png", (0, 0), "mod_assets/amana/q.png")
image amana 6r = im.Composite((960, 960), (0, 0), "mod_assets/amana/3.png", (0, 0), "mod_assets/amana/r.png")
image amana 6s = im.Composite((960, 960), (0, 0), "mod_assets/amana/3.png", (0, 0), "mod_assets/amana/s.png")
image amana 6t = im.Composite((960, 960), (0, 0), "mod_assets/amana/3.png", (0, 0), "mod_assets/amana/t.png")
image amana 6u = im.Composite((960, 960), (0, 0), "mod_assets/amana/3.png", (0, 0), "mod_assets/amana/u.png")
image amana 6v = im.Composite((960, 960), (0, 0), "mod_assets/amana/3.png", (0, 0), "mod_assets/amana/v.png")
image amana 6w = im.Composite((960, 960), (0, 0), "mod_assets/amana/3.png", (0, 0), "mod_assets/amana/w.png")
image amana 6x = im.Composite((960, 960), (0, 0), "mod_assets/amana/3.png", (0, 0), "mod_assets/amana/x.png")
image amana 6y = im.Composite((960, 960), (0, 0), "mod_assets/amana/3.png", (0, 0), "mod_assets/amana/y.png")
image amana 6y1 = im.Composite((960, 960), (0, 0), "mod_assets/amana/3.png", (0, 0), "mod_assets/amana/y1.png")
image amana 6y2 = im.Composite((960, 960), (0, 0), "mod_assets/amana/3.png", (0, 0), "mod_assets/amana/y2.png")
image amana 6y3 = im.Composite((960, 960), (0, 0), "mod_assets/amana/3.png", (0, 0), "mod_assets/amana/y3.png")
image amana 6y4 = im.Composite((960, 960), (0, 0), "mod_assets/amana/3.png", (0, 0), "mod_assets/amana/y4.png")
image amana 6y5 = im.Composite((960, 960), (0, 0), "mod_assets/amana/3.png", (0, 0), "mod_assets/amana/y5.png")
image amana 6y6 = im.Composite((960, 960), (0, 0), "mod_assets/amana/3.png", (0, 0), "mod_assets/amana/y6.png")
image amana 6y7 = im.Composite((960, 960), (0, 0), "mod_assets/amana/3.png", (0, 0), "mod_assets/amana/y7.png")
image amana 6z1 = im.Composite((960, 960), (0, 0), "mod_assets/amana/3.png", (0, 0), "mod_assets/amana/za.png")
image amana 6z2 = im.Composite((960, 960), (0, 0), "mod_assets/amana/3.png", (0, 0), "mod_assets/amana/zb.png")
image amana 6z3 = im.Composite((960, 960), (0, 0), "mod_assets/amana/3.png", (0, 0), "mod_assets/amana/zc.png")
image amana 6z4 = im.Composite((960, 960), (0, 0), "mod_assets/amana/3.png", (0, 0), "mod_assets/amana/zd.png")

image cleb 1a = im.Composite((840, 840), (0, 0), "mod_assets/cleb/1l.png", (0, 0), "mod_assets/cleb/1r.png", (0, 0), "mod_assets/cleb/a.png")
image cleb 1b = im.Composite((840, 840), (0, 0), "mod_assets/cleb/1l.png", (0, 0), "mod_assets/cleb/1r.png", (0, 0), "mod_assets/cleb/b.png")
image cleb 1c = im.Composite((840, 840), (0, 0), "mod_assets/cleb/1l.png", (0, 0), "mod_assets/cleb/1r.png", (0, 0), "mod_assets/cleb/c.png")
image cleb 1d = im.Composite((840, 840), (0, 0), "mod_assets/cleb/1l.png", (0, 0), "mod_assets/cleb/1r.png", (0, 0), "mod_assets/cleb/d.png")
image cleb 1e = im.Composite((840, 840), (0, 0), "mod_assets/cleb/1l.png", (0, 0), "mod_assets/cleb/1r.png", (0, 0), "mod_assets/cleb/e.png")
image cleb 1f = im.Composite((840, 840), (0, 0), "mod_assets/cleb/1l.png", (0, 0), "mod_assets/cleb/1r.png", (0, 0), "mod_assets/cleb/f.png")
image cleb 1g = im.Composite((840, 840), (0, 0), "mod_assets/cleb/1l.png", (0, 0), "mod_assets/cleb/1r.png", (0, 0), "mod_assets/cleb/g.png")
image cleb 1h = im.Composite((840, 840), (0, 0), "mod_assets/cleb/1l.png", (0, 0), "mod_assets/cleb/1r.png", (0, 0), "mod_assets/cleb/h.png")
image cleb 1i = im.Composite((840, 840), (0, 0), "mod_assets/cleb/1l.png", (0, 0), "mod_assets/cleb/1r.png", (0, 0), "mod_assets/cleb/i.png")
image cleb 1j = im.Composite((840, 840), (0, 0), "mod_assets/cleb/1l.png", (0, 0), "mod_assets/cleb/1r.png", (0, 0), "mod_assets/cleb/j.png")
image cleb 1k = im.Composite((840, 840), (0, 0), "mod_assets/cleb/1l.png", (0, 0), "mod_assets/cleb/1r.png", (0, 0), "mod_assets/cleb/k.png")
image cleb 1l = im.Composite((840, 840), (0, 0), "mod_assets/cleb/1l.png", (0, 0), "mod_assets/cleb/1r.png", (0, 0), "mod_assets/cleb/l.png")
image cleb 1m = im.Composite((840, 840), (0, 0), "mod_assets/cleb/1l.png", (0, 0), "mod_assets/cleb/1r.png", (0, 0), "mod_assets/cleb/m.png")
image cleb 1n = im.Composite((840, 840), (0, 0), "mod_assets/cleb/1l.png", (0, 0), "mod_assets/cleb/1r.png", (0, 0), "mod_assets/cleb/n.png")
image cleb 1o = im.Composite((840, 840), (0, 0), "mod_assets/cleb/1l.png", (0, 0), "mod_assets/cleb/1r.png", (0, 0), "mod_assets/cleb/o.png")
image cleb 1p = im.Composite((840, 840), (0, 0), "mod_assets/cleb/1l.png", (0, 0), "mod_assets/cleb/1r.png", (0, 0), "mod_assets/cleb/p.png")
image cleb 1q = im.Composite((840, 840), (0, 0), "mod_assets/cleb/1l.png", (0, 0), "mod_assets/cleb/1r.png", (0, 0), "mod_assets/cleb/q.png")
image cleb 1r = im.Composite((840, 840), (0, 0), "mod_assets/cleb/1l.png", (0, 0), "mod_assets/cleb/1r.png", (0, 0), "mod_assets/cleb/r.png")
image cleb 1s = im.Composite((840, 840), (0, 0), "mod_assets/cleb/1l.png", (0, 0), "mod_assets/cleb/1r.png", (0, 0), "mod_assets/cleb/s.png")
image cleb 1t = im.Composite((840, 840), (0, 0), "mod_assets/cleb/1l.png", (0, 0), "mod_assets/cleb/1r.png", (0, 0), "mod_assets/cleb/t.png")
image cleb 1u = im.Composite((840, 840), (0, 0), "mod_assets/cleb/1l.png", (0, 0), "mod_assets/cleb/1r.png", (0, 0), "mod_assets/cleb/u.png")
image cleb 1v = im.Composite((840, 840), (0, 0), "mod_assets/cleb/1l.png", (0, 0), "mod_assets/cleb/1r.png", (0, 0), "mod_assets/cleb/v.png")
image cleb 1w = im.Composite((840, 840), (0, 0), "mod_assets/cleb/1l.png", (0, 0), "mod_assets/cleb/1r.png", (0, 0), "mod_assets/cleb/w.png")
image cleb 1x = im.Composite((840, 840), (0, 0), "mod_assets/cleb/1l.png", (0, 0), "mod_assets/cleb/1r.png", (0, 0), "mod_assets/cleb/x.png")
image cleb 1y = im.Composite((840, 840), (0, 0), "mod_assets/cleb/1l.png", (0, 0), "mod_assets/cleb/1r.png", (0, 0), "mod_assets/cleb/y.png")
image cleb 1z = im.Composite((840, 840), (0, 0), "mod_assets/cleb/1l.png", (0, 0), "mod_assets/cleb/1r.png", (0, 0), "mod_assets/cleb/z.png")



image cleb 2a = im.Composite((840, 840), (0, 0), "mod_assets/cleb/2l.png", (0, 0), "mod_assets/cleb/1r.png", (0, 0), "mod_assets/cleb/a.png")
image cleb 2b = im.Composite((840, 840), (0, 0), "mod_assets/cleb/2l.png", (0, 0), "mod_assets/cleb/1r.png", (0, 0), "mod_assets/cleb/b.png")
image cleb 2c = im.Composite((840, 840), (0, 0), "mod_assets/cleb/2l.png", (0, 0), "mod_assets/cleb/1r.png", (0, 0), "mod_assets/cleb/c.png")
image cleb 2d = im.Composite((840, 840), (0, 0), "mod_assets/cleb/2l.png", (0, 0), "mod_assets/cleb/1r.png", (0, 0), "mod_assets/cleb/d.png")
image cleb 2e = im.Composite((840, 840), (0, 0), "mod_assets/cleb/2l.png", (0, 0), "mod_assets/cleb/1r.png", (0, 0), "mod_assets/cleb/e.png")
image cleb 2f = im.Composite((840, 840), (0, 0), "mod_assets/cleb/2l.png", (0, 0), "mod_assets/cleb/1r.png", (0, 0), "mod_assets/cleb/f.png")
image cleb 2g = im.Composite((840, 840), (0, 0), "mod_assets/cleb/2l.png", (0, 0), "mod_assets/cleb/1r.png", (0, 0), "mod_assets/cleb/g.png")
image cleb 2h = im.Composite((840, 840), (0, 0), "mod_assets/cleb/2l.png", (0, 0), "mod_assets/cleb/1r.png", (0, 0), "mod_assets/cleb/h.png")
image cleb 2i = im.Composite((840, 840), (0, 0), "mod_assets/cleb/2l.png", (0, 0), "mod_assets/cleb/1r.png", (0, 0), "mod_assets/cleb/i.png")
image cleb 2j = im.Composite((840, 840), (0, 0), "mod_assets/cleb/2l.png", (0, 0), "mod_assets/cleb/1r.png", (0, 0), "mod_assets/cleb/j.png")
image cleb 2k = im.Composite((840, 840), (0, 0), "mod_assets/cleb/2l.png", (0, 0), "mod_assets/cleb/1r.png", (0, 0), "mod_assets/cleb/k.png")
image cleb 2l = im.Composite((840, 840), (0, 0), "mod_assets/cleb/2l.png", (0, 0), "mod_assets/cleb/1r.png", (0, 0), "mod_assets/cleb/l.png")
image cleb 2m = im.Composite((840, 840), (0, 0), "mod_assets/cleb/2l.png", (0, 0), "mod_assets/cleb/1r.png", (0, 0), "mod_assets/cleb/m.png")
image cleb 2n = im.Composite((840, 840), (0, 0), "mod_assets/cleb/2l.png", (0, 0), "mod_assets/cleb/1r.png", (0, 0), "mod_assets/cleb/n.png")
image cleb 2o = im.Composite((840, 840), (0, 0), "mod_assets/cleb/2l.png", (0, 0), "mod_assets/cleb/1r.png", (0, 0), "mod_assets/cleb/o.png")
image cleb 2p = im.Composite((840, 840), (0, 0), "mod_assets/cleb/2l.png", (0, 0), "mod_assets/cleb/1r.png", (0, 0), "mod_assets/cleb/p.png")
image cleb 2q = im.Composite((840, 840), (0, 0), "mod_assets/cleb/2l.png", (0, 0), "mod_assets/cleb/1r.png", (0, 0), "mod_assets/cleb/q.png")
image cleb 2r = im.Composite((840, 840), (0, 0), "mod_assets/cleb/2l.png", (0, 0), "mod_assets/cleb/1r.png", (0, 0), "mod_assets/cleb/r.png")
image cleb 2s = im.Composite((840, 840), (0, 0), "mod_assets/cleb/2l.png", (0, 0), "mod_assets/cleb/1r.png", (0, 0), "mod_assets/cleb/s.png")
image cleb 2t = im.Composite((840, 840), (0, 0), "mod_assets/cleb/2l.png", (0, 0), "mod_assets/cleb/1r.png", (0, 0), "mod_assets/cleb/t.png")
image cleb 2u = im.Composite((840, 840), (0, 0), "mod_assets/cleb/2l.png", (0, 0), "mod_assets/cleb/1r.png", (0, 0), "mod_assets/cleb/u.png")
image cleb 2v = im.Composite((840, 840), (0, 0), "mod_assets/cleb/2l.png", (0, 0), "mod_assets/cleb/1r.png", (0, 0), "mod_assets/cleb/v.png")
image cleb 2w = im.Composite((840, 840), (0, 0), "mod_assets/cleb/2l.png", (0, 0), "mod_assets/cleb/1r.png", (0, 0), "mod_assets/cleb/w.png")
image cleb 2x = im.Composite((840, 840), (0, 0), "mod_assets/cleb/2l.png", (0, 0), "mod_assets/cleb/1r.png", (0, 0), "mod_assets/cleb/x.png")
image cleb 2y = im.Composite((840, 840), (0, 0), "mod_assets/cleb/2l.png", (0, 0), "mod_assets/cleb/1r.png", (0, 0), "mod_assets/cleb/y.png")
image cleb 2z = im.Composite((840, 840), (0, 0), "mod_assets/cleb/2l.png", (0, 0), "mod_assets/cleb/1r.png", (0, 0), "mod_assets/cleb/z.png")



image cleb 3a = im.Composite((840, 840), (0, 0), "mod_assets/cleb/1l.png", (0, 0), "mod_assets/cleb/2r.png", (0, 0), "mod_assets/cleb/a.png")
image cleb 3b = im.Composite((840, 840), (0, 0), "mod_assets/cleb/1l.png", (0, 0), "mod_assets/cleb/2r.png", (0, 0), "mod_assets/cleb/b.png")
image cleb 3c = im.Composite((840, 840), (0, 0), "mod_assets/cleb/1l.png", (0, 0), "mod_assets/cleb/2r.png", (0, 0), "mod_assets/cleb/c.png")
image cleb 3d = im.Composite((840, 840), (0, 0), "mod_assets/cleb/1l.png", (0, 0), "mod_assets/cleb/2r.png", (0, 0), "mod_assets/cleb/d.png")
image cleb 3e = im.Composite((840, 840), (0, 0), "mod_assets/cleb/1l.png", (0, 0), "mod_assets/cleb/2r.png", (0, 0), "mod_assets/cleb/e.png")
image cleb 3f = im.Composite((840, 840), (0, 0), "mod_assets/cleb/1l.png", (0, 0), "mod_assets/cleb/2r.png", (0, 0), "mod_assets/cleb/f.png")
image cleb 3g = im.Composite((840, 840), (0, 0), "mod_assets/cleb/1l.png", (0, 0), "mod_assets/cleb/2r.png", (0, 0), "mod_assets/cleb/g.png")
image cleb 3h = im.Composite((840, 840), (0, 0), "mod_assets/cleb/1l.png", (0, 0), "mod_assets/cleb/2r.png", (0, 0), "mod_assets/cleb/h.png")
image cleb 3i = im.Composite((840, 840), (0, 0), "mod_assets/cleb/1l.png", (0, 0), "mod_assets/cleb/2r.png", (0, 0), "mod_assets/cleb/i.png")
image cleb 3j = im.Composite((840, 840), (0, 0), "mod_assets/cleb/1l.png", (0, 0), "mod_assets/cleb/2r.png", (0, 0), "mod_assets/cleb/j.png")
image cleb 3k = im.Composite((840, 840), (0, 0), "mod_assets/cleb/1l.png", (0, 0), "mod_assets/cleb/2r.png", (0, 0), "mod_assets/cleb/k.png")
image cleb 3l = im.Composite((840, 840), (0, 0), "mod_assets/cleb/1l.png", (0, 0), "mod_assets/cleb/2r.png", (0, 0), "mod_assets/cleb/l.png")
image cleb 3m = im.Composite((840, 840), (0, 0), "mod_assets/cleb/1l.png", (0, 0), "mod_assets/cleb/2r.png", (0, 0), "mod_assets/cleb/m.png")
image cleb 3n = im.Composite((840, 840), (0, 0), "mod_assets/cleb/1l.png", (0, 0), "mod_assets/cleb/2r.png", (0, 0), "mod_assets/cleb/n.png")
image cleb 3o = im.Composite((840, 840), (0, 0), "mod_assets/cleb/1l.png", (0, 0), "mod_assets/cleb/2r.png", (0, 0), "mod_assets/cleb/o.png")
image cleb 3p = im.Composite((840, 840), (0, 0), "mod_assets/cleb/1l.png", (0, 0), "mod_assets/cleb/2r.png", (0, 0), "mod_assets/cleb/p.png")
image cleb 3q = im.Composite((840, 840), (0, 0), "mod_assets/cleb/1l.png", (0, 0), "mod_assets/cleb/2r.png", (0, 0), "mod_assets/cleb/q.png")
image cleb 3r = im.Composite((840, 840), (0, 0), "mod_assets/cleb/1l.png", (0, 0), "mod_assets/cleb/2r.png", (0, 0), "mod_assets/cleb/r.png")
image cleb 3s = im.Composite((840, 840), (0, 0), "mod_assets/cleb/1l.png", (0, 0), "mod_assets/cleb/2r.png", (0, 0), "mod_assets/cleb/s.png")
image cleb 3t = im.Composite((840, 840), (0, 0), "mod_assets/cleb/1l.png", (0, 0), "mod_assets/cleb/2r.png", (0, 0), "mod_assets/cleb/t.png")
image cleb 3u = im.Composite((840, 840), (0, 0), "mod_assets/cleb/1l.png", (0, 0), "mod_assets/cleb/2r.png", (0, 0), "mod_assets/cleb/u.png")
image cleb 3v = im.Composite((840, 840), (0, 0), "mod_assets/cleb/1l.png", (0, 0), "mod_assets/cleb/2r.png", (0, 0), "mod_assets/cleb/v.png")
image cleb 3w = im.Composite((840, 840), (0, 0), "mod_assets/cleb/1l.png", (0, 0), "mod_assets/cleb/2r.png", (0, 0), "mod_assets/cleb/w.png")
image cleb 3x = im.Composite((840, 840), (0, 0), "mod_assets/cleb/1l.png", (0, 0), "mod_assets/cleb/2r.png", (0, 0), "mod_assets/cleb/x.png")
image cleb 3y = im.Composite((840, 840), (0, 0), "mod_assets/cleb/1l.png", (0, 0), "mod_assets/cleb/2r.png", (0, 0), "mod_assets/cleb/y.png")
image cleb 3z = im.Composite((840, 840), (0, 0), "mod_assets/cleb/1l.png", (0, 0), "mod_assets/cleb/2r.png", (0, 0), "mod_assets/cleb/z.png")



image cleb 4a = im.Composite((840, 840), (0, 0), "mod_assets/cleb/2l.png", (0, 0), "mod_assets/cleb/2r.png", (0, 0), "mod_assets/cleb/a.png")
image cleb 4b = im.Composite((840, 840), (0, 0), "mod_assets/cleb/2l.png", (0, 0), "mod_assets/cleb/2r.png", (0, 0), "mod_assets/cleb/b.png")
image cleb 4c = im.Composite((840, 840), (0, 0), "mod_assets/cleb/2l.png", (0, 0), "mod_assets/cleb/2r.png", (0, 0), "mod_assets/cleb/c.png")
image cleb 4d = im.Composite((840, 840), (0, 0), "mod_assets/cleb/2l.png", (0, 0), "mod_assets/cleb/2r.png", (0, 0), "mod_assets/cleb/d.png")
image cleb 4e = im.Composite((840, 840), (0, 0), "mod_assets/cleb/2l.png", (0, 0), "mod_assets/cleb/2r.png", (0, 0), "mod_assets/cleb/e.png")
image cleb 4f = im.Composite((840, 840), (0, 0), "mod_assets/cleb/2l.png", (0, 0), "mod_assets/cleb/2r.png", (0, 0), "mod_assets/cleb/f.png")
image cleb 4g = im.Composite((840, 840), (0, 0), "mod_assets/cleb/2l.png", (0, 0), "mod_assets/cleb/2r.png", (0, 0), "mod_assets/cleb/g.png")
image cleb 4h = im.Composite((840, 840), (0, 0), "mod_assets/cleb/2l.png", (0, 0), "mod_assets/cleb/2r.png", (0, 0), "mod_assets/cleb/h.png")
image cleb 4i = im.Composite((840, 840), (0, 0), "mod_assets/cleb/2l.png", (0, 0), "mod_assets/cleb/2r.png", (0, 0), "mod_assets/cleb/i.png")
image cleb 4j = im.Composite((840, 840), (0, 0), "mod_assets/cleb/2l.png", (0, 0), "mod_assets/cleb/2r.png", (0, 0), "mod_assets/cleb/j.png")
image cleb 4k = im.Composite((840, 840), (0, 0), "mod_assets/cleb/2l.png", (0, 0), "mod_assets/cleb/2r.png", (0, 0), "mod_assets/cleb/k.png")
image cleb 4l = im.Composite((840, 840), (0, 0), "mod_assets/cleb/2l.png", (0, 0), "mod_assets/cleb/2r.png", (0, 0), "mod_assets/cleb/l.png")
image cleb 4m = im.Composite((840, 840), (0, 0), "mod_assets/cleb/2l.png", (0, 0), "mod_assets/cleb/2r.png", (0, 0), "mod_assets/cleb/m.png")
image cleb 4n = im.Composite((840, 840), (0, 0), "mod_assets/cleb/2l.png", (0, 0), "mod_assets/cleb/2r.png", (0, 0), "mod_assets/cleb/n.png")
image cleb 4o = im.Composite((840, 840), (0, 0), "mod_assets/cleb/2l.png", (0, 0), "mod_assets/cleb/2r.png", (0, 0), "mod_assets/cleb/o.png")
image cleb 4p = im.Composite((840, 840), (0, 0), "mod_assets/cleb/2l.png", (0, 0), "mod_assets/cleb/2r.png", (0, 0), "mod_assets/cleb/p.png")
image cleb 4q = im.Composite((840, 840), (0, 0), "mod_assets/cleb/2l.png", (0, 0), "mod_assets/cleb/2r.png", (0, 0), "mod_assets/cleb/q.png")
image cleb 4r = im.Composite((840, 840), (0, 0), "mod_assets/cleb/2l.png", (0, 0), "mod_assets/cleb/2r.png", (0, 0), "mod_assets/cleb/r.png")
image cleb 4s = im.Composite((840, 840), (0, 0), "mod_assets/cleb/2l.png", (0, 0), "mod_assets/cleb/2r.png", (0, 0), "mod_assets/cleb/s.png")
image cleb 4t = im.Composite((840, 840), (0, 0), "mod_assets/cleb/2l.png", (0, 0), "mod_assets/cleb/2r.png", (0, 0), "mod_assets/cleb/t.png")
image cleb 4u = im.Composite((840, 840), (0, 0), "mod_assets/cleb/2l.png", (0, 0), "mod_assets/cleb/2r.png", (0, 0), "mod_assets/cleb/u.png")
image cleb 4v = im.Composite((840, 840), (0, 0), "mod_assets/cleb/2l.png", (0, 0), "mod_assets/cleb/2r.png", (0, 0), "mod_assets/cleb/v.png")
image cleb 4w = im.Composite((840, 840), (0, 0), "mod_assets/cleb/2l.png", (0, 0), "mod_assets/cleb/2r.png", (0, 0), "mod_assets/cleb/w.png")
image cleb 4x = im.Composite((840, 840), (0, 0), "mod_assets/cleb/2l.png", (0, 0), "mod_assets/cleb/2r.png", (0, 0), "mod_assets/cleb/x.png")
image cleb 4y = im.Composite((840, 840), (0, 0), "mod_assets/cleb/2l.png", (0, 0), "mod_assets/cleb/2r.png", (0, 0), "mod_assets/cleb/y.png")
image cleb 4z = im.Composite((840, 840), (0, 0), "mod_assets/cleb/2l.png", (0, 0), "mod_assets/cleb/2r.png", (0, 0), "mod_assets/cleb/z.png")



image cleb 5a = im.Composite((840, 840), (0, 0), "mod_assets/cleb/1l.png", (0, 0), "mod_assets/cleb/1r.png", (0, 0), "mod_assets/cleb/2ta.png")
image cleb 5b = im.Composite((840, 840), (0, 0), "mod_assets/cleb/1l.png", (0, 0), "mod_assets/cleb/1r.png", (0, 0), "mod_assets/cleb/2tb.png")
image cleb 5c = im.Composite((840, 840), (0, 0), "mod_assets/cleb/1l.png", (0, 0), "mod_assets/cleb/1r.png", (0, 0), "mod_assets/cleb/2tc.png")
image cleb 5d = im.Composite((840, 840), (0, 0), "mod_assets/cleb/1l.png", (0, 0), "mod_assets/cleb/1r.png", (0, 0), "mod_assets/cleb/2td.png")
image cleb 5e = im.Composite((840, 840), (0, 0), "mod_assets/cleb/1l.png", (0, 0), "mod_assets/cleb/1r.png", (0, 0), "mod_assets/cleb/2te.png")
image cleb 5f = im.Composite((840, 840), (0, 0), "mod_assets/cleb/1l.png", (0, 0), "mod_assets/cleb/1r.png", (0, 0), "mod_assets/cleb/2tf.png")
image cleb 5g = im.Composite((840, 840), (0, 0), "mod_assets/cleb/1l.png", (0, 0), "mod_assets/cleb/1r.png", (0, 0), "mod_assets/cleb/2tg.png")
image cleb 5h = im.Composite((840, 840), (0, 0), "mod_assets/cleb/1l.png", (0, 0), "mod_assets/cleb/1r.png", (0, 0), "mod_assets/cleb/2th.png")
image cleb 5i = im.Composite((840, 840), (0, 0), "mod_assets/cleb/1l.png", (0, 0), "mod_assets/cleb/1r.png", (0, 0), "mod_assets/cleb/2ti.png")



image cleb 6a = im.Composite((840, 840), (0, 0), "mod_assets/cleb/2l.png", (0, 0), "mod_assets/cleb/1r.png", (0, 0), "mod_assets/cleb/2ta.png")
image cleb 6b = im.Composite((840, 840), (0, 0), "mod_assets/cleb/2l.png", (0, 0), "mod_assets/cleb/1r.png", (0, 0), "mod_assets/cleb/2tb.png")
image cleb 6c = im.Composite((840, 840), (0, 0), "mod_assets/cleb/2l.png", (0, 0), "mod_assets/cleb/1r.png", (0, 0), "mod_assets/cleb/2tc.png")
image cleb 6d = im.Composite((840, 840), (0, 0), "mod_assets/cleb/2l.png", (0, 0), "mod_assets/cleb/1r.png", (0, 0), "mod_assets/cleb/2td.png")
image cleb 6e = im.Composite((840, 840), (0, 0), "mod_assets/cleb/2l.png", (0, 0), "mod_assets/cleb/1r.png", (0, 0), "mod_assets/cleb/2te.png")
image cleb 6f = im.Composite((840, 840), (0, 0), "mod_assets/cleb/2l.png", (0, 0), "mod_assets/cleb/1r.png", (0, 0), "mod_assets/cleb/2tf.png")
image cleb 6g = im.Composite((840, 840), (0, 0), "mod_assets/cleb/2l.png", (0, 0), "mod_assets/cleb/1r.png", (0, 0), "mod_assets/cleb/2tg.png")
image cleb 6h = im.Composite((840, 840), (0, 0), "mod_assets/cleb/2l.png", (0, 0), "mod_assets/cleb/1r.png", (0, 0), "mod_assets/cleb/2th.png")
image cleb 6i = im.Composite((840, 840), (0, 0), "mod_assets/cleb/2l.png", (0, 0), "mod_assets/cleb/1r.png", (0, 0), "mod_assets/cleb/2ti.png")



image cleb 7a = im.Composite((840, 840), (0, 0), "mod_assets/cleb/1l.png", (0, 0), "mod_assets/cleb/2r.png", (0, 0), "mod_assets/cleb/2ta.png")
image cleb 7b = im.Composite((840, 840), (0, 0), "mod_assets/cleb/1l.png", (0, 0), "mod_assets/cleb/2r.png", (0, 0), "mod_assets/cleb/2tb.png")
image cleb 7c = im.Composite((840, 840), (0, 0), "mod_assets/cleb/1l.png", (0, 0), "mod_assets/cleb/2r.png", (0, 0), "mod_assets/cleb/2tc.png")
image cleb 7d = im.Composite((840, 840), (0, 0), "mod_assets/cleb/1l.png", (0, 0), "mod_assets/cleb/2r.png", (0, 0), "mod_assets/cleb/2td.png")
image cleb 7e = im.Composite((840, 840), (0, 0), "mod_assets/cleb/1l.png", (0, 0), "mod_assets/cleb/2r.png", (0, 0), "mod_assets/cleb/2te.png")
image cleb 7f = im.Composite((840, 840), (0, 0), "mod_assets/cleb/1l.png", (0, 0), "mod_assets/cleb/2r.png", (0, 0), "mod_assets/cleb/2tf.png")
image cleb 7g = im.Composite((840, 840), (0, 0), "mod_assets/cleb/1l.png", (0, 0), "mod_assets/cleb/2r.png", (0, 0), "mod_assets/cleb/2tg.png")
image cleb 7h = im.Composite((840, 840), (0, 0), "mod_assets/cleb/1l.png", (0, 0), "mod_assets/cleb/2r.png", (0, 0), "mod_assets/cleb/2th.png")
image cleb 7i = im.Composite((840, 840), (0, 0), "mod_assets/cleb/1l.png", (0, 0), "mod_assets/cleb/2r.png", (0, 0), "mod_assets/cleb/2ti.png")



image cleb 8a = im.Composite((840, 840), (0, 0), "mod_assets/cleb/2l.png", (0, 0), "mod_assets/cleb/2r.png", (0, 0), "mod_assets/cleb/2ta.png")
image cleb 8b = im.Composite((840, 840), (0, 0), "mod_assets/cleb/2l.png", (0, 0), "mod_assets/cleb/2r.png", (0, 0), "mod_assets/cleb/2tb.png")
image cleb 8c = im.Composite((840, 840), (0, 0), "mod_assets/cleb/2l.png", (0, 0), "mod_assets/cleb/2r.png", (0, 0), "mod_assets/cleb/2tc.png")
image cleb 8d = im.Composite((840, 840), (0, 0), "mod_assets/cleb/2l.png", (0, 0), "mod_assets/cleb/2r.png", (0, 0), "mod_assets/cleb/2td.png")
image cleb 8e = im.Composite((840, 840), (0, 0), "mod_assets/cleb/2l.png", (0, 0), "mod_assets/cleb/2r.png", (0, 0), "mod_assets/cleb/2te.png")
image cleb 8f = im.Composite((840, 840), (0, 0), "mod_assets/cleb/2l.png", (0, 0), "mod_assets/cleb/2r.png", (0, 0), "mod_assets/cleb/2tf.png")
image cleb 8g = im.Composite((840, 840), (0, 0), "mod_assets/cleb/2l.png", (0, 0), "mod_assets/cleb/2r.png", (0, 0), "mod_assets/cleb/2tg.png")
image cleb 8h = im.Composite((840, 840), (0, 0), "mod_assets/cleb/2l.png", (0, 0), "mod_assets/cleb/2r.png", (0, 0), "mod_assets/cleb/2th.png")
image cleb 8i = im.Composite((840, 840), (0, 0), "mod_assets/cleb/2l.png", (0, 0), "mod_assets/cleb/2r.png", (0, 0), "mod_assets/cleb/2ti.png")



image cleb 9a = im.Composite((840, 840), (0, 0), "mod_assets/cleb/3.png", (0, 0), "mod_assets/cleb/a.png")
image cleb 9b = im.Composite((840, 840), (0, 0), "mod_assets/cleb/3.png", (0, 0), "mod_assets/cleb/b.png")
image cleb 9c = im.Composite((840, 840), (0, 0), "mod_assets/cleb/3.png", (0, 0), "mod_assets/cleb/c.png")
image cleb 9d = im.Composite((840, 840), (0, 0), "mod_assets/cleb/3.png", (0, 0), "mod_assets/cleb/d.png")
image cleb 9e = im.Composite((840, 840), (0, 0), "mod_assets/cleb/3.png", (0, 0), "mod_assets/cleb/e.png")
image cleb 9f = im.Composite((840, 840), (0, 0), "mod_assets/cleb/3.png", (0, 0), "mod_assets/cleb/f.png")
image cleb 9g = im.Composite((840, 840), (0, 0), "mod_assets/cleb/3.png", (0, 0), "mod_assets/cleb/g.png")
image cleb 9h = im.Composite((840, 840), (0, 0), "mod_assets/cleb/3.png", (0, 0), "mod_assets/cleb/h.png")
image cleb 9i = im.Composite((840, 840), (0, 0), "mod_assets/cleb/3.png", (0, 0), "mod_assets/cleb/i.png")
image cleb 9j = im.Composite((840, 840), (0, 0), "mod_assets/cleb/3.png", (0, 0), "mod_assets/cleb/j.png")
image cleb 9k = im.Composite((840, 840), (0, 0), "mod_assets/cleb/3.png", (0, 0), "mod_assets/cleb/k.png")
image cleb 9l = im.Composite((840, 840), (0, 0), "mod_assets/cleb/3.png", (0, 0), "mod_assets/cleb/l.png")
image cleb 9m = im.Composite((840, 840), (0, 0), "mod_assets/cleb/3.png", (0, 0), "mod_assets/cleb/m.png")
image cleb 9n = im.Composite((840, 840), (0, 0), "mod_assets/cleb/3.png", (0, 0), "mod_assets/cleb/n.png")
image cleb 9o = im.Composite((840, 840), (0, 0), "mod_assets/cleb/3.png", (0, 0), "mod_assets/cleb/o.png")
image cleb 9p = im.Composite((840, 840), (0, 0), "mod_assets/cleb/3.png", (0, 0), "mod_assets/cleb/p.png")
image cleb 9q = im.Composite((840, 840), (0, 0), "mod_assets/cleb/3.png", (0, 0), "mod_assets/cleb/q.png")
image cleb 9r = im.Composite((840, 840), (0, 0), "mod_assets/cleb/3.png", (0, 0), "mod_assets/cleb/r.png")
image cleb 9s = im.Composite((840, 840), (0, 0), "mod_assets/cleb/3.png", (0, 0), "mod_assets/cleb/s.png")
image cleb 9t = im.Composite((840, 840), (0, 0), "mod_assets/cleb/3.png", (0, 0), "mod_assets/cleb/t.png")
image cleb 9u = im.Composite((840, 840), (0, 0), "mod_assets/cleb/3.png", (0, 0), "mod_assets/cleb/u.png")
image cleb 9v = im.Composite((840, 840), (0, 0), "mod_assets/cleb/3.png", (0, 0), "mod_assets/cleb/v.png")
image cleb 9w = im.Composite((840, 840), (0, 0), "mod_assets/cleb/3.png", (0, 0), "mod_assets/cleb/w.png")
image cleb 9x = im.Composite((840, 840), (0, 0), "mod_assets/cleb/3.png", (0, 0), "mod_assets/cleb/x.png")
image cleb 9y = im.Composite((840, 840), (0, 0), "mod_assets/cleb/3.png", (0, 0), "mod_assets/cleb/y.png")
image cleb 9z = im.Composite((840, 840), (0, 0), "mod_assets/cleb/3.png", (0, 0), "mod_assets/cleb/z.png")



image cleb 1 = im.Composite((840, 840), (0, 0), "mod_assets/cleb/3.png", (0, 0), "mod_assets/cleb/2ta.png")
image cleb 2 = im.Composite((840, 840), (0, 0), "mod_assets/cleb/3.png", (0, 0), "mod_assets/cleb/2tb.png")
image cleb 3 = im.Composite((840, 840), (0, 0), "mod_assets/cleb/3.png", (0, 0), "mod_assets/cleb/2tc.png")
image cleb 4 = im.Composite((840, 840), (0, 0), "mod_assets/cleb/3.png", (0, 0), "mod_assets/cleb/2td.png")
image cleb 5 = im.Composite((840, 840), (0, 0), "mod_assets/cleb/3.png", (0, 0), "mod_assets/cleb/2te.png")
image cleb 6 = im.Composite((840, 840), (0, 0), "mod_assets/cleb/3.png", (0, 0), "mod_assets/cleb/2tf.png")
image cleb 7 = im.Composite((840, 840), (0, 0), "mod_assets/cleb/3.png", (0, 0), "mod_assets/cleb/2tg.png")
image cleb 8 = im.Composite((840, 840), (0, 0), "mod_assets/cleb/3.png", (0, 0), "mod_assets/cleb/2th.png")
image cleb 9 = im.Composite((840, 840), (0, 0), "mod_assets/cleb/3.png", (0, 0), "mod_assets/cleb/2ti.png")
image cleb scream = im.Composite((840, 840), (0, 0), "mod_assets/cleb/1l.png", (0, 0), "mod_assets/cleb/1r.png", (0, 0), "mod_assets/cleb/scream.png")

image phoenix 1a = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/1l.png", (0, 0), "mod_assets/phoenix/1r.png", (179, 90), "mod_assets/phoenix/a.png")
image phoenix 1b = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/1l.png", (0, 0), "mod_assets/phoenix/1r.png", (179, 90), "mod_assets/phoenix/b.png")
image phoenix 1c = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/1l.png", (0, 0), "mod_assets/phoenix/1r.png", (179, 90), "mod_assets/phoenix/c.png")
image phoenix 1d = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/1l.png", (0, 0), "mod_assets/phoenix/1r.png", (179, 90), "mod_assets/phoenix/d.png")
image phoenix 1e = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/1l.png", (0, 0), "mod_assets/phoenix/1r.png", (179, 90), "mod_assets/phoenix/e.png")
image phoenix 1f = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/1l.png", (0, 0), "mod_assets/phoenix/1r.png", (179, 90), "mod_assets/phoenix/f.png")
image phoenix 1g = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/1l.png", (0, 0), "mod_assets/phoenix/1r.png", (179, 90), "mod_assets/phoenix/g.png")
image phoenix 1h = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/1l.png", (0, 0), "mod_assets/phoenix/1r.png", (179, 90), "mod_assets/phoenix/h.png")
image phoenix 1i = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/1l.png", (0, 0), "mod_assets/phoenix/1r.png", (179, 90), "mod_assets/phoenix/i.png")
image phoenix 1j = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/1l.png", (0, 0), "mod_assets/phoenix/1r.png", (179, 90), "mod_assets/phoenix/j.png")
image phoenix 1k = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/1l.png", (0, 0), "mod_assets/phoenix/1r.png", (179, 90), "mod_assets/phoenix/k.png")
image phoenix 1l = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/1l.png", (0, 0), "mod_assets/phoenix/1r.png", (179, 90), "mod_assets/phoenix/l.png")
image phoenix 1m = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/1l.png", (0, 0), "mod_assets/phoenix/1r.png", (179, 90), "mod_assets/phoenix/m.png")
image phoenix 1n = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/1l.png", (0, 0), "mod_assets/phoenix/1r.png", (179, 90), "mod_assets/phoenix/n.png")
image phoenix 1o = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/1l.png", (0, 0), "mod_assets/phoenix/1r.png", (179, 90), "mod_assets/phoenix/o.png")
image phoenix 1p = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/1l.png", (0, 0), "mod_assets/phoenix/1r.png", (179, 90), "mod_assets/phoenix/p.png")
image phoenix 1q = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/1l.png", (0, 0), "mod_assets/phoenix/1r.png", (179, 90), "mod_assets/phoenix/q.png")
image phoenix 1r = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/1l.png", (0, 0), "mod_assets/phoenix/1r.png", (179, 90), "mod_assets/phoenix/r.png")
image phoenix 1s = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/1l.png", (0, 0), "mod_assets/phoenix/1r.png", (179, 90), "mod_assets/phoenix/s.png")
image phoenix 1t = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/1l.png", (0, 0), "mod_assets/phoenix/1r.png", (179, 90), "mod_assets/phoenix/t.png")
image phoenix 1u = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/1l.png", (0, 0), "mod_assets/phoenix/1r.png", (179, 90), "mod_assets/phoenix/u.png")
image phoenix 1v = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/1l.png", (0, 0), "mod_assets/phoenix/1r.png", (179, 90), "mod_assets/phoenix/v.png")
image phoenix 1w = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/1l.png", (0, 0), "mod_assets/phoenix/1r.png", (179, 90), "mod_assets/phoenix/w.png")
image phoenix 1x = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/1l.png", (0, 0), "mod_assets/phoenix/1r.png", (179, 90), "mod_assets/phoenix/x.png")
image phoenix 1y = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/1l.png", (0, 0), "mod_assets/phoenix/1r.png", (179, 90), "mod_assets/phoenix/y.png")
image phoenix 1z = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/1l.png", (0, 0), "mod_assets/phoenix/1r.png", (179, 90), "mod_assets/phoenix/z.png")

image phoenix 2a = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/1l.png", (0, 0), "mod_assets/phoenix/2r.png", (179, 90), "mod_assets/phoenix/a.png")
image phoenix 2b = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/1l.png", (0, 0), "mod_assets/phoenix/2r.png", (179, 90), "mod_assets/phoenix/b.png")
image phoenix 2c = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/1l.png", (0, 0), "mod_assets/phoenix/2r.png", (179, 90), "mod_assets/phoenix/c.png")
image phoenix 2d = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/1l.png", (0, 0), "mod_assets/phoenix/2r.png", (179, 90), "mod_assets/phoenix/d.png")
image phoenix 2e = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/1l.png", (0, 0), "mod_assets/phoenix/2r.png", (179, 90), "mod_assets/phoenix/e.png")
image phoenix 2f = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/1l.png", (0, 0), "mod_assets/phoenix/2r.png", (179, 90), "mod_assets/phoenix/f.png")
image phoenix 2g = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/1l.png", (0, 0), "mod_assets/phoenix/2r.png", (179, 90), "mod_assets/phoenix/g.png")
image phoenix 2h = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/1l.png", (0, 0), "mod_assets/phoenix/2r.png", (179, 90), "mod_assets/phoenix/h.png")
image phoenix 2i = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/1l.png", (0, 0), "mod_assets/phoenix/2r.png", (179, 90), "mod_assets/phoenix/i.png")
image phoenix 2j = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/1l.png", (0, 0), "mod_assets/phoenix/2r.png", (179, 90), "mod_assets/phoenix/j.png")
image phoenix 2k = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/1l.png", (0, 0), "mod_assets/phoenix/2r.png", (179, 90), "mod_assets/phoenix/k.png")
image phoenix 2l = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/1l.png", (0, 0), "mod_assets/phoenix/2r.png", (179, 90), "mod_assets/phoenix/l.png")
image phoenix 2m = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/1l.png", (0, 0), "mod_assets/phoenix/2r.png", (179, 90), "mod_assets/phoenix/m.png")
image phoenix 2n = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/1l.png", (0, 0), "mod_assets/phoenix/2r.png", (179, 90), "mod_assets/phoenix/n.png")
image phoenix 2o = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/1l.png", (0, 0), "mod_assets/phoenix/2r.png", (179, 90), "mod_assets/phoenix/o.png")
image phoenix 2p = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/1l.png", (0, 0), "mod_assets/phoenix/2r.png", (179, 90), "mod_assets/phoenix/p.png")
image phoenix 2q = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/1l.png", (0, 0), "mod_assets/phoenix/2r.png", (179, 90), "mod_assets/phoenix/q.png")
image phoenix 2r = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/1l.png", (0, 0), "mod_assets/phoenix/2r.png", (179, 90), "mod_assets/phoenix/r.png")
image phoenix 2s = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/1l.png", (0, 0), "mod_assets/phoenix/2r.png", (179, 90), "mod_assets/phoenix/s.png")
image phoenix 2t = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/1l.png", (0, 0), "mod_assets/phoenix/2r.png", (179, 90), "mod_assets/phoenix/t.png")
image phoenix 2u = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/1l.png", (0, 0), "mod_assets/phoenix/2r.png", (179, 90), "mod_assets/phoenix/u.png")
image phoenix 2v = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/1l.png", (0, 0), "mod_assets/phoenix/2r.png", (179, 90), "mod_assets/phoenix/v.png")
image phoenix 2w = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/1l.png", (0, 0), "mod_assets/phoenix/2r.png", (179, 90), "mod_assets/phoenix/w.png")
image phoenix 2x = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/1l.png", (0, 0), "mod_assets/phoenix/2r.png", (179, 90), "mod_assets/phoenix/x.png")
image phoenix 2y = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/1l.png", (0, 0), "mod_assets/phoenix/2r.png", (179, 90), "mod_assets/phoenix/y.png")
image phoenix 2z = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/1l.png", (0, 0), "mod_assets/phoenix/2r.png", (179, 90), "mod_assets/phoenix/z.png")

image phoenix 3a = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/2l.png", (0, 0), "mod_assets/phoenix/1r.png", (179, 90), "mod_assets/phoenix/a.png")
image phoenix 3b = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/2l.png", (0, 0), "mod_assets/phoenix/1r.png", (179, 90), "mod_assets/phoenix/b.png")
image phoenix 3c = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/2l.png", (0, 0), "mod_assets/phoenix/1r.png", (179, 90), "mod_assets/phoenix/c.png")
image phoenix 3d = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/2l.png", (0, 0), "mod_assets/phoenix/1r.png", (179, 90), "mod_assets/phoenix/d.png")
image phoenix 3e = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/2l.png", (0, 0), "mod_assets/phoenix/1r.png", (179, 90), "mod_assets/phoenix/e.png")
image phoenix 3f = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/2l.png", (0, 0), "mod_assets/phoenix/1r.png", (179, 90), "mod_assets/phoenix/f.png")
image phoenix 3g = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/2l.png", (0, 0), "mod_assets/phoenix/1r.png", (179, 90), "mod_assets/phoenix/g.png")
image phoenix 3h = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/2l.png", (0, 0), "mod_assets/phoenix/1r.png", (179, 90), "mod_assets/phoenix/h.png")
image phoenix 3i = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/2l.png", (0, 0), "mod_assets/phoenix/1r.png", (179, 90), "mod_assets/phoenix/i.png")
image phoenix 3j = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/2l.png", (0, 0), "mod_assets/phoenix/1r.png", (179, 90), "mod_assets/phoenix/j.png")
image phoenix 3k = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/2l.png", (0, 0), "mod_assets/phoenix/1r.png", (179, 90), "mod_assets/phoenix/k.png")
image phoenix 3l = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/2l.png", (0, 0), "mod_assets/phoenix/1r.png", (179, 90), "mod_assets/phoenix/l.png")
image phoenix 3m = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/2l.png", (0, 0), "mod_assets/phoenix/1r.png", (179, 90), "mod_assets/phoenix/m.png")
image phoenix 3n = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/2l.png", (0, 0), "mod_assets/phoenix/1r.png", (179, 90), "mod_assets/phoenix/n.png")
image phoenix 3o = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/2l.png", (0, 0), "mod_assets/phoenix/1r.png", (179, 90), "mod_assets/phoenix/o.png")
image phoenix 3p = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/2l.png", (0, 0), "mod_assets/phoenix/1r.png", (179, 90), "mod_assets/phoenix/p.png")
image phoenix 3q = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/2l.png", (0, 0), "mod_assets/phoenix/1r.png", (179, 90), "mod_assets/phoenix/q.png")
image phoenix 3r = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/2l.png", (0, 0), "mod_assets/phoenix/1r.png", (179, 90), "mod_assets/phoenix/r.png")
image phoenix 3s = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/2l.png", (0, 0), "mod_assets/phoenix/1r.png", (179, 90), "mod_assets/phoenix/s.png")
image phoenix 3t = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/2l.png", (0, 0), "mod_assets/phoenix/1r.png", (179, 90), "mod_assets/phoenix/t.png")
image phoenix 3u = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/2l.png", (0, 0), "mod_assets/phoenix/1r.png", (179, 90), "mod_assets/phoenix/u.png")
image phoenix 3v = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/2l.png", (0, 0), "mod_assets/phoenix/1r.png", (179, 90), "mod_assets/phoenix/v.png")
image phoenix 3w = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/2l.png", (0, 0), "mod_assets/phoenix/1r.png", (179, 90), "mod_assets/phoenix/w.png")
image phoenix 3x = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/2l.png", (0, 0), "mod_assets/phoenix/1r.png", (179, 90), "mod_assets/phoenix/x.png")
image phoenix 3y = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/2l.png", (0, 0), "mod_assets/phoenix/1r.png", (179, 90), "mod_assets/phoenix/y.png")
image phoenix 3z = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/2l.png", (0, 0), "mod_assets/phoenix/1r.png", (179, 90), "mod_assets/phoenix/z.png")

image phoenix 4a = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/2l.png", (0, 0), "mod_assets/phoenix/2r.png", (179, 90), "mod_assets/phoenix/a.png")
image phoenix 4b = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/2l.png", (0, 0), "mod_assets/phoenix/2r.png", (179, 90), "mod_assets/phoenix/b.png")
image phoenix 4c = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/2l.png", (0, 0), "mod_assets/phoenix/2r.png", (179, 90), "mod_assets/phoenix/c.png")
image phoenix 4d = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/2l.png", (0, 0), "mod_assets/phoenix/2r.png", (179, 90), "mod_assets/phoenix/d.png")
image phoenix 4e = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/2l.png", (0, 0), "mod_assets/phoenix/2r.png", (179, 90), "mod_assets/phoenix/e.png")
image phoenix 4f = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/2l.png", (0, 0), "mod_assets/phoenix/2r.png", (179, 90), "mod_assets/phoenix/f.png")
image phoenix 4g = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/2l.png", (0, 0), "mod_assets/phoenix/2r.png", (179, 90), "mod_assets/phoenix/g.png")
image phoenix 4h = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/2l.png", (0, 0), "mod_assets/phoenix/2r.png", (179, 90), "mod_assets/phoenix/h.png")
image phoenix 4i = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/2l.png", (0, 0), "mod_assets/phoenix/2r.png", (179, 90), "mod_assets/phoenix/i.png")
image phoenix 4j = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/2l.png", (0, 0), "mod_assets/phoenix/2r.png", (179, 90), "mod_assets/phoenix/j.png")
image phoenix 4k = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/2l.png", (0, 0), "mod_assets/phoenix/2r.png", (179, 90), "mod_assets/phoenix/k.png")
image phoenix 4l = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/2l.png", (0, 0), "mod_assets/phoenix/2r.png", (179, 90), "mod_assets/phoenix/l.png")
image phoenix 4m = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/2l.png", (0, 0), "mod_assets/phoenix/2r.png", (179, 90), "mod_assets/phoenix/m.png")
image phoenix 4n = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/2l.png", (0, 0), "mod_assets/phoenix/2r.png", (179, 90), "mod_assets/phoenix/n.png")
image phoenix 4o = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/2l.png", (0, 0), "mod_assets/phoenix/2r.png", (179, 90), "mod_assets/phoenix/o.png")
image phoenix 4p = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/2l.png", (0, 0), "mod_assets/phoenix/2r.png", (179, 90), "mod_assets/phoenix/p.png")
image phoenix 4q = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/2l.png", (0, 0), "mod_assets/phoenix/2r.png", (179, 90), "mod_assets/phoenix/q.png")
image phoenix 4r = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/2l.png", (0, 0), "mod_assets/phoenix/2r.png", (179, 90), "mod_assets/phoenix/r.png")
image phoenix 4s = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/2l.png", (0, 0), "mod_assets/phoenix/2r.png", (179, 90), "mod_assets/phoenix/s.png")
image phoenix 4t = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/2l.png", (0, 0), "mod_assets/phoenix/2r.png", (179, 90), "mod_assets/phoenix/t.png")
image phoenix 4u = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/2l.png", (0, 0), "mod_assets/phoenix/2r.png", (179, 90), "mod_assets/phoenix/u.png")
image phoenix 4v = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/2l.png", (0, 0), "mod_assets/phoenix/2r.png", (179, 90), "mod_assets/phoenix/v.png")
image phoenix 4w = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/2l.png", (0, 0), "mod_assets/phoenix/2r.png", (179, 90), "mod_assets/phoenix/w.png")
image phoenix 4x = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/2l.png", (0, 0), "mod_assets/phoenix/2r.png", (179, 90), "mod_assets/phoenix/x.png")
image phoenix 4y = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/2l.png", (0, 0), "mod_assets/phoenix/2r.png", (179, 90), "mod_assets/phoenix/y.png")
image phoenix 4z = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/2l.png", (0, 0), "mod_assets/phoenix/2r.png", (179, 90), "mod_assets/phoenix/z.png")

image phoenix 5a = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/3a.png")
image phoenix 5b = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/3b.png")
image phoenix 5c = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/3c.png")
image phoenix 5d = im.Composite((960, 960), (0, 0), "mod_assets/phoenix/3d.png")

image phoenix glitch_1:
    "mod_assets/phoenix/glitch1.png"
    pause 0.01666
    "mod_assets/phoenix/glitch2.png"
    pause 0.01666
    repeat

image phoenix glitch_2:
    "mod_assets/phoenix/end-glitch1.png"
    0.15
    "mod_assets/phoenix/end-glitch2.png"
    0.15
    repeat

image phoenix glitch_3:
    "mod_assets/phoenix/noface1.png"
    0.15
    "mod_assets/phoenix/noface1b.png"
    0.15
    repeat

image mgt 1a = "mod_assets/mgt/DEVIOUSMGT.png"
image mgt 1b = "mod_assets/mgt/MGT_angry.png"
image mgt 1c = "mod_assets/mgt/MGT_bruh.png"
image mgt 1d = "mod_assets/mgt/MGT_idle.png"
image mgt 1e = "mod_assets/mgt/MGT_sus.png"
image mgt 1f = "mod_assets/mgt/MGT_what.png"
image mgt bruh = "mod_assets/mgt/bruh_momento.png"
image mgt fuck_me_if_you_can = "mod_assets/mgt/Fuck_with_me_if_you_can.png"
image mgt looking_away = "mod_assets/mgt/looking_away_from_him.png"
image mgt me_when_agni = "mod_assets/mgt/me_when_agni.png"
image mgt no_reaction = "mod_assets/mgt/no_reactions.png"
image mgt no_reaction = "mod_assets/mgt/no_reactions.png"
image mgt say_what = "mod_assets/mgt/SayWhat.png"
image mgt screw_you = "mod_assets/mgt/screw_you.png"
image mgt talking_2 = "mod_assets/mgt/talking_2.png"
image mgt talking_mad_shit = "mod_assets/mgt/talking_mad_shit.png"
image mgt whatever = "mod_assets/mgt/talking.png"
image mgt whole_squad_laughing = "mod_assets/mgt/you_made_the_whole_squad_laughing.png"

image fit 1a = im.Composite((960, 960), (0, 0), "mod_assets/fit/1l.png", (0, 0), "mod_assets/fit/1r.png", (0, 0), "mod_assets/fit/a.png")
image fit 1b = im.Composite((960, 960), (0, 0), "mod_assets/fit/1l.png", (0, 0), "mod_assets/fit/1r.png", (0, 0), "mod_assets/fit/b.png")
image fit 1c = im.Composite((960, 960), (0, 0), "mod_assets/fit/1l.png", (0, 0), "mod_assets/fit/1r.png", (0, 0), "mod_assets/fit/c.png")
image fit 1d = im.Composite((960, 960), (0, 0), "mod_assets/fit/1l.png", (0, 0), "mod_assets/fit/1r.png", (0, 0), "mod_assets/fit/d.png")
image fit 1e = im.Composite((960, 960), (0, 0), "mod_assets/fit/1l.png", (0, 0), "mod_assets/fit/1r.png", (0, 0), "mod_assets/fit/e.png")
image fit 1f = im.Composite((960, 960), (0, 0), "mod_assets/fit/1l.png", (0, 0), "mod_assets/fit/1r.png", (0, 0), "mod_assets/fit/f.png")
image fit 1g = im.Composite((960, 960), (0, 0), "mod_assets/fit/1l.png", (0, 0), "mod_assets/fit/1r.png", (0, 0), "mod_assets/fit/g.png")
image fit 1g1 = im.Composite((960, 960), (0, 0), "mod_assets/fit/1l.png", (0, 0), "mod_assets/fit/1r.png", (0, 0), "mod_assets/fit/g1.png")
image fit 1g2 = im.Composite((960, 960), (0, 0), "mod_assets/fit/1l.png", (0, 0), "mod_assets/fit/1r.png", (0, 0), "mod_assets/fit/g2.png")
image fit 1g3 = im.Composite((960, 960), (0, 0), "mod_assets/fit/1l.png", (0, 0), "mod_assets/fit/1r.png", (0, 0), "mod_assets/fit/g3.png")
image fit 1g4 = im.Composite((960, 960), (0, 0), "mod_assets/fit/1l.png", (0, 0), "mod_assets/fit/1r.png", (0, 0), "mod_assets/fit/g4.png")
image fit 1h = im.Composite((960, 960), (0, 0), "mod_assets/fit/1l.png", (0, 0), "mod_assets/fit/1r.png", (0, 0), "mod_assets/fit/h.png")
image fit 1i = im.Composite((960, 960), (0, 0), "mod_assets/fit/1l.png", (0, 0), "mod_assets/fit/1r.png", (0, 0), "mod_assets/fit/i.png")
image fit 1j = im.Composite((960, 960), (0, 0), "mod_assets/fit/1l.png", (0, 0), "mod_assets/fit/1r.png", (0, 0), "mod_assets/fit/j.png")
image fit 1k = im.Composite((960, 960), (0, 0), "mod_assets/fit/1l.png", (0, 0), "mod_assets/fit/1r.png", (0, 0), "mod_assets/fit/k.png")
image fit 1l = im.Composite((960, 960), (0, 0), "mod_assets/fit/1l.png", (0, 0), "mod_assets/fit/1r.png", (0, 0), "mod_assets/fit/l.png")
image fit 1m = im.Composite((960, 960), (0, 0), "mod_assets/fit/1l.png", (0, 0), "mod_assets/fit/1r.png", (0, 0), "mod_assets/fit/m.png")
image fit 1n = im.Composite((960, 960), (0, 0), "mod_assets/fit/1l.png", (0, 0), "mod_assets/fit/1r.png", (0, 0), "mod_assets/fit/n.png")
image fit 1o = im.Composite((960, 960), (0, 0), "mod_assets/fit/1l.png", (0, 0), "mod_assets/fit/1r.png", (0, 0), "mod_assets/fit/o.png")
image fit 1p = im.Composite((960, 960), (0, 0), "mod_assets/fit/1l.png", (0, 0), "mod_assets/fit/1r.png", (0, 0), "mod_assets/fit/p.png")
image fit 1q = im.Composite((960, 960), (0, 0), "mod_assets/fit/1l.png", (0, 0), "mod_assets/fit/1r.png", (0, 0), "mod_assets/fit/q.png")
image fit 1r = im.Composite((960, 960), (0, 0), "mod_assets/fit/1l.png", (0, 0), "mod_assets/fit/1r.png", (0, 0), "mod_assets/fit/r.png")

image fit 2a = im.Composite((960, 960), (0, 0), "mod_assets/fit/1l.png", (0, 0), "mod_assets/fit/2r.png", (0, 0), "mod_assets/fit/a.png")
image fit 2b = im.Composite((960, 960), (0, 0), "mod_assets/fit/1l.png", (0, 0), "mod_assets/fit/2r.png", (0, 0), "mod_assets/fit/b.png")
image fit 2c = im.Composite((960, 960), (0, 0), "mod_assets/fit/1l.png", (0, 0), "mod_assets/fit/2r.png", (0, 0), "mod_assets/fit/c.png")
image fit 2d = im.Composite((960, 960), (0, 0), "mod_assets/fit/1l.png", (0, 0), "mod_assets/fit/2r.png", (0, 0), "mod_assets/fit/d.png")
image fit 2e = im.Composite((960, 960), (0, 0), "mod_assets/fit/1l.png", (0, 0), "mod_assets/fit/2r.png", (0, 0), "mod_assets/fit/e.png")
image fit 2f = im.Composite((960, 960), (0, 0), "mod_assets/fit/1l.png", (0, 0), "mod_assets/fit/2r.png", (0, 0), "mod_assets/fit/f.png")
image fit 2g = im.Composite((960, 960), (0, 0), "mod_assets/fit/1l.png", (0, 0), "mod_assets/fit/2r.png", (0, 0), "mod_assets/fit/g.png")
image fit 2g1 = im.Composite((960, 960), (0, 0), "mod_assets/fit/1l.png", (0, 0), "mod_assets/fit/2r.png", (0, 0), "mod_assets/fit/g1.png")
image fit 2g2 = im.Composite((960, 960), (0, 0), "mod_assets/fit/1l.png", (0, 0), "mod_assets/fit/2r.png", (0, 0), "mod_assets/fit/g2.png")
image fit 2g3 = im.Composite((960, 960), (0, 0), "mod_assets/fit/1l.png", (0, 0), "mod_assets/fit/2r.png", (0, 0), "mod_assets/fit/g3.png")
image fit 2g4 = im.Composite((960, 960), (0, 0), "mod_assets/fit/1l.png", (0, 0), "mod_assets/fit/2r.png", (0, 0), "mod_assets/fit/g4.png")
image fit 2h = im.Composite((960, 960), (0, 0), "mod_assets/fit/1l.png", (0, 0), "mod_assets/fit/2r.png", (0, 0), "mod_assets/fit/h.png")
image fit 2i = im.Composite((960, 960), (0, 0), "mod_assets/fit/1l.png", (0, 0), "mod_assets/fit/2r.png", (0, 0), "mod_assets/fit/i.png")
image fit 2j = im.Composite((960, 960), (0, 0), "mod_assets/fit/1l.png", (0, 0), "mod_assets/fit/2r.png", (0, 0), "mod_assets/fit/j.png")
image fit 2k = im.Composite((960, 960), (0, 0), "mod_assets/fit/1l.png", (0, 0), "mod_assets/fit/2r.png", (0, 0), "mod_assets/fit/k.png")
image fit 2l = im.Composite((960, 960), (0, 0), "mod_assets/fit/1l.png", (0, 0), "mod_assets/fit/2r.png", (0, 0), "mod_assets/fit/l.png")
image fit 2m = im.Composite((960, 960), (0, 0), "mod_assets/fit/1l.png", (0, 0), "mod_assets/fit/2r.png", (0, 0), "mod_assets/fit/m.png")
image fit 2n = im.Composite((960, 960), (0, 0), "mod_assets/fit/1l.png", (0, 0), "mod_assets/fit/2r.png", (0, 0), "mod_assets/fit/n.png")
image fit 2o = im.Composite((960, 960), (0, 0), "mod_assets/fit/1l.png", (0, 0), "mod_assets/fit/2r.png", (0, 0), "mod_assets/fit/o.png")
image fit 2p = im.Composite((960, 960), (0, 0), "mod_assets/fit/1l.png", (0, 0), "mod_assets/fit/2r.png", (0, 0), "mod_assets/fit/p.png")
image fit 2q = im.Composite((960, 960), (0, 0), "mod_assets/fit/1l.png", (0, 0), "mod_assets/fit/2r.png", (0, 0), "mod_assets/fit/q.png")
image fit 2r = im.Composite((960, 960), (0, 0), "mod_assets/fit/1l.png", (0, 0), "mod_assets/fit/2r.png", (0, 0), "mod_assets/fit/r.png")

image fit 3a = im.Composite((960, 960), (0, 0), "mod_assets/fit/2l.png", (0, 0), "mod_assets/fit/1r.png", (0, 0), "mod_assets/fit/a.png")
image fit 3b = im.Composite((960, 960), (0, 0), "mod_assets/fit/2l.png", (0, 0), "mod_assets/fit/1r.png", (0, 0), "mod_assets/fit/b.png")
image fit 3c = im.Composite((960, 960), (0, 0), "mod_assets/fit/2l.png", (0, 0), "mod_assets/fit/1r.png", (0, 0), "mod_assets/fit/c.png")
image fit 3d = im.Composite((960, 960), (0, 0), "mod_assets/fit/2l.png", (0, 0), "mod_assets/fit/1r.png", (0, 0), "mod_assets/fit/d.png")
image fit 3e = im.Composite((960, 960), (0, 0), "mod_assets/fit/2l.png", (0, 0), "mod_assets/fit/1r.png", (0, 0), "mod_assets/fit/e.png")
image fit 3f = im.Composite((960, 960), (0, 0), "mod_assets/fit/2l.png", (0, 0), "mod_assets/fit/1r.png", (0, 0), "mod_assets/fit/f.png")
image fit 3g = im.Composite((960, 960), (0, 0), "mod_assets/fit/2l.png", (0, 0), "mod_assets/fit/1r.png", (0, 0), "mod_assets/fit/g.png")
image fit 3g1 = im.Composite((960, 960), (0, 0), "mod_assets/fit/2l.png", (0, 0), "mod_assets/fit/1r.png", (0, 0), "mod_assets/fit/g1.png")
image fit 3g2 = im.Composite((960, 960), (0, 0), "mod_assets/fit/2l.png", (0, 0), "mod_assets/fit/1r.png", (0, 0), "mod_assets/fit/g2.png")
image fit 3g3 = im.Composite((960, 960), (0, 0), "mod_assets/fit/2l.png", (0, 0), "mod_assets/fit/1r.png", (0, 0), "mod_assets/fit/g3.png")
image fit 3g4 = im.Composite((960, 960), (0, 0), "mod_assets/fit/2l.png", (0, 0), "mod_assets/fit/1r.png", (0, 0), "mod_assets/fit/g4.png")
image fit 3h = im.Composite((960, 960), (0, 0), "mod_assets/fit/2l.png", (0, 0), "mod_assets/fit/1r.png", (0, 0), "mod_assets/fit/h.png")
image fit 3i = im.Composite((960, 960), (0, 0), "mod_assets/fit/2l.png", (0, 0), "mod_assets/fit/1r.png", (0, 0), "mod_assets/fit/i.png")
image fit 3j = im.Composite((960, 960), (0, 0), "mod_assets/fit/2l.png", (0, 0), "mod_assets/fit/1r.png", (0, 0), "mod_assets/fit/j.png")
image fit 3k = im.Composite((960, 960), (0, 0), "mod_assets/fit/2l.png", (0, 0), "mod_assets/fit/1r.png", (0, 0), "mod_assets/fit/k.png")
image fit 3l = im.Composite((960, 960), (0, 0), "mod_assets/fit/2l.png", (0, 0), "mod_assets/fit/1r.png", (0, 0), "mod_assets/fit/l.png")
image fit 3m = im.Composite((960, 960), (0, 0), "mod_assets/fit/2l.png", (0, 0), "mod_assets/fit/1r.png", (0, 0), "mod_assets/fit/m.png")
image fit 3n = im.Composite((960, 960), (0, 0), "mod_assets/fit/2l.png", (0, 0), "mod_assets/fit/1r.png", (0, 0), "mod_assets/fit/n.png")
image fit 3o = im.Composite((960, 960), (0, 0), "mod_assets/fit/2l.png", (0, 0), "mod_assets/fit/1r.png", (0, 0), "mod_assets/fit/o.png")
image fit 3p = im.Composite((960, 960), (0, 0), "mod_assets/fit/2l.png", (0, 0), "mod_assets/fit/1r.png", (0, 0), "mod_assets/fit/p.png")
image fit 3q = im.Composite((960, 960), (0, 0), "mod_assets/fit/2l.png", (0, 0), "mod_assets/fit/1r.png", (0, 0), "mod_assets/fit/q.png")
image fit 3r = im.Composite((960, 960), (0, 0), "mod_assets/fit/2l.png", (0, 0), "mod_assets/fit/1r.png", (0, 0), "mod_assets/fit/r.png")

image fit 4a = im.Composite((960, 960), (0, 0), "mod_assets/fit/2l.png", (0, 0), "mod_assets/fit/2r.png", (0, 0), "mod_assets/fit/a.png")
image fit 4b = im.Composite((960, 960), (0, 0), "mod_assets/fit/2l.png", (0, 0), "mod_assets/fit/2r.png", (0, 0), "mod_assets/fit/b.png")
image fit 4c = im.Composite((960, 960), (0, 0), "mod_assets/fit/2l.png", (0, 0), "mod_assets/fit/2r.png", (0, 0), "mod_assets/fit/c.png")
image fit 4d = im.Composite((960, 960), (0, 0), "mod_assets/fit/2l.png", (0, 0), "mod_assets/fit/2r.png", (0, 0), "mod_assets/fit/d.png")
image fit 4e = im.Composite((960, 960), (0, 0), "mod_assets/fit/2l.png", (0, 0), "mod_assets/fit/2r.png", (0, 0), "mod_assets/fit/e.png")
image fit 4f = im.Composite((960, 960), (0, 0), "mod_assets/fit/2l.png", (0, 0), "mod_assets/fit/2r.png", (0, 0), "mod_assets/fit/f.png")
image fit 4g = im.Composite((960, 960), (0, 0), "mod_assets/fit/2l.png", (0, 0), "mod_assets/fit/2r.png", (0, 0), "mod_assets/fit/g.png")
image fit 4g1 = im.Composite((960, 960), (0, 0), "mod_assets/fit/2l.png", (0, 0), "mod_assets/fit/2r.png", (0, 0), "mod_assets/fit/g1.png")
image fit 4g3 = im.Composite((960, 960), (0, 0), "mod_assets/fit/2l.png", (0, 0), "mod_assets/fit/2r.png", (0, 0), "mod_assets/fit/g2.png")
image fit 4g3 = im.Composite((960, 960), (0, 0), "mod_assets/fit/2l.png", (0, 0), "mod_assets/fit/2r.png", (0, 0), "mod_assets/fit/g3.png")
image fit 4g4 = im.Composite((960, 960), (0, 0), "mod_assets/fit/2l.png", (0, 0), "mod_assets/fit/2r.png", (0, 0), "mod_assets/fit/g4.png")
image fit 4h = im.Composite((960, 960), (0, 0), "mod_assets/fit/2l.png", (0, 0), "mod_assets/fit/2r.png", (0, 0), "mod_assets/fit/h.png")
image fit 4i = im.Composite((960, 960), (0, 0), "mod_assets/fit/2l.png", (0, 0), "mod_assets/fit/2r.png", (0, 0), "mod_assets/fit/i.png")
image fit 4j = im.Composite((960, 960), (0, 0), "mod_assets/fit/2l.png", (0, 0), "mod_assets/fit/2r.png", (0, 0), "mod_assets/fit/j.png")
image fit 4k = im.Composite((960, 960), (0, 0), "mod_assets/fit/2l.png", (0, 0), "mod_assets/fit/2r.png", (0, 0), "mod_assets/fit/k.png")
image fit 4l = im.Composite((960, 960), (0, 0), "mod_assets/fit/2l.png", (0, 0), "mod_assets/fit/2r.png", (0, 0), "mod_assets/fit/l.png")
image fit 4m = im.Composite((960, 960), (0, 0), "mod_assets/fit/2l.png", (0, 0), "mod_assets/fit/2r.png", (0, 0), "mod_assets/fit/m.png")
image fit 4n = im.Composite((960, 960), (0, 0), "mod_assets/fit/2l.png", (0, 0), "mod_assets/fit/2r.png", (0, 0), "mod_assets/fit/n.png")
image fit 4o = im.Composite((960, 960), (0, 0), "mod_assets/fit/2l.png", (0, 0), "mod_assets/fit/2r.png", (0, 0), "mod_assets/fit/o.png")
image fit 4p = im.Composite((960, 960), (0, 0), "mod_assets/fit/2l.png", (0, 0), "mod_assets/fit/2r.png", (0, 0), "mod_assets/fit/p.png")
image fit 4q = im.Composite((960, 960), (0, 0), "mod_assets/fit/2l.png", (0, 0), "mod_assets/fit/2r.png", (0, 0), "mod_assets/fit/q.png")
image fit 4r = im.Composite((960, 960), (0, 0), "mod_assets/fit/2l.png", (0, 0), "mod_assets/fit/2r.png", (0, 0), "mod_assets/fit/r.png")

image fit 5a = im.Composite((960, 960), (0, 0), "mod_assets/fit/3a.png")

image sammy 1a = im.Composite((960, 960), (0, 0), "mod_assets/samyballin/1.png")

image harumi 1a = im.Composite((960, 960), (0, 0), "mod_assets/harumi/1.png", (0, 0), "mod_assets/harumi/a.png")
image harumi 1b = im.Composite((960, 960), (0, 0), "mod_assets/harumi/1.png", (0, 0), "mod_assets/harumi/b.png")
image harumi 1c = im.Composite((960, 960), (0, 0), "mod_assets/harumi/1.png", (0, 0), "mod_assets/harumi/c.png")
image harumi 1d = im.Composite((960, 960), (0, 0), "mod_assets/harumi/1.png", (0, 0), "mod_assets/harumi/d.png")
image harumi 1e = im.Composite((960, 960), (0, 0), "mod_assets/harumi/1.png", (0, 0), "mod_assets/harumi/e.png")
image harumi 1f = im.Composite((960, 960), (0, 0), "mod_assets/harumi/1.png", (0, 0), "mod_assets/harumi/f.png")
image harumi 1g = im.Composite((960, 960), (0, 0), "mod_assets/harumi/1.png", (0, 0), "mod_assets/harumi/g.png")
image harumi 1h = im.Composite((960, 960), (0, 0), "mod_assets/harumi/1.png", (0, 0), "mod_assets/harumi/h.png")
image harumi 1i = im.Composite((960, 960), (0, 0), "mod_assets/harumi/1.png", (0, 0), "mod_assets/harumi/i.png")
image harumi 1j = im.Composite((960, 960), (0, 0), "mod_assets/harumi/1.png", (0, 0), "mod_assets/harumi/j.png")
image harumi 1k = im.Composite((960, 960), (0, 0), "mod_assets/harumi/1.png", (0, 0), "mod_assets/harumi/k.png")
image harumi 1l = im.Composite((960, 960), (0, 0), "mod_assets/harumi/1.png", (0, 0), "mod_assets/harumi/l.png")
image harumi 1m = im.Composite((960, 960), (0, 0), "mod_assets/harumi/1.png", (0, 0), "mod_assets/harumi/m.png")
image harumi 1n = im.Composite((960, 960), (0, 0), "mod_assets/harumi/1.png", (0, 0), "mod_assets/harumi/n.png")
image harumi 1o = im.Composite((960, 960), (0, 0), "mod_assets/harumi/1.png", (0, 0), "mod_assets/harumi/o.png")
image harumi 1p = im.Composite((960, 960), (0, 0), "mod_assets/harumi/1.png", (0, 0), "mod_assets/harumi/p.png")
image harumi 1q = im.Composite((960, 960), (0, 0), "mod_assets/harumi/1.png", (0, 0), "mod_assets/harumi/q.png")
image harumi 1r = im.Composite((960, 960), (0, 0), "mod_assets/harumi/1.png", (0, 0), "mod_assets/harumi/r.png")
image harumi 1s = im.Composite((960, 960), (0, 0), "mod_assets/harumi/1.png", (0, 0), "mod_assets/harumi/s.png")
image harumi 1t = im.Composite((960, 960), (0, 0), "mod_assets/harumi/1.png", (0, 0), "mod_assets/harumi/t.png")
image harumi 1u = im.Composite((960, 960), (0, 0), "mod_assets/harumi/1.png", (0, 0), "mod_assets/harumi/u.png")
image harumi 1v = im.Composite((960, 960), (0, 0), "mod_assets/harumi/1.png", (0, 0), "mod_assets/harumi/v.png")
image harumi 1w = im.Composite((960, 960), (0, 0), "mod_assets/harumi/1.png", (0, 0), "mod_assets/harumi/w.png")
image harumi 1x = im.Composite((960, 960), (0, 0), "mod_assets/harumi/1.png", (0, 0), "mod_assets/harumi/x.png")
image harumi 1y = im.Composite((960, 960), (0, 0), "mod_assets/harumi/1.png", (0, 0), "mod_assets/harumi/y.png")

image harumi 2a = im.Composite((960, 960), (0, 0), "mod_assets/harumi/2.png", (0, 0), "mod_assets/harumi/a.png")
image harumi 2b = im.Composite((960, 960), (0, 0), "mod_assets/harumi/2.png", (0, 0), "mod_assets/harumi/b.png")
image harumi 2c = im.Composite((960, 960), (0, 0), "mod_assets/harumi/2.png", (0, 0), "mod_assets/harumi/c.png")
image harumi 2d = im.Composite((960, 960), (0, 0), "mod_assets/harumi/2.png", (0, 0), "mod_assets/harumi/d.png")
image harumi 2e = im.Composite((960, 960), (0, 0), "mod_assets/harumi/2.png", (0, 0), "mod_assets/harumi/e.png")
image harumi 2f = im.Composite((960, 960), (0, 0), "mod_assets/harumi/2.png", (0, 0), "mod_assets/harumi/f.png")
image harumi 2g = im.Composite((960, 960), (0, 0), "mod_assets/harumi/2.png", (0, 0), "mod_assets/harumi/g.png")
image harumi 2h = im.Composite((960, 960), (0, 0), "mod_assets/harumi/2.png", (0, 0), "mod_assets/harumi/h.png")
image harumi 2i = im.Composite((960, 960), (0, 0), "mod_assets/harumi/2.png", (0, 0), "mod_assets/harumi/i.png")
image harumi 2j = im.Composite((960, 960), (0, 0), "mod_assets/harumi/2.png", (0, 0), "mod_assets/harumi/j.png")
image harumi 2k = im.Composite((960, 960), (0, 0), "mod_assets/harumi/2.png", (0, 0), "mod_assets/harumi/k.png")
image harumi 2l = im.Composite((960, 960), (0, 0), "mod_assets/harumi/2.png", (0, 0), "mod_assets/harumi/l.png")
image harumi 2m = im.Composite((960, 960), (0, 0), "mod_assets/harumi/2.png", (0, 0), "mod_assets/harumi/m.png")
image harumi 2n = im.Composite((960, 960), (0, 0), "mod_assets/harumi/2.png", (0, 0), "mod_assets/harumi/n.png")
image harumi 2o = im.Composite((960, 960), (0, 0), "mod_assets/harumi/2.png", (0, 0), "mod_assets/harumi/o.png")
image harumi 2p = im.Composite((960, 960), (0, 0), "mod_assets/harumi/2.png", (0, 0), "mod_assets/harumi/p.png")
image harumi 2q = im.Composite((960, 960), (0, 0), "mod_assets/harumi/2.png", (0, 0), "mod_assets/harumi/q.png")
image harumi 2r = im.Composite((960, 960), (0, 0), "mod_assets/harumi/2.png", (0, 0), "mod_assets/harumi/r.png")
image harumi 2s = im.Composite((960, 960), (0, 0), "mod_assets/harumi/2.png", (0, 0), "mod_assets/harumi/s.png")
image harumi 2t = im.Composite((960, 960), (0, 0), "mod_assets/harumi/2.png", (0, 0), "mod_assets/harumi/t.png")
image harumi 2u = im.Composite((960, 960), (0, 0), "mod_assets/harumi/2.png", (0, 0), "mod_assets/harumi/u.png")
image harumi 2v = im.Composite((960, 960), (0, 0), "mod_assets/harumi/2.png", (0, 0), "mod_assets/harumi/v.png")
image harumi 2w = im.Composite((960, 960), (0, 0), "mod_assets/harumi/2.png", (0, 0), "mod_assets/harumi/w.png")
image harumi 2x = im.Composite((960, 960), (0, 0), "mod_assets/harumi/2.png", (0, 0), "mod_assets/harumi/x.png")
image harumi 2y = im.Composite((960, 960), (0, 0), "mod_assets/harumi/2.png", (0, 0), "mod_assets/harumi/y.png")

image harumi 3a = im.Composite((960, 960), (0, 0), "mod_assets/harumi/3.png", (0, 0), "mod_assets/harumi/a.png")
image harumi 3b = im.Composite((960, 960), (0, 0), "mod_assets/harumi/3.png", (0, 0), "mod_assets/harumi/b.png")
image harumi 3c = im.Composite((960, 960), (0, 0), "mod_assets/harumi/3.png", (0, 0), "mod_assets/harumi/c.png")
image harumi 3d = im.Composite((960, 960), (0, 0), "mod_assets/harumi/3.png", (0, 0), "mod_assets/harumi/d.png")
image harumi 3e = im.Composite((960, 960), (0, 0), "mod_assets/harumi/3.png", (0, 0), "mod_assets/harumi/e.png")
image harumi 3f = im.Composite((960, 960), (0, 0), "mod_assets/harumi/3.png", (0, 0), "mod_assets/harumi/f.png")
image harumi 3g = im.Composite((960, 960), (0, 0), "mod_assets/harumi/3.png", (0, 0), "mod_assets/harumi/g.png")
image harumi 3h = im.Composite((960, 960), (0, 0), "mod_assets/harumi/3.png", (0, 0), "mod_assets/harumi/h.png")
image harumi 3i = im.Composite((960, 960), (0, 0), "mod_assets/harumi/3.png", (0, 0), "mod_assets/harumi/i.png")
image harumi 3j = im.Composite((960, 960), (0, 0), "mod_assets/harumi/3.png", (0, 0), "mod_assets/harumi/j.png")
image harumi 3k = im.Composite((960, 960), (0, 0), "mod_assets/harumi/3.png", (0, 0), "mod_assets/harumi/k.png")
image harumi 3l = im.Composite((960, 960), (0, 0), "mod_assets/harumi/3.png", (0, 0), "mod_assets/harumi/l.png")
image harumi 3m = im.Composite((960, 960), (0, 0), "mod_assets/harumi/3.png", (0, 0), "mod_assets/harumi/m.png")
image harumi 3n = im.Composite((960, 960), (0, 0), "mod_assets/harumi/3.png", (0, 0), "mod_assets/harumi/n.png")
image harumi 3o = im.Composite((960, 960), (0, 0), "mod_assets/harumi/3.png", (0, 0), "mod_assets/harumi/o.png")
image harumi 3p = im.Composite((960, 960), (0, 0), "mod_assets/harumi/3.png", (0, 0), "mod_assets/harumi/p.png")
image harumi 3q = im.Composite((960, 960), (0, 0), "mod_assets/harumi/3.png", (0, 0), "mod_assets/harumi/q.png")
image harumi 3r = im.Composite((960, 960), (0, 0), "mod_assets/harumi/3.png", (0, 0), "mod_assets/harumi/r.png")
image harumi 3s = im.Composite((960, 960), (0, 0), "mod_assets/harumi/3.png", (0, 0), "mod_assets/harumi/s.png")
image harumi 3t = im.Composite((960, 960), (0, 0), "mod_assets/harumi/3.png", (0, 0), "mod_assets/harumi/t.png")
image harumi 3u = im.Composite((960, 960), (0, 0), "mod_assets/harumi/3.png", (0, 0), "mod_assets/harumi/u.png")
image harumi 3v = im.Composite((960, 960), (0, 0), "mod_assets/harumi/3.png", (0, 0), "mod_assets/harumi/v.png")
image harumi 3w = im.Composite((960, 960), (0, 0), "mod_assets/harumi/3.png", (0, 0), "mod_assets/harumi/w.png")
image harumi 3x = im.Composite((960, 960), (0, 0), "mod_assets/harumi/3.png", (0, 0), "mod_assets/harumi/x.png")
image harumi 3y = im.Composite((960, 960), (0, 0), "mod_assets/harumi/3.png", (0, 0), "mod_assets/harumi/y.png")

image harumi 1ba = im.Composite((960, 960), (0, 0), "mod_assets/harumi/1b.png", (0, 0), "mod_assets/harumi/a.png")
image harumi 1bb = im.Composite((960, 960), (0, 0), "mod_assets/harumi/1b.png", (0, 0), "mod_assets/harumi/b.png")
image harumi 1bc = im.Composite((960, 960), (0, 0), "mod_assets/harumi/1b.png", (0, 0), "mod_assets/harumi/c.png")
image harumi 1bd = im.Composite((960, 960), (0, 0), "mod_assets/harumi/1b.png", (0, 0), "mod_assets/harumi/d.png")
image harumi 1be = im.Composite((960, 960), (0, 0), "mod_assets/harumi/1b.png", (0, 0), "mod_assets/harumi/e.png")
image harumi 1bf = im.Composite((960, 960), (0, 0), "mod_assets/harumi/1b.png", (0, 0), "mod_assets/harumi/f.png")
image harumi 1bg = im.Composite((960, 960), (0, 0), "mod_assets/harumi/1b.png", (0, 0), "mod_assets/harumi/g.png")
image harumi 1bh = im.Composite((960, 960), (0, 0), "mod_assets/harumi/1b.png", (0, 0), "mod_assets/harumi/h.png")
image harumi 1bi = im.Composite((960, 960), (0, 0), "mod_assets/harumi/1b.png", (0, 0), "mod_assets/harumi/i.png")
image harumi 1bj = im.Composite((960, 960), (0, 0), "mod_assets/harumi/1b.png", (0, 0), "mod_assets/harumi/j.png")
image harumi 1bk = im.Composite((960, 960), (0, 0), "mod_assets/harumi/1b.png", (0, 0), "mod_assets/harumi/k.png")
image harumi 1bl = im.Composite((960, 960), (0, 0), "mod_assets/harumi/1b.png", (0, 0), "mod_assets/harumi/l.png")
image harumi 1bm = im.Composite((960, 960), (0, 0), "mod_assets/harumi/1b.png", (0, 0), "mod_assets/harumi/m.png")
image harumi 1bn = im.Composite((960, 960), (0, 0), "mod_assets/harumi/1b.png", (0, 0), "mod_assets/harumi/n.png")
image harumi 1bo = im.Composite((960, 960), (0, 0), "mod_assets/harumi/1b.png", (0, 0), "mod_assets/harumi/o.png")
image harumi 1bp = im.Composite((960, 960), (0, 0), "mod_assets/harumi/1b.png", (0, 0), "mod_assets/harumi/p.png")
image harumi 1bq = im.Composite((960, 960), (0, 0), "mod_assets/harumi/1b.png", (0, 0), "mod_assets/harumi/q.png")
image harumi 1br = im.Composite((960, 960), (0, 0), "mod_assets/harumi/1b.png", (0, 0), "mod_assets/harumi/r.png")
image harumi 1bs = im.Composite((960, 960), (0, 0), "mod_assets/harumi/1b.png", (0, 0), "mod_assets/harumi/s.png")
image harumi 1bt = im.Composite((960, 960), (0, 0), "mod_assets/harumi/1b.png", (0, 0), "mod_assets/harumi/t.png")
image harumi 1bu = im.Composite((960, 960), (0, 0), "mod_assets/harumi/1b.png", (0, 0), "mod_assets/harumi/u.png")
image harumi 1bv = im.Composite((960, 960), (0, 0), "mod_assets/harumi/1b.png", (0, 0), "mod_assets/harumi/v.png")
image harumi 1bw = im.Composite((960, 960), (0, 0), "mod_assets/harumi/1b.png", (0, 0), "mod_assets/harumi/w.png")
image harumi 1bx = im.Composite((960, 960), (0, 0), "mod_assets/harumi/1b.png", (0, 0), "mod_assets/harumi/x.png")
image harumi 1by = im.Composite((960, 960), (0, 0), "mod_assets/harumi/1b.png", (0, 0), "mod_assets/harumi/y.png")

image harumi 2ba = im.Composite((960, 960), (0, 0), "mod_assets/harumi/2b.png", (0, 0), "mod_assets/harumi/a.png")
image harumi 2bb = im.Composite((960, 960), (0, 0), "mod_assets/harumi/2b.png", (0, 0), "mod_assets/harumi/b.png")
image harumi 2bc = im.Composite((960, 960), (0, 0), "mod_assets/harumi/2b.png", (0, 0), "mod_assets/harumi/c.png")
image harumi 2bd = im.Composite((960, 960), (0, 0), "mod_assets/harumi/2b.png", (0, 0), "mod_assets/harumi/d.png")
image harumi 2be = im.Composite((960, 960), (0, 0), "mod_assets/harumi/2b.png", (0, 0), "mod_assets/harumi/e.png")
image harumi 2bf = im.Composite((960, 960), (0, 0), "mod_assets/harumi/2b.png", (0, 0), "mod_assets/harumi/f.png")
image harumi 2bg = im.Composite((960, 960), (0, 0), "mod_assets/harumi/2b.png", (0, 0), "mod_assets/harumi/g.png")
image harumi 2bh = im.Composite((960, 960), (0, 0), "mod_assets/harumi/2b.png", (0, 0), "mod_assets/harumi/h.png")
image harumi 2bi = im.Composite((960, 960), (0, 0), "mod_assets/harumi/2b.png", (0, 0), "mod_assets/harumi/i.png")
image harumi 2bj = im.Composite((960, 960), (0, 0), "mod_assets/harumi/2b.png", (0, 0), "mod_assets/harumi/j.png")
image harumi 2bk = im.Composite((960, 960), (0, 0), "mod_assets/harumi/2b.png", (0, 0), "mod_assets/harumi/k.png")
image harumi 2bl = im.Composite((960, 960), (0, 0), "mod_assets/harumi/2b.png", (0, 0), "mod_assets/harumi/l.png")
image harumi 2bm = im.Composite((960, 960), (0, 0), "mod_assets/harumi/2b.png", (0, 0), "mod_assets/harumi/m.png")
image harumi 2bn = im.Composite((960, 960), (0, 0), "mod_assets/harumi/2b.png", (0, 0), "mod_assets/harumi/n.png")
image harumi 2bo = im.Composite((960, 960), (0, 0), "mod_assets/harumi/2b.png", (0, 0), "mod_assets/harumi/o.png")
image harumi 2bp = im.Composite((960, 960), (0, 0), "mod_assets/harumi/2b.png", (0, 0), "mod_assets/harumi/p.png")
image harumi 2bq = im.Composite((960, 960), (0, 0), "mod_assets/harumi/2b.png", (0, 0), "mod_assets/harumi/q.png")
image harumi 2br = im.Composite((960, 960), (0, 0), "mod_assets/harumi/2b.png", (0, 0), "mod_assets/harumi/r.png")
image harumi 2bs = im.Composite((960, 960), (0, 0), "mod_assets/harumi/2b.png", (0, 0), "mod_assets/harumi/s.png")
image harumi 2bt = im.Composite((960, 960), (0, 0), "mod_assets/harumi/2b.png", (0, 0), "mod_assets/harumi/t.png")
image harumi 2bu = im.Composite((960, 960), (0, 0), "mod_assets/harumi/2b.png", (0, 0), "mod_assets/harumi/u.png")
image harumi 2bv = im.Composite((960, 960), (0, 0), "mod_assets/harumi/2b.png", (0, 0), "mod_assets/harumi/v.png")
image harumi 2bw = im.Composite((960, 960), (0, 0), "mod_assets/harumi/2b.png", (0, 0), "mod_assets/harumi/w.png")
image harumi 2bx = im.Composite((960, 960), (0, 0), "mod_assets/harumi/2b.png", (0, 0), "mod_assets/harumi/x.png")
image harumi 2by = im.Composite((960, 960), (0, 0), "mod_assets/harumi/2b.png", (0, 0), "mod_assets/harumi/y.png")

image harumi 3ba = im.Composite((960, 960), (0, 0), "mod_assets/harumi/3b.png", (0, 0), "mod_assets/harumi/a.png")
image harumi 3bb = im.Composite((960, 960), (0, 0), "mod_assets/harumi/3b.png", (0, 0), "mod_assets/harumi/b.png")
image harumi 3bc = im.Composite((960, 960), (0, 0), "mod_assets/harumi/3b.png", (0, 0), "mod_assets/harumi/c.png")
image harumi 3bd = im.Composite((960, 960), (0, 0), "mod_assets/harumi/3b.png", (0, 0), "mod_assets/harumi/d.png")
image harumi 3be = im.Composite((960, 960), (0, 0), "mod_assets/harumi/3b.png", (0, 0), "mod_assets/harumi/e.png")
image harumi 3bf = im.Composite((960, 960), (0, 0), "mod_assets/harumi/3b.png", (0, 0), "mod_assets/harumi/f.png")
image harumi 3bg = im.Composite((960, 960), (0, 0), "mod_assets/harumi/3b.png", (0, 0), "mod_assets/harumi/g.png")
image harumi 3bh = im.Composite((960, 960), (0, 0), "mod_assets/harumi/3b.png", (0, 0), "mod_assets/harumi/h.png")
image harumi 3bi = im.Composite((960, 960), (0, 0), "mod_assets/harumi/3b.png", (0, 0), "mod_assets/harumi/i.png")
image harumi 3bj = im.Composite((960, 960), (0, 0), "mod_assets/harumi/3b.png", (0, 0), "mod_assets/harumi/j.png")
image harumi 3bk = im.Composite((960, 960), (0, 0), "mod_assets/harumi/3b.png", (0, 0), "mod_assets/harumi/k.png")
image harumi 3bl = im.Composite((960, 960), (0, 0), "mod_assets/harumi/3b.png", (0, 0), "mod_assets/harumi/l.png")
image harumi 3bm = im.Composite((960, 960), (0, 0), "mod_assets/harumi/3b.png", (0, 0), "mod_assets/harumi/m.png")
image harumi 3bn = im.Composite((960, 960), (0, 0), "mod_assets/harumi/3b.png", (0, 0), "mod_assets/harumi/n.png")
image harumi 3bo = im.Composite((960, 960), (0, 0), "mod_assets/harumi/3b.png", (0, 0), "mod_assets/harumi/o.png")
image harumi 3bp = im.Composite((960, 960), (0, 0), "mod_assets/harumi/3b.png", (0, 0), "mod_assets/harumi/p.png")
image harumi 3bq = im.Composite((960, 960), (0, 0), "mod_assets/harumi/3b.png", (0, 0), "mod_assets/harumi/q.png")
image harumi 3br = im.Composite((960, 960), (0, 0), "mod_assets/harumi/3b.png", (0, 0), "mod_assets/harumi/r.png")
image harumi 3bs = im.Composite((960, 960), (0, 0), "mod_assets/harumi/3b.png", (0, 0), "mod_assets/harumi/s.png")
image harumi 3bt = im.Composite((960, 960), (0, 0), "mod_assets/harumi/3b.png", (0, 0), "mod_assets/harumi/t.png")
image harumi 3bu = im.Composite((960, 960), (0, 0), "mod_assets/harumi/3b.png", (0, 0), "mod_assets/harumi/u.png")
image harumi 3bv = im.Composite((960, 960), (0, 0), "mod_assets/harumi/3b.png", (0, 0), "mod_assets/harumi/v.png")
image harumi 3bw = im.Composite((960, 960), (0, 0), "mod_assets/harumi/3b.png", (0, 0), "mod_assets/harumi/w.png")
image harumi 3bx = im.Composite((960, 960), (0, 0), "mod_assets/harumi/3b.png", (0, 0), "mod_assets/harumi/x.png")
image harumi 3by = im.Composite((960, 960), (0, 0), "mod_assets/harumi/3b.png", (0, 0), "mod_assets/harumi/y.png")

image harumi 1ca = im.Composite((960, 960), (0, 0), "mod_assets/harumi/1c.png", (0, 0), "mod_assets/harumi/a.png")
image harumi 1cb = im.Composite((960, 960), (0, 0), "mod_assets/harumi/1c.png", (0, 0), "mod_assets/harumi/b.png")
image harumi 1cc = im.Composite((960, 960), (0, 0), "mod_assets/harumi/1c.png", (0, 0), "mod_assets/harumi/c.png")
image harumi 1cd = im.Composite((960, 960), (0, 0), "mod_assets/harumi/1c.png", (0, 0), "mod_assets/harumi/d.png")
image harumi 1ce = im.Composite((960, 960), (0, 0), "mod_assets/harumi/1c.png", (0, 0), "mod_assets/harumi/e.png")
image harumi 1cf = im.Composite((960, 960), (0, 0), "mod_assets/harumi/1c.png", (0, 0), "mod_assets/harumi/f.png")
image harumi 1cg = im.Composite((960, 960), (0, 0), "mod_assets/harumi/1c.png", (0, 0), "mod_assets/harumi/g.png")
image harumi 1ch = im.Composite((960, 960), (0, 0), "mod_assets/harumi/1c.png", (0, 0), "mod_assets/harumi/h.png")
image harumi 1ci = im.Composite((960, 960), (0, 0), "mod_assets/harumi/1c.png", (0, 0), "mod_assets/harumi/i.png")
image harumi 1cj = im.Composite((960, 960), (0, 0), "mod_assets/harumi/1c.png", (0, 0), "mod_assets/harumi/j.png")
image harumi 1ck = im.Composite((960, 960), (0, 0), "mod_assets/harumi/1c.png", (0, 0), "mod_assets/harumi/k.png")
image harumi 1cl = im.Composite((960, 960), (0, 0), "mod_assets/harumi/1c.png", (0, 0), "mod_assets/harumi/l.png")
image harumi 1cm = im.Composite((960, 960), (0, 0), "mod_assets/harumi/1c.png", (0, 0), "mod_assets/harumi/m.png")
image harumi 1cn = im.Composite((960, 960), (0, 0), "mod_assets/harumi/1c.png", (0, 0), "mod_assets/harumi/n.png")
image harumi 1co = im.Composite((960, 960), (0, 0), "mod_assets/harumi/1c.png", (0, 0), "mod_assets/harumi/o.png")
image harumi 1cp = im.Composite((960, 960), (0, 0), "mod_assets/harumi/1c.png", (0, 0), "mod_assets/harumi/p.png")
image harumi 1cq = im.Composite((960, 960), (0, 0), "mod_assets/harumi/1c.png", (0, 0), "mod_assets/harumi/q.png")
image harumi 1cr = im.Composite((960, 960), (0, 0), "mod_assets/harumi/1c.png", (0, 0), "mod_assets/harumi/r.png")
image harumi 1cs = im.Composite((960, 960), (0, 0), "mod_assets/harumi/1c.png", (0, 0), "mod_assets/harumi/s.png")
image harumi 1ct = im.Composite((960, 960), (0, 0), "mod_assets/harumi/1c.png", (0, 0), "mod_assets/harumi/t.png")
image harumi 1cu = im.Composite((960, 960), (0, 0), "mod_assets/harumi/1c.png", (0, 0), "mod_assets/harumi/u.png")
image harumi 1cv = im.Composite((960, 960), (0, 0), "mod_assets/harumi/1c.png", (0, 0), "mod_assets/harumi/v.png")
image harumi 1cw = im.Composite((960, 960), (0, 0), "mod_assets/harumi/1c.png", (0, 0), "mod_assets/harumi/w.png")
image harumi 1cx = im.Composite((960, 960), (0, 0), "mod_assets/harumi/1c.png", (0, 0), "mod_assets/harumi/x.png")
image harumi 1cy = im.Composite((960, 960), (0, 0), "mod_assets/harumi/1c.png", (0, 0), "mod_assets/harumi/y.png")

image harumi 2ca = im.Composite((960, 960), (0, 0), "mod_assets/harumi/2c.png", (0, 0), "mod_assets/harumi/a.png")
image harumi 2cb = im.Composite((960, 960), (0, 0), "mod_assets/harumi/2c.png", (0, 0), "mod_assets/harumi/b.png")
image harumi 2cc = im.Composite((960, 960), (0, 0), "mod_assets/harumi/2c.png", (0, 0), "mod_assets/harumi/c.png")
image harumi 2cd = im.Composite((960, 960), (0, 0), "mod_assets/harumi/2c.png", (0, 0), "mod_assets/harumi/d.png")
image harumi 2ce = im.Composite((960, 960), (0, 0), "mod_assets/harumi/2c.png", (0, 0), "mod_assets/harumi/e.png")
image harumi 2cf = im.Composite((960, 960), (0, 0), "mod_assets/harumi/2c.png", (0, 0), "mod_assets/harumi/f.png")
image harumi 2cg = im.Composite((960, 960), (0, 0), "mod_assets/harumi/2c.png", (0, 0), "mod_assets/harumi/g.png")
image harumi 2ch = im.Composite((960, 960), (0, 0), "mod_assets/harumi/2c.png", (0, 0), "mod_assets/harumi/h.png")
image harumi 2ci = im.Composite((960, 960), (0, 0), "mod_assets/harumi/2c.png", (0, 0), "mod_assets/harumi/i.png")
image harumi 2cj = im.Composite((960, 960), (0, 0), "mod_assets/harumi/2c.png", (0, 0), "mod_assets/harumi/j.png")
image harumi 2ck = im.Composite((960, 960), (0, 0), "mod_assets/harumi/2c.png", (0, 0), "mod_assets/harumi/k.png")
image harumi 2cl = im.Composite((960, 960), (0, 0), "mod_assets/harumi/2c.png", (0, 0), "mod_assets/harumi/l.png")
image harumi 2cm = im.Composite((960, 960), (0, 0), "mod_assets/harumi/2c.png", (0, 0), "mod_assets/harumi/m.png")
image harumi 2cn = im.Composite((960, 960), (0, 0), "mod_assets/harumi/2c.png", (0, 0), "mod_assets/harumi/n.png")
image harumi 2co = im.Composite((960, 960), (0, 0), "mod_assets/harumi/2c.png", (0, 0), "mod_assets/harumi/o.png")
image harumi 2cp = im.Composite((960, 960), (0, 0), "mod_assets/harumi/2c.png", (0, 0), "mod_assets/harumi/p.png")
image harumi 2cq = im.Composite((960, 960), (0, 0), "mod_assets/harumi/2c.png", (0, 0), "mod_assets/harumi/q.png")
image harumi 2cr = im.Composite((960, 960), (0, 0), "mod_assets/harumi/2c.png", (0, 0), "mod_assets/harumi/r.png")
image harumi 2cs = im.Composite((960, 960), (0, 0), "mod_assets/harumi/2c.png", (0, 0), "mod_assets/harumi/s.png")
image harumi 2ct = im.Composite((960, 960), (0, 0), "mod_assets/harumi/2c.png", (0, 0), "mod_assets/harumi/t.png")
image harumi 2cu = im.Composite((960, 960), (0, 0), "mod_assets/harumi/2c.png", (0, 0), "mod_assets/harumi/u.png")
image harumi 2cv = im.Composite((960, 960), (0, 0), "mod_assets/harumi/2c.png", (0, 0), "mod_assets/harumi/v.png")
image harumi 2cw = im.Composite((960, 960), (0, 0), "mod_assets/harumi/2c.png", (0, 0), "mod_assets/harumi/w.png")
image harumi 2cx = im.Composite((960, 960), (0, 0), "mod_assets/harumi/2c.png", (0, 0), "mod_assets/harumi/x.png")
image harumi 2cy = im.Composite((960, 960), (0, 0), "mod_assets/harumi/2c.png", (0, 0), "mod_assets/harumi/y.png")

image harumi 3ca = im.Composite((960, 960), (0, 0), "mod_assets/harumi/3c.png", (0, 0), "mod_assets/harumi/a.png")
image harumi 3cb = im.Composite((960, 960), (0, 0), "mod_assets/harumi/3c.png", (0, 0), "mod_assets/harumi/b.png")
image harumi 3cc = im.Composite((960, 960), (0, 0), "mod_assets/harumi/3c.png", (0, 0), "mod_assets/harumi/c.png")
image harumi 3cd = im.Composite((960, 960), (0, 0), "mod_assets/harumi/3c.png", (0, 0), "mod_assets/harumi/d.png")
image harumi 3ce = im.Composite((960, 960), (0, 0), "mod_assets/harumi/3c.png", (0, 0), "mod_assets/harumi/e.png")
image harumi 3cf = im.Composite((960, 960), (0, 0), "mod_assets/harumi/3c.png", (0, 0), "mod_assets/harumi/f.png")
image harumi 3cg = im.Composite((960, 960), (0, 0), "mod_assets/harumi/3c.png", (0, 0), "mod_assets/harumi/g.png")
image harumi 3ch = im.Composite((960, 960), (0, 0), "mod_assets/harumi/3c.png", (0, 0), "mod_assets/harumi/h.png")
image harumi 3ci = im.Composite((960, 960), (0, 0), "mod_assets/harumi/3c.png", (0, 0), "mod_assets/harumi/i.png")
image harumi 3cj = im.Composite((960, 960), (0, 0), "mod_assets/harumi/3c.png", (0, 0), "mod_assets/harumi/j.png")
image harumi 3ck = im.Composite((960, 960), (0, 0), "mod_assets/harumi/3c.png", (0, 0), "mod_assets/harumi/k.png")
image harumi 3cl = im.Composite((960, 960), (0, 0), "mod_assets/harumi/3c.png", (0, 0), "mod_assets/harumi/l.png")
image harumi 3cm = im.Composite((960, 960), (0, 0), "mod_assets/harumi/3c.png", (0, 0), "mod_assets/harumi/m.png")
image harumi 3cn = im.Composite((960, 960), (0, 0), "mod_assets/harumi/3c.png", (0, 0), "mod_assets/harumi/n.png")
image harumi 3co = im.Composite((960, 960), (0, 0), "mod_assets/harumi/3c.png", (0, 0), "mod_assets/harumi/o.png")
image harumi 3cp = im.Composite((960, 960), (0, 0), "mod_assets/harumi/3c.png", (0, 0), "mod_assets/harumi/p.png")
image harumi 3cq = im.Composite((960, 960), (0, 0), "mod_assets/harumi/3c.png", (0, 0), "mod_assets/harumi/q.png")
image harumi 3cr = im.Composite((960, 960), (0, 0), "mod_assets/harumi/3c.png", (0, 0), "mod_assets/harumi/r.png")
image harumi 3cs = im.Composite((960, 960), (0, 0), "mod_assets/harumi/3c.png", (0, 0), "mod_assets/harumi/s.png")
image harumi 3ct = im.Composite((960, 960), (0, 0), "mod_assets/harumi/3c.png", (0, 0), "mod_assets/harumi/t.png")
image harumi 3cu = im.Composite((960, 960), (0, 0), "mod_assets/harumi/3c.png", (0, 0), "mod_assets/harumi/u.png")
image harumi 3cv = im.Composite((960, 960), (0, 0), "mod_assets/harumi/3c.png", (0, 0), "mod_assets/harumi/v.png")
image harumi 3cw = im.Composite((960, 960), (0, 0), "mod_assets/harumi/3c.png", (0, 0), "mod_assets/harumi/w.png")
image harumi 3cx = im.Composite((960, 960), (0, 0), "mod_assets/harumi/3c.png", (0, 0), "mod_assets/harumi/x.png")
image harumi 3cy = im.Composite((960, 960), (0, 0), "mod_assets/harumi/3c.png", (0, 0), "mod_assets/harumi/y.png")

image cg_yuri 1 = im.Composite((1500, 1075), (0, 0), "mod_assets/cg_yuri/b/1.png", (0, 0), "mod_assets/cg_yuri/a.png")
image cg_yuri 2 = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/2.png", (0, 0),  "mod_assets/cg_yuri/a.png")
image cg_yuri 3 = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/3.png", (0, 0), "mod_assets/cg_yuri/a.png")

image cg_yuri 1a = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/1.png", (0, 0), "mod_assets/cg_yuri/a.png")
image cg_yuri 1b = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/1.png", (0, 0), "mod_assets/cg_yuri/b.png")
image cg_yuri 1c = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/1.png", (0, 0), "mod_assets/cg_yuri/c.png")
image cg_yuri 1d = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/1.png", (0, 0), "mod_assets/cg_yuri/d.png")
image cg_yuri 1e = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/1.png", (0, 0), "mod_assets/cg_yuri/e.png")
image cg_yuri 1f = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/1.png", (0, 0), "mod_assets/cg_yuri/f.png")
image cg_yuri 1g = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/1.png", (0, 0), "mod_assets/cg_yuri/g.png")
image cg_yuri 1h = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/1.png", (0, 0), "mod_assets/cg_yuri/h.png")
image cg_yuri 1i = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/1.png", (0, 0), "mod_assets/cg_yuri/i.png")
image cg_yuri 1j = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/1.png", (0, 0), "mod_assets/cg_yuri/j.png")
image cg_yuri 1k = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/1.png", (0, 0), "mod_assets/cg_yuri/k.png")
image cg_yuri 1l = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/1.png", (0, 0), "mod_assets/cg_yuri/l.png")
image cg_yuri 1m = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/1.png", (0, 0), "mod_assets/cg_yuri/m.png")
image cg_yuri 1n = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/1.png", (0, 0), "mod_assets/cg_yuri/n.png")

image cg_yuri 2a = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/2.png", (0, 0), "mod_assets/cg_yuri/a.png")
image cg_yuri 2b = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/2.png", (0, 0), "mod_assets/cg_yuri/b.png")
image cg_yuri 2c = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/2.png", (0, 0), "mod_assets/cg_yuri/c.png")
image cg_yuri 2d = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/2.png", (0, 0), "mod_assets/cg_yuri/d.png")
image cg_yuri 2e = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/2.png", (0, 0), "mod_assets/cg_yuri/e.png")
image cg_yuri 2f = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/2.png", (0, 0), "mod_assets/cg_yuri/f.png")
image cg_yuri 2g = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/2.png", (0, 0), "mod_assets/cg_yuri/g.png")
image cg_yuri 2h = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/2.png", (0, 0), "mod_assets/cg_yuri/h.png")
image cg_yuri 2i = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/2.png", (0, 0), "mod_assets/cg_yuri/i.png")
image cg_yuri 2j = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/2.png", (0, 0), "mod_assets/cg_yuri/j.png")
image cg_yuri 2k = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/2.png", (0, 0), "mod_assets/cg_yuri/k.png")
image cg_yuri 2l = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/2.png", (0, 0), "mod_assets/cg_yuri/l.png")
image cg_yuri 2m = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/2.png", (0, 0), "mod_assets/cg_yuri/m.png")
image cg_yuri 2n = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/2.png", (0, 0), "mod_assets/cg_yuri/n.png")

image cg_yuri 3a = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/1.png", (0, 0), "mod_assets/cg_yuri/a.png")
image cg_yuri 3b = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/1.png", (0, 0), "mod_assets/cg_yuri/b.png")
image cg_yuri 3c = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/1.png", (0, 0), "mod_assets/cg_yuri/c.png")
image cg_yuri 3d = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/1.png", (0, 0), "mod_assets/cg_yuri/d.png")
image cg_yuri 3e = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/1.png", (0, 0), "mod_assets/cg_yuri/e.png")
image cg_yuri 3f = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/1.png", (0, 0), "mod_assets/cg_yuri/f.png")
image cg_yuri 3g = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/1.png", (0, 0), "mod_assets/cg_yuri/g.png")
image cg_yuri 3h = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/1.png", (0, 0), "mod_assets/cg_yuri/h.png")
image cg_yuri 3i = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/1.png", (0, 0), "mod_assets/cg_yuri/i.png")
image cg_yuri 3j = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/1.png", (0, 0), "mod_assets/cg_yuri/j.png")
image cg_yuri 3k = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/1.png", (0, 0), "mod_assets/cg_yuri/k.png")
image cg_yuri 3l = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/1.png", (0, 0), "mod_assets/cg_yuri/l.png")
image cg_yuri 3m = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/1.png", (0, 0), "mod_assets/cg_yuri/m.png")
image cg_yuri 3n = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/1.png", (0, 0), "mod_assets/cg_yuri/n.png")

#soldi
image amaya 1a = im.Composite((960, 960), (0, 0), "mod_assets/amaya/1.png", (0, 0), "mod_assets/amaya/a.png")
image amaya 1b = im.Composite((960, 960), (0, 0), "mod_assets/amaya/1.png", (0, 0), "mod_assets/amaya/b.png")
image amaya 1c = im.Composite((960, 960), (0, 0), "mod_assets/amaya/1.png", (0, 0), "mod_assets/amaya/c.png")
image amaya 1d = im.Composite((960, 960), (0, 0), "mod_assets/amaya/1.png", (0, 0), "mod_assets/amaya/d.png")
image amaya 1e = im.Composite((960, 960), (0, 0), "mod_assets/amaya/1.png", (0, 0), "mod_assets/amaya/e.png")
image amaya 1f = im.Composite((960, 960), (0, 0), "mod_assets/amaya/1.png", (0, 0), "mod_assets/amaya/f.png")
image amaya 1g = im.Composite((960, 960), (0, 0), "mod_assets/amaya/1.png", (0, 0), "mod_assets/amaya/g.png")
image amaya 1h = im.Composite((960, 960), (0, 0), "mod_assets/amaya/1.png", (0, 0), "mod_assets/amaya/h.png")
image amaya 1i = im.Composite((960, 960), (0, 0), "mod_assets/amaya/1.png", (0, 0), "mod_assets/amaya/i.png")
image amaya 1j = im.Composite((960, 960), (0, 0), "mod_assets/amaya/1.png", (0, 0), "mod_assets/amaya/j.png")
image amaya 1k = im.Composite((960, 960), (0, 0), "mod_assets/amaya/1.png", (0, 0), "mod_assets/amaya/k.png")
image amaya 1l = im.Composite((960, 960), (0, 0), "mod_assets/amaya/1.png", (0, 0), "mod_assets/amaya/l.png")
image amaya 1m = im.Composite((960, 960), (0, 0), "mod_assets/amaya/1.png", (0, 0), "mod_assets/amaya/m.png")
image amaya 1n = im.Composite((960, 960), (0, 0), "mod_assets/amaya/1.png", (0, 0), "mod_assets/amaya/n.png")
image amaya 1o = im.Composite((960, 960), (0, 0), "mod_assets/amaya/1.png", (0, 0), "mod_assets/amaya/o.png")
image amaya 1p = im.Composite((960, 960), (0, 0), "mod_assets/amaya/1.png", (0, 0), "mod_assets/amaya/p.png")
image amaya 1q = im.Composite((960, 960), (0, 0), "mod_assets/amaya/1.png", (0, 0), "mod_assets/amaya/q.png")
image amaya 1r = im.Composite((960, 960), (0, 0), "mod_assets/amaya/1.png", (0, 0), "mod_assets/amaya/r.png")
image amaya 1s = im.Composite((960, 960), (0, 0), "mod_assets/amaya/1.png", (0, 0), "mod_assets/amaya/s.png")
image amaya 1t = im.Composite((960, 960), (0, 0), "mod_assets/amaya/1.png", (0, 0), "mod_assets/amaya/t.png")
image amaya 1u = im.Composite((960, 960), (0, 0), "mod_assets/amaya/1.png", (0, 0), "mod_assets/amaya/u.png")
image amaya 1v = im.Composite((960, 960), (0, 0), "mod_assets/amaya/1.png", (0, 0), "mod_assets/amaya/v.png")
image amaya 1w = im.Composite((960, 960), (0, 0), "mod_assets/amaya/1.png", (0, 0), "mod_assets/amaya/w.png")
image amaya 1x = im.Composite((960, 960), (0, 0), "mod_assets/amaya/1.png", (0, 0), "mod_assets/amaya/x.png")
image amaya 1y = im.Composite((960, 960), (0, 0), "mod_assets/amaya/1.png", (0, 0), "mod_assets/amaya/y.png")
image amaya 1z = im.Composite((960, 960), (0, 0), "mod_assets/amaya/1.png", (0, 0), "mod_assets/amaya/z.png")


image amaya 2a = im.Composite((960, 960), (0, 0), "mod_assets/amaya/2.png", (0, 0), "mod_assets/amaya/a.png")
image amaya 2b = im.Composite((960, 960), (0, 0), "mod_assets/amaya/2.png", (0, 0), "mod_assets/amaya/b.png")
image amaya 2c = im.Composite((960, 960), (0, 0), "mod_assets/amaya/2.png", (0, 0), "mod_assets/amaya/c.png")
image amaya 2d = im.Composite((960, 960), (0, 0), "mod_assets/amaya/2.png", (0, 0), "mod_assets/amaya/d.png")
image amaya 2e = im.Composite((960, 960), (0, 0), "mod_assets/amaya/2.png", (0, 0), "mod_assets/amaya/e.png")
image amaya 2f = im.Composite((960, 960), (0, 0), "mod_assets/amaya/2.png", (0, 0), "mod_assets/amaya/f.png")
image amaya 2g = im.Composite((960, 960), (0, 0), "mod_assets/amaya/2.png", (0, 0), "mod_assets/amaya/g.png")
image amaya 2h = im.Composite((960, 960), (0, 0), "mod_assets/amaya/2.png", (0, 0), "mod_assets/amaya/h.png")
image amaya 2i = im.Composite((960, 960), (0, 0), "mod_assets/amaya/2.png", (0, 0), "mod_assets/amaya/i.png")
image amaya 2j = im.Composite((960, 960), (0, 0), "mod_assets/amaya/2.png", (0, 0), "mod_assets/amaya/j.png")
image amaya 2k = im.Composite((960, 960), (0, 0), "mod_assets/amaya/2.png", (0, 0), "mod_assets/amaya/k.png")
image amaya 2l = im.Composite((960, 960), (0, 0), "mod_assets/amaya/2.png", (0, 0), "mod_assets/amaya/l.png")
image amaya 2m = im.Composite((960, 960), (0, 0), "mod_assets/amaya/2.png", (0, 0), "mod_assets/amaya/m.png")
image amaya 2n = im.Composite((960, 960), (0, 0), "mod_assets/amaya/2.png", (0, 0), "mod_assets/amaya/n.png")
image amaya 2o = im.Composite((960, 960), (0, 0), "mod_assets/amaya/2.png", (0, 0), "mod_assets/amaya/o.png")
image amaya 2p = im.Composite((960, 960), (0, 0), "mod_assets/amaya/2.png", (0, 0), "mod_assets/amaya/p.png")
image amaya 2q = im.Composite((960, 960), (0, 0), "mod_assets/amaya/2.png", (0, 0), "mod_assets/amaya/q.png")
image amaya 2r = im.Composite((960, 960), (0, 0), "mod_assets/amaya/2.png", (0, 0), "mod_assets/amaya/r.png")
image amaya 2s = im.Composite((960, 960), (0, 0), "mod_assets/amaya/2.png", (0, 0), "mod_assets/amaya/s.png")
image amaya 2t = im.Composite((960, 960), (0, 0), "mod_assets/amaya/2.png", (0, 0), "mod_assets/amaya/t.png")
image amaya 2u = im.Composite((960, 960), (0, 0), "mod_assets/amaya/2.png", (0, 0), "mod_assets/amaya/u.png")
image amaya 2v = im.Composite((960, 960), (0, 0), "mod_assets/amaya/2.png", (0, 0), "mod_assets/amaya/v.png")
image amaya 2w = im.Composite((960, 960), (0, 0), "mod_assets/amaya/2.png", (0, 0), "mod_assets/amaya/w.png")
image amaya 2x = im.Composite((960, 960), (0, 0), "mod_assets/amaya/2.png", (0, 0), "mod_assets/amaya/x.png")
image amaya 2y = im.Composite((960, 960), (0, 0), "mod_assets/amaya/2.png", (0, 0), "mod_assets/amaya/y.png")
image amaya 2z = im.Composite((960, 960), (0, 0), "mod_assets/amaya/2.png", (0, 0), "mod_assets/amaya/z.png")


image amaya 3a = im.Composite((960, 960), (0, 0), "mod_assets/amaya/3.png", (0, 0), "mod_assets/amaya/a.png")
image amaya 3b = im.Composite((960, 960), (0, 0), "mod_assets/amaya/3.png", (0, 0), "mod_assets/amaya/b.png")
image amaya 3c = im.Composite((960, 960), (0, 0), "mod_assets/amaya/3.png", (0, 0), "mod_assets/amaya/c.png")
image amaya 3d = im.Composite((960, 960), (0, 0), "mod_assets/amaya/3.png", (0, 0), "mod_assets/amaya/d.png")
image amaya 3e = im.Composite((960, 960), (0, 0), "mod_assets/amaya/3.png", (0, 0), "mod_assets/amaya/e.png")
image amaya 3f = im.Composite((960, 960), (0, 0), "mod_assets/amaya/3.png", (0, 0), "mod_assets/amaya/f.png")
image amaya 3g = im.Composite((960, 960), (0, 0), "mod_assets/amaya/3.png", (0, 0), "mod_assets/amaya/g.png")
image amaya 3h = im.Composite((960, 960), (0, 0), "mod_assets/amaya/3.png", (0, 0), "mod_assets/amaya/h.png")
image amaya 3i = im.Composite((960, 960), (0, 0), "mod_assets/amaya/3.png", (0, 0), "mod_assets/amaya/i.png")
image amaya 3j = im.Composite((960, 960), (0, 0), "mod_assets/amaya/3.png", (0, 0), "mod_assets/amaya/j.png")
image amaya 3k = im.Composite((960, 960), (0, 0), "mod_assets/amaya/3.png", (0, 0), "mod_assets/amaya/k.png")
image amaya 3l = im.Composite((960, 960), (0, 0), "mod_assets/amaya/3.png", (0, 0), "mod_assets/amaya/l.png")
image amaya 3m = im.Composite((960, 960), (0, 0), "mod_assets/amaya/3.png", (0, 0), "mod_assets/amaya/m.png")
image amaya 3n = im.Composite((960, 960), (0, 0), "mod_assets/amaya/3.png", (0, 0), "mod_assets/amaya/n.png")
image amaya 3o = im.Composite((960, 960), (0, 0), "mod_assets/amaya/3.png", (0, 0), "mod_assets/amaya/o.png")
image amaya 3p = im.Composite((960, 960), (0, 0), "mod_assets/amaya/3.png", (0, 0), "mod_assets/amaya/p.png")
image amaya 3q = im.Composite((960, 960), (0, 0), "mod_assets/amaya/3.png", (0, 0), "mod_assets/amaya/q.png")
image amaya 3r = im.Composite((960, 960), (0, 0), "mod_assets/amaya/3.png", (0, 0), "mod_assets/amaya/r.png")
image amaya 3s = im.Composite((960, 960), (0, 0), "mod_assets/amaya/3.png", (0, 0), "mod_assets/amaya/s.png")
image amaya 3t = im.Composite((960, 960), (0, 0), "mod_assets/amaya/3.png", (0, 0), "mod_assets/amaya/t.png")
image amaya 3u = im.Composite((960, 960), (0, 0), "mod_assets/amaya/3.png", (0, 0), "mod_assets/amaya/u.png")
image amaya 3v = im.Composite((960, 960), (0, 0), "mod_assets/amaya/3.png", (0, 0), "mod_assets/amaya/v.png")
image amaya 3w = im.Composite((960, 960), (0, 0), "mod_assets/amaya/3.png", (0, 0), "mod_assets/amaya/w.png")
image amaya 3x = im.Composite((960, 960), (0, 0), "mod_assets/amaya/3.png", (0, 0), "mod_assets/amaya/x.png")
image amaya 3y = im.Composite((960, 960), (0, 0), "mod_assets/amaya/3.png", (0, 0), "mod_assets/amaya/y.png")
image amaya 3z = im.Composite((960, 960), (0, 0), "mod_assets/amaya/3.png", (0, 0), "mod_assets/amaya/z.png")


image amaya 4a = im.Composite((960, 960), (0, 0), "mod_assets/amaya/4.png", (0, 0), "mod_assets/amaya/a.png")
image amaya 4b = im.Composite((960, 960), (0, 0), "mod_assets/amaya/4.png", (0, 0), "mod_assets/amaya/b.png")
image amaya 4c = im.Composite((960, 960), (0, 0), "mod_assets/amaya/4.png", (0, 0), "mod_assets/amaya/c.png")
image amaya 4d = im.Composite((960, 960), (0, 0), "mod_assets/amaya/4.png", (0, 0), "mod_assets/amaya/d.png")
image amaya 4e = im.Composite((960, 960), (0, 0), "mod_assets/amaya/4.png", (0, 0), "mod_assets/amaya/e.png")
image amaya 4f = im.Composite((960, 960), (0, 0), "mod_assets/amaya/4.png", (0, 0), "mod_assets/amaya/f.png")
image amaya 4g = im.Composite((960, 960), (0, 0), "mod_assets/amaya/4.png", (0, 0), "mod_assets/amaya/g.png")
image amaya 4h = im.Composite((960, 960), (0, 0), "mod_assets/amaya/4.png", (0, 0), "mod_assets/amaya/h.png")
image amaya 4i = im.Composite((960, 960), (0, 0), "mod_assets/amaya/4.png", (0, 0), "mod_assets/amaya/i.png")
image amaya 4j = im.Composite((960, 960), (0, 0), "mod_assets/amaya/4.png", (0, 0), "mod_assets/amaya/j.png")
image amaya 4k = im.Composite((960, 960), (0, 0), "mod_assets/amaya/4.png", (0, 0), "mod_assets/amaya/k.png")
image amaya 4l = im.Composite((960, 960), (0, 0), "mod_assets/amaya/4.png", (0, 0), "mod_assets/amaya/l.png")
image amaya 4m = im.Composite((960, 960), (0, 0), "mod_assets/amaya/4.png", (0, 0), "mod_assets/amaya/m.png")
image amaya 4n = im.Composite((960, 960), (0, 0), "mod_assets/amaya/4.png", (0, 0), "mod_assets/amaya/n.png")
image amaya 4o = im.Composite((960, 960), (0, 0), "mod_assets/amaya/4.png", (0, 0), "mod_assets/amaya/o.png")
image amaya 4p = im.Composite((960, 960), (0, 0), "mod_assets/amaya/4.png", (0, 0), "mod_assets/amaya/p.png")
image amaya 4q = im.Composite((960, 960), (0, 0), "mod_assets/amaya/4.png", (0, 0), "mod_assets/amaya/q.png")
image amaya 4r = im.Composite((960, 960), (0, 0), "mod_assets/amaya/4.png", (0, 0), "mod_assets/amaya/r.png")
image amaya 4s = im.Composite((960, 960), (0, 0), "mod_assets/amaya/4.png", (0, 0), "mod_assets/amaya/s.png")
image amaya 4t = im.Composite((960, 960), (0, 0), "mod_assets/amaya/4.png", (0, 0), "mod_assets/amaya/t.png")
image amaya 4u = im.Composite((960, 960), (0, 0), "mod_assets/amaya/4.png", (0, 0), "mod_assets/amaya/u.png")
image amaya 4v = im.Composite((960, 960), (0, 0), "mod_assets/amaya/4.png", (0, 0), "mod_assets/amaya/v.png")
image amaya 4w = im.Composite((960, 960), (0, 0), "mod_assets/amaya/4.png", (0, 0), "mod_assets/amaya/w.png")
image amaya 4x = im.Composite((960, 960), (0, 0), "mod_assets/amaya/4.png", (0, 0), "mod_assets/amaya/x.png")
image amaya 4y = im.Composite((960, 960), (0, 0), "mod_assets/amaya/4.png", (0, 0), "mod_assets/amaya/y.png")
image amaya 4z = im.Composite((960, 960), (0, 0), "mod_assets/amaya/4.png", (0, 0), "mod_assets/amaya/z.png")

image lueck 1a = im.Composite((960, 960), (0, 0), "mod_assets/lueck/1.png", (0, 0), "mod_assets/lueck/a.png")
image lueck 1b = im.Composite((960, 960), (0, 0), "mod_assets/lueck/1.png", (0, 0), "mod_assets/lueck/b.png")
image lueck 1c = im.Composite((960, 960), (0, 0), "mod_assets/lueck/1.png", (0, 0), "mod_assets/lueck/c.png")
image lueck 1d = im.Composite((960, 960), (0, 0), "mod_assets/lueck/1.png", (0, 0), "mod_assets/lueck/d.png")
image lueck 1e = im.Composite((960, 960), (0, 0), "mod_assets/lueck/1.png", (0, 0), "mod_assets/lueck/e.png")

image bryson 1a = im.Composite((960, 960), (0, 0), "mod_assets/bryson/1.png")
image bryson 1b = im.Composite((960, 960), (0, 0), "mod_assets/bryson/2.png")

image aahilj 1a = im.Composite((960, 960), (0, 0), "mod_assets/aahilj/1.png")

image nekolais 1 = im.Composite((960, 960), (0, 0), "mod_assets/nekolais/1.png")

image atazoth 1a = im.Composite((960, 960), (0, 0), "mod_assets/atazoth/3a.png", (0, 0), "mod_assets/atazoth/c1.png")
image atazoth 1b = im.Composite((960, 960), (0, 0), "mod_assets/atazoth/3a.png", (0, 0), "mod_assets/atazoth/c2.png")

image mask_child:
    "images/cg/monika/child_2.png"
    xtile 2

image mask_mask:
    "images/cg/monika/mask.png"
    xtile 3

image mask_mask_flip:
    "images/cg/monika/mask.png"
    xtile 3 xzoom -1


image maskb:
    "images/cg/monika/maskb.png"
    xtile 3

image mask_test = AnimatedMask("#ff6000", "mask_mask", "maskb", 0.10, 32)
image mask_test2 = AnimatedMask("#ffffff", "mask_mask", "maskb", 0.03, 16)
image mask_test3 = AnimatedMask("#ff6000", "mask_mask_flip", "maskb", 0.10, 32)
image mask_test4 = AnimatedMask("#ffffff", "mask_mask_flip", "maskb", 0.03, 16)

image mask_2:
    "images/cg/monika/mask_2.png"
    xtile 3 subpixel True
    block:
        xoffset 1280
        linear 1200 xoffset 0
        repeat

image mask_3:
    "images/cg/monika/mask_3.png"
    xtile 3 subpixel True
    block:
        xoffset 1280
        linear 180 xoffset 0
        repeat

image monika_room = "images/cg/monika/monika_room.png"
image monika_room_highlight:
    "images/cg/monika/monika_room_highlight.png"
    function monika_alpha
image monika_bg = "images/cg/monika/monika_bg.png"
image monika_bg_highlight:
    "images/cg/monika/monika_bg_highlight.png"
    function monika_alpha
image monika_scare = "images/cg/monika/monika_scare.png"

image monika_body_glitch1:
    "images/cg/monika/monika_glitch1.png"
    0.15
    "images/cg/monika/monika_glitch2.png"
    0.15
    "images/cg/monika/monika_glitch1.png"
    0.15
    "images/cg/monika/monika_glitch2.png"
    1.00
    "images/cg/monika/monika_glitch1.png"
    0.15
    "images/cg/monika/monika_glitch2.png"
    0.15
    "images/cg/monika/monika_glitch1.png"
    0.15
    "images/cg/monika/monika_glitch2.png"

image monika_body_glitch2:
    "images/cg/monika/monika_glitch3.png"
    0.15
    "images/cg/monika/monika_glitch4.png"
    0.15
    "images/cg/monika/monika_glitch3.png"
    0.15
    "images/cg/monika/monika_glitch4.png"
    1.00
    "images/cg/monika/monika_glitch3.png"
    0.15
    "images/cg/monika/monika_glitch4.png"
    0.15
    "images/cg/monika/monika_glitch3.png"
    0.15
    "images/cg/monika/monika_glitch4.png"


image room_glitch = "images/cg/monika/monika_bg_glitch.png"

image room_mask = LiveComposite((1280, 720), (0, 0), "mask_test", (0, 0), "mask_test2")
image room_mask2 = LiveComposite((1280, 720), (0, 0), "mask_test3", (0, 0), "mask_test4")

define drakewipe = ImageDissolve("/mod_assets/drake.png", 1.5, ramplen=8)

## Character Variables
# This is where the characters are declared in the mod.
# To define a new character with assets, declare a character variable like in this example:
#   define e = DynamicCharacter('e_name', image='eileen', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
# To define a new character without assets, declare a character variable like this instead:
#   define en = Character('Eileen & Nat', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")

define narrator = Character(ctc="ctc", ctc_position="fixed")
define mc = DynamicCharacter('player', ctc="ctc", ctc_position="fixed")
define s = DynamicCharacter('s_name', image='sayori', ctc="ctc", ctc_position="fixed", who_color="#fff", who_outlines=[(3, "#7fd9ff", -1, 1), (2, "#7fd9ff", -1, 1)])
define m = DynamicCharacter('m_name', image='monika', ctc="ctc", ctc_position="fixed", who_color="#fff", who_outlines=[(3, "#89cf46", -1, 1), (2, "#89cf46", -1, 1)])
define n = DynamicCharacter('n_name', image='natsuki', ctc="ctc", ctc_position="fixed", who_color="#fff", who_outlines=[(3, "#fbadb8", -1, 1), (2, "#fbadb8", -1, 1)])
define y = DynamicCharacter('y_name', image='yuri', ctc="ctc", ctc_position="fixed")
define ny = Character('Nat & Yuri', ctc="ctc", ctc_position="fixed")

define k = DynamicCharacter('k_name', image='kryo', ctc="ctc", ctc_position="fixed", who_color="#fff", who_outlines=[(3, "#35BB2A", -1, 1), (2, "#35BB2A", -1, 1)])
define h = DynamicCharacter('mc_name', image='headlocker', ctc="ctc", ctc_position="fixed", who_color="#fff", who_outlines=[(3, "#35BB2A", -1, 1), (2, "#35BB2A", -1, 1)])
define e = DynamicCharacter('e_name', image='empyre', ctc="ctc", ctc_position="fixed", who_color="#fff", who_outlines=[(3, "#000", -1, 1), (2, "#000", -1, 1)])
define a = DynamicCharacter('a_name', image='amana', ctc="ctc", ctc_position="fixed", who_color="#fff", who_outlines=[(3, "#8a0afa", -1, 1), (2, "#8a0afa", -1, 1)])
define b = DynamicCharacter('b_name', image='braethan', ctc="ctc", ctc_position="fixed", who_color="#969696", who_outlines=[(3, "#cfcfcf", -1, 1), (2, "#fff", -1, 1)])
define ni = DynamicCharacter('ninja_name', image='junichi', ctc="ctc", ctc_position="fixed", who_color="#fff", who_outlines=[(3, "#0084ff", -1, 1), (2, "#0084ff", -1, 1)])
define g = DynamicCharacter('g_name', image='dpmc', ctc="ctc", ctc_position="fixed", who_color="#fff", who_outlines=[(3, "#c1b91d", -1, 1), (2, "#c1b91d", -1, 1)])
define c = DynamicCharacter('c_name', image='cleb', ctc="ctc", ctc_position="fixed", who_color="#fff", who_outlines=[(3, "#ff00ea", -1, 1), (2, "#ff00ea", -1, 1)])
define cpc = DynamicCharacter('cp_name', image='kotonoha', ctc="ctc", ctc_position="fixed", who_color="#fff", who_outlines=[(3, "#d676c3", -1, 1), (2, "#d676c3", -1, 1)])
define r = DynamicCharacter('r_name', image='reiko', ctc="ctc", ctc_position="fixed", who_color="#fff", who_outlines=[(3, "#ff0000", -1, 1), (2, "#ff0000", -1, 1)])
define mgt = DynamicCharacter('mgt_name', image='mgt', ctc="ctc", ctc_position="fixed", who_color="#fff", who_outlines=[(3, "#ff5900", -1, 1), (2, "#ff5900", -1, 1)])
define me = DynamicCharacter('me_name', image='chadmc', ctc="ctc", ctc_position="fixed", who_color="#fff", who_outlines=[(3, "#ff0000", -1, 1), (2, "#ff0000", -1, 1)])
define do = DynamicCharacter('do_name', image='doomslayer', ctc="ctc", ctc_position="fixed", who_color="#fff", who_outlines=[(3, "#ff0000", -1, 1), (2, "#ff0000", -1, 1)])
define co = DynamicCharacter('co_name', image='sayonika', ctc="ctc", ctc_position="fixed", who_color="#000", who_outlines=[(3, "#fff", -1, 1), (2, "#fff", -1, 1)])
define wo = DynamicCharacter('wo_name', image='nastya', ctc="ctc", ctc_position="fixed", who_color="#000", who_outlines=[(3, "#fff", -1, 1), (2, "#fff", -1, 1)])
define svt = DynamicCharacter('svt_name', image='soverytired', ctc="ctc", ctc_position="fixed", who_color="#fff", who_outlines=[(3, "#be54d8", -1, 1), (2, "#be54d8", -1, 1)])
define sp = DynamicCharacter('sp_name', image='protag', ctc="ctc", ctc_position="fixed", who_color="#fff", who_outlines=[(3, "#1daed3", -1, 1), (2, "#1daed3", -1, 1)])
define ph = DynamicCharacter('ph_name', image='phoenix', ctc="ctc", ctc_position="fixed", who_color="#fff", who_outlines=[(3, "#d6801e", -1, 1), (2, "#d6801e", -1, 1)])
define leo = DynamicCharacter('leo_name', image='leo', ctc="ctc", ctc_position="fixed", who_color="#fff", who_outlines=[(3, "#a1bd02", -1, 1), (2, "#a1bd02", -1, 1)])
define dl = DynamicCharacter('dl_name', image='david', ctc="ctc", ctc_position="fixed", who_color="#fff", who_outlines=[(3, "#d1009d", -1, 1), (2, "#d1009d", -1, 1)])
define ghy = DynamicCharacter("ghy_name", image='ghyuri', ctc="ctc", ctc_position="fixed", who_outlines=[(3, "#70007a", -1, 1), (2, "#70007a", -1, 1)])
define ch = DynamicCharacter('ch_name', image='dadsuki', ctc="ctc", ctc_position="fixed", who_color="#fff", who_outlines=[(3, "#40e9ff", -1, 1), (2, "#40e9ff", -1, 1)])
define sh = DynamicCharacter('sh_name', image='amy', ctc="ctc", ctc_position="fixed", who_color="#fff", who_outlines=[(3, "#c01c37", -1, 1), (2, "#c01c37", -1, 1)])
define sa = DynamicCharacter('sa_name', image='sammy', ctc="ctc", ctc_position="fixed", who_color="#fff", who_outlines=[(3, "#ac5487", -1, 1), (2, "#ac5487", -1, 1)])
define le = DynamicCharacter('le_name', image='skinny_mc', ctc="ctc", ctc_position="fixed", who_color="#fff", who_outlines=[(3, "#8b8d00", -1, 1), (2, "#8b8d00", -1, 1)])
define bja = DynamicCharacter('bja_name', image='miyuki', ctc="ctc", ctc_position="fixed", who_color="#fff", who_outlines=[(3, "#b82b78", -1, 1), (2, "#b82b78", -1, 1)])
define uzu = DynamicCharacter('uzu_name', image='harumi', ctc="ctc", ctc_position="fixed", who_color="#fff", who_outlines=[(3, "#6485c4", -1, 1), (2, "#6485c4", -1, 1)])
define f = DynamicCharacter('f_name', image='fit', ctc="ctc", ctc_position="fixed", who_color="#fff", who_outlines=[(3, "#19920e", -1, 1), (2, "#19920e", -1, 1)])
define ak = DynamicCharacter('ak_name', image='chitoge', ctc="ctc", ctc_position="fixed", who_color="#fff", who_outlines=[(3, "#bb3f19", -1, 1), (2, "#bb3f19", -1, 1)])
define cgy = DynamicCharacter('cgy_name', image='cg_yuri', ctc="ctc", ctc_position="fixed", who_color="#fff", who_outlines=[(3, "#70007a", -1, 1), (2, "#70007a", -1, 1)])
define so = DynamicCharacter('so_name', image='amaya', ctc="ctc", ctc_position="fixed", who_color="#fff", who_outlines=[(3, "#0d648d", -1, 1), (2, "#0d648d", -1, 1)])
define anon = DynamicCharacter('anon_name', image='cg_yuri', ctc="ctc", ctc_position="fixed", who_color="#fff", who_outlines=[(3, "#000000", -1, 1), (2, "#000000", -1, 1)])
define lu = DynamicCharacter('lu_name', image='lueck', ctc="ctc", ctc_position="fixed", who_color="#fff", who_outlines=[(3, "#A39B99", -1, 1), (2, "#A39B99", -1, 1)])
define bry = DynamicCharacter('bry_name', image='bryson', ctc="ctc", ctc_position="fixed", who_color="#fff", who_outlines=[(3, "#7586F0", -1, 1), (2, "#7586F0", -1, 1)])
define cool = DynamicCharacter('cool_name', image='elyssa', ctc="ctc", ctc_position="fixed", who_color="#fff", who_outlines=[(3, "#7586F0", -1, 1), (2, "#7586F0", -1, 1)])
define aa = DynamicCharacter('aa_name', image='aahilj', ctc="ctc", ctc_position="fixed", who_color="#fff", who_outlines=[(3, "#7fd9ff", -1, 1), (2, "#7fd9ff", -1, 1)])
define neko = DynamicCharacter('neko_name', image='nekolais', ctc="ctc", ctc_position="fixed", who_color="#fff", who_outlines=[(3, "#7586F0", -1, 1), (2, "#7586F0", -1, 1)])
define ata = DynamicCharacter('ata_name', image='atazoth', ctc="ctc", ctc_position="fixed", who_color="#fff", who_outlines=[(3, "#ca9025", -1, 1), (2, "#ca9025", -1, 1)])
# This variable determines whether to allow the player to dismiss pauses.
# By default this is set by config.developer which is normally set to false
# once you packaged your mod.
define _dismiss_pause = config.developer

## [BETA] Pronoun Variables
# This section adds the feature to use player pronouns within the game text easily.
# To use this feature, simply ask the user for their pronoun and use it here.
# For capitalization, use heC, himC, areC and hesC
default persistent.he = ""
default persistent.him = ""
default persistent.are = ""
default persistent.hes = ""
default he = persistent.he
default him = persistent.him
default are = persistent.are
default hes = persistent.hes
default he_capital = he.capitalize()
default him_capital = him.capitalize()
default are_capital = are.capitalize()
default hes_capital = hes.capitalize()

## Extra Settings Variables
# This section controls whether the mod is censored or is in let's play mode.
default persistent.uncensored_mode = False
default persistent.lets_play = False

## Variables
# This section declares variables when the mod runs for the first time on all saves.
# To make a new persistent variable, make a new variable with the 'persistent.' in it's name
# like in this example:
#   default persistent.monika = 1
# To make a non-persistent variable, make a new variable like this instead:
#   default cookies = False
# To make sure a variable is set to a given condition use 'define' rather than 'default'.

default persistent.playername = ""
default player = persistent.playername
default persistent.playthrough = 0
default persistent.yuri_kill = 0
default persistent.seen_eyes = None
default persistent.seen_sticker = None
default persistent.ghost_menu = None
default persistent.seen_ghost_menu = None
default seen_eyes_this_chapter = False
default persistent.anticheat = 0
default persistent.clear = [False, False, False, False, False, False, False, False, False, False]
default persistent.special_poems = None
default persistent.clearall = None
default persistent.menu_bg_m = None
default persistent.first_load = None
default persistent.first_poem = None
default persistent.seen_colors_poem = None
default persistent.monika_back = None

default in_sayori_kill = None
default in_yuri_kill = None
default anticheat = 0
define config.mouse = None
default allow_skipping = True
default basedir = config.basedir
default chapter = 0
default currentpos = 0
default faint_effect = None

# Default Name Variables
# To define a default name make a character name variable like in this example:
#   default e_name = "Eileen"

default s_name = "Sayori"
default m_name = "Monika"
default n_name = "Natsuki"
default y_name = "Yuri"
default k_name = "Kryo"
default mc_name = "Headlocker"
default a_name = "Amana"
default e_name = "Empyre"
default b_name = "Braethan"
default co_name = "Codex"
default ninja_name = "Ninja"
default g_name = "Gubbey"
default c_name = "Kayla"
default cp_name = "CPC"
default mgt_name = "MGT"
default me_name = "M3rc"
default r_name = "Retronika"
default wo_name = "iiTzWolfyy"
default do_name = "Doom Slayer"
default dl_name = "David Locklin"
default f_name = "Fit"
default leo_name = "Leomonade"
default ph_name = "Phoenix"
default svt_name = "SoVeryTired"
default sp_name = "Spirit"
default ghy_name = "G.H. Yuri"
default ch_name = "Chillington"
default sh_name = "Shane"
default sa_name = "Samyballin"
default le_name = "Legend"
default bja_name = "Billy J"
default uzu_name = "Uzumaki"
default ak_name = "Akai"
default cgy_name = "Yuri"
default so_name = "Soldi"
default anon_name = "???"
default lu_name = "LueckBoiii"
default bry_name = "BrysonBruv"
default cool_name = "CoolDigger"
default aa_name = "Aahilj"
default neko_name = "NekoLaiS"
default ata_name = "Atazoth"

# Poem Variables
# This section records how much each character likes your poem in-game.
# Syntax:
#   -1 - Bad
#   0 - Neutral
#   1 - Good
# To add a new poem person, make a poem array like in this example:
#   default e_poemappeal = [0, 0, 0]

default n_poemappeal = [0, 0, 0]
default s_poemappeal = [0, 0, 0]
default y_poemappeal = [0, 0, 0]
default m_poemappeal = [0, 0, 0]

# This variable keeps tracks on which person won the poem session after each day.
default poemwinner = ['sayori', 'sayori', 'sayori']

# These variables keep track on who has read your poem during poem sharing
default s_readpoem = False
default n_readpoem = False
default y_readpoem = False
default m_readpoem = False

# This variable keeps track on how many people have read your poem.
default poemsread = 0

# These variables control if we have seen Natsuki's or Yuri's exclusive scenes
default n_exclusivewatched = False
default y_exclusivewatched = False

# These variables track whether we gave Yuri our poem in Act 2 and if she
# ran away during Act 2 poem sharing.
default y_gave = False
default y_ranaway = False

# These variables track whether we read Natsuki's or Yuri's 3rd poem in poem sharing.
default n_read3 = False
default y_read3 = False

# This variable tracks which person we sided with in Day 2 of the game.
default ch1_choice = "sayori"

# This variable tracks if we gave Natsuki our poem first during poem sharing.
default n_poemearly = False

# These variables track whether we tried to help Monika or Sayori during Day 3's ending.
default help_sayori = None
default help_monika = None

# These variables track which route Day 4 will play and who is their name.
default ch4_scene = "yuri"
default ch4_name = "Yuri"

# This variable tracks whether we accepted Sayori's confession or not.
default sayori_confess = True

# This variable tracks whether we read Natsuki's 3rd poem in Act 2.
default natsuki_23 = None
