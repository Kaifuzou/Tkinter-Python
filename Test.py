import tkinter as tk

# Tạo cửa sổ
window = tk.Tk()
window.title("PHạm Minh Hội")

# Tạo Frame chính
main_frame = tk.Frame(window)
main_frame.pack()

# Tạo 4 Frame con
frame1 = tk.Frame(main_frame)
frame2 = tk.Frame(main_frame)
frame3 = tk.Frame(main_frame)
frame4 = tk.Frame(main_frame)

# Hiển thị Frame con trong Frame chính
frame1.grid(row=0, column=0)
frame2.grid(row=0, column=1)
frame3.grid(row=1, column=0)
frame4.grid(row=1, column=1)

# Tạo các Label trong các Frame con
label1 = tk.Label(frame1, text="Ho va ten")
label2 = tk.Label(frame2, text="Pham Minh Hoi")
label3 = tk.Label(frame3, text="MSSV")
label4 = tk.Label(frame4, text="62133748")

# Hiển thị Label trong các Frame con
label1.pack()
label2.pack()
label3.pack()
label4.pack()

# Bắt đầu vòng lặp chạy cửa sổ
window.mainloop()
