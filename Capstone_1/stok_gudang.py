import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# =========================
# KONEKSI DATABASE
# =========================
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345",
        database="db_gudang"
    )

# =========================
# CRUD FUNCTION
# =========================
def get_all_data():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM sparepart")
    data = cursor.fetchall()
    db.close()
    return data

def insert_data(nama, kategori, merk, harga, stok, tanggal):
    try:
        datetime.strptime(tanggal, "%Y-%m-%d")

        if not isinstance(harga, int) or not isinstance(stok, int):
            raise ValueError("Harga dan stok harus angka")

        db = connect_db()
        cursor = db.cursor()

        cursor.execute("SELECT id, stok FROM sparepart WHERE nama_part=%s AND merk=%s", (nama, merk))
        result = cursor.fetchone()

        if result:
            new_stok = result[1] + stok
            cursor.execute("UPDATE sparepart SET stok=%s WHERE id=%s", (new_stok, result[0]))
        else:
            sql = """INSERT INTO sparepart 
                     (nama_part, kategori, merk, harga, stok, tanggal_masuk)
                     VALUES (%s, %s, %s, %s, %s, %s)"""
            cursor.execute(sql, (nama, kategori, merk, harga, stok, tanggal))

        db.commit()
        db.close()
        return "success"

    except ValueError as ve:
        return f"error: {str(ve)}"
    except Exception as e:
        return f"error: {str(e)}"

def update_data(id, nama, kategori, merk, harga, stok, tanggal):
    db = connect_db()
    cursor = db.cursor()
    sql = """UPDATE sparepart SET 
             nama_part=%s, kategori=%s, merk=%s, harga=%s, stok=%s, tanggal_masuk=%s
             WHERE id=%s"""
    cursor.execute(sql, (nama, kategori, merk, harga, stok, tanggal, id))
    db.commit()
    db.close()

def delete_data(id, jumlah_hapus):
    db = connect_db()
    cursor = db.cursor()

    cursor.execute("SELECT stok FROM sparepart WHERE id=%s", (id,))
    result = cursor.fetchone()

    if result:
        if jumlah_hapus >= result[0]:
            cursor.execute("DELETE FROM sparepart WHERE id=%s", (id,))
        else:
            cursor.execute("UPDATE sparepart SET stok=%s WHERE id=%s", (result[0] - jumlah_hapus, id))

    db.commit()
    db.close()

def get_dataframe():
    db = connect_db()
    df = pd.read_sql("SELECT * FROM sparepart", db)
    db.close()
    return df

# =========================
# GUI APPLICATION
# =========================
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Stok Gudang")
        self.root.geometry("1000x600")
        self.root.configure(bg="#ecf0f1")

        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview", rowheight=28)
        style.map("Treeview", background=[("selected", "#3498db")])

        tk.Label(self.root, text="APLIKASI STOK GUDANG SPAREPART",
                 font=("Arial", 16, "bold"),
                 bg="#2c3e50", fg="white", pady=10).pack(fill="x")

        main_frame = tk.Frame(self.root, bg="#ecf0f1")
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        form_frame = tk.Frame(main_frame, bg="#ecf0f1")
        form_frame.pack(side="left", fill="y", padx=10)

        table_frame = tk.Frame(main_frame)
        table_frame.pack(side="right", fill="both", expand=True)

        # VARIABLES
        self.nama = tk.StringVar()
        self.kategori = tk.StringVar()
        self.merk = tk.StringVar()
        self.harga = tk.StringVar()
        self.stok = tk.StringVar()
        self.tanggal = tk.StringVar()
        self.selected_id = None

        # FORM
        labels = ["Nama", "Kategori", "Merk", "Harga", "Stok", "Tanggal (YYYY-MM-DD)"]
        vars = [self.nama, self.kategori, self.merk, self.harga, self.stok, self.tanggal]

        for i, (l, v) in enumerate(zip(labels, vars)):
            tk.Label(form_frame, text=l, bg="#ecf0f1", font=("Arial", 10, "bold"))\
                .grid(row=i, column=0, sticky="w", pady=5)
            tk.Entry(form_frame, textvariable=v, width=25)\
                .grid(row=i, column=1, pady=5)

        # BUTTON
        btn_frame = tk.Frame(form_frame, bg="#ecf0f1")
        btn_frame.grid(row=6, column=0, columnspan=2, pady=15)

        tk.Button(btn_frame, text="Tambah", width=12, bg="#2ecc71", fg="white", command=self.add).grid(row=0, column=0, padx=5, pady=5)
        tk.Button(btn_frame, text="Update", width=12, bg="#3498db", fg="white", command=self.update).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(btn_frame, text="Delete", width=12, bg="#e74c3c", fg="white", command=self.delete).grid(row=1, column=0, padx=5, pady=5)
        tk.Button(btn_frame, text="Clear", width=12, bg="#95a5a6", fg="white", command=self.clear).grid(row=1, column=1, padx=5, pady=5)
        tk.Button(btn_frame, text="Statistik", width=12, bg="#f39c12", fg="white", command=self.show_statistik).grid(row=2, column=0, padx=5, pady=5)
        tk.Button(btn_frame, text="Visualisasi", width=12, bg="#9b59b6", fg="white", command=self.visualisasi).grid(row=2, column=1, padx=5, pady=5)

        # TABLE
        columns = ("id","nama","kategori","merk","harga","stok","tanggal")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings")

        for col in columns:
            self.tree.heading(col, text=col.upper())
            self.tree.column(col, anchor="center", width=100)

        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)

        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.tree.bind("<<TreeviewSelect>>", self.select_data)

        self.load_data()

    def load_data(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for data in get_all_data():
            self.tree.insert("", "end", values=data)

    def select_data(self, event):
        data = self.tree.item(self.tree.focus(), "values")
        if data:
            self.selected_id = data[0]
            self.nama.set(data[1])
            self.kategori.set(data[2])
            self.merk.set(data[3])
            self.harga.set(data[4])
            self.stok.set(data[5])
            self.tanggal.set(data[6])

    def validate(self):
        try:
            int(self.harga.get())
            int(self.stok.get())
            return True
        except:
            return False

    def add(self):
        if not self.validate():
            messagebox.showerror("Error", "Harga/Stok harus angka")
            return

        result = insert_data(
            self.nama.get(),
            self.kategori.get(),
            self.merk.get(),
            int(self.harga.get()),
            int(self.stok.get()),
            self.tanggal.get()
        )

        if "error" in result:
            messagebox.showerror("Error", result)
        else:
            self.load_data()
            messagebox.showinfo("Sukses", "Data berhasil ditambahkan / stok diperbarui")

    def update(self):
        if not self.selected_id:
            messagebox.showwarning("Warning","Pilih data dulu")
            return
        
        from datetime import datetime
        
        try:
            datetime.strptime(self.tanggal.get(), "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Error", "Format tanggal harus YYYY-MM-DD")
            return
        
        try:
            harga = int(self.harga.get())
            stok = int(self.stok.get())
        except:
            messagebox.showerror("Error", "Harga dan stok harus angka")
            return
        
        confirm = messagebox.askyesno("Konfirmasi","Apakah yakin update data?")
        if confirm:
            update_data(
                self.selected_id,
                self.nama.get(),
                self.kategori.get(),
                self.merk.get(),
                int(self.harga.get()),
                int(self.stok.get()),
                self.tanggal.get()
            )
        self.load_data()
        messagebox.showinfo("Sukses","Data diupdate")

    def delete(self):
        if not self.selected_id:
            return

        jumlah = simpledialog.askinteger("Input", "Jumlah stok dikurangi:")
        if jumlah:
            delete_data(self.selected_id, jumlah)
            self.load_data()

    def clear(self):
        self.selected_id = None
        self.nama.set("")
        self.kategori.set("")
        self.merk.set("")
        self.harga.set("")
        self.stok.set("")
        self.tanggal.set("")

    def show_statistik(self):
        df = get_dataframe()
        if df.empty:
            return

        info = f"""
Rata-rata Harga: {df['harga'].mean():,.0f}
Rata-rata Stok : {df['stok'].mean():,.0f}
Total Stok     : {df['stok'].sum():,.0f}
"""
        messagebox.showinfo("Statistik", info)

    def visualisasi(self):
        df = get_dataframe()
        if df.empty:
            return

        win = tk.Toplevel(self.root)
        win.title("Dasboard Visualisasi")
        win.geometry("300x200")

        tk.Label(win, text="Pilih Jenis Visualisasi", font=("Arial", 12, "bold")).pack(pady=10)

        tk.Button(win, text="Pie Chart (Kategori)", width=25, command=lambda: self.show_pie(df)).pack(pady=5)
        tk.Button(win, text="Bar Chart (Merk)", width=25, command=lambda: self.show_bar(df)).pack(pady=5)
        tk.Button(win, text="Histogram Harga", width=25, command=lambda: self.show_hist(df)).pack(pady=5)

    def show_pie(self, df):
        plt.figure(figsize=(6,6))

        df["kategori"].value_counts().plot.pie(
            autopct='%1.1f%%',
            startangle=90,
            colors=plt.cm.Pastel1.colors
        )

        plt.title("Distribusi Kategori Sparepart", fontsize=14)
        plt.ylabel("")  # hilangkan label kosong
        plt.tight_layout()
        plt.show()

    def show_bar(self, df):
        plt.figure(figsize=(8,5))

        data = df["merk"].value_counts()
        bars = data.plot(kind='bar', color='skyblue')

        plt.title("Jumlah Sparepart per Merk", fontsize=14)
        plt.xlabel("Merk")
        plt.ylabel("Jumlah")
        plt.xticks(rotation=45)

        # Tambahkan angka di atas bar
        for i, v in enumerate(data):
            plt.text(i, v + 0.5, str(v), ha='center')

        plt.tight_layout()
        plt.show()

    def show_hist(self, df):
        plt.figure(figsize=(7,5))

        plt.hist(df["harga"], bins=10, color='orange', edgecolor='black')

        plt.title("Distribusi Harga Sparepart", fontsize=14)
        plt.xlabel("Harga")
        plt.ylabel("Frekuensi")

        plt.tight_layout()
        plt.show()

# =========================
# MAIN
# =========================
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()