######### Code to play the audio files ###########
screen play_song(song, startpoint = 0):
    on "show" action Play("music", "<from {point}>".format(point = startpoint)+song.file, loop=None
    )
    text "{song_name}".format(song_name = song.name)  font "fonts/DollieScriptPersonalUse-K3P7.ttf" size 150  xalign 0.5 yalign 0.3

    timer song.length-startpoint action [SetVariable("song.has_played", True), SetVariable("playingcode", 2), SetVariable("playingpoint",0), Return()]

    bar:
        value AudioPositionValue(channel='music',update_interval=0.1)
        xalign 0.5
        yalign 0.5
        xsize 500
        xmaximum 50

    imagebutton:
        xalign 0.1
        yalign 0.9
        xoffset -30
        yoffset 30
        idle "images/return.png"
        hover "images/returnhover.png"
        action Call("creators_menu")
    if renpy.music.get_pause():
        imagebutton:
            xalign 0.5
            yalign 0.9
            xoffset -30
            yoffset 30
            idle "images/play.png"
            hover "images/playhover.png"
            action None
    else:
        imagebutton:
            xalign 0.5
            yalign 0.9
            xoffset -30
            yoffset 30
            idle "images/pause.png"
            hover "images/pausehover.png"
            action [SetVariable("playingcode", 1), Return()]

    imagebutton:
        xalign 0.9
        yalign 0.9
        xoffset -30
        yoffset 30
        idle "images/quit.png"
        hover "images/quithover.png"
        action Quit(confirm=None)
screen pause_song():
    imagebutton:
        xalign 0.5
        yalign 0.9
        xoffset -30
        yoffset 30
        idle "images/play.png"
        hover "images/playhover.png"
        action [SetVariable("playingcode", 0), Return()]

    #text "{Position}".format(Position = playingpoint)  font "fonts/BebasNeuePro-Thin.ttf" size 150  xalign 0.5 yalign 0.3
    text "Paused" font "fonts/DollieScriptPersonalUse-K3P7.ttf" size 150  xalign 0.5 yalign 0.3

######## Handles Playing video Content ###########
screen my_scr:
    key "K_RETURN" action Hide("nonexistent_screen")
    key "K_KP_ENTER" action Hide("nonexistent_screen")
    key "K_SPACE" action Hide("nonexistent_screen")
    key "mousedown_4" action Hide("nonexistent_screen")
    key "K_PAGEUP" action Hide("nonexistent_screen")
    key "mousedown_5" action Hide("nonexistent_screen")
    key "K_PAGEDOWN" action Hide("nonexistent_screen")
    key "mouseup_3" action Hide("nonexistent_screen")
    key "mouseup_1" action Hide("nonexistent_screen")
    key "K_ESCAPE" action Return("smth")
screen video_menu:
    imagebutton:
        xalign 0.1
        yalign 0.1
        xoffset -30
        yoffset 30
        idle "images/pavlovs_sissy.png" #change this button pavlovs sissy
        hover "images/pavlovs_sissy_hover.png" #change this button pavlovs sissy
        action Call("video1")
    imagebutton:
        xalign 0.5
        yalign 0.3
        xoffset -30
        yoffset 30
        idle "images/bambiinthebox.png" #change this button pavlovs sissy
        hover "images/bambiintheboxhovered.png" #change this button pavlovs sissy
        action Call("video2")


    imagebutton:
        xalign 0.9
        yalign 0.1
        xoffset -30
        yoffset 30
        idle "images/hellosissy.png" #change this button pavlovs sissy
        hover "images/hellosissyhovered.png" #change this button pavlovs sissy
        action Call("video4")

    imagebutton:
        xalign 0.5
        yalign 0.1
        xoffset -30
        yoffset 30
        idle "images/brainwasher.png" #change this button pavlovs sissy
        hover "images/brainwasherhovered.png" #change this button pavlovs sissy
        action Call("video5")

    imagebutton:
        xalign 0.1
        yalign 0.9
        xoffset -30
        yoffset 30
        idle "images/return.png"
        hover "images/returnhover.png"
        action Call("creators_menu")

    imagebutton:
        xalign 0.9
        yalign 0.9
        xoffset -30
        yoffset 30
        idle "images/quit.png"
        hover "images/quithover.png"
        action Quit(confirm=None)
screen video1:
    add "video1"
    imagebutton:
        xalign 0.05
        yalign 0.95
        xoffset -30
        yoffset 30
        idle "images/returnvideo.png"
        hover "images/returnvideohover.png"
        action Call("creators_menu")

screen video2:
    add "video2"
    imagebutton:
        xalign 0.05
        yalign 0.95
        xoffset -30
        yoffset 30
        idle "images/returnvideo.png"
        hover "images/returnvideohover.png"
        action Call("creators_menu")



screen video4:
    add "video4"
    imagebutton:
        xalign 0.05
        yalign 0.95
        xoffset -30
        yoffset 30
        idle "images/returnvideo.png"
        hover "images/returnvideohover.png"
        action Call("creators_menu")

screen video5:
    add "video5"
    imagebutton:
        xalign 0.05
        yalign 0.95
        xoffset -30
        yoffset 30
        idle "images/returnvideo.png"
        hover "images/returnvideohover.png"
        action Call("creators_menu")

######## Main Selection Area ###########
screen creators_menu():
    imagebutton:
        xalign 0.2
        yalign 0.1
        xoffset -30
        yoffset 30
        idle "images/bambisleep_playlists.png"
        hover "images/bambisleep_playlistshover.png"
        action Call("bambi_sleep")

    imagebutton:
        xalign 0.8
        yalign 0.1
        xoffset -30
        yoffset 30
        idle "images/bambi4eva_playlists.png"
        hover "images/bambi4eva_playlisthover.png"
        action Call("bambi4eva_menu")

    imagebutton:
        xalign 0.2
        yalign 0.3
        xoffset -30
        yoffset 30
        idle "images/bimbouniversity.png"
        hover "images/bimbouniversityhover.png"
        action Call("bu_menu")

    imagebutton:
        xalign 0.8
        yalign 0.3
        xoffset -30
        yoffset 30
        idle "images/video.png"
        hover "images/videohovered.png"
        action Call("video_menu")

    imagebutton:
        xalign 0.9
        yalign 0.9
        xoffset -30
        yoffset 30
        idle "images/quit.png"
        hover "images/quithover.png"
        action Quit(confirm=None)

######### BU Content ##########
screen bimbouniversity():
    imagebutton:
        xalign 0.5
        yalign 0.1
        xoffset -30
        yoffset 30
        idle "images/bimbouniversity.png"

    imagebutton:
        xalign 0.05
        yalign 0.3
        xoffset -30
        yoffset 30
        idle "images/bimboeuphoria.png"
        hover "images/bimboeuphoriahovered.png"
        action Call("bu_euphoria_menu")

    imagebutton:
        xalign 0.1
        yalign 0.9
        xoffset -30
        yoffset 30
        idle "images/return.png"
        hover "images/returnhover.png"
        action Call("creators_menu")

    imagebutton:
        xalign 0.9
        yalign 0.9
        xoffset -30
        yoffset 30
        idle "images/quit.png"
        hover "images/quithover.png"
        action Quit(confirm=None)
screen bu_euphoria():
    imagebutton:
        xalign 0.5
        yalign 0.1
        xoffset -30
        yoffset 30
        idle "images/bimboeuphoria.png"

    imagebutton:
        xalign 0.05
        yalign 0.3
        xoffset -30
        yoffset 30
        idle "images/dumbbitch.png"
        hover "images/dumbbitchhovered.png"
        action Call("song_player",Dumb_Bitch,"bu_euphoria_menu")

    imagebutton:
        xalign 0.5
        yalign 0.3
        xoffset -30
        yoffset 30
        idle "images/publicslut.png"
        hover "images/publicsluthovered.png"
        action Call("song_player",Public_Slut,"bu_euphoria_menu")

    imagebutton:
        xalign 0.1
        yalign 0.9
        xoffset -30
        yoffset 30
        idle "images/return.png"
        hover "images/returnhover.png"
        action Call("creators_menu")

    imagebutton:
        xalign 0.9
        yalign 0.9
        xoffset -30
        yoffset 30
        idle "images/quit.png"
        hover "images/quithover.png"
        action Quit(confirm=None)

########## Bambi4Eva Content #########
screen bambi4eva():
    imagebutton:
        xalign 0.05
        yalign 0.1
        xoffset -30
        yoffset 30
        idle "images/Bambi_Forever_wipers.png"
        hover "images/Bambi_Forever_wipershover.png"
        action Call("song_player",Bambi4everw,"bambi4eva_menu")

    imagebutton:
        xalign 0.5
        yalign 0.1
        xoffset -30
        yoffset 30
        idle "images/Bimbo_Night_Night_wipers.png"
        hover "images/Bimbo_Night_Night_wipershover.png"
        action Call("song_player",BimboNightNightw,"bambi4eva_menu")

    imagebutton:
        xalign 0.95
        yalign 0.1
        xoffset -30
        yoffset 30
        idle "images/Bambis_Dreamhouse_wipers.png"
        hover "images/Bambis_Dreamhouse_wipershover.png"
        action Call("song_player",BambisDreamHousew,"bambi4eva_menu")

    imagebutton:
        xalign 0.05
        yalign 0.3
        xoffset -30
        yoffset 30
        idle "images/bambi_forever.png"
        hover "images/bambi_foreverhovered.png"
        action Call("song_player",Bambi4ever,"bambi4eva_menu")

    imagebutton:
        xalign 0.5
        yalign 0.3
        xoffset -30
        yoffset 30
        idle "images/bimbo_night_night.png"
        hover "images/bimbo_night_night_hovered.png"
        action Call("song_player",BimboNightNight,"bambi4eva_menu")

    imagebutton:
        xalign 0.95
        yalign 0.3
        xoffset -30
        yoffset 30
        idle "images/bambis_dreamhouse.png"
        hover "images/bambis_dreamhousehovered.png"
        action Call("song_player",BambisDreamHouse,"bambi4eva_menu")


    imagebutton:
        xalign 0.1
        yalign 0.9
        xoffset -30
        yoffset 30
        idle "images/return.png"
        hover "images/returnhover.png"
        action Call("creators_menu")

    imagebutton:
        xalign 0.9
        yalign 0.9
        xoffset -30
        yoffset 30
        idle "images/quit.png"
        hover "images/quithover.png"
        action Quit(confirm=None)

######## Bambi Prime Content ###########
screen bambi_sleep():
    imagebutton:
        xalign 0.05
        yalign 0.1
        xoffset -30
        yoffset 30
        idle "images/officialplaylists.png"
        hover "images/officialplaylistshover.png"
        action Call("official_playlists")

    imagebutton:
        xalign 0.5
        yalign 0.1
        xoffset -30
        yoffset 30
        idle "images/ten_day_challenge.png"
        hover "images/ten_day_challenge_hover.png"
        action Call("ten_days_menu")

    imagebutton:
        xalign 0.95
        yalign 0.1
        xoffset -30
        yoffset 30
        idle "images/20day.png"
        hover "images/20dayhover.png"
        action Call("twenty_days_weeks_menu")

    imagebutton:
        xalign 0.05
        yalign 0.3
        xoffset -30
        yoffset 30
        idle "images/beginner_bambis.png"
        hover "images/beginner_bambis_hover.png"
        action Call("beginner_bambis_menu")

    imagebutton:
        xalign 0.5
        yalign 0.3
        xoffset -30
        yoffset 30
        idle "images/bambi_refresher.png"
        hover "images/bambi_refresherhover.png"
        action Call("bambi_refresher_menu")

    imagebutton:
        xalign 0.95
        yalign 0.3
        xoffset -30
        yoffset 30
        idle "images/mindblower.png"
        hover "images/mindblower_hover.png"
        action Call("mindblower_menu")

    imagebutton:
        xalign 0.05
        yalign 0.5
        xoffset -30
        yoffset 30
        idle "images/bambi_time.png"
        hover "images/bambi_timehovered.png"
        action Call("bambi_time_menu")

    imagebutton:###########
        xalign 0.5
        yalign 0.5
        xoffset -30
        yoffset 30
        idle "images/newstandard.png"
        hover "images/newstandardhovered.png"
        action Call("the_new_standard_menu")

    imagebutton:
        xalign 0.9
        yalign 0.9
        xoffset -30
        yoffset 30
        idle "images/quit.png"
        hover "images/quithover.png"
        action Quit(confirm=None)

    imagebutton:
        xalign 0.1
        yalign 0.9
        xoffset -30
        yoffset 30
        idle "images/return.png"
        hover "images/returnhover.png"
        action Call("creators_menu")
screen official_playlists_menu():
    imagebutton:
        xalign 0.5
        yalign 0.1
        xoffset -30
        yoffset 30
        idle "images/officialplaylists.png"

    imagebutton:
        xalign 0.05
        yalign 0.3
        xoffset -30
        yoffset 30
        idle "images/deeptrance.png"
        hover "images/deeptrancehover.png"
        action Call("song_player",deep_trance_programming,"official_playlists")

    imagebutton:
        xalign 0.525
        yalign 0.3
        xoffset -30
        yoffset 30
        idle "images/personality.png"
        hover "images/personalityhover.png"
        action Call("song_player",personality_programming,"official_playlists")

    imagebutton:
        xalign 1.0
        yalign 0.3
        xoffset -30
        yoffset 30
        idle "images/iq.png"
        hover "images/iqhover.png"
        action Call("song_player",iq_programming,"official_playlists")

    imagebutton:
        xalign 0.05
        yalign 0.5
        xoffset -30
        yoffset 30
        idle "images/attitude.png"
        hover "images/attitudehover.png"
        action Call("song_player",attitude_programming,"official_playlists")

    imagebutton:
        xalign 0.525
        yalign 0.5
        xoffset -30
        yoffset 30
        idle "images/takeover.png"
        hover "images/takeoverhover.png"
        action Call("song_player",takeover_programming,"official_playlists")

    imagebutton:
        xalign 1.0
        yalign 0.5
        xoffset -30
        yoffset 30
        idle "images/cockslut.png"
        hover "images/cocksluthover.png"
        action Call("song_player",cockslut_programming,"official_playlists")

    imagebutton:
        xalign 0.25
        yalign 0.7
        xoffset -30
        yoffset 30
        idle "images/uniform.png"
        hover "images/uniformhover.png"
        action Call("song_player",uniform_programming,"official_playlists")

    imagebutton:
        xalign 0.75
        yalign 0.7
        xoffset -30
        yoffset 30
        idle "images/maid.png"
        hover "images/maidhover.png"
        action Call("song_player",maid_programming,"official_playlists")

    imagebutton:
        xalign 0.9
        yalign 0.9
        xoffset -30
        yoffset 30
        idle "images/quit.png"
        hover "images/quithover.png"
        action Quit(confirm=None)

    imagebutton:
        xalign 0.1
        yalign 0.9
        xoffset -30
        yoffset 30
        idle "images/return.png"
        hover "images/returnhover.png"
        action Call("bambi_sleep")

######## BimboBear Content ###########
screen twenty_days_weeks_menu():
    imagebutton:
        xalign 0.5
        yalign 0.1
        xoffset -30
        yoffset 30
        idle "images/20day.png"

    $path = weekPlayed([day_1,day_2,day_3],"week1")

    imagebutton:
        xalign 0.1
        yalign 0.3
        xoffset -30
        yoffset 30
        idle path
        hover "images/week1hover.png"
        action Call("twenty_days_week1")

    $path = weekPlayed([day_4,day_5,day_6],"week2")

    imagebutton:
        xalign 0.3
        yalign 0.3
        xoffset -30
        yoffset 30
        idle path
        hover "images/week2hover.png"
        action Call("twenty_days_week2")

    $path = weekPlayed([day_7,day_8],"week3")

    imagebutton:
        xalign 0.5
        yalign 0.3
        xoffset -30
        yoffset 30
        idle path
        hover "images/week3hover.png"
        action Call("twenty_days_week3")

    $path = ""
    $path = weekPlayed([day_9,day_10],"week4")

    imagebutton:
        xalign 0.7
        yalign 0.3
        xoffset -30
        yoffset 30
        idle path
        hover "images/week4hover.png"
        action Call("twenty_days_week4")

    $path = weekPlayed([day_11,day_12,day_13],"week5")

    imagebutton:
        xalign 0.9
        yalign 0.3
        xoffset -30
        yoffset 30
        idle path
        hover "images/week5hover.png"
        action Call("twenty_days_week5")

    $path = weekPlayed([day_14,day_15,day_16],"week6")

    imagebutton:
        xalign 0.1
        yalign 0.5
        xoffset -30
        yoffset 30
        idle path
        hover "images/week6hover.png"
        action Call("twenty_days_week6")

    $path = weekPlayed([day_17,day_18,day_19],"week7")

    imagebutton:
        xalign 0.3
        yalign 0.5
        xoffset -30
        yoffset 30
        idle path
        hover "images/week7hover.png"
        action Call("twenty_days_week7")

    $path = weekPlayed([day_20],"week8")

    imagebutton:
        xalign 0.5
        yalign 0.5
        xoffset -30
        yoffset 30
        idle path
        hover "images/week8hover.png"
        action Call("twenty_days_week8")

    imagebutton:
        xalign 0.1
        yalign 0.9
        xoffset -30
        yoffset 30
        idle "images/return.png"
        hover "images/returnhover.png"
        action Call("bambi_sleep")



    imagebutton:
        xalign 0.9
        yalign 0.9
        xoffset -30
        yoffset 30
        idle "images/quit.png"
        hover "images/quithover.png"
        action Quit(confirm=None)
screen week1():
    imagebutton:
        xalign 0.5
        yalign 0.1
        xoffset -30
        yoffset 30
        idle "images/20day.png"


    imagebutton:
        xalign 0.5
        yalign 0.3
        xoffset -30
        yoffset 30
        idle "images/week1.png"

    $path = day_1.hasplayed()

    imagebutton:
        xalign 0.3
        yalign 0.5
        xoffset -30
        yoffset 30
        idle path
        hover "images/day1hover.png"
        action Call("song_player",day_1,"twenty_days_week1")

    $path = day_2.hasplayed()

    imagebutton:
        xalign 0.5
        yalign 0.5
        xoffset -30
        yoffset 30
        idle path
        hover "images/day2hover.png"
        action Call("song_player",day_2,"twenty_days_week1")

    $path = day_3.hasplayed()

    imagebutton:
        xalign 0.7
        yalign 0.5
        xoffset -30
        yoffset 30
        idle path
        hover "images/day3hover.png"
        action Call("song_player",day_3,"twenty_days_week1")

    imagebutton:
        xalign 0.9
        yalign 0.9
        xoffset -30
        yoffset 30
        idle "images/quit.png"
        hover "images/quithover.png"
        action Quit(confirm=None)

    imagebutton:
        xalign 0.1
        yalign 0.9
        xoffset -30
        yoffset 30
        idle "images/return.png"
        hover "images/returnhover.png"
        action Call("twenty_days_weeks_menu")
screen week2():
    imagebutton:
        xalign 0.5
        yalign 0.1
        xoffset -30
        yoffset 30
        idle "images/20day.png"

    imagebutton:
        xalign 0.5
        yalign 0.3
        xoffset -30
        yoffset 30
        idle "images/week2.png"

    $path = day_4.hasplayed()

    imagebutton:
        xalign 0.3
        yalign 0.5
        xoffset -30
        yoffset 30
        idle path
        hover "images/day4hover.png"
        action Call("song_player",day_4,"twenty_days_week2")

    $path = day_5.hasplayed()

    imagebutton:
        xalign 0.5
        yalign 0.5
        xoffset -30
        yoffset 30
        idle path
        hover "images/day5hover.png"
        action Call("song_player",day_5,"twenty_days_week2")

    $path = day_6.hasplayed()

    imagebutton:
        xalign 0.7
        yalign 0.5
        xoffset -30
        yoffset 30
        idle path
        hover "images/day6hover.png"
        action Call("song_player",day_6,"twenty_days_week2")

    imagebutton:
        xalign 0.9
        yalign 0.9
        xoffset -30
        yoffset 30
        idle "images/quit.png"
        hover "images/quithover.png"
        action Quit(confirm=None)

    imagebutton:
        xalign 0.1
        yalign 0.9
        xoffset -30
        yoffset 30
        idle "images/return.png"
        hover "images/returnhover.png"
        action Call("twenty_days_weeks_menu")
screen week3():
    imagebutton:
        xalign 0.5
        yalign 0.1
        xoffset -30
        yoffset 30
        idle "images/20day.png"

    imagebutton:
        xalign 0.5
        yalign 0.3
        xoffset -30
        yoffset 30
        idle "images/week3.png"

    $path = day_7.hasplayed()

    imagebutton:
        xalign 0.3
        yalign 0.5
        xoffset -30
        yoffset 30
        idle path
        hover "images/day7hover.png"
        action Call("song_player",day_7,"twenty_days_week3")

    $path = day_8.hasplayed()

    imagebutton:
        xalign 0.5
        yalign 0.5
        xoffset -30
        yoffset 30
        idle path
        hover "images/day8hover.png"
        action Call("song_player",day_8,"twenty_days_week3")

    imagebutton:
        xalign 0.9
        yalign 0.9
        xoffset -30
        yoffset 30
        idle "images/quit.png"
        hover "images/quithover.png"
        action Quit(confirm=None)

    imagebutton:
        xalign 0.1
        yalign 0.9
        xoffset -30
        yoffset 30
        idle "images/return.png"
        hover "images/returnhover.png"
        action Call("twenty_days_weeks_menu")
screen week4():
    imagebutton:
        xalign 0.5
        yalign 0.1
        xoffset -30
        yoffset 30
        idle "images/20day.png"

    imagebutton:
        xalign 0.5
        yalign 0.3
        xoffset -30
        yoffset 30
        idle "images/week4.png"

    $path = day_9.hasplayed()

    imagebutton:
        xalign 0.3
        yalign 0.5
        xoffset -30
        yoffset 30
        idle path
        hover "images/day9hover.png"
        action Call("song_player",day_9,"twenty_days_week4")

    $path = day_10.hasplayed()

    imagebutton:
        xalign 0.5
        yalign 0.5
        xoffset -30
        yoffset 30
        idle path
        hover "images/day10hover.png"
        action Call("song_player",day_10,"twenty_days_week4")

    imagebutton:
        xalign 0.7
        yalign 0.5
        xoffset -30
        yoffset 30
        idle "images/dayoff1.png"
        hover "images/dayoff1_hover.png"
        action Call("song_player",day_off_1,"twenty_days_week4")


    imagebutton:
        xalign 0.9
        yalign 0.9
        xoffset -30
        yoffset 30
        idle "images/quit.png"
        hover "images/quithover.png"
        action Quit(confirm=None)

    imagebutton:
        xalign 0.1
        yalign 0.9
        xoffset -30
        yoffset 30
        idle "images/return.png"
        hover "images/returnhover.png"
        action Call("twenty_days_weeks_menu")
screen week5():
    imagebutton:
        xalign 0.5
        yalign 0.1
        xoffset -30
        yoffset 30
        idle "images/20day.png"

    imagebutton:
        xalign 0.5
        yalign 0.3
        xoffset -30
        yoffset 30
        idle "images/week5.png"

    $path = day_11.hasplayed()

    imagebutton:
        xalign 0.3
        yalign 0.5
        xoffset -30
        yoffset 30
        idle path
        hover "images/day11hover.png"
        action Call("song_player",day_11,"twenty_days_week5")

    $path = day_12.hasplayed()

    imagebutton:
        xalign 0.5
        yalign 0.5
        xoffset -30
        yoffset 30
        idle path
        hover "images/day12hover.png"
        action Call("song_player",day_12,"twenty_days_week5")

    $path = day_13.hasplayed()

    imagebutton:
        xalign 0.7
        yalign 0.5
        xoffset -30
        yoffset 30
        idle path
        hover "images/day13hover.png"
        action Call("song_player",day_13,"twenty_days_week5")

    imagebutton:
        xalign 0.9
        yalign 0.9
        xoffset -30
        yoffset 30
        idle "images/quit.png"
        hover "images/quithover.png"
        action Quit(confirm=None)

    imagebutton:
        xalign 0.1
        yalign 0.9
        xoffset -30
        yoffset 30
        idle "images/return.png"
        hover "images/returnhover.png"
        action Call("twenty_days_weeks_menu")
screen week6():

    imagebutton:
        xalign 0.5
        yalign 0.1
        xoffset -30
        yoffset 30
        idle "images/20day.png"

    imagebutton:
        xalign 0.5
        yalign 0.3
        xoffset -30
        yoffset 30
        idle "images/week6.png"

    $path = day_14.hasplayed()

    imagebutton:

        xalign 0.3
        yalign 0.5
        xoffset -30
        yoffset 30
        idle path
        hover "images/day14hover.png"
        action Call("song_player",day_14,"twenty_days_week6")

    $path = day_15.hasplayed()

    imagebutton:
        xalign 0.5
        yalign 0.5
        xoffset -30
        yoffset 30
        idle path
        hover "images/day15hover.png"
        action Call("song_player",day_15,"twenty_days_week6")

    $path = day_16.hasplayed()

    imagebutton:
        xalign 0.7
        yalign 0.5
        xoffset -30
        yoffset 30
        idle path
        hover "images/day16hover.png"
        action Call("song_player",day_16,"twenty_days_week6")

    imagebutton:
        xalign 0.9
        yalign 0.9
        xoffset -30
        yoffset 30
        idle "images/quit.png"
        hover "images/quithover.png"
        action Quit(confirm=None)

    imagebutton:
        xalign 0.1
        yalign 0.9
        xoffset -30
        yoffset 30
        idle "images/return.png"
        hover "images/returnhover.png"
        action Call("twenty_days_weeks_menu")
screen week7():
    imagebutton:
        xalign 0.5
        yalign 0.1
        xoffset -30
        yoffset 30
        idle "images/20day.png"

    imagebutton:
        xalign 0.5
        yalign 0.3
        xoffset -30
        yoffset 30
        idle "images/week7.png"

    $path = day_17.hasplayed()

    imagebutton:
        xalign 0.3
        yalign 0.5
        xoffset -30
        yoffset 30
        idle path
        hover "images/day17hover.png"
        action Call("song_player",day_17,"twenty_days_week7")

    $path = day_18.hasplayed()

    imagebutton:
        xalign 0.5
        yalign 0.5
        xoffset -30
        yoffset 30
        idle path
        hover "images/day18hover.png"
        action Call("song_player",day_18,"twenty_days_week7")


    $path = day_19.hasplayed()

    imagebutton:
        xalign 0.7
        yalign 0.5
        xoffset -30
        yoffset 30
        idle path
        hover "images/day19hover.png"
        action Call("song_player",day_19,"twenty_days_week7")

    imagebutton:
        xalign 0.5
        yalign 0.7
        xoffset -30
        yoffset 30
        idle "images/dayoff2.png"
        hover "images/dayoff2_hover.png"
        action Call("song_player",day_off_2,"twenty_days_week7")

    imagebutton:
        xalign 0.9
        yalign 0.9
        xoffset -30
        yoffset 30
        idle "images/quit.png"
        hover "images/quithover.png"
        action Quit(confirm=None)

    imagebutton:
        xalign 0.1
        yalign 0.9
        xoffset -30
        yoffset 30
        idle "images/return.png"
        hover "images/returnhover.png"
        action Call("twenty_days_weeks_menu")
screen week8():
    imagebutton:
        xalign 0.5
        yalign 0.1
        xoffset -30
        yoffset 30
        idle "images/20day.png"

    imagebutton:
        xalign 0.5
        yalign 0.3
        xoffset -30
        yoffset 30
        idle "images/week8.png"

    $path = day_20.hasplayed()

    imagebutton:
        xalign 0.3
        yalign 0.5
        xoffset -30
        yoffset 30
        idle "images/day20.png"
        hover "images/day20hover.png"
        action Call("song_player",day_20,"twenty_days_week8")

    imagebutton:
        xalign 0.9
        yalign 0.9
        xoffset -30
        yoffset 30
        idle "images/quit.png"
        hover "images/quithover.png"
        action Quit(confirm=None)

    imagebutton:
        xalign 0.1
        yalign 0.9
        xoffset -30
        yoffset 30
        idle "images/return.png"
        hover "images/returnhover.png"
        action Call("twenty_days_weeks_menu")

#########User from Reddit Content ##########
screen ten_days_menu():
    imagebutton:
        xalign 0.5
        yalign 0.1
        xoffset -30
        yoffset 30
        idle "images/ten_day_challenge.png"

    imagebutton:
        xalign 0.3
        yalign 0.3
        xoffset -30
        yoffset 30
        idle "images/ten_day1.png"
        hover "images/ten_day1hover.png"
        action Call("song_player",ten_day_day_1,"ten_days_menu")

    imagebutton:
        xalign 0.5
        yalign 0.3
        xoffset -30
        yoffset 30
        idle "images/ten_day2.png"
        hover "images/ten_day2hover.png"
        action Call("song_player",ten_day_day_2,"ten_days_menu")

    imagebutton:
        xalign 0.7
        yalign 0.3
        xoffset -30
        yoffset 30
        idle "images/ten_day3.png"
        hover "images/ten_day3hover.png"
        action Call("song_player",ten_day_day_3,"ten_days_menu")

    imagebutton:
        xalign 0.3
        yalign 0.5
        xoffset -30
        yoffset 30
        idle "images/ten_day4.png"
        hover "images/ten_day4hover.png"
        action Call("song_player",ten_day_day_4,"ten_days_menu")

    imagebutton:
        xalign 0.5
        yalign 0.5
        xoffset -30
        yoffset 30
        idle "images/ten_day5.png"
        hover "images/ten_day5hover.png"
        action Call("song_player",ten_day_day_5,"ten_days_menu")

    imagebutton:
        xalign 0.7
        yalign 0.5
        xoffset -30
        yoffset 30
        idle "images/ten_day6.png"
        hover "images/ten_day6hover.png"
        action Call("song_player",ten_day_day_6,"ten_days_menu")

    imagebutton:
        xalign 0.3
        yalign 0.7
        xoffset -30
        yoffset 30
        idle "images/ten_day7.png"
        hover "images/ten_day7hover.png"
        action Call("song_player",ten_day_day_7,"ten_days_menu")

    imagebutton:
        xalign 0.5
        yalign 0.7
        xoffset -30
        yoffset 30
        idle "images/ten_day8.png"
        hover "images/ten_day8hover.png"
        action Call("song_player",ten_day_day_8,"ten_days_menu")

    imagebutton:
        xalign 0.7
        yalign 0.7
        xoffset -30
        yoffset 30
        idle "images/ten_day9.png"
        hover "images/ten_day9hover.png"
        action Call("song_player",ten_day_day_9,"ten_days_menu")

    imagebutton:
        xalign 0.5
        yalign 0.9
        xoffset -30
        yoffset 30
        idle "images/ten_day10.png"
        hover "images/ten_day10hover.png"
        action Call("song_player",ten_day_day_10,"ten_days_menu")

    imagebutton:
        xalign 0.9
        yalign 0.9
        xoffset -30
        yoffset 30
        idle "images/quit.png"
        hover "images/quithover.png"
        action Quit(confirm=None)

    imagebutton:
        xalign 0.1
        yalign 0.9
        xoffset -30
        yoffset 30
        idle "images/return.png"
        hover "images/returnhover.png"
        action Call("bambi_sleep")

######## Refresh and Polish Content ###########
screen beginner_bambis_menu():
    imagebutton:
        xalign 0.5
        yalign 0.1
        xoffset -30
        yoffset 30
        idle "images/beginner_bambis.png"

    imagebutton:
        xalign 0.1
        yalign 0.3
        xoffset -30
        yoffset 30
        idle "images/bambi_starter.png"
        hover "images/bambi_starter_hover.png"
        action Call("song_player",bambi_starter,"beginner_bambis_menu")

    imagebutton:
        xalign 0.5
        yalign 0.3
        xoffset -30
        yoffset 30
        idle "images/bambi_conditioner.png"
        hover "images/bambi_conditioner_hover.png"
        action Call("song_player",bambi_conditioner,"beginner_bambis_menu")

    imagebutton:
        xalign 0.9
        yalign 0.3
        xoffset -30
        yoffset 30
        idle "images/bambi_reinforcement.png"
        hover "images/bambi_reinforcement_hover.png"
        action Call("song_player",bambi_reinforcement,"beginner_bambis_menu")

    imagebutton:
        xalign 0.1
        yalign 0.5
        xoffset -30
        yoffset 30
        idle "images/bambi_enforcement.png"
        hover "images/bambi_enforcement_hover.png"
        action Call("song_player",bambi_enforcement,"beginner_bambis_menu")

    imagebutton:
        xalign 0.5
        yalign 0.5
        xoffset -30
        yoffset 30
        idle "images/bambi_mental_makeover.png"
        hover "images/bambi_mental_makeover_hover.png"
        action Call("song_player",bambi_mental_makeover,"beginner_bambis_menu")

    imagebutton:
        xalign 0.9
        yalign 0.9
        xoffset -30
        yoffset 30
        idle "images/quit.png"
        hover "images/quithover.png"
        action Quit(confirm=None)

    imagebutton:
        xalign 0.1
        yalign 0.9
        xoffset -30
        yoffset 30
        idle "images/return.png"
        hover "images/returnhover.png"
        action Call("bambi_sleep")


    ########################### Screens for the Bambi Refresher ################################
screen bambi_refresher_menu():
    imagebutton:
        xalign 0.5
        yalign 0.1
        xoffset -30
        yoffset 30
        idle "images/bambi_refresher.png"

    imagebutton:
        xalign 0.1
        yalign 0.3
        xoffset -30
        yoffset 30
        idle "images/bambi_refresher.png"
        hover "images/bambi_refresherhover.png"
        action Call("song_player",bambi_refresher,"bambi_refresher_menu")


    imagebutton:
        xalign 0.9
        yalign 0.9
        xoffset -30
        yoffset 30
        idle "images/quit.png"
        hover "images/quithover.png"
        action Quit(confirm=None)

    imagebutton:
        xalign 0.1
        yalign 0.9
        xoffset -30
        yoffset 30
        idle "images/return.png"
        hover "images/returnhover.png"
        action Call("bambi_sleep")
screen mindblower_menu():
    imagebutton:
        xalign 0.5
        yalign 0.1
        xoffset -30
        yoffset 30
        idle "images/mindblower.png"

    imagebutton:
        xalign 0.1
        yalign 0.3
        xoffset -30
        yoffset 30
        idle "images/mindblower.png"
        hover "images/mindblower_hover.png"
        action Call("song_player",Mindblower,"mindblower_menu")

    imagebutton:
        xalign 0.9
        yalign 0.9
        xoffset -30
        yoffset 30
        idle "images/quit.png"
        hover "images/quithover.png"
        action Quit(confirm=None)

    imagebutton:
        xalign 0.1
        yalign 0.9
        xoffset -30
        yoffset 30
        idle "images/return.png"
        hover "images/returnhover.png"
        action Call("bambi_sleep")
screen bambi_time_menu():
    imagebutton:
        xalign 0.5
        yalign 0.1
        xoffset -30
        yoffset 30
        idle "images/bambi_time.png"

    imagebutton:
        xalign 0.1
        yalign 0.3
        xoffset -30
        yoffset 30
        idle "images/bambi_time.png"
        hover "images/bambi_timehovered.png"
        action Call("song_player",Bambitime,"bambi_time_menu")


    imagebutton:
        xalign 0.9
        yalign 0.9
        xoffset -30
        yoffset 30
        idle "images/quit.png"
        hover "images/quithover.png"
        action Quit(confirm=None)

    imagebutton:
        xalign 0.1
        yalign 0.9
        xoffset -30
        yoffset 30
        idle "images/return.png"
        hover "images/returnhover.png"
        action Call("bambi_sleep")
screen the_new_standard_menu():
    imagebutton:
        xalign 0.5
        yalign 0.1
        xoffset -30
        yoffset 30
        idle "images/newstandard.png"

    imagebutton:
        xalign 0.1
        yalign 0.3
        xoffset -30
        yoffset 30
        idle "images/newstandard.png"
        hover "images/newstandardhovered.png"
        action Call("song_player",the_new_standard,"the_new_standard_menu")

    imagebutton:
        xalign 0.9
        yalign 0.9
        xoffset -30
        yoffset 30
        idle "images/quit.png"
        hover "images/quithover.png"
        action Quit(confirm=None)

    imagebutton:
        xalign 0.1
        yalign 0.9
        xoffset -30
        yoffset 30
        idle "images/return.png"
        hover "images/returnhover.png"
        action Call("bambi_sleep")
