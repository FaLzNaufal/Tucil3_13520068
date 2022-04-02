import tkinter as tk
from Puzzle import *
root = tk.Tk()
root.columnconfigure([0,1], weight=1)
root.rowconfigure([0,1], weight=1)
iterator = 0
jawaban = []
matriksAwal = []
def InitMatriks():
    try:
        global jawaban
        global matriksAwal
        matriksAwal = GetMatriksAwal(entry.get())
        jawaban = []
        buttonNext['state'] = 'disabled'
        buttonPrev['state'] = 'disabled'
        buttonRewind['state'] = 'disabled'
        buttonFastForward['state'] = 'disabled'
        buttonNext.grid(row=0, column=3,rowspan=4, sticky="nsew")
        buttonPrev.grid(row=0, column=1, rowspan=4, sticky="nsew")
        buttonFastForward.grid(row=0, column=4,rowspan=4, sticky="nsew")
        buttonRewind.grid(row=0, column=0, rowspan=4, sticky="nsew")
        

        for widget in matriksFrame.winfo_children():
            widget.destroy()
        for i in range(4):
            for j in range(4):
                relief = "raised"
                number = matriksAwal[i][j]
                if number == 16:
                    number = " "
                    relief = "sunken"
                label = tk.Label(master=matriksFrame, relief=relief, borderwidth=10, text=number, font=('bold',50))
                label.grid(row=i, column=j,sticky="nsew")
        buttonSolve = tk.Button(master=inputFrame, text="Solve", relief="raised", borderwidth=5, command=Solve)
        buttonSolve.grid(row=3, column=2,sticky="nsew")
    except:
        print("File tidak ditemukan")
def Update():
    global matriksFrame
    for i in range(4):
        for j in range(4):
            relief = "raised"
            number = jawaban[iterator].matriks[i][j]
            if number == 16:
                number = " "
                relief = "sunken"
            matriksFrame.winfo_children()[4*i+j]["text"] = number
            matriksFrame.winfo_children()[4*i+j]["relief"] = relief

def Next():
    global iterator
    if iterator > 0:
        iterator -= 1
        buttonPrev['state'] = 'active'
        buttonRewind['state'] = 'active'
    if iterator <= 0:
        buttonNext['state'] = 'disabled'
        buttonFastForward['state'] = 'disabled'
    Update()
def Prev():
    global iterator
    if iterator < len(jawaban)-1:
        iterator += 1
        buttonNext['state'] = 'active'
        buttonFastForward['state'] = 'active'
    if iterator >= len(jawaban)-1:
        buttonPrev['state'] = 'disabled'
        buttonRewind['state'] = 'disabled'
    Update()
def FastForward():
    buttonFastForward['state'] = 'disabled'
    if iterator > 0:
        Next()
        root.after(100, FastForward)
def Rewind():
    buttonRewind['state'] = 'disabled'
    if iterator < len(jawaban)-1:
        Prev()
        root.after(100, Rewind)
def Solve():
    global jawaban
    global iterator
    jawaban, arr, sum, duration, totalSimpul = Run(matriksAwal)
    iterator = len(jawaban)-1
    if iterator > 0:
        buttonNext['state'] = 'normal'
        buttonFastForward['state'] = 'normal'
        buttonPrev['state'] = 'disabled'
        buttonRewind['state'] = 'disabled'
    for widget in detailFrame.winfo_children():
        widget.destroy()
    tableHeadLeft = tk.Label(master=detailFrame, text = 'i', relief="groove", borderwidth=2)
    tableHeadLeft.grid(row=0, column=0, sticky="nsew")
    tableHeadRight = tk.Label(master=detailFrame, text = 'Kurang(i):', relief="groove", borderwidth=2)
    tableHeadRight.grid(row=0, column=1, sticky="nsew")
    for i in range(16):
        detailLabelIndex = tk.Label(master=detailFrame, text = i+1, relief="groove", borderwidth=1)
        detailLabelIndex.grid(row=i+1, column=0, sticky="nsew")
        detailLabelValue = tk.Label(master=detailFrame, text = arr[i], relief="groove", borderwidth=1)
        detailLabelValue.grid(row=i+1, column=1, sticky="nsew")
    total = tk.Label(master=detailFrame, text = "Sigma(KURANG(i)) + X = "+str(sum), relief="groove", borderwidth=1)
    total.grid(row=17, column=0, columnspan= 2, sticky="nsew")
    durationLabel = tk.Label(master=detailFrame, text = "Durasi = "+str(duration), relief="groove", borderwidth=1)
    durationLabel.grid(row=18, column=0, columnspan= 2, sticky="nsew")
    simpulText = "Total Simpul = "+str(totalSimpul)
    if totalSimpul <= 0:
        simpulText = "Persoalan tidak bisa diselesaikan"
    simpulLabel = tk.Label(master=detailFrame, text = simpulText, relief="groove", borderwidth=1)
    simpulLabel.grid(row=19, column=0, columnspan= 2, sticky="nsew")

# inputFrame    
inputFrame = tk.Frame(master=root)
inputFrame.grid(row=1, column=0, sticky="nsew")
inputFrame.columnconfigure([0,1,2,3,4], weight=1)
inputFrame.rowconfigure([0,1,2,3], weight=1)
inputLabel = tk.Label(master=inputFrame, text="Masukkan Nama File:")
inputLabel.grid(row=0, column=2,sticky="nsew")
entry = tk.Entry(master=inputFrame)
entry.grid(row=1, column=2,sticky="nsew")
buttonOpen = tk.Button(master=inputFrame, text="Open", relief="raised", borderwidth=5, command=InitMatriks)
buttonOpen.grid(row=2, column=2,sticky="nsew")
buttonNext = tk.Button(master=inputFrame, text="Next", relief="raised", borderwidth=5,command=Next, state="disabled")
buttonPrev = tk.Button(master=inputFrame, text="Prev", relief="raised", borderwidth=5, command=Prev, state="disabled")
buttonFastForward = tk.Button(master=inputFrame, text="Fast Forward", relief="raised", borderwidth=5,command=lambda:FastForward(), state="disabled")
buttonRewind = tk.Button(master=inputFrame, text="Rewind", relief="raised", borderwidth=5, command=lambda:Rewind(), state="disabled")

# matriksFrame
matriksFrame = tk.Frame(master=root, relief="sunken", borderwidth=10)
matriksFrame.grid(row=0, column=0)
matriksFrame.rowconfigure([0,1,2,3],minsize=150,weight=1)
matriksFrame.columnconfigure([0,1,2,3],minsize=150,weight=1)

# detailFrame
detailFrame = tk.Frame(master=root, relief="ridge", borderwidth=10)
detailFrame.grid(row=0, column=1, rowspan=2, sticky="nsew")
detailFrame.rowconfigure([i for i in range(20)],weight=1)
detailFrame.columnconfigure([0,1],weight=1)

root.mainloop()