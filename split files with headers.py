from tkinter import *
from tkinter import filedialog
class App:
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()

        self.getFile = Button(self.frame, text="Select File", command=self.getFileName)
        self.getFile.pack(side=LEFT)

        self.numFilesEntry = Entry(self.frame, width=50)
        self.numFilesEntry.pack()

        self.quitButton = Button(self.frame, text="QUIT", fg="red", command=self.frame.quit)
        self.quitButton.pack(side=LEFT)


    def getFileName(self):
        filepath = filedialog.askopenfilename()
        numfiles = int(self.numFilesEntry.get())
        if numfiles > 0:
            outputfile = filedialog.asksaveasfilename()
            self.splitFiles(filepath, numfiles, outputfile)
            print("Done")
        else:
            print("no number of files selected")
        print("Quitting")
        self.frame.quit()

    def splitFiles(self, filename, numfiles, outputfile):
        f = open(filename, "r")
        lines = f.readlines()

        print(len(lines))
        header = lines[0]
        numLines = int(len(lines) / numfiles) + 1

        fileCounter = 0
        lineStart = 1
        lineEnd = lineStart + numLines
        while fileCounter < numfiles:
            name = outputfile + str(fileCounter) + ".csv"
            newF = open(name, "w")
            print(name)
            print("\t" + str(lineStart) + " -> " + str(lineEnd))
            if lineEnd > len(lines):
                lineEnd = int(len(lines))
            newF.write(header)
            newF.writelines(lines[lineStart:lineEnd])
            newF.close()
            fileCounter = fileCounter + 1
            lineStart = lineStart + numLines
            lineEnd = lineEnd + numLines

root = Tk()
app = App(root)
root.mainloop()
root.destroy()
