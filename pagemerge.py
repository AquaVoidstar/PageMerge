import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename 
from PIL import Image


class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.pages = []

    def create_widgets(self):
        self.getFile = tk.Button(self, text = "File Select",
                                 fg="green", command = self.file_search)
        self.getFile.pack(side = "top")

        self.convertb = tk.Button(self)
        self.convertb["text"] = "Convert JPG to PDF"
        self.convertb["command"] = self.convert
        self.convertb.pack(side="top")

        self.merge_save = tk.Button(self)
        self.merge_save["text"] = "Merge and Save Doc"
        self.merge_save["command"] = self.merge
        self.merge_save.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def merge(self):
        if len(self.pages) >= 1:
            filename = asksaveasfilename(defaultextension = ".pdf",initialdir="/home/mondo/",
                title="Choose filename")
            self.pages[0].save(filename, save_all=True, append_images = self.pages[1:])
        else:
            print("No files have been selected")

    def file_search(self):
        filename = askopenfilename(initialdir = "/home/mondo/Downloads/", filetypes = ((("jpeg files","*.jpg"),("pdf files","*.pdf"))))
        self.pages.append(filename)


    def convert(self):
        for i, path in enumerate(self.pages):
            if type(self.pages[i]) == str:
                # if self.pages[i][:]
                self.pages[i] = Image.open(path)
                self.pages[i] = self.pages[i].convert('RGB')
    


if __name__ =="__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()