import pygame, os, imageio, shutil


class VideoEditor:
    def __init__(self, image_folder):
        self.frames = []
        self.nb_frames = 0
        self.image_folder = image_folder

        if os.path.exists(image_folder):
            shutil.rmtree(image_folder)   
        os.makedirs(image_folder, exist_ok=True)

    def captureScreen(self, screen):
        pygame.image.save(screen, f"{self.image_folder}/frame_{self.nb_frames:05d}.png")
        self.nb_frames+=1
        '''frame = pygame.surfarray.array3d(screen)[:,:,:3]

        #L'image apparait pour je ne sait quelle raison avec une symetrie le long d'une diagonale.. Bref on fait une transposé et ca répare le truc
        #frame = np.transpose(frame, axes=(1, 0, 2)) # Transpose width and height |  same as np.swapaxes(frame, 0, 1)
        imageio.imwrite(os.path.join(self.image_folder, f"frame_{self.nb_frames:05d}.png"), np.swapaxes(frame, 0, 1))
        self.nb_frames+=1'''

    def diskFramesToMp4(self, output_video_filename, fps=30 ):
        images = [imageio.imread(os.path.join(self.image_folder, filename)) for filename in sorted(os.listdir(self.image_folder))]
        imageio.mimsave(output_video_filename, images, fps=fps)