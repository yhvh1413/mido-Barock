import mido
from mido import Message, MidiFile, MidiTrack
#训练
#测试
mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

def yin(yin,pai,qian=0,tong=0,liang=64,qi=2):              #yin是指哪个音，pai是指时间（节拍），qian是noteon里的time，liang是指音量，tong是通道，
    track.append(Message('program_change',channel=tong,program=qi,time=0))  #pi是乐器 默认钢琴（2）
    track.append(Message('note_on', note=yin, velocity=liang, time=qian,channel=tong))  #音开始
    track.append(Message('note_off', note=yin, velocity=liang, time=pai,channel=tong))

def beat(time):                  #与mido的拍子互换
    time /= 60 * 1000
    time = 1/time
    return time


def myin(fu,pai,time,qian=None,yue=2):   #不同音，不同节奏
    pig = int(beat(time))
    if qian == None:
        x = len(pai)
        for i in range(x):
            if type(fu[i]) == str:
                fu[i] = num(fu[i])
            yin(fu[i],pai[i]*pig,qi=yue)
    
    elif qian and len(qian) == 1:
        x = len(pai)
        for i in range(x):
            if type(fu[i]) == str:
                fu[i] = num(fu[i])
            yin(fu[i],pai[i]*pig,qian,qi=yue)
    
    else:
        x = len(pai)
        for i in range(x):
            if type(fu[i]) == str:
                fu[i] = num(fu[i])
            yin(fu[i],pai[i]*pig,qian[i],qi=yue)
