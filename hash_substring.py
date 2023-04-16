# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    text = input()
    if "F" in text :
        with open(f"test/06") as f:
            patt = f.readline()
            text = f.readline()
    elif "I" in text:
        patt = input()
        text = input()  
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    return (patt.rstrip(), patt.rstrip())

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    pnlg = len(pattern)
    txlg = len(text)
    hasht=0
    hashp=0
    chs = 56
    q =11
    bup=1
    rez = []
    for i in range(pnlg-1):
        bup = (bup*chs)%q
    for i in range(pnlg):
        hashp=(hashp*chs+ord(text[i]))%q
        hasht=(hasht*chs+ord(text[i]))%q
    for i in range(txlg-pnlg+1):
        if hashp == hasht:
            for j in range(pnlg):
                if text[i+j] == pattern[j]:
                    rez.append(i)
                else:
                    break
        if i < txlg-pnlg:
            hasht = (chs *(hasht - ord (text[i])*bup)+ord (text[i+pnlg])) % q
            if hasht < 0:
                hasht=hasht+q

    # and return an iterable variable
    return arr


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

