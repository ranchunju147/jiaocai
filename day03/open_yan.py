def open_write():
    kjj_l=open('love.text','w+')
    for i in  range(6):
        kjj_l.write('I LOVE YANYAN\n')
def open_():
    kjj_l=open('love.text','a+')
    for i in range(6):
        kjj_l.write('你好Y\n')
def oenp_read():
    kjj_l=open('love.text','r')
    print(kjj_l.readline())





if __name__ == '__main__':
    # open_()
    oenp_read()
    open_write()