#replication of png binary file
buff=60000

file=open("F:\\lco py3\\sample.png",'rb')
newfile=open("F:\lco py3\\copy.jpg",'wb')

buffer= file.read(buff)
while len(buffer):
    newfile.write(buffer)
    buffer=file.read(buff)

print('\ndone')    

