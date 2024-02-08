import sys
import moviepy.editor as mp
#python src/merge.py temp/output_audio.mp3 temp/output_video.mp4 output/finalOutput.mp4

# Access the arguments
audio_path = sys.argv[1]
video_path = sys.argv[2]
output_path = sys.argv[3]

# Use the arguments
print("Creating {} from {} video and {} audio:".format(output_path, video_path, audio_path))




# Load the output audio clip
audio = mp.AudioFileClip(audio_path)

# Load the output video clip
video1 = mp.VideoFileClip(video_path)

# Combine the video and audio clips
final = video1.set_audio(audio)

# Write the final output video file
final.write_videofile(output_path, codec='libx264', audio_codec='libvorbis')
