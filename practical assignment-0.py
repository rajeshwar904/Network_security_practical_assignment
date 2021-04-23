import tkinter as tk

  
"""Function to encrypt the plaintext and display the ciphertext in "ciphertext" label"""
def ptoc(entry):
	"""Defining the character set"""
	c=['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a',
		'Z','Y','X','W','V','U','T','S','R','Q','P','O','N','M','L','K','J','I','H','G','F','E','D','C','B','A',' ']
	"""Dictionary used to get the position of the ciphertext character in the character set"""
	dic={   'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,
	        'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,
	        'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,
	        'w':22,'x':23,'y':24,'z':25,
	        'A' : 26,'B' : 27,'C' : 28,'D' : 29,'E' : 30,'F' : 31,'G' : 32,'H' : 33,'I' : 34,'J' : 35,'K' : 36,'L' : 37,
	        'M' : 38,'N' : 39,
	        'O' : 40,'P' : 41,'Q' : 42,'R' : 43,'S' : 44,'T' : 45,'U' : 46,'V' : 47,'W' : 48,'X' : 49,'Y' : 50,'Z' : 51,' ':52
	    }
	"""Building the ciphertext for the plaintext"""
	ret = ""
	for i in entry:
		ret=ret + c[dic[i]]
	ciphertext['text']=ret

"""Function to decrypt the ciphertext and display the plaintext in "plaintext_decryption" label"""
def ctop(entry):
	"""Defining the character set"""
	c=['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a',
		'Z','Y','X','W','V','U','T','S','R','Q','P','O','N','M','L','K','J','I','H','G','F','E','D','C','B','A',' ']
	"""Dictionary used to get the position of the plaintext character in the character set"""
	dic={   'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,
	        'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,
	        'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,
	        'w':22,'x':23,'y':24,'z':25,
	        'A' : 26,'B' : 27,'C' : 28,'D' : 29,'E' : 30,'F' : 31,'G' : 32,'H' : 33,'I' : 34,'J' : 35,'K' : 36,'L' : 37,
	        'M' : 38,'N' : 39,'O' : 40,
	        'P' : 41,'Q' : 42,'R' : 43,'S' : 44,'T' : 45,'U' : 46,'V' : 47,'W' : 48,'X' : 49,'Y' : 50,'Z' : 51,' ' : 52
	    }
	"""Building the plaintext for the ciphertext"""
	ret = ""
	for i in entry:
		ret=ret + c[dic[i]]
	plaintext_decryption['text']=ret

"""defining Root"""
root=tk.Tk()
"""Defining the initial size of the root"""
canvas = tk.Canvas(root, height=400, width=700)
canvas.pack()

"""Defining the frame for decryption process"""
frame=tk.Frame(root,bg="#184d47")
frame.place(relx=0.1,rely=0.05,relwidth=0.8, relheight=0.4)

"""Labels/Headings for the display"""
label=tk.Label(frame,text="For the encryption process",font=('Times New Roman TUR',15))
label.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.15)
encrypt = tk.Label(frame, text="PLAINTEXT", fg="#c64756", bg="#96bb7c",font=('Times New Roman TUR',10))
encrypt.place(relx=0.05,rely=0.35,relwidth=0.35,relheight=0.15)
output=tk.Label(frame, text="CIPHER TEXT", fg="#c64756", bg="#96bb7c",font=('Times New Roman TUR',10))
output.place(relx=0.6,rely=0.35,relwidth=0.35,relheight=0.15)
arrow=tk.Label(frame,text="---->",font=('MS Sans Serif',10))
arrow.place( relx=0.45,rely=0.5,relwidth=0.1,relheight=0.1)
"""Taking the input from the user interface"""
plaintext=tk.Entry(frame,font=30)
plaintext.place(relx=0.05,rely=0.55,relwidth=0.35,relheight=0.15)
"""Label to display output"""
ciphertext=tk.Label(frame,font=30)
ciphertext.place(relx=0.6,rely=0.55,relwidth=0.35,relheight=0.15)
"""Button for encryption"""
but1=tk.Button(frame,text="ENCRYPT",command=lambda : ptoc(plaintext.get()),bg="#fad586",font=('Times New Roman TUR',12))
but1.place(relx=0.25,rely=0.8,relwidth=0.5,relheight=0.15)
"""Defining the frame for decryption process"""
frame1=tk.Frame(root,bg="#184d47")
frame1.place(relx=0.1,rely=0.55,relwidth=0.8, relheight=0.4)
"""Labels/Headings for the display"""
label1=tk.Label(frame1,text="For the decryption process",font=('Times New Roman TUR',15))
label1.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.2)
encrypt1 = tk.Label(frame1, text="CIPHER TEXT", fg="#c64756", bg="#96bb7c",font=('Times New Roman TUR',10))
encrypt1.place(relx=0.05,rely=0.35,relwidth=0.35,relheight=0.15)
output1=tk.Label(frame1, text="PLAINTEXT", fg="#c64756", bg="#96bb7c",font=('Times New Roman TUR',10))
output1.place(relx=0.6,rely=0.35,relwidth=0.35,relheight=0.15)
arrow1=tk.Label(frame1,text="---->",font=('MS Sans Serif',10))
arrow1.place( relx=0.45,rely=0.5,relwidth=0.1,relheight=0.1)
"""Taking the input from the user interface"""
ciphertext_input=tk.Entry(frame1,font=30)
ciphertext_input.place(relx=0.05,rely=0.55,relwidth=0.35,relheight=0.15)
"""Label to display output"""
plaintext_decryption=tk.Label(frame1,font=30)
plaintext_decryption.place(relx=0.6,rely=0.55,relwidth=0.35,relheight=0.15)
"""Button for decryption"""
but11=tk.Button(frame1,text="DECRYPT",command=lambda : ctop(ciphertext_input.get()),bg="#fad586",font=('Times New Roman TUR',12))
but11.place(relx=0.25,rely=0.8,relwidth=0.5,relheight=0.15)

root.mainloop()
