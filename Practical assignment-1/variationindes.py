import matplotlib.pyplot as plt
from encryptiononly import *
import tkinter as tk
from PIL import ImageTk, Image


#This functions calls the encryption function with required parameters and finally plots the graph to demonstrate avalanche effect
def encrypt(plaintext: str,key: str, r: int=16, hw:int=32, hdp:int=0, hdk:int=0):

	rkb,round_ciphertexts,final= encryption(plaintext,key,r,hw,0,0)
	rkb1,round_ciphertexts1,final1=  encryption(plaintext,key,r,hw,hdp,hdk)
	# The round numbers on the x-axis
	x = [a for a in range(1,r+1)]
	# The difference on number of characters in every round between the round ciphertexts on the y-axis
	y=calc_diff(round_ciphertexts,round_ciphertexts1)
	
	# plotting the points 
	plt.plot(x, y)
  
	# naming the x axis
	plt.xlabel('Number of rounds')
	# naming the y axis
	plt.ylabel('Difference of number of bits')
  
	# giving a title to the graph
	plt.title('Avalanche effect')
  
	# function to show the plot
	plt.show()


root=tk.Tk()
root.title("practical_assignment-1")

#Fixing the initial size of the canvas
canvas = tk.Canvas(root, height=400, width=700)
canvas.pack()
frame=tk.Frame(root,bg="#184d47")
frame.place(relx=0.05,rely=0.05,relwidth=0.9, relheight=0.9)
label=tk.Label(frame,text="Avalanche effect with different hyperparameters",font=('Times New Roman TUR',17))
label.place(relx=0.1,rely=0.05,relwidth=0.8,relheight=0.1)

#headings 
ph = tk.Label(frame, text="PLAINTEXT", fg="#c64756", bg="#96bb7c",font=('Times New Roman TUR',12))
ph.place(relx=0.05,rely=0.175,relwidth=0.35,relheight=0.075)
kh=tk.Label(frame, text="KEY", fg="#c64756", bg="#96bb7c",font=('Times New Roman TUR',12))
kh.place(relx=0.6,rely=0.175,relwidth=0.35,relheight=0.075)

#plaintext and key inputs
p=tk.Entry(frame,font=30)
p.place(relx=0.05,rely=0.275,relwidth=0.35,relheight=0.075)
k=tk.Entry(frame,font=30)
k.place(relx=0.6,rely=0.275,relwidth=0.35,relheight=0.075)

#headings
wh = tk.Label(frame, text="HALF-WIDTH (16,32,64)", fg="#c64756", bg="#96bb7c",font=('Times New Roman TUR',12))
wh.place(relx=0.05,rely=0.375,relwidth=0.35,relheight=0.075)
rh=tk.Label(frame, text="NO.OF ROUNDS(8,16,32)", fg="#c64756", bg="#96bb7c",font=('Times New Roman TUR',12))
rh.place(relx=0.6,rely=0.375,relwidth=0.35,relheight=0.075)

#halfwidth and number of rounds inputs
w=tk.Entry(frame,font=30)
w.place(relx=0.05,rely=0.475,relwidth=0.35,relheight=0.075)
r=tk.Entry(frame,font=30)
r.place(relx=0.6,rely=0.475,relwidth=0.35,relheight=0.075)


#headings
hdph = tk.Label(frame, text="HAMMING_DIST FOR KEY", fg="#c64756", bg="#96bb7c",font=('Times New Roman TUR',12))
hdph.place(relx=0.05,rely=0.575,relwidth=0.35,relheight=0.075)
hdkh=tk.Label(frame, text="HAMMING DIST FOR PLAINTEXT", fg="#c64756", bg="#96bb7c",font=('Times New Roman TUR',11))
hdkh.place(relx=0.6,rely=0.575,relwidth=0.35,relheight=0.075)


#hamming distacne for plaintext and hamming distance of key inputs
hdp=tk.Entry(frame,font=30)
hdp.place(relx=0.05,rely=0.675,relwidth=0.35,relheight=0.075)
hdk=tk.Entry(frame,font=30)
hdk.place(relx=0.6,rely=0.675,relwidth=0.35,relheight=0.075)

#Button to start the encryption process
but1=tk.Button(frame,text="PLOT GRAPH",command=lambda : encrypt(p.get(),k.get(),int(r.get()),int(w.get()),int(hdp.get()),int(hdk.get())),bg="#fad586",font=('Times New Roman TUR',15))
but1.place(relx=0.35,rely=0.825,relwidth=0.3,relheight=0.075)




root.mainloop()

