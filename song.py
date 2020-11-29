class Album:
    def __init__(self,name, group):
        self.name = name
        self.group = group

        self.track = []


    def add_track (self, track):
        self.track.append(track)


    def get_tracks (self):
        for item in self.track:
            print(f' Песня:{item.name} , идет: {item.time}минут')


    def get_duration (self):
        cash = []
        for item in self.track:
            cash.append(item.time)
            print(sum(cash))



class Track:

    def __init__(self, name, time):
        self.name = name
        self.time = time



    def show (self):
        self.time = int(time)
        for item in self.track:
            print(f' Песня:{item.name} , идет: {item.time}минуты')




dance = Track('Последний танец', 3)
dance1 = Track('Phantom', 3)
muz = Track('rockstar', 4)
muz1 = Track('vinst', 6)
muz2 = Track('sunshine', 3)
muz3 = Track('WWS', 2)
A_n = Album('no name', 'tini_lin')
A_n1 = Album('no mure', 'usa')




A_n.add_track(dance)
A_n.add_track(dance1)
A_n.add_track(muz)
A_n1.add_track(muz1)
A_n1.add_track(muz2)
A_n1.add_track(muz3)
#for item in A_n.track:
    #print(item.name , item.time)

A_n.get_tracks()
A_n.get_duration()
#A_n1.get_tracks()
#A_n1.get_duration()
