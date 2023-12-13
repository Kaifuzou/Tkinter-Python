#Trong Tkinter, grid là một phương thức được sử dụng để định vị và định kích thước
# cho các widget trên giao diện người dùng bằng cách chia giao diện thành các ô lưới.
# Dưới đây là một số thuộc tính quan trọng của phương thức grid:

import tkinter as tk

# Tạo cửa sổ
window = tk.Tk()
window.title("Grid")  # Đặt tiêu đề cửa sổ

#1. row và column: Xác định vị trí hàng và cột của widget trong lưới.
label = tk.Label(window, text="Hello, Tkinter!")
label.grid(row=0, column=0)

#2.sticky: Xác định cách widget sẽ dính vào ô lưới. Giá trị có thể là bất kỳ sự kết hợp nào
# của "N" (North), "S" (South), "E" (East), "W" (West), "NE", "NW", "SE", "SW", hoặc "NSWE"
#label.grid(row=0, column=0, sticky="w")

#3. rowspan và columnspan: Xác định số lượng hàng và cột mà widget sẽ chiếm.
#label.grid(row=0, column=0, rowspan=2, columnspan=2)

#4.padx và pady: Xác định khoảng cách ngang và dọc giữa widget và các đường lưới xung quanh.
#label.grid(row=0, column=0, padx=10, pady=10)

#5.ipadx và ipady: Xác định khoảng cách ngang và dọc giữa nội dung của widget và khung xung quanh nó.
#label.grid(row=0, column=0, ipadx=5, ipady=5)

#6. columnconfigure và rowconfigure: Xác định cấu hình của cột và hàng, chẳng hạn như trọng số của chúng.
#window.columnconfigure(0, weight=1)
#window.rowconfigure(0, weight=1)


# Chạy vòng lặp cửa sổ
window.mainloop()
