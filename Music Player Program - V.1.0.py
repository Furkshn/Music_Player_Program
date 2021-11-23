


                ##################################################

                #          Music Player Program

                ##################################################



def music_player():

    from pygame import mixer

    mixer.init()
    while True:

        try:
            music_file_name = input("""
            Enter the name of the music you want to play: 
            """)
            mixer.music.load(music_file_name + ".mp3")
            mixer.music.set_volume(0.7)
            mixer.music.play()
            break

        except:

            print("""
            
            Undetected Music Error !
    
                Please select existing music files.""")
            continue


    while True:

        print("""
        
        Stop the music by pressing the P key.
        
            Resume the music by pressing the R key.
        
                Stop the program by pressing the E key.
                
        """)

        process = input("")

        if process == "p" or process == "P":
            mixer.music.pause()

        elif process == "r" or process == "R":
            mixer.music.unpause()

        elif process == "e" or process == "E":

            print("""
            Music Player Program is Closing...
            """)
            mixer.music.stop()
            break


music_player()