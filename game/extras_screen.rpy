## Copyright 2019-2023 Azariel Del Carmen (bronya_rand). All rights reserved.

# extras_screen.rpy
# This file contains the screen code for the extras menu for more screen options
# (Achievements/Gallery)
#
# To add a new slot to this menu, increase either the row or column count and copy
# the frames provided below already as a base to your own extras menu option.
# Make sure that the vpgrid is full or else you will get an error.
# Use `null` (without `'s) if you need to fill empty space.

default enable_gallery = True
default enable_achievements = False

screen extras():
    tag menu
    style_prefix "extras"

    use game_menu(_("Extras")):

        fixed:
                
            vpgrid id "ext":

                rows 1
                cols 3
                        
                xalign 0.5
                yalign 0.4

                spacing 18

                if enable_gallery:
                    frame:
                        xsize 160
                        ysize 140

                        vbox:
                            xalign 0.5
                            yalign 0.5

                            imagebutton:
                                idle Composite((150, 130), (50, 20), "mod_assets/mod_extra_images/gallery.png", (40, 75), Text("Gallery", style="extras_text"))
                                hover Composite((150, 130), (50, 20), "mod_assets/mod_extra_images/gallery.png", (38, 73), Text("Gallery", style="extras_hover_text"))
                                action ShowMenu("gallery")

                if enable_achievements: 
                    frame:
                        xsize 160
                        ysize 140

                        vbox:
                            xalign 0.5
                            yalign 0.5
            
                            imagebutton:
                                idle Composite((150, 130), (50, 20), "mod_assets/mod_extra_images/achievements.png", (40, 75), Text("Awards", style="extras_text"))
                                hover Composite((150, 130), (50, 20), "mod_assets/mod_extra_images/achievements.png", (38, 73), Text("Awards", style="extras_hover_text"))
                                action ShowMenu("achievements")

                frame:
                    xsize 160
                    ysize 140

                    vbox:
                        xalign 0.5
                        yalign 0.5
            
                        imagebutton:
                            idle Composite((150, 130), (50, 20), "mod_assets/mod_extra_images/about.png", (40, 75), Text("Credits", style="extras_text"))
                            hover Composite((150, 130), (50, 20), "mod_assets/mod_extra_images/about.png", (38, 73), Text("Credits", style="extras_hover_text"))
                            action ShowMenu("about")

            vbar value YScrollValue("ext") xalign 0.99 ysize 560

style extras_text:
    color "#000"
    outlines []
    size 20

style extras_hover_text is extras_text:
    outlines [(2, "#cacaca", 0, 0), (2, "#cacaca", 2, 2)]

style extras_image_button:
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound
