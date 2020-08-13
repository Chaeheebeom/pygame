# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#-*-coding:utf-9-*-

from tkinter import *
from tkinter.ttk import *
from urllib.request import urlopen

#from pytube import YouTube
from bs4 import BeautifulSoup

class PlayMaster(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        self.master = master
        self.master.title("pyPlay")
        self.pack(fill=BOTH, expand=True)

        # 검색
        frame1 = Frame(self)
        frame1.pack(fill=X)

        lblName = Label(frame1, text="검색", width=10)
        lblName.pack(side=LEFT, padx=10, pady=10)

        self.entryName = Entry(frame1)
        self.entryName.bind("<Return>", self.enter)
        self.entryName.pack(fill=BOTH, padx=10, expand=True)

        btnSave = Button(frame1, text="검색", command=self.onClick)

        btnSave.pack(side=RIGHT, padx=10, pady=10)

        #화면창
        frame3 = Frame(self)
        frame3.pack(fill=BOTH, expand=True)

        txtComment = Text(frame3)
        txtComment.pack(fill=X, pady=10, padx=10)

    def onClick(self):
        txt = str(self.entryName.get())
        self.getUrl(txt)

    def enter(self,event):
        txt = str(self.entryName.get())
        self.getUrl(txt)

    def download(self,text):
        #yt = YouTube("https://www.youtube.com/watch?v=.")
        pass
        #yt.streams.filter(only_audio=True).first().download()

    def getUrl(self,txt):
        url = "https://www.youtube.com/results?search_query="+txt
        soup = BeautifulSoup(urlopen(url), "html.parser", from_encoding='utf-8')
        print("url : ",url)
        LinkListRAW = soup.findAll(class_="yt-lockup-content")

        for LINK_RAW in LinkListRAW:
            parseLink = LINK_RAW.find("a")
            MovieCode = parseLink.get("href").replace("/watch?v=", "")
            print("[영상코드]" + MovieCode)

def main():
    root = Tk()
    root.geometry("600x550+100+100")
    app = PlayMaster(root)
    root.mainloop()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
