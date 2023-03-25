from tkinter import *
from func import *
from PIL import ImageTk, Image


class Products:
    def __init__(self, name, price, description, image):
        self.name = name
        self.price = price
        self.description = description
        self.image = image


class Giohang:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)

    def tong(self):
        return sum([p.price for p in self.products])


class App:
    def __init__(self, master):
        self.master = master
        self.master.title("ỨNG DỤNG BÁN HÀNG")

        # Header
        self.header = Frame(self.master, bg="white", pady=20)
        self.header.pack(side=TOP, fill=X)

        # Mở và xử lý ảnh
        image = Image.open("C:\\Users\Admin\OneDrive\Máy tính\Kỹ Thuật Lập Trình\\techhub.png")
        image = image.resize((100, 50))  # Thay đổi kích thước ảnh
        # Tạo đối tượng PhotoImage từ ảnh đã xử lý
        photo = ImageTk.PhotoImage(image)
        # Tạo label để hiển thị ảnh trên giao diện
        self.logo = Label(self.header, image=photo, bg="white")
        self.logo.image = photo
        self.logo.place(relx=0.01, rely=0.5, anchor=W)

        self.name = Label(self.header, text="TECH HUB SHOP", font=("Times New Roman", 35), bg="white")
        self.name.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.login_button = Button(self.header, text="Đăng nhập/Đăng ký", font=("Times New Roman", 12), bg="white")
        self.login_button.pack(padx=10, anchor=E)

        # Sidebar
        self.sidebar = Frame(self.master, bg="white", padx=10, pady=10)
        self.sidebar.pack(side=LEFT, fill=Y)
        self.categories = ["Laptop", "Laptop Gaming", "PC Gaming", "PC Đồ Họa", "Apple", "Màn Hình", "Bàn phím", "Chuột", "Tai nghe - Loa", "Phụ kiện"]

        for category in self.categories:
            button = Button(self.sidebar, text=category, font=("Times New Roman", 12), bg="white")
            button.pack(side=TOP, pady=10)

        # Tạo một canvas để chứa danh sách sản phẩm
        self.canvas = Canvas(master, bg="white", highlightthickness=0)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)

        # Tạo một scrollbar và liên kết nó với canvas
        self.scrollbar = Scrollbar(master, orient=VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.canvas.config(yscrollcommand=self.scrollbar.set)

        # Tạo một frame để chứa danh sách sản phẩm
        self.product_list = Frame(self.canvas, padx=10, pady=10, bg="white")
        self.canvas.create_window((0, 0), window=self.product_list, anchor=NW)

        # Thêm danh sách sản phẩm vào frame
        self.products = [Products("Áo sơ mi nam", 500000, "Chất liệu cotton, kiểu dáng trẻ trung",
                                  "https://ik.imagekit.io/nhom2/default-image.jpg?updatedAt=1679737574283"),
                         Products("Điện thoại Samsung Galaxy S21", 20000000,
                                  "Màn hình 6.2 inch, RAM 8GB, bộ nhớ 128GB",
                                  "https://ik.imagekit.io/nhom2/default-image.jpg?updatedAt=1679737574283"),
                         Products("Sữa tắm Baby & Mom", 100000, "Dành cho trẻ em, không gây kích ứng da",
                                  "https://ik.imagekit.io/nhom2/default-image.jpg?updatedAt=1679737574283"),
                         Products("Sách Harry Potter và Hòn đá Phù thủy", 200000,
                                  "Tác giả J.K. Rowling, phiên bản bìa mềm",
                                  "https://ik.imagekit.io/nhom2/default-image.jpg?updatedAt=1679737574283"),
                         Products("Son môi Maybelline Superstay Matte Ink", 150000,
                                  "Chất son mịn, không bị lem, lên màu chuẩn",
                                  "https://ik.imagekit.io/nhom2/default-image.jpg?updatedAt=1679737574283")]

        for product in self.products:
            frame = Frame(self.product_list, bg="white", bd=1, relief=SOLID)
            frame.pack(side=TOP, pady=10, fill=X)
            photo_sanpham = xuly_image(product.image, 150, 150)
            image_label = Label(frame, image=photo_sanpham, bg="white")
            image_label.photo = photo_sanpham
            image_label.pack(side=LEFT, padx=10, pady=10)

            product_info = Frame(frame, bg="white")
            product_info.pack(side=LEFT, fill=BOTH, expand=True)

            name_label = Label(product_info, text=product.name, font=("Times New Roman", 16), bg="white")
            name_label.pack(side=TOP, padx=10, pady=10)

            price_label = Label(product_info, text="Giá: {} VNĐ".format(product.price), font=("Times New Roman", 12), bg="white")
            price_label.pack(side=TOP, padx=10, pady=10)

            description_label = Label(product_info, text=product.description, font=("Times New Roman", 12), bg="white",
                                      wraplength=200)
            description_label.pack(side=TOP, padx=10, pady=10)

            add_to_cart_button = Button(product_info, text="Thêm vào giỏ hàng", font=("Times New Roman", 12), bg="white",
                                        command=lambda p=product: self.add_to_cart(p))
            add_to_cart_button.pack(side=TOP, padx=10, pady=10)

        # Giỏ hàng
        self.cart = Giohang()
        self.cart_frame = Frame(self.master, bg="white", padx=10, pady=10)
        self.cart_frame.pack(side=RIGHT, fill=BOTH)

        cart_title = Label(self.cart_frame, text="Giỏ hàng", font=("Times New Roman", 16), bg="white")
        cart_title.pack(side=TOP, pady=10)

        self.cart_list = Frame(self.cart_frame, bg="white")
        self.cart_list.pack(side=TOP, fill=BOTH, expand=True)

        self.total_label = Label(self.cart_frame, text="Tổng tiền: 0 VNĐ", font=("Times New Roman", 14), bg="white")
        self.total_label.pack(side=BOTTOM, pady=10)

    def add_to_cart(self, product):
        self.cart.add_product(product)
        cart_item = Frame(self.cart_list, bg="white")
        cart_item.pack(side=TOP, fill=X, pady=10)

        name_label = Label(cart_item, text=product.name, font=("Times New Roman", 12), bg="white")
        name_label.pack(side=LEFT, padx=10)

        price_label = Label(cart_item, text="{} VNĐ".format(product.price), font=("Times New Roman", 12), bg="white")
        price_label.pack(side=RIGHT, padx=10)

        remove_button = Button(cart_item, text="Xóa", font=("Times New Roman", 12), bg="white",
                               command=lambda p=product: self.remove_from_cart(p, cart_item))
        remove_button.pack(side=RIGHT, padx=10)

        self.total_label.config(text="Tổng tiền: {} VNĐ".format(self.cart.tong()))

    def remove_from_cart(self, product, cart_item):
        self.cart.remove_product(product)
        cart_item.destroy()
        self.total_label.config(text="Tổng tiền: {} VNĐ".format(self.cart.tong()))


root = Tk()
root.geometry("1500x700")
app = App(root)
root.mainloop()
