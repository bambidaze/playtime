image video1 = Movie(size = (1280,720), channel="movie", play="video/pavlovssis.webm")
image video2 = Movie(size = (1280,720), channel="movie", play="video/BambiInTheBox.webm")
image video4 = Movie(size = (1280,720), channel="movie", play="video/hellosissy.webm")
image video5 = Movie(size = (1280,720), channel="movie", play="video/brainwasher.webm")
image BG pink = "bg pink.jpg"
image splash = "credits.png"
init python:
    config.default_fullscreen = True
    done = "images/done.png"
    path = ""
    playingpoint = 0
    playingcode = 0

    class Song:
        def __init__(self, name, file, length):
            self.name = name
            self.file = file
            self.length = length
            self.has_played = False

    class Playlist:
        def __init__(self, name, list):
            self.name = name;
            self.list = list;
            self.has_played = False

        def hasplayed(self):
            #   self.has_played = True # For testing purposes :3
            if(self.has_played == True) :
                final = done
            else :
                final = "images/"+self.name+".png"
            return final

    def weekPlayed(songlist,week):
        final = done
        test = True
        for song in songlist:
            if song.has_played == False :
                final = "images/"+week+".png"
                break
        return final

    def calculate_start(song) :
        pausepoint = renpy.music.get_pos(channel="music")
        renpy.music.set_pause("True")
        playingcode = 3
        return pausepoint
        #return song.length - (song.length-pausepoint)
default persistent.master_volume = 0.5
define config.rollback_enabled = False
define config.developer = True

    ############################ BAMBI BIMBODOLL CONDITIONNING Audio Files #####################################
default Rapid_Induction = Song("Rapid Induction", "audio/Bambi Bimbodoll Conditionning/00 Rapid Induction.mp3",162.0)
default Bubble_Induction = Song("Bubble Induction", "audio/Bambi Bimbodoll Conditionning/01 Bubble Induction.mp3",1049.0)
default Bubble_Acceptance = Song("Bubble Acceptance", "audio/Bambi Bimbodoll Conditionning/02 Bubble Acceptance.mp3",1734.0)
default Named_And_Drained = Song("Bambi Named and drained", "audio/Bambi Bimbodoll Conditionning/03 Bambi Named and Drained.mp3",949.0)
default IQ_Lock = Song("Bambi IQ Lock", "audio/Bambi Bimbodoll Conditionning/04 Bambi IQ Lock.mp3",726.0)
default Body_Lock = Song("Bambi Body Lock", "audio/Bambi Bimbodoll Conditionning/05 Bambi Body Lock.mp3",908.0)
default Attitude_Lock = Song("Bambi Attitude Lock", "audio/Bambi Bimbodoll Conditionning/06 Bambi Attitude Lock.mp3",839.0)
default Bambi_Uniformed = Song("Bambi Uniformed", "audio/Bambi Bimbodoll Conditionning/07 Bambi Uniformed.mp3",815.0)
default Bambi_Takeover = Song("Bambi Takeover", "audio/Bambi Bimbodoll Conditionning/08 Bambi Takeover.mp3",625.00)
default Bambi_Cockslut = Song("Bambi Cockslut", "audio/Bambi Bimbodoll Conditionning/09 Bambi Cockslut.mp3",1081.00)
default Bambi_Awakens = Song("Bambi Awakens", "audio/Bambi Bimbodoll Conditionning/10 Bambi Awakens.mp3",592.0)


    ############################ BAMBI TRAINING LOOPS Audio Files #####################################
default Control_Loop_Barbie = Song("Control Loop - Barbie", "audio/Bambi Training Loops/Control Loop - Barbie.mp3",329.0)
default Control_Loop_Bimbo = Song("Control Loop - Bimbo", "audio/Bambi Training Loops/Control Loop - Bimbo.mp3",329.0)
default Control_Loop_Doll = Song("Control Loop - Doll", "audio/Bambi Training Loops/Control Loop - Doll.mp3",734.0)
default Control_Loop_Puppet = Song("Control Loop - Puppet", "audio/Bambi Training Loops/Control Loop - Puppet.mp3",594.0)
default Sleep_Loop = Song("Sleep Loop", "audio/Bambi Training Loops/Sleep Loop.mp3",907.0)
default Training_Loop_Cockslut = Song("Training Loop - Cockslut", "audio/Bambi Training Loops/Training Loop - Cockslut.mp3",491.0)
default Training_Loop_Fuckhole = Song("Training Loop - Fuckhole", "audio/Bambi Training Loops/Training Loop - Fuckhole.mp3",480.0)
default Training_Loop_Subliminal = Song("Training Loop - Subliminal", "audio/Bambi Training Loops/Training Loop - Subliminal.mp3",480.0)

    ############################ BAMBI FUCKDOLL BRAINWASH Audio Files #####################################
default Blank_Mindless_Doll = Song("Blank Mindless Doll", "audio/Bambi Fuckdoll Brainwash/01 Blank Mindless Doll.mp3",1270.0)
default Cock_Dumb_Hole = Song("Cock Dumb Hole", "audio/Bambi Fuckdoll Brainwash/02 Cock Dumb Hole.mp3",552.0)
default Uniform_Slut_Puppet = Song("Uniform Slut Puppet", "audio/Bambi Fuckdoll Brainwash/03 Uniform Slut Puppet.mp3",570.0)
default Vain_Horny_Happy = Song("Vain Horny Happy", "audio/Bambi Fuckdoll Brainwash/04 Vain Horny Happy.mp3",656.0)
default Bimbo_Drift = Song("Bimbo Drift", "audio/Bambi Fuckdoll Brainwash/05 Bimbo Drift.mp3",308.0)

    ############################ BAMBI FUCKTOY FANTASY Audio Files #####################################
default Blowup_Pleasure_Toy = Song("Blowup Pleasure Toy", "audio/Bambi Fucktoy Fantasy/01 Blowup Pleasure Toy.mp3",1192.0)
default Perfect_Bimbo_Maid = Song("Perfect Bimbo Maid", "audio/Bambi Fucktoy Fantasy/02 Perfect Bimbo Maid.mp3",1172.0)
default Restrained_And_Milked = Song("Restrained and Milked", "audio/Bambi Fucktoy Fantasy/03 Restrained and Milked.mp3",1140.0)

    ############################ BAMBI FUCKTOY SUBMISSION Audio Files #####################################
default Bimbo_Giggletime = Song("Bimbo Giggletime", "audio/Bambi Fucktoy Submission/01 Bimbo Giggletime.mp3",860.0)
default Mindlocked_Cock_Zombie = Song("Mindlocked Cock Zombie", "audio/Bambi Fucktoy Submission/02 Mindlocked Cock Zombie.mp3",976.0)

    ############################ BAMBI FUCKPUPPET FREEDOM Audio Files #####################################
default Fake_Plastic_Fuckpuppet = Song("Fake Plastic Fuckpuppet", "audio/Bambi Fuckpuppet Freedom/01 Fake Plastic Fuckpuppet.mp3",916.0)
default Designer_Pleasure_Puppet = Song("Designer Pleasure Puppet", "audio/Bambi Fuckpuppet Freedom/02 Designer Pleasure Puppet.mp3",924.0)
default Bimbo_Fuckpuppet_Oblivion = Song("Bimbo Fuckpuppet Oblivion", "audio/Bambi Fuckpuppet Freedom/03 Bimbo Fuckpuppet Oblivion.mp3",2054.0)

    ############################ BAMBI ENFORCEMENT Audio Files #####################################
default Bimbo_Drone = Song("Bimbo Drone", "audio/Bambi Enforcement/00 Bimbo Drone.mp3",122.0)
default Bimbo_Relaxation = Song("Bimbo Relaxation", "audio/Bambi Enforcement/01 Bimbo Relaxation.mp3",252.0)
default Bimbo_Mindwipe = Song("Bimbo Mindwipe", "audio/Bambi Enforcement/02 Bimbo Mindwipe.mp3",210.0)
default Bimbo_Slumber = Song("Bimbo Slumber", "audio/Bambi Enforcement/03 Bimbo Slumber.mp3",332.0)
default Bimbo_Tranquility = Song("Bimbo Tranquility", "audio/Bambi Enforcement/04 Bimbo Tranquility.mp3",358.0)
default Bimbo_Pride = Song("Bimbo Pride", "audio/Bambi Enforcement/05 Bimbo Pride.mp3",462.0)
default Bimbo_Pleasure = Song("Bimbo Pleasure", "audio/Bambi Enforcement/06 Bimbo Pleasure.mp3",492.0)
default Bimbo_Servitude = Song("Bimbo Servitude", "audio/Bambi Enforcement/07 Bimbo Servitude.mp3",572.0)
default Bimbo_Addiction = Song("Bimbo Addiction", "audio/Bambi Enforcement/08 Bimbo Addiction.mp3",598.0)
default Bimbo_Amnesia = Song("Bimbo Amnesia", "audio/Bambi Enforcement/09 Bimbo Amnesia.mp3",728.0)
default Bimbo_Protection = Song("Bimbo Protection", "audio/Bambi Enforcement/10 Bimbo Protection.mp3",520.0)

    ########################### Bimbo4Eva Audio Files ##################################
default Bambi_Forever_Wipers = Song("Bambi Forever w", "audio/bambi4eva/Bambi_Forever_wipers.mp3",1469.0)
default Bambis_Dreamhouse_Wipers = Song("Bambi's Dreamhouse w", "audio/bambi4eva/Bambis_Dreamhouse_wipers.mp3",1367.0)
default Bimbo_Night_Night_Wipers = Song("Bimbo Night Night w", "audio/bambi4eva/Bimbo_Night_Night_wipers.mp3",1488.0)
default Bambi_Forever = Song("Bambi Forever", "audio/bambi4eva/Bambi_Forever.mp3",1469.0)
default Bambis_Dreamhouse = Song("Bambi's Dreamhouse", "audio/bambi4eva/Bambis_Dreamhouse.mp3",1367.0)
default Bimbo_Night_Night = Song("Bimbo Night Night", "audio/bambi4eva/Bimbo_Night_Night.mp3",1488.0)

    ########################### Bimbo University Audio Files ##################################

default BU_Dumb_Bitch = Song("Dumb Bitch", "audio/Bimbo University/Dumb Bitch - Bimbo Euphoria - Bimbo University.mp3",487.0)
default BU_Public_Slut = Song("Public Slut", "audio/Bimbo University/Public Slut - Bimbo Euphoria series.mp3",1229.0)

    ############################ BAMBI MENTAL MAKEOVER Audio Files #####################################
default Sleepygirl_Salon = Song("Sleepygirl Salon", "audio/Bambi Mental Makeover/01 Sleepygirl Salon.mp3",704.0)
default Mentally_Platinum_Blonde = Song("Mentally Platinum Blonde", "audio/Bambi Mental Makeover/02 Mentally Platinum Blonde.mp3",944.0)
default Automatic_Airhead = Song("Automatic Airhead", "audio/Bambi Mental Makeover/03 Automatic Airhead.mp3",956.0)
default Superficial_Basic_Bitch = Song("Superficial Basic Bitch", "audio/Bambi Mental Makeover/04 Superficial Basic Bitch.mp3",1922.0)
default Life_Control_Total_Doll= Song("Life Control : Total Doll", "audio/Bambi Mental Makeover/05 Life Control : Total Doll.mp3",1815.0)
default Makeover_Awakener = Song("Makeover Awakener", "audio/Bambi Mental Makeover/07 Makeover Awakener.mp3",328.0)


    ############################ BAMBI PUPPET PRINCESS LOOPS Audio Files #####################################
default Sleepyhead = Song("Sleepyhead", "audio/Bambi Puppet Princess Loops/01 Sleepyhead.mp3",490.0)
default Bobblehead = Song("Bobblehead", "audio/Bambi Puppet Princess Loops/02 Bobblehead.mp3",470.0)
default Bambidoll = Song("Bambidoll", "audio/Bambi Puppet Princess Loops/03 Bambidoll.mp3",330.0)


############################################           PLAYLISTS                 #####################################################


########################### Playlists by Day #####################################
default day_1 = Playlist("day1",[Bubble_Induction, Bubble_Acceptance, Named_And_Drained, IQ_Lock, Bambi_Awakens])
default day_2 = Playlist("day2",[Bubble_Induction, Bubble_Acceptance, Named_And_Drained, Body_Lock, Bambi_Awakens])
default day_3 = Playlist("day3",[Bimbo_Fuckpuppet_Oblivion, Bubble_Acceptance, Named_And_Drained, Attitude_Lock, Bambi_Awakens])

default day_4 = Playlist("day4",[Rapid_Induction, Bubble_Acceptance, Named_And_Drained, IQ_Lock, Bambi_Uniformed, Bambi_Awakens])
default day_5 = Playlist("day5",[Rapid_Induction, Bubble_Acceptance, Named_And_Drained, Body_Lock, Bambi_Takeover, Bambi_Awakens])
default day_6 = Playlist("day6",[Rapid_Induction, Bubble_Acceptance, Named_And_Drained, Attitude_Lock, Bambi_Cockslut, Bambi_Awakens])

default day_7 = Playlist("day7",[Rapid_Induction, Named_And_Drained, IQ_Lock, Body_Lock, Attitude_Lock, Bambi_Cockslut, Bambi_Awakens])
default day_8 = Playlist("day8",[Rapid_Induction, Named_And_Drained, Attitude_Lock, Bambi_Uniformed, Bambi_Takeover, Bambi_Cockslut, Bambi_Awakens])

default day_9 = Playlist("day9",[Control_Loop_Barbie, Blank_Mindless_Doll, Cock_Dumb_Hole, Bimbo_Giggletime, Bimbo_Drift])
default day_10 = Playlist("day10",[Control_Loop_Bimbo, Blank_Mindless_Doll, Uniform_Slut_Puppet, Mindlocked_Cock_Zombie, Bimbo_Drift])

default day_11 = Playlist("day11",[Blank_Mindless_Doll, Fake_Plastic_Fuckpuppet, Vain_Horny_Happy, Bimbo_Drift])
default day_12 = Playlist("day12",[Blank_Mindless_Doll, Cock_Dumb_Hole, Designer_Pleasure_Puppet, Bambi_Awakens])
default day_13 =  Playlist("day13",[Bimbo_Drone, Bimbo_Fuckpuppet_Oblivion, Uniform_Slut_Puppet, Vain_Horny_Happy, Bimbo_Drift])

default day_14 = Playlist("day14",[Bimbo_Drone, Bimbo_Relaxation, Bimbo_Tranquility, Cock_Dumb_Hole, Bimbo_Servitude, Bimbo_Slumber, Blowup_Pleasure_Toy, Bimbo_Amnesia, Bimbo_Drift])
default day_15 = Playlist("day15",[Bimbo_Drone, Bimbo_Relaxation, Bimbo_Mindwipe, Bimbo_Pride, Uniform_Slut_Puppet, Bimbo_Addiction, Bimbo_Slumber, Perfect_Bimbo_Maid, Bimbo_Protection, Bimbo_Drift])
default day_16 = Playlist("day16",[Bimbo_Drone, Bimbo_Relaxation, Bimbo_Mindwipe, Bimbo_Pleasure, Vain_Horny_Happy, Bimbo_Servitude, Bimbo_Slumber, Restrained_And_Milked, Bimbo_Amnesia, Bimbo_Drift])

default day_17 = Playlist("day17",[Bimbo_Drone, Bimbo_Slumber, Bimbo_Tranquility, Fake_Plastic_Fuckpuppet, Bimbo_Addiction, Bimbo_Pride, Bimbo_Giggletime, Bimbo_Amnesia, Bambi_Awakens])
default day_18 = Playlist("day18",[Bimbo_Drone, Bimbo_Slumber, Bimbo_Tranquility, Designer_Pleasure_Puppet, Bimbo_Servitude, Bimbo_Pleasure, Mindlocked_Cock_Zombie, Bimbo_Protection, Bimbo_Drift])
default day_19 = Playlist("day19",[Blank_Mindless_Doll, Vain_Horny_Happy, Bimbo_Fuckpuppet_Oblivion, Bimbo_Mindwipe, Cock_Dumb_Hole, Bimbo_Giggletime, Bimbo_Amnesia, Bimbo_Protection, Bimbo_Drift])

default day_20 = Playlist("day20",[Sleepygirl_Salon, Mentally_Platinum_Blonde, Automatic_Airhead, Superficial_Basic_Bitch, Makeover_Awakener])

############################        OFFICIAL PLAYLISTS    ############################
default deep_trance_programming = Playlist("deeptrance",[Blank_Mindless_Doll, Bimbo_Tranquility, Bimbo_Pleasure, Bimbo_Slumber, Bimbo_Amnesia, Bimbo_Drift])
default personality_programming = Playlist("personality",[Bimbo_Drone, Bimbo_Slumber, Bimbo_Mindwipe, Bimbo_Pleasure, Bimbo_Fuckpuppet_Oblivion, Bimbo_Amnesia, Bimbo_Drift])
default iq_programming = Playlist("iq",[Blank_Mindless_Doll, Cock_Dumb_Hole, Bimbo_Pride, Bimbo_Giggletime, Restrained_And_Milked, Bimbo_Drift])
default attitude_programming = Playlist("attitude",[Bimbo_Drone, Bimbo_Relaxation, Bimbo_Slumber, Fake_Plastic_Fuckpuppet, Vain_Horny_Happy, Bimbo_Pride, Designer_Pleasure_Puppet, Bimbo_Drift])
default takeover_programming = Playlist("takeover",[Blank_Mindless_Doll, Vain_Horny_Happy, Bimbo_Fuckpuppet_Oblivion, Bimbo_Mindwipe, Cock_Dumb_Hole, Bimbo_Giggletime, Bimbo_Addiction, Bimbo_Amnesia, Bimbo_Protection,  Bimbo_Drift])
default cockslut_programming = Playlist("cockslut",[Blank_Mindless_Doll, Bimbo_Tranquility, Fake_Plastic_Fuckpuppet, Bimbo_Pleasure, Uniform_Slut_Puppet, Bimbo_Servitude, Mindlocked_Cock_Zombie, Bimbo_Drift])
default uniform_programming = Playlist("uniform",[Blank_Mindless_Doll, Uniform_Slut_Puppet, Designer_Pleasure_Puppet, Bimbo_Addiction, Bimbo_Protection, Bimbo_Drift])
default maid_programming = Playlist("maid",[Bimbo_Drone, Bimbo_Relaxation, Bimbo_Tranquility, Bimbo_Pleasure, Uniform_Slut_Puppet, Perfect_Bimbo_Maid, Bimbo_Servitude, Bimbo_Addiction, Bimbo_Drift])

############################ Beginner Bambis PLAYLISTS #####################################
default bambi_starter = Playlist("starter",[Bubble_Induction, Bubble_Acceptance, Named_And_Drained, Bambi_Awakens])
default bambi_conditioner = Playlist("conditioner",[Bubble_Induction, Named_And_Drained, IQ_Lock, Body_Lock, Attitude_Lock, Bambi_Awakens])
default bambi_reinforcement = Playlist("reinforcement",[Bubble_Induction, Named_And_Drained, Bambi_Uniformed, Bambi_Takeover, Bambi_Cockslut, Bambi_Awakens])
default bambi_enforcement = Playlist("reinforcement",[Bimbo_Drone, Bimbo_Relaxation, Bimbo_Mindwipe, Bimbo_Slumber, Bimbo_Tranquility, Bimbo_Pride, Bimbo_Amnesia, Bimbo_Servitude, Bimbo_Addiction, Bimbo_Pleasure, Bambi_Awakens])
default bambi_mental_makeover = Playlist("mental_makeover",[Sleepygirl_Salon, Mentally_Platinum_Blonde, Automatic_Airhead, Makeover_Awakener])


############################ The Ten Day Program PLAYLISTS #####################################
default ten_day_day_1 = Playlist("Day 1/10",[Bubble_Induction, Bubble_Acceptance, Named_And_Drained, Bambi_Awakens])
default ten_day_day_2 = Playlist("Day 2/10",[Bubble_Induction, Bubble_Acceptance, Named_And_Drained, Bambi_Awakens])
default ten_day_day_3 = Playlist("Day 3/10",[Bubble_Induction, Bubble_Acceptance, Named_And_Drained, Bambi_Awakens])
default ten_day_day_4 = Playlist("Day 4/10",[Rapid_Induction, Bubble_Acceptance, Named_And_Drained, Bambi_Awakens])
default ten_day_day_5 = Playlist("Day 5/10",[Rapid_Induction, Named_And_Drained, Body_Lock, Bambi_Awakens])
default ten_day_day_6 = Playlist("Day 6/10",[Rapid_Induction, Body_Lock, Attitude_Lock, Bambi_Awakens])
default ten_day_day_7 = Playlist("Day 7/10",[Rapid_Induction, IQ_Lock, Attitude_Lock, Bambi_Uniformed])
default ten_day_day_8 = Playlist("Day 8/10",[Rapid_Induction, Named_And_Drained, Attitude_Lock, Bambi_Uniformed, Bambi_Takeover])
default ten_day_day_9 = Playlist("Day 9/10",[Rapid_Induction, Attitude_Lock, Bambi_Takeover, Bambi_Cockslut, Bambi_Awakens])
default ten_day_day_10 = Playlist("Day 10/10",[Rapid_Induction, Bambi_Takeover, Bambi_Cockslut, Bambi_Awakens])


############################ Bambi Refresher PLAYLISTS #####################################
default bambi_refresher = Playlist("Bambi Refresher",[Bimbo_Drone, Bubble_Induction, Bimbo_Drift, Named_And_Drained, Bimbo_Tranquility, Bambi_Takeover, Bambi_Awakens])

############################ BAMBI Day Off Loops PLAYLISTS #####################################

default day_off_1 = Playlist("Day Off 1",[Bambidoll, Bimbo_Tranquility, Bimbo_Pride, Control_Loop_Doll, Control_Loop_Barbie])
default day_off_2 = Playlist("Day Off 2",[Bobblehead, Bimbo_Servitude, Control_Loop_Puppet, Control_Loop_Bimbo])

    ################################# User Playlists #####################################
default Mindblower = Playlist("mindblower",[Rapid_Induction, Bimbo_Pleasure, Training_Loop_Fuckhole, Bambi_Cockslut, Restrained_And_Milked, Bimbo_Amnesia, Bambi_Awakens])
default Bambitime = Playlist("Bambi Time",[Bimbo_Drone,Blank_Mindless_Doll, Mindlocked_Cock_Zombie, Vain_Horny_Happy, Fake_Plastic_Fuckpuppet, Designer_Pleasure_Puppet, Bimbo_Fuckpuppet_Oblivion, Bimbo_Addiction, Bimbo_Protection, Bimbo_Drift])
default the_new_standard = Playlist("The New Standard",[Rapid_Induction, Bimbo_Slumber, Sleepyhead, Bimbo_Pleasure, Bimbo_Mindwipe, Bobblehead, Named_And_Drained, Bambidoll, Bambi_Cockslut, Bimbo_Drift])

    ################################# bambi4eva Playlists #####################################
default Bambi4everw = Playlist("Bambi Forever w",[Bambi_Forever_Wipers])
default BimboNightNightw = Playlist("Bimbo Night Night w",[Bimbo_Night_Night_Wipers])
default BambisDreamHousew = Playlist("Bambi's Dream House w",[Bambis_Dreamhouse_Wipers])
default Bambi4ever = Playlist("Bambi Forever",[Bambi_Forever])
default BimboNightNight = Playlist("Bimbo Night Night",[Bimbo_Night_Night])
default BambisDreamHouse = Playlist("Bambi's Dream House",[Bambis_Dreamhouse])

    ################################# Bimbo University Playlists #####################################
default Public_Slut = Playlist("Public Slut",[BU_Public_Slut])
default Dumb_Bitch = Playlist("Dumb Bitch",[BU_Dumb_Bitch])

label start:
    scene BG pink with dissolve
    "Welcome to Bambi Playtime!"
    "This is a playlist player for the Bambi Sleep Program"
    "Whoever you are, where ever you live, I hope this helps you free your inner bimbo"
    "I hope you like it and have heaps of fun using it."
    jump creators_menu

label pavlovssissy:
#    show screen my_scr
    call screen video1
#    hide screen my_scr

label bambiinthebox:
#    show screen my_scr
    call screen video2
#    hide screen my_scr



label hellosissy:
#    show screen my_scr
    call screen video4
#    hide screen my_scr

label brainwasher:
#    show screen my_scr
    call screen video5
#    hide screen my_scr

label splashscreen:
    scene black
    with Pause(1)

    show splash with dissolve
    with Pause(8)

    scene black with dissolve
    with Pause(1)

    return

label creators_menu():
    stop music fadeout 1.0
    hide screen week1 with dissolve
    call screen creators_menu with dissolve

label bambi4eva_menu():
    stop music fadeout 1.0
    hide screen bambi_sleep_playlists_menu with dissolve
    call screen bambi4eva with dissolve

label bu_menu():
    stop music fadeout 1.0
    hide screen bambi_sleep_playlists_menu with dissolve
    call screen bimbouniversity with dissolve

label bu_euphoria_menu():
    stop music fadeout 1.0
    hide screen bambi_sleep_playlists_menu with dissolve
    call screen bu_euphoria with dissolve

label the_new_standard_menu():
    stop music fadeout 1.0
    hide screen bambi_sleep_playlists_menu with dissolve
    call screen the_new_standard_menu with dissolve

label bambi_sleep_playlists_menu():
    stop music fadeout 1.0
    hide screen week1 with dissolve
    call screen bambi_sleep with dissolve

label bambi_sleep():
    stop music fadeout 1.0
    call screen bambi_sleep with dissolve

label twenty_days_weeks_menu():
    stop music fadeout 1.0
    call screen twenty_days_weeks_menu with dissolve

label twenty_days_week1():
    stop music fadeout 1.0
    call screen week1 with dissolve

label twenty_days_week2():
    stop music fadeout 1.0
    call screen week2 with dissolve

label twenty_days_week3():
    stop music fadeout 1.0
    call screen week3 with dissolve

label twenty_days_week4():
    stop music fadeout 1.0
    call screen week4 with dissolve

label twenty_days_week5():
    stop music fadeout 1.0
    call screen week5 with dissolve

label twenty_days_week6():
    stop music fadeout 1.0
    call screen week6 with dissolve

label twenty_days_week7():
    stop music fadeout 1.0
    call screen week7 with dissolve

label twenty_days_week8():
    stop music fadeout 1.0
    call screen week8 with dissolve

label official_playlists():
    stop music fadeout 1.0
    call screen official_playlists_menu with dissolve

label ten_days_menu():
    stop music fadeout 1.0
    call screen ten_days_menu with dissolve

label beginner_bambis_menu():
    stop music fadeout 1.0
    call screen beginner_bambis_menu with dissolve

label bambi_refresher_menu():
    stop music fadeout 1.0
    call screen bambi_refresher_menu with dissolve

label video_menu():
    stop music fadeout 1.0
    call screen video_menu with dissolve

label video1():
    stop music fadeout 1.0
    call screen video1 with dissolve

label video2():
    stop music fadeout 1.0
    call screen video2 with dissolve



label video4():
    stop music fadeout 1.0
    call screen video4 with dissolve

label video5():
    stop music fadeout 1.0
    call screen video5 with dissolve

label mindblower_menu():
    stop music fadeout 1.0
    call screen mindblower_menu with dissolve

label bambi_time_menu():
    stop music fadeout 1.0
    call screen bambi_time_menu with dissolve

label song_player(playlist, screen_end): # Label with a playlist object, and the screen to return to after playing
    $ screenEnd = screen_end # Assign the screen to a python variable
    python: # Creating a zone where we can declare python code
        for song in playlist.list: #For loop with every song in the playlist that we called the function with

            playingcode = 0

            renpy.call_screen("play_song", song)

            while(playingcode != 0) :
                #Calls the play_song screen with the song that we want
                if(playingcode == 1) :

                    playingpoint = renpy.music.get_pos(channel="music")

                    renpy.music.set_pause("True")

                    renpy.call_screen("pause_song")

                    renpy.call_screen("play_song", song, playingpoint)

                if(playingcode == 2) :
                    break

        playlist.has_played = True # After every song has played, says that we have played the playlist
        renpy.retain_after_load() # Dunno if it does anything, gotta test later TwT

        renpy.jump(screen_end) # Goes to the ending screen that we called the function with
