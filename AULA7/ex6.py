class Tv:
    def __init__(self, channel, volume):
        self.channel, self.volume = channel, volume
    def changeChannel(self, vlr):
        self.channel += vlr
        print(f'Canal - {self.channel}')
    def changeVolume(self, vlr1):
        self.volume += vlr1
        print(f'Volume - {self.volume}')

tv = Tv(int(input('Qual canal deseja?: ')), int(input('Qual o volume?: ')))
while True:
    if chnl := input('Proximo canal ou anterior?: ').lower() == 'proximo':
        tv.changeChannel(1)
    else:
        tv.changeChannel(-1)
    
    if vlm := input('Aumentar ou Diminuir o volume?: ').lower() == 'aumentar':
        tv.changeVolume(1)
    else:
        tv.changeVolume(-1)
    True