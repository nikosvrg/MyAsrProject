#split my recording to multiple wav files

from pydub import AudioSegment
from pydub.utils import make_chunk
#from pydub.silence import split_on_silence


def split_to_words(filename,directory)
myaudio = AudioSegment.from_file("test_recording.wav." , "wav")
chunk_length_ms = 3000 # pydub calculates in millisec 3*1000
chunks = make_chunks(myaudio, chunk_length_ms) #Make chunks of 3 sec

#Export all of the individual chunks as wav files

for i, chunk in enumerate(chunks):
    chunk_name = directory+"chunk{0}.wav".format(i)
    print ("exporting", chunk_name)
    chunk.export(chunk_name, format="wav")