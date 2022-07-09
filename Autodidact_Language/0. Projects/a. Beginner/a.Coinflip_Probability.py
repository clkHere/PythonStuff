import random, itertools, threading, time, sys

#Create coinflip arrays to hold random choices and results
h=[] #heads
tail=[] #tails
coinflip = ['heads', 'tails']
start = 0
trial = int(input("How many trails would you like to run?\n"))

#START loading
done = False
#here is the animation
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            sys.stdout.write('\r\nCoinflip Probability Complete!\n')
            break
        sys.stdout.write('\rPerforming the coinflips ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    

t = threading.Thread(target=animate)
t.start()

#long process here
time.sleep(10)
done = True

#End loading

#Calculate and Show results
print("\n")
while start < trial:  
    if random.choice(coinflip) == 'heads':
        h.append('heads')
        start = start +1
    else:
        tail.append('tails')
        start = start +1
        
totValue = len(h) + len(tail)
hPerct = len(h)/totValue
tPerct = len(tail)/totValue

print(f'RESULTS:\n\n{start} trials were run and here are the results:\n\tHeads percentage is: {hPerct}%\n\tTails percentage is: {tPerct}%')
