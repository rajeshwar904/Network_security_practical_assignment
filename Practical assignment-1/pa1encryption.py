import tkinter as tk
from PIL import ImageTk, Image
from encryptiononly  import * 

def encrypt(plaintext,key,r,hw):
	rkb,round_ciphertexts,final =encryption(plaintext,key,r,hw)
	c['text']=final
	
root=tk.Tk()
root.title("practical assignment-1")
canvas = tk.Canvas(root, height=400, width=700)
canvas.pack()
frame=tk.Frame(root,bg="#184d47")
frame.place(relx=0.05,rely=0.05,relwidth=0.9, relheight=0.9)
label=tk.Label(frame,text="DES encryption process with different hyper parameters",font=('Times New Roman TUR',15))
label.place(relx=0.1,rely=0.05,relwidth=0.8,relheight=0.1)
#headings
ph = tk.Label(frame, text="PLAINTEXT", fg="#c64756", bg="#96bb7c",font=('Times New Roman TUR',12))
ph.place(relx=0.05,rely=0.175,relwidth=0.35,relheight=0.075)
kh=tk.Label(frame, text="KEY", fg="#c64756", bg="#96bb7c",font=('Times New Roman TUR',12))
kh.place(relx=0.6,rely=0.175,relwidth=0.35,relheight=0.075)

#inputs
p=tk.Entry(frame,font=30)
p.place(relx=0.05,rely=0.275,relwidth=0.35,relheight=0.075)
k=tk.Entry(frame,font=30)
k.place(relx=0.6,rely=0.275,relwidth=0.35,relheight=0.075)

#headings
wh = tk.Label(frame, text="HALFWIDTH(16,32,64)", fg="#c64756", bg="#96bb7c",font=('Times New Roman TUR',12))
wh.place(relx=0.05,rely=0.375,relwidth=0.35,relheight=0.075)
rh=tk.Label(frame, text="NO OF ROUNDS(8,16,32)", fg="#c64756", bg="#96bb7c",font=('Times New Roman TUR',12))
rh.place(relx=0.6,rely=0.375,relwidth=0.35,relheight=0.075)

#inputs
w=tk.Entry(frame,font=30)
w.place(relx=0.05,rely=0.475,relwidth=0.35,relheight=0.075)
r=tk.Entry(frame,font=30)
r.place(relx=0.6,rely=0.475,relwidth=0.35,relheight=0.075)


but1=tk.Button(frame,text="ENCRYPT",command=lambda : encrypt(p.get(),k.get(),int(r.get()),int(w.get())),bg="#fad586",font=('Times New Roman TUR',15))
but1.place(relx=0.35,rely=0.6,relwidth=0.3,relheight=0.1)

#cipher text output
c = tk.Label(frame, fg="#c64756",font=('Times New Roman TUR',15))
c.place(relx=0.1,rely=0.75,relwidth=0.8,relheight=0.1)

root.mainloop()