import pygame
from soundLib import *
from videoLib import *
from const import *


print("Init mainWsoundbis..")
   # Define the duration of the blank section (in seconds)



audioEditor = AudioEditor()
audioEditor.add_clip("input/audio/test3.mp3")
audioEditor.add_clip("input/audio/test2.mp3")


videoEditor = VideoEditor(image_folder)



# Initialize Pygame
pygame.init()

# Set up the screen dimensions

screen = pygame.display.set_mode((screen_width, screen_height))

# Initialize the clock
clock = pygame.time.Clock()

#arbitrary
collision = False
end_simulation=False
tasks = []


# Main loop
print(" Done.")
print("Recording..")

for i in range(num_frames_max):



    ###########################
    #   EVENTS
    ###########################
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                collision = True
            if event.key == pygame.K_t:
                pygame.image.save(screen, "temp/testee.png")
            if event.key == pygame.K_q:
                end_simulation = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_r:
                collision = False

    if end_simulation:
        break


    ###########################
    #   ANIMATION
    ###########################
    screen.fill((i % 255, 255 - i % 255, 255))

    if collision:
        pygame.draw.circle(screen, (255, 0, 0), (15, 15), 10)

    pygame.draw.circle(screen, (255, 0, 0), (15, i%255*5), 10)

    pygame.display.flip()





    ###########################
    #   RECORD PROCESSES
    ###########################
    # Capture the current frame
    videoEditor.captureScreen(screen)
    

    #Music event
    if i % (fps * audio_partitioning) == 0:
        if collision:
            audioEditor.add_audio(2, audio_partitioning)
        else:
            audioEditor.add_audio(0, audio_partitioning)



         

    #clock.tick(fps)    #balec 
pygame.quit()
print(" Done.")
print("Saving..")

    
#videoEditor.memToDiskFrames(image_folder)
videoEditor.diskFramesToMp4(output_video_filename, fps)

audioEditor.write(audio_video_filename)
print(" Done")