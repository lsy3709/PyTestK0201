from tkinter import *
from tkinter.filedialog import *
from tkinter.simpledialog import *

## 함수 선언 부분 ##
def func_open() :
    filename = askopenfilename(parent = window, filetypes = (("GIF 파일", "*.gif"), ("모든 파일", "*.*")))
    photo = PhotoImage(file = filename)

    width = photo.width()
    height = photo.height()

    for i in range(height) :
        for k in range(width) :
            r, g, b = photo.get(k, i)
            print("rgb의 값 조회  r : %d, g: %d, b: %d" %(r,g,b))
            grey = int((r+g+b)/3)
            print("grey의 값 조회 grey : %d" % grey)
            print ("RGB 코드의 값 조회 : #%02x%02x%02x " % (grey, grey, grey) )
            photo.put("#%02x%02x%02x" % (grey, grey, grey), (k, i))

    pLabel.configure(image = photo)
    pLabel.image = photo

def func_exit() :
    window.quit()
    window.destroy()


## 메인 코드  부분 ##
window = Tk()
window.geometry("500x500")
window.title("명화 감상하기(흑백)")

photo = PhotoImage()
pLabel = Label(window, image = photo)
pLabel.pack(expand=1, anchor = CENTER)

mainMenu = Menu(window)
window.config(menu = mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "파일", menu = fileMenu)
fileMenu.add_command(label = "파일 열기", command = func_open)
fileMenu.add_separator()
fileMenu.add_command(label = "프로그램 종료", command = func_exit)





window.mainloop()
