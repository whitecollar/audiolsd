import pyaudio
import wave
import datetime
import telebot
import time
import serial
from pydub import AudioSegment
import os
from telebot import apihelper
import logging

while True:
    TOKEN = '1829642580:AAEojR4JRS4X4oZr0qRz_q8ppO8naSLokKA'
    form_1 = pyaudio.paInt16 # 16-bit resolution
    chans = 1 # 1 channel
    samp_rate = 44100 # 44.1kHz sampling rate
    chunk = 4096 # 2^12 samples for buffer
    record_secs = 1800 # seconds to record
    dev_index = 1 # device index found by p.get_device_info_by_index(ii)
    now = datetime.datetime.now()
    #print str(now)
    wav_output_filename = str(now) + '.wav' #'test1.wav' # name of .wav file
    mp3_output_filename = str(now) + '.mp3'

    #recipient = "89069749066"
    recipient = "89509932923"
    phone = serial.Serial("/dev/ttyS1",  9600, timeout=5)
    time.sleep(0.5)
    phone.write(b'ATZ\r')
    time.sleep(1)
    phone.write(b'ATH\r')
    time.sleep(1)
    #phone.write(b'ATD"'+recipient.encode() +b'"\r')
    phone.write(b'ATD'+recipient.encode() +b';\r')
    #while(1):
    print(phone.readline())
    time.sleep(5)
    print(phone.readline())
    audio = pyaudio.PyAudio() # create pyaudio instantiation

    # create pyaudio stream
    stream = audio.open(format = form_1,rate = samp_rate,channels = chans, \
                        input_device_index = dev_index,input = True, \
                        frames_per_buffer=chunk)
    print("recording")
    frames = []

    # loop through stream and append audio chunks to frame array
    for ii in range(0,int((samp_rate/chunk)*record_secs)):
        data = stream.read(chunk)
        frames.append(data)
        #print(phone.readline())
    print("finished recording")

    # stop the stream, close it, and terminate the pyaudio instantiation
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # save the audio frames as .wav file
    wavefile = wave.open(wav_output_filename,'wb')
    wavefile.setnchannels(chans)
    wavefile.setsampwidth(audio.get_sample_size(form_1))
    wavefile.setframerate(samp_rate)
    wavefile.writeframes(b''.join(frames))
    wavefile.close()

    phone.write(b'ATH\r')

    AudioSegment.from_wav(wav_output_filename).export(mp3_output_filename, format="mp3")

    os.remove (wav_output_filename)
    logger = telebot.logger
    telebot.logger.setLevel(logging.DEBUG)
    tb = telebot.TeleBot(TOKEN)
    apihelper.SESSION_TIME_TO_LIVE = 5 * 60
    audio = open (mp3_output_filename, 'rb')
    tb.send_audio('-1001206972540', audio, timeout=60)
#    tb.send_audio('-1001206972540', "FILEID")
