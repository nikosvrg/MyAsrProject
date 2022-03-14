import os
import os.path
import shutil

train_audio_path = 'recordings'

recordings = [f for f in os.listdir(train_audio_path) if os.path.isfile(os.path.join(train_audio_path,f))]
for recording in recordings:
     new_folder = recording.split('_')[0]

     new_path = os.path.join(train_audio_path, new_folder)
     if not os.path.exists(new_path):
       os.makedirs(new_path)

     old_recording_path = os.path.join(train_audio_path, recording)
     new_recording_path = os.path.join(new_path, recording)
     shutil.move(old_recording_path, new_path)

