import threading
import time

threadList=[]
mainList=[]


def sleep5(threadcount):
    for j in range(int(threadcount)):
        threadList.append(j)
        print("in thread, j is " + str(j))
        time.sleep(0.5)

maincount=input("Please input 1st (main) No.")
threadcount=input("Please input 2nd (thread) No.")

cat=threading.Thread(target=sleep5, args=[threadcount])
cat.start()

for i in range(int(maincount)):
    mainList.append(i)
    print("in main, i ="+str(i))
    time.sleep(0.5)

cat.join()
print("Finish all")
print("thread="+str(threadList))
print("main="+str(mainList))
