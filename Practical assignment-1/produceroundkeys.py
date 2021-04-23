from encryptiononly import *

def encrypt(key,r,hw):
	key=get_2hw_bit_key(key,hw)
	rkb = produce_round_keys(key,r,hw)
	for i in range(len(rkb)):
		c['text']+= "Round Key"+str(i+1)+": "+rkb[i]+"\n"
root=tk.Tk()
root.title("practical assignment-1")
canvas = tk.Canvas(root, height=400, width=700)
canvas.pack()
frame=tk.Frame(root,bg="#184d47")
frame.place(relx=0,rely=0,relwidth=1, relheight=1)
label=tk.Label(frame,text="PRODUCE ROUND KEYS",font=('Times New Roman TUR',15))
label.place(relx=0.1,rely=0.05,relwidth=0.8,relheight=0.1)
#headings

kh=tk.Label(frame, text="KEY in binary", fg="#c64756", bg="#96bb7c",font=('Times New Roman TUR',12))
kh.place(relx=0,rely=0.175,relwidth=0.3,relheight=0.075)
wh = tk.Label(frame, text="HALFWIDTH(16,32,64)", fg="#c64756", bg="#96bb7c",font=('Times New Roman TUR',12))
wh.place(relx=0.35,rely=0.175,relwidth=0.3,relheight=0.075)
rh=tk.Label(frame, text="NO OF ROUNDS(8,16,32)", fg="#c64756", bg="#96bb7c",font=('Times New Roman TUR',12))
rh.place(relx=0.7,rely=0.175,relwidth=0.3,relheight=0.075)
#inputs

k=tk.Entry(frame,font=('Times New Roman TUR',10))
k.place(relx=0,rely=0.275,relwidth=0.3,relheight=0.075)

w=tk.Entry(frame,font=('Times New Roman TUR',10))
w.place(relx=0.35,rely=0.275,relwidth=0.3,relheight=0.075)
r=tk.Entry(frame,font=('Times New Roman TUR',10))
r.place(relx=0.7,rely=0.275,relwidth=0.3,relheight=0.075)


but1=tk.Button(frame,text="ROUND KEYS",command=lambda : encrypt(k.get(),int(r.get()),int(w.get())),bg="#fad586",font=('Times New Roman TUR',15))
but1.place(relx=0.35,rely=0.4,relwidth=0.3,relheight=0.075)

#cipher text output
c = tk.Label(frame, fg="#c64756",font=('Times New Roman TUR',12))
c.place(relx=0.1,rely=0.5,relwidth=0.8)

root.mainloop()