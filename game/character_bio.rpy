init -10 python:
    class BioCharacter:
        def __init__(self, name, bio, appear, image, logo, chibi=None, chibi_hover=None):
            self.name = name
            self.bio = bio
            self.appear = appear
            self.image = image
            self.logo = logo
            self.chibi = chibi
            self.chibi_hover = chibi_hover

# Example character data
define characters = [
    BioCharacter("Monika", "Death is deceptive and fleeting.\n\n'Everyday, I imagine a future where I can be with you.'", "{i}Doki Doki Literature Club!{/i} (2017)\n{i}Monika After Story{/i} (2017)\n{i}DDLC Plus!{/i} (2021)", "monika lean summer happ blaw m2", "mod_assets/bio_ddlc.png", "mod_assets/chibi/moni.png", "mod_assets/chibi/moni1.png"),
    BioCharacter("Natsuki", "Bitchass wife.\n\n'Baka.'", "{i}Doki Doki Literature Club!{/i} (2017)\n{i}Exit Music{/i} (2018)\n{i}DDLC Plus!{/i} (2021)", "natsuki turned winter lsur", "mod_assets/bio_ddlc.png", "mod_assets/chibi/nat.png", "mod_assets/chibi/nat1.png"),
    BioCharacter("Sayori", "Your favorite depressed girl is back.\n\n'What's the greatest kind of knot that you can tie with ease?'", "{i}Doki Doki Literature Club!{/i} (2017)\n{i}Salvation{/i} (2018)\n{i}DDLC Plus!{/i} (2021)", "sayori turned bridal happ lup rup mo ce", "mod_assets/bio_ddlc.png", "mod_assets/chibi/sayo.png", "mod_assets/chibi/sayo1.png"),
    BioCharacter("Yuri", "Character not found.\n\n'After all, doesn't a hot cup of tea help you enjoy a good book?'", "{i}Doki Doki Literature Club!{/i} (2017)\n{i}Fallen Angel{/i} (2019)\n{i}DDLC Plus!{/i} (2021)", "yuri turned casual worr", "mod_assets/bio_ddlc.png", "mod_assets/chibi/yuri.png", "mod_assets/chibi/yuri1.png"),
    BioCharacter("Grappling\nHook Yuri", "Multiverse traveling Doki that somehow ended up here.\n\n'I'm, uh, sorry to break it to you, but Photoshop is very real.'", "{i}Grappling Hook Yuri: Origin Arc{/i} (2022)\n{i}Crossbow Yuri{/i} (2023)\n{i}Deceptive Hearts 2{/i} (2025)", "ghyuri turned angr lup rhook", "mod_assets/ghy.jpg", "mod_assets/chibi/ghy.png", "mod_assets/chibi/ghy.png"),
    BioCharacter("Kryo", "Former husband to Monika and an active DDLC modder, Kryo has made his way down the modding rabbit hole and ended up as a protagonist in at least 4 mods.\n\n'I want to hug a tree at 105 MPH.'", "{i}The Monika Mod{/i} (2023)\n{i}Emerald Affection: Act 1{/i} (2023)\n{i}Yuri Gets a Haircut{/i} (2024)", "kryo 1a", "mod_assets/dh1.png", "mod_assets/chibi/kryo.png", "mod_assets/chibi/kryo1.png"),
    BioCharacter("Headlocker", "From just another fan of base DDLC and the modding community to becoming a modder himself and then overseeing said community itself. Yeah, he would have laughed at your face for being a dirty liar, but it seems anything is possible. Headlocker is thankful for having found his people and cherising the memories he's made there! Though, he would be quick to say...\n\n'Nothing and nobody is real!'", "{i}Welcome to the Anime Club{/i} (2023)\n{i}Anchoring Souls Anthology{/i} (Future)", "headlocker turned winter happ", "mod_assets/dh1.png", "mod_assets/chibi/head.png", "mod_assets/chibi/head1.png"),
    BioCharacter("AwesomeNinjaXD", "A DDLC modder since 2021, AwesomeNinjaXD joined the Discord server in 2023 and has been a member and homie ever since. He also made the spin-off, {i}Judgement Day{/i}.\n\n'Thigh Guy. Chiaki is my waifu.'", "{i}Project N{/i} (2022)\n{i}XD Demo{/i} (2023)\n{i}An Old Friend{/i} (Future)", "junichi base casual happ", "mod_assets/dh1.png", "mod_assets/chibi/ninja.png", "mod_assets/chibi/ninja1.png"),
    BioCharacter("Kayla", "Married Natsuki IRL and also hosted the 2023 Natsuki mod jam. Will not vore you.\n\n'Lesbians.'", "{i}The Monika Mod{/i} (2023)\n{i}Crossbow Yuri{/i} (2023)", "cleb 1i", "mod_assets/dh1.png", "mod_assets/chibi/kayla.png", "mod_assets/chibi/kayla1.png"),
    BioCharacter("Retronika", "A DDMC member since late 2021, Retro's mostly known for their smaller mods as well as being a founding member of Team Hope. Sometimes they don't agree with the general culture of the server, but that doesn't stop them from trying to make sure everyone has a good time. They're also really, really into garlic bread for some reason.\n\n'What are we doing here, again?'", "{i}Sayori Gets a Burger{/i} (2021)\n{i}Date to Dream Of{/i} (2023)\n{i}RealityCross{/i} (Future)", "reiko tough casual m3 e1 b1", "mod_assets/dh1.png", "mod_assets/chibi/retro.png", "mod_assets/chibi/retro1.png"),
    BioCharacter("Amana", "Beloved husbando and resident Yuri simp.\n\n'SAUSAGELOCKEEER!!!'", "{i}The Reflection (2025)", "amana 4", "mod_assets/dh1.png", "mod_assets/chibi/amana.png", "mod_assets/chibi/amana1.png"),
    BioCharacter("Spirit", "SpiritH0F, better known as just Spirit, is a mod developer, former DDMC committee member, and an avid mod enthusiast - despite his active shitting on certain 'divisive' mods... \n\n'Dammit, chat's getting horny again...'", "{i}The Rising Night{/i} (2023) (Solo)\n{i}Sayori Gets a Vape{/i} (2024) (Team)", "protag turned rdown e2", "mod_assets/logo.png", "mod_assets/chibi/spirit.png", "mod_assets/chibi/spirit1.png"),
    BioCharacter("Fit", "Has made an ungodly amount of DDLC mods. His art cooks though.\n\n'One day, I will fight for Truth, Justice, and a Better Tomorrow.'", "{i}Space{/i} (2021)\n{i}I Am Monika{/i} (2022)\n{i}Grad Days{/i} (Future)", "fit 2a", "mod_assets/logo.png", "mod_assets/chibi/fit.png", "mod_assets/chibi/fit1.png"),
    BioCharacter("David Locklin", "David Locklin is a modding enthusiast who has unintentionally developed a Cult of Personality in the DDMC.\n\n'He just like me fr (foreign relations).'", "{i}Foreign Relations Act 1{/i} (2024)", "david 2a", "mod_assets/logo.png", "mod_assets/chibi/david.png", "mod_assets/chibi/david1.png"),
    BioCharacter("Empyre", "Musician, modder, Fortnite extraordinaire.\n\n'Fwaaaah'\n-playboi carti", "{i}Grappling Hook Yuri: The Origin Arc{/i} (2022)\n{i}The Monika Mod{/i} (2023)\n{i}Paper Thin Hearts{/i} (2023)", "mh_mc turned casual rpocket md", "mod_assets/dh1.png", "mod_assets/chibi/empyre.png", "mod_assets/chibi/empyre1.png"),
    BioCharacter("CPC", "full name 'cringe potato chip,' cpc objectively has one of the lowest iq levels out of anyone in the ddmc. he insists that he is kotonoha's partner, and in his free time he enjoys working on his ddlc mods and making music. (we have no idea how he got into either deceptive hearts mod, we didn't even write him into it. he just showed up and started telling us about the fitness gram pacer test)\n\n'take care of yourself, kid. 'cause someone really cares about you.'", "{i}DDMC Celebration{/i} (2023)\n{i}Silver and Emerald{/i} (2024)\n{i}Her Story{/i} (2024)", "kotonoha toward winter surp lchest", "mod_assets/dh1.png", "mod_assets/chibi/cpc.png", "mod_assets/chibi/cpc1.png"),
    BioCharacter("M3rc", "A very talented coder who has made his way through modding. Once stayed up until 4am to watch a stream of the original mod.\n\n'Guess I'm not sleeping tonight.'", "{i}Broken Poet: Act 1{/i} (2024)\n{i}Cardboard Box{/i} (2024)\n{i}Yuri Gets a Haircut{/i} (2024)", "chadmc cross winter lsur", "mod_assets/dh1.png", "mod_assets/chibi/merc.png", "mod_assets/chibi/merc1.png"),
    BioCharacter("Legend", "Resident Persona addict, as he is up there in hours with Spirit.\n\n'Codex Biden allegations.'", "{i}Future Mod{/i} (2100)", "skinny_mc turned happ om4", "mod_assets/logo.png", "mod_assets/chibi/legend.png", "mod_assets/chibi/legend.png"),
    BioCharacter("Phoenix", "Joining the DDMC in mid 2023, Phoenix is known for his discussions regarding Christianity and being a member of the DDMC's Committee.\n\nJohn 3:16: 'For God so loved the world, that He gave his only Son, that whoever believes in Him should not perish but have eternal life.'", "No mods, but rest assured, he's a cool dude.", "phoenix 3q", "mod_assets/logo.png", "mod_assets/chibi/phoenix.png", "mod_assets/chibi/phoenix1.png"),
    BioCharacter("Chillington", "Chillington, a new DDLC fan, quickly took to the challenge of modding the game and is now going through the ups and downs of learning RenPy.\n\n'Did you know I'm 6'4?'", "No mods, but rest assured, he's a cool dude.", "dadsuki turned curi", "mod_assets/logo.png", "mod_assets/chibi/chillington.png", "mod_assets/chibi/chillington1.png"),
    BioCharacter("Braethan", "Admin of DDMC, few know his whereabouts.\n\n'John Madden.'\n\nHi, I'm Saul Goodman. Did you know that you have rights? The constitution says you do! And so do I. Conscience gets expensive, doesn't it? For a substantial fee, and I do mean substantial, you and your loved ones can vanish. Untraceable. I want it in a money order and make it out to Ice Station Zebra Associates. That's my loan out. It's totally legit … it's done just for tax purposes. After that we can discuss Visa or Mastercard, but definitely not American Express, so don't even ask, all right? You're a high-risk client. You're gonna need the deluxe service. It's gonna cost you. If you're committed enough, you can make any story work. I once told a woman I was Kevin Costner, and it worked because I believed it. I never should have let my dojo membership run out. Better safe than sorry. That's my motto. As to your dead guy, occupational hazard. Drug dealer getting shot? I'm gonna go out on a limb here and say it's been known to happen. Don't drink and drive, but if you do, call me.", "No mods, but rest assured, he's a cool dude.", "saul turned circus laug", "mod_assets/dh1.png", "mod_assets/chibi/brae.png", "mod_assets/chibi/brae1.png"),
    BioCharacter("Gubbey", "Lurks around in chat waiting for the unsuspecting chatter to say 'stuff.'\n\n'I'm stuff.'", "{i}Downpour{/i} (2023)", "dpmc 1l", "mod_assets/dh1.png", "mod_assets/chibi/gubbey.png", "mod_assets/chibi/gubbey1.png"),
    BioCharacter("Doomslayer", "Reads {i}Berserk{/i} and {i}Chainsaw Man{/i}. Probably has also played {i}Doom{/i} at some point.\n\n'Eminem being real quite since midlicker dropped.'\n\n'Nah, I'd win.'", "No mods, but rest assured, he's a cool dude.", "doomslayer 1a", "mod_assets/dh1.png", "mod_assets/chibi/doom.png", "mod_assets/chibi/doom1.png"),
    BioCharacter("Shane", "The newest member to join the DDMC, He currently owns a metal pipe shop and sinks every ship he's in/near… Originally started because he wanted to throw his hat into the ring of modding… When he's not chatting on the phone he hates to type on, he writes and listens to music… Notably rock and metal bands… He's alright with mostly everyone although he has mood swings on occasion… In short, just be patient,  don't hold grudges or think you are better than everyone else and you'll be fine…\n\n'Cheese, the solution to every problem!.'", "{i}Manifested Nightmares{/i} (Future)", "amy cross casual lsur", "mod_assets/logo.png", "mod_assets/chibi/shane.png", "mod_assets/chibi/shane1.png"),
    BioCharacter("Uzumaki", "A regular civilian in DDMC. He just likes to hang out and chill. He's trying to make his own mod, but is the biggest procrastinator on Earth.\n\n'Ugh, I'll just start writing it tomorrow.'", "{i}See You Again{/i} (Future)", "harumi 2q", "mod_assets/logo.png", "mod_assets/chibi/uzumaki.png", "mod_assets/chibi/uzumaki1.png"),
    BioCharacter("MGT", "Local SilvaGunner resident and meme maker, MGT has made his way into the modding scene and has gotten involved in a few mods himself.\n\n'Yeah he deserves another discord nitro scam for his fragile soul.'", "{i}Natsuki Becomes President of the United States{/i} (2023)", "mgt 1a", "mod_assets/dh1.png", "mod_assets/chibi/mgt.png", "mod_assets/chibi/mgt1.png"),
    BioCharacter("Leomonade", "beware of his cooking, extremely dangerous to those who are weak\n\n'I am the one who makes god pray.'", "No mods, but rest assured, he's a cool dude.", "wallace turned casual yand", "mod_assets/logo.png", "mod_assets/chibi/leo.png", "mod_assets/chibi/leo1.png"),
    BioCharacter("SoVeryTired", "SoVeryTired first played DDLC in 2021 and it continues to feed off his imagination like a parasite. One of the co-writers of 2022's Grappling Hook Yuri mod, he is working towards finishing up a DDLC x Jurassic Park mod ONCE HE GETS MORE THAN ONE MINUTE ALONE TO HIMSELF TO WRITE AND CODE SERIOUSLY IT'S BEEN YEARS AT THIS POINT.\n\n'Only three things in life are certain: Death, taxes and my ability to procrastinate.'", "{i}Grappling Hook Yuri: The Origin Arc{/i} (2022)\n{i}Jurassic Park{/i} (Future)", "soverytired 1b", "mod_assets/logo.png", "mod_assets/chibi/svt2.png", "mod_assets/chibi/svt2.png"),
    BioCharacter("SamyBallin", "ripped straight out from the dream of a wannabe cool boy roblox player, Jake was born in the creative world of a roleplaying game.\n\n'wsg y'all, check out my insta ahaha.'", "{i}Unnamed Mod{/i} (Future)", "sammy 1a", "mod_assets/logo.png", "mod_assets/chibi/samyballin.png", "mod_assets/chibi/samyballin1.png"),
    BioCharacter("Billy", "Idk just put black as my bio or smth\n\n'Fuck it, we ball.'", "{i}Jacking a Box{/i} (2024)\n{i}Sayori's Kitchen Tale{/i} (2024)\n{i}Point of You{/i} (Future)", "miyuki turned winter peace rhip mc ef", "mod_assets/logo.png", "mod_assets/chibi/billy.png", "mod_assets/chibi/billy1.png"),
    BioCharacter("Soldi", "A calm, yet a shy person who still thinks everything is new around. Sometimes kind of an idiot, but he's made a long journey during modding...and now, he's decided to try something new.\n\n'Peck.'", "{i}Prison Architect{/i} (Unavailable)\n{i}Sunshine Days!{/i} (Future)", "amaya 1b", "mod_assets/logo.png", "mod_assets/chibi/soldi.png", "mod_assets/chibi/soldi1.png"),
    BioCharacter("Akai", "Akai, a being who acts childishly for his age. Likes to use ':3' in his chats.\n\n'Hi :3.'", "{i}100 Club Members Who Really Love You S1{/i} (Ongoing)", "chitoge turned lbehind ma ee bb", "mod_assets/logo.png", "mod_assets/chibi/akai.png", "mod_assets/chibi/akai1.png"),
    BioCharacter("BrysonBruv", "Bryson_bruv is so skibidi as they say, and isn't a woman despite having a female avatar and such, watch serial experiments lain bye\n\n'When I fannum, she taxes on my gyatt till I skibidi only in Ohio would I leave skibyori hanging just gyattika if I do say so my myself'", "{i}Brainrot Club{/i} (2024)\n{i}Brainrot Club 2: Redux/Remaster{/i} (2024)\n{i}Brainrot Club 3{/i} (Future)", "bryson 1a", "mod_assets/logo.png", "mod_assets/chibi/bryson.png", "mod_assets/chibi/bryson.png"),
    BioCharacter("LueckBoiii", "Lueckboiii plays mods. Lots of mods. He's played tons of them, his favorite being Night Rain. Other than that, he likes Nirvana.\n\n'Those who know:'", "{i}Brainrot Club{/i} (2024)\n{i}Brainrot Club 2: Redux/Remaster{/i} (2024)\n{i}Brainrot Club 3{/i} (Future)", "lueck 1a", "mod_assets/logo.png", "mod_assets/chibi/lueck.png", "mod_assets/chibi/lueck.png"),
    BioCharacter("Aahilj", "A new mod maker who managed to create 5 mods in 3 months, and won't stop anytime soon.\n\n'I'm a DDLC modder, not a DDLC fan'", "{i}Act 4 Plus{/i} (2024)\n{i}Collapse Demo{/i} (2024)\n{i}Shyness and Confidence Demo{/i} (2024)", "aahilj 1a", "mod_assets/logo.png", "mod_assets/chibi/aahilj.png", "mod_assets/chibi/aahilj1.png"),
    BioCharacter("NekoLaiS", "Russian programmer and member of the Elysium Team.\n\n'Spent most of my time in the Russian sigment of the fandom, but relatively recently came to the English sigment.'", "{i}World of Dreams{/i} (2019-Now)\n{i}HCCH{/i} (2022)\n{i}Survival Club{/i} (Future)", "nekolais 1", "mod_assets/logo.png", "mod_assets/chibi/neko.png", "mod_assets/chibi/neko.png"),
    BioCharacter("Atazoth", "Starting his Journey through ddlc when he got whooping cough, Atazoth now dedicates his free time to DDMC and a bunch of virtual girls.\n\n'Throughout The clubroom and comedy channel, I alone am the Sayori one.'", "{i}Thoughts of Pink and Yellow{/i} (2024)\n{i}Forgotten Love{/i} (2024)", "atazoth 1a", "mod_assets/logo.png", "mod_assets/chibi/atazoth.png", "mod_assets/chibi/atazoth.png"),
    BioCharacter("CoolDigger", "The best backup one could ask for.\n\n'...'", "No mods, but rest assured, he's a cool dude.", "elyssa turned lab doub", "mod_assets/logo.png", "mod_assets/chibi/cool.png", "mod_assets/chibi/cool1.png"),
    BioCharacter("iiTzWolfyy", "Having discovered DDLC in the end of 2022, he learned the Ren'Py language to make mods, but has mostly helped the DDMC community with their issues. Has quite a lot of ambition, but is too lazy to really do anything nowadays, especially working on his mod...\n\n'The most striking scars are the ones hiding the deepest wounds.'", "{i}The Renewal{/i} (2023-20??)\n{i}Deceptive Hearts{/i} (2024)", "nastya cross sweater happ om ce", "mod_assets/dh1.png", "mod_assets/chibi/wolfyy.png", "mod_assets/chibi/wolfyy1.png"),
    BioCharacter("Codex", "Finding DDLC in 2021, Codex, has made his way through modding and made many friends along the way.\n\n'All Dokis are mid.'", "{i}Exit Spoof{/i} (2023)\n{i}Deceptive Hearts{/i} (2024)\n{i}Deceptive Hearts 2{/i} (2025)", "sayonika turned winter lpoint eh mb", "mod_assets/dh1.png", "mod_assets/chibi/codex.png", "mod_assets/chibi/codex1.png")
]

default index = 0
default current_character = characters[index]

init -5 python:
    def update_character(new_index):
        store.index = new_index
        store.current_character = characters[new_index]

transform single_chibi:
    easein_quad 0.12 yoffset -30
    easeout_quad 0.12 yoffset 0
    easein_quad 0.12 yoffset -30
    easeout_quad 0.12 yoffset 0
    repeat

transform both_chibis:
    easein_quad 0.12 yoffset -30
    easeout_quad 0.12 yoffset 0
    easein_quad 0.12 yoffset -30
    easeout_quad 0.12 yoffset 0
    repeat

screen bio_screen:
    tag menu

    add "mod_assets/bg.jpg"

    vbox: # Character name, logo, and chibi
        xalign 0.1
        yalign 0.1
        spacing 10
        text "[current_character.name]" style "character_name_title" xalign 0.5
        null height 5
        add current_character.logo xalign 0.5 size(300, 300)
        null height 30
        if current_character.chibi is not None:
            imagebutton:
                xalign 0.5
                action NullAction()
                idle current_character.chibi
                if current_character.chibi_hover is None:
                    at transform:
                        xalign 0.5
                        on hover:
                            single_chibi
                        on idle:
                            easeout_quad .1 yoffset 0
                else:
                    hover current_character.chibi_hover
                    at transform:
                        xalign 0.5
                        on hover:
                            both_chibis
                        on idle:
                            easeout_quad .1 yoffset 0

    vbox: # Main sprite and arrows underneath
        xalign 0.4 yalign 0.5
        add current_character.image xalign 0.0 yalign 0.6 zoom 0.5

        # Nav buttons
        hbox:
            style_prefix "arrows"

            xalign 0.5
            yalign 0.97
            spacing 20

            textbutton "<" action If(
                index > 0, 
                true=Function(update_character, index - 1), 
                false=Function(update_character, len(characters) - 1)
            )

            text [current_character.name] style "character_name_style"

            textbutton ">" action If(
                index < len(characters) - 1, 
                true=Function(update_character, index + 1), 
                false=Function(update_character, 0)
            )

    null width 30

    # Bio section
    frame:
        background "mod_assets/bio_box.png"
        xalign 1
        yalign 0.4
        padding (790, 130, 160, 220)
        vbox: # Character info
            xfill True
            box_wrap True
            viewport:
                scrollbars "vertical"
                mousewheel True
                draggable True
                text "[current_character.bio]" size 22 justify True

    frame: # Previous apperances
        background None
        xalign 1
        yalign 0.4
        padding (790, 455, 160, 10)
        vbox:
            xfill True
            box_wrap True
            text "[current_character.appear]" size 16 justify True


    textbutton _("Return"):
        style "return_button"

        action Return()

style character_name_style:
    font "mod_assets/fonts/SometypeMono-VariableFont_wght.ttf"
    color "#fff"
    outlines [(4, text_outline_color, 0, 0), (2, text_outline_color, 2, 2)]

style character_name_title is character_name_style:
    size 45 
    xalign 0.5

style arrows_button is gui_button
style arrows_button_text is gui_button_text

style arrows_button:
    size_group "arrows"
    properties gui.button_properties("arrows_button")

style arrows_button_text:
    properties gui.button_text_properties("arrows_button")
    font "mod_assets/fonts/SometypeMono-VariableFont_wght.ttf"
    color "#fff"
    outlines [(4, text_outline_color, 0, 0), (2, text_outline_color, 2, 2)]
    hover_outlines [(4, "#fac", 0, 0), (2, "#fac", 2, 2)]