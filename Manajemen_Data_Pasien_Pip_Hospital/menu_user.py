import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

# --- KONFIGURASI WARNA ---
CARD_COLOR = "#ffffff"     # Warna Kartu (Putih)
BTN_PRIMARY = "#578CA9"    # Tombol Utama
BTN_HOVER = "#4a7a94"      # Warna saat tombol disentuh mouse
BTN_LOGOUT = "#87CEEB"     # Tombol Logout
BTN_LOGOUT_HOVER = "#5eb6dd"
TEXT_COLOR = "#34495e"     # Warna Teks Judul

# --- PATH GAMBAR ABSOLUT ---
basedir = os.path.dirname(os.path.abspath(__file__))
LOGO_FILENAME = os.path.join(basedir, "logo.png")

class MenuUserApp:
    def __init__(window, root):
        # Menggunakan 'window' sebagai pengganti 'self'
        window.root = root
        window.root.title("PIP Hospital Center - User Menu")
        window.root.geometry("400x700")
        window.root.resizable(False, False)

        # Setting tema warna aplikasi (CustomTkinter)
        ctk.set_appearance_mode("Dark") 
        window.root.configure(fg_color="white") 

        # --- 1. CONTAINER UTAMA (KARTU PUTIH ROUNDED) ---
        window.main_frame = ctk.CTkFrame(
            window.root, 
            width=380, 
            height=650, 
            fg_color=CARD_COLOR,  
            corner_radius=30      
        )
        window.main_frame.place(relx=0.5, rely=0.5, anchor="center")
        window.main_frame.pack_propagate(False)

        # --- 2. LOGO GAMBAR ---
        print(f"Mencari logo di: {LOGO_FILENAME}")
        if os.path.exists(LOGO_FILENAME):
            try:
                img_asli = Image.open(LOGO_FILENAME)
                img_ctk = ctk.CTkImage(light_image=img_asli, dark_image=img_asli, size=(120, 100))
                
                label_logo = ctk.CTkLabel(window.main_frame, text="", image=img_ctk)
                label_logo.pack(pady=(50, 10))
            except Exception as e:
                ctk.CTkLabel(window.main_frame, text=f"Error Gambar", text_color="red").pack(pady=(50, 10))
        else:
            ctk.CTkLabel(window.main_frame, text="[LOGO KOSONG]", text_color="red").pack(pady=(50, 10))

        # --- 3. JUDUL ---
        ctk.CTkLabel(
            window.main_frame, 
            text="Selamat Datang di Pip Hospital", 
            font=("Times New Roman", 16, "bold"), 
            text_color=TEXT_COLOR
        ).pack(pady=(5, 0))
        
        ctk.CTkLabel(
            window.main_frame, 
            text="Silakan Pilih Menu", 
            font=("Times New Roman", 14), 
            text_color="gray"
        ).pack(pady=(0, 30))

        # --- 4. TOMBOL MENU (ROUNDED) ---
        # Memanggil fungsi internal juga harus pakai window.
        window.buat_tombol("Read Data Pasien", window.aksi_read_data)
        window.buat_tombol("Permohonan Kunjungan", window.aksi_permohonan)
        window.buat_tombol("Cek Status Kunjungan", window.aksi_cek_status)

        # --- 5. TOMBOL LOGOUT ---
        btn_logout = ctk.CTkButton(
            window.main_frame, 
            text="Logout", 
            font=("Times New Roman", 16, "bold"),
            fg_color=BTN_LOGOUT,        
            text_color="white",         
            hover_color=BTN_LOGOUT_HOVER, 
            height=45,
            width=250,
            corner_radius=15,           
            command=window.aksi_logout
        )
        btn_logout.pack(side="bottom", pady=(0, 50))

    def buat_tombol(window, text, command):
        """Fungsi helper untuk membuat tombol, parameter pertama adalah window"""
        btn = ctk.CTkButton(
            window.main_frame, 
            text=text, 
            font=("Times New Roman", 16, "bold"),
            fg_color=BTN_PRIMARY,       
            text_color="white",         
            hover_color=BTN_HOVER,
            height=50,
            width=280,
            corner_radius=15,           
            command=command
        )
        btn.pack(pady=10)

    # --- FUNGSI AKSI ---
    # Perhatikan parameter pertamanya sekarang adalah 'window'
    def aksi_read_data(window):
        messagebox.showinfo("Info", "Membuka Data Pasien...")

    def aksi_permohonan(window):
        messagebox.showinfo("Info", "Membuka Form Permohonan...")

    def aksi_cek_status(window):
        messagebox.showinfo("Info", "Mengecek Status...")

    def aksi_logout(window):
        if messagebox.askyesno("Konfirmasi", "Yakin ingin keluar?"):
            window.root.destroy()

if __name__ == "__main__":
    root = ctk.CTk()
    app = MenuUserApp(root)
    root.mainloop()