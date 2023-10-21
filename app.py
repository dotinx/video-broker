import random
import sys

def buffer_edit(buf : bytes) -> bytes:
    global k,tgt_log
    random_edit_seed = random.randint(0,k + 100)
    if k > random_edit_seed:
        buf = buf[0:-1] + b"\114"
    k += 1
    if record:
        tgt_log.write(str(k) +" " + str(random_edit_seed) +"\n")
    return buf
def main(argv : list) -> int:
    global k,tgt_log
    filename_source = "source.mp4"
    filename_target = "target.mp4"
    buf_size = 114514
    record = False
    
    for i in range(1,len(argv)):
        if sys.argv[i] == "--record":
            record = True
        if i == len(sys.argv) - 1:
            continue
        if sys.argv[i] in ["--buffer","--randseed"]:
            buf_size = int(str(argv[i + 1]))
        if sys.argv[i] in ["--source","--file","--from","--input","--in"]:
            filename_source = str(argv[i + 1])
        if sys.argv[i] in ["--target","--output","--out"]:
            filename_target = str(argv[i + 1])
    
    source = open(filename_source,"rb")
    target = open(filename_target,"wb+")
    
    if record:
        tgt_log = open(str(filename_source) + ".log","w+")
    
    k = 0
    
    while True:
        buf = source.read(buf_size)
        if buf:
            target.write(buffer_edit(buf))
        else:
            break
    target.close()
    source.close()
    
if __name__ == '__main__':
    main(sys.argv)
