from tkinter import filedialog, messagebox, Button, Tk, Label
import shutil
import os
import easygui

print("___________hi__________")


def file_open_box():  #مسیر فایل
    path = easygui.fileopenbox()
    return path


def directory_open_box():
    path = filedialog.askdirectory()  #مسیر دایرکتوری
    return path


def open_file():
    path = file_open_box()
    try:
        os.startfile(path)
    except:
        messagebox.showinfo("خطا", "!فایل مورد نظر یافت نشد!")


#-------کپی کردن فایل ها-----------
def copy_file():
    source = file_open_box()
    destination = directory_open_box()
    try:
        shutil.copy(source, destination)
        messagebox.showinfo("انجام شد!", "فایل مورد نظر کپی شد.")
    except:
        messagebox.showinfo("خطا!", "کپی انجام نشد")


#-----------پاک کردن فایل----------
def delete_file():
    path = file_open_box()
    try:
        os.remove(path)
        messagebox.showinfo("انجام شد!", "فایل مورد نظر حذف شد.")
    except:
        messagebox.showinfo("خطا!", "فایل حذف نشد")


#-------تغییر نام---------
def rename_file():
    try:
        file = file_open_box()
        print(file)
        path1 = os.path.dirname(file)
        print(path1)
        extendtion = os.path.splitext(file)[1]
        print(extendtion)
        nem_nema = input("enter new name:")
        path2 = os.path.join(path1, nem_nema + extendtion)
        print(path2)
        os.rename(file, path2)
        messagebox.showinfo("انجام شد!", "نام با موفقیت تغییر کرد")
    except:
        messagebox.showinfo("خطا!", "نام تغییر نکرد")


#برای جابه جایی-----
def move_file():
    source = file_open_box()
    destination = directory_open_box()
    if source == destination:
        messagebox.showinfo("خطا!!", "انتقال با خطا مواجه شد!")
    else:
        try:
            shutil.move(source, destination)
            messagebox.showinfo("موفق", "فایل با موفقیت انتقال یافت")
        except:
            messagebox.showinfo("خطا", "انتقال با خطا مواجه شد!")


#-----ساخت فایل و فولدر
def make_directory():
    path = directory_open_box()  #مسیری که باید بگیرم
    name = input("folder,s name:")
    path = os.path.join(path, name)

    try:
        os.mkdir(path)  # مسیر ما را میسازه
        #messagebox.showinfo("موفق", "دایرکتوری با موفقیت ایجاد شد!")
    except:
        messagebox.showinfo("خطا", "دایرکتوری ساخته نشد!")


#----حذف دایرکتوری
def remove_directory():
    path = directory_open_box()
    try:
        os.rmdir(path)
    except:
        messagebox.showinfo("خطا", "دایرکتوری حذف نشد!")


#لیست کل فایل موجود در دایرکتوری
def list_files():
    path = directory_open_box()
    file_list = os.listdir(path)
    for i in file_list:
        print(i)


#-------------tk-------
window = Tk()
window.title("مدیریت فایل من")
window.configure(background='black')
window.geometry('300x350')
Label(window, text="چکاری میخوایید انجام بدید؟" ,width=25,bd=9,pady=6 ).pack()  #پک برای نشان دادن هر کدوم
Button(window, command=open_file, text= "باز کردن " ,bd=8, fg="blue", activebackground="red", bg="white",width=16).pack()
Button(window, command=copy_file, text="کپی کردن " ,bd=8, fg="blue", activebackground="red", bg="white",width=16).pack()
Button(window, command=delete_file, text="حذف کردن" ,bd=8, fg="blue", activebackground="red", bg="white",width=16).pack()
Button(window, command=rename_file, text="تغییر نام " ,bd=8, fg="blue", activebackground="red", bg="white",width=16).pack()
Button(window, command=move_file, text="انتقال فایل" ,bd=8, fg="blue", activebackground="red", bg="white",width=16).pack()
Button(window, command=make_directory, text="ایجاد پوشه" ,bd=8, fg="blue", activebackground="red", bg="white",width=16).pack()
Button(window, command=remove_directory, text="حذف پوشه" ,bd=8, fg="blue", activebackground="red", bg="white",width=16).pack()
Button(window, command=list_files, text="لیست تمام فایل موجود" ,bd=8, fg="blue", activebackground="red", bg="white",width=16).pack()

window.mainloop()  #برای نمایش====
print("end..")
