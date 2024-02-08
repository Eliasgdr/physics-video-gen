from moviepy.editor import AudioClip, AudioFileClip, concatenate_audioclips

class AudioEditor:
    def __init__(self):
        self.__audio_clip = []
        self.__nb_clips = 1
        self.__output_clip = AudioClip(lambda t: [0], 0)
        self.__index_clip = []

    def add_clip(self, path):
        try:
            audio_clip = AudioFileClip(path)
            self.__audio_clip.append(audio_clip)
            self.__index_clip.append(0)
            self.__nb_clips += 1
        except FileNotFoundError as e:
            print(f"File not found: {e.filename}")
        except Exception as e:
            print(f"An error occurred while adding clip: {e}")

    def add_audio(self, clip, seconds=1):
        try:
            if not 0 <= clip < self.__nb_clips:
                print("Invalid clip index.")
                return

            if clip == 0:
                added_audio = AudioClip(lambda t: [0], seconds)
            else:
                if self.__index_clip[clip - 1] + seconds > self.__audio_clip[clip - 1].duration:
                    self.__index_clip[clip - 1] = 0

                added_audio = self.__audio_clip[clip - 1].subclip(self.__index_clip[clip - 1],
                                                                  self.__index_clip[clip - 1] + seconds)
                self.__index_clip[clip - 1] += seconds

            self.__output_clip = concatenate_audioclips([self.__output_clip, added_audio])
        except IndexError:
            print("Index out of range.")
        except Exception as e:
            print(f"An error occurred while adding audio: {e}")

    def write(self, path):
        try:
            if self.__output_clip:
                self.__output_clip.write_audiofile(path, codec='libmp3lame', fps=44100)
            else:
                print("Output clip is not set.")
        except FileNotFoundError as e:
            print(f"Output path not found: {e.filename}")
        except Exception as e:
            print(f"An error occurred while writing the audio file: {e}")