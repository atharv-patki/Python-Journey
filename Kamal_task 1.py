from tkinter import *
from requests import *
root=Tk()
root.title("Motivational MSG App By Atharv Patki")
root.geometry("1000x400+300+50")
f=("Lucida Calligraphy",30,"bold")
ft=("Cambria",30,"italic")
root.configure(bg="lightblue") 	
def gm():
	try:
		url="https://zenquotes.io/api/random"
		res=get(url)
		data=res.json()
		quote=data[0]["q"]
		lab.configure(text=quote,wraplength=700)
	except Exception as e:
		msg="issue"+str(e)
		lab.configure(text=msg)
btn = Button(root, text="Get Msg", font=ft, command=gm, bg="lightpink", fg="black", padx=20, pady=10)
lab = Label(root, font=f, bg="lightblue", fg="black", wraplength=700)
btn.pack(pady=50)
lab.pack(pady=130)
root.mainloop()