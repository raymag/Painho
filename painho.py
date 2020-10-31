import time
import datetime
import os

class Painho:
    def __init__(self):
        self.goingToBed = False

    def isBedTime(self):
        now = datetime.datetime.now()
        if now.hour == 21 and now.minute >= 30:
            return True
        elif now.hour > 21: 
            return True
        return False

    def goToBedSon(self):
        if self.goingToBed == False:
            print("It's bed time, son...")
            os.system("shutdown /s /t 60") 
            self.goingToBed = True

    def check_son(self):
        print("Checking you, son...")
        print(self.isBedTime())
        if self.isBedTime():
            self.goToBedSon()    
    
    def watch(self):
        while True:
            self.check_son()
            time.sleep(60)

if __name__ == "__main__":
    painho = Painho()
    painho.watch()