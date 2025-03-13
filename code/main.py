import customtkinter as ctk
from backup_create import create_backup as bc

whatDo = {
    "create": 0,
    "upload": 1
}


class DatabaseBackupApp:
    def __init__(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.app = ctk.CTk()
        self.app.title("MySQL backup")
        self.app.geometry("500x550")

        self.create_widgets()

    def create_widgets(self):
        self.frame = ctk.CTkFrame(self.app)
        self.frame.pack(pady=20, padx=20, fill="both", expand=True)

        self.label_ip = ctk.CTkLabel(self.frame, text="Host")
        self.label_ip.pack(pady=(10, 0))

        self.entry_ip = ctk.CTkEntry(self.frame)
        self.entry_ip.pack(pady=5)

        self.label_port = ctk.CTkLabel(self.frame, text="Port")
        self.label_port.pack(pady=(10, 0))

        self.entry_port = ctk.CTkEntry(self.frame)
        self.entry_port.pack(pady=5)

        self.label_user = ctk.CTkLabel(self.frame, text="User")
        self.label_user.pack(pady=(10, 0))

        self.entry_user = ctk.CTkEntry(self.frame)
        self.entry_user.pack(pady=5)

        self.label_password = ctk.CTkLabel(self.frame, text="Password")
        self.label_password.pack(pady=(10, 0))

        self.entry_password = ctk.CTkEntry(self.frame, show="*")
        self.entry_password.pack(pady=5)

        self.label_db_name = ctk.CTkLabel(self.frame, text="Database Name")
        self.label_db_name.pack(pady=(10, 0))

        self.entry_db_name = ctk.CTkEntry(self.frame)
        self.entry_db_name.pack(pady=5)

        self.create_button = ctk.CTkButton(self.frame, text="Create", command=self.create_button_callback)
        self.create_button.pack(pady=20)

    def create_button_callback(self):
        ip = self.entry_ip.get()
        port = self.entry_port.get()
        user = self.entry_user.get()
        password = self.entry_password.get()
        db_name = self.entry_db_name.get()

        bc(db_host=ip, db_name=db_name, db_user=user, db_password=password, db_port=int(port))
        print(f"IP: {ip}, Port: {port}, User: {user}, Password: {password}, Database: {db_name}")

    def run(self):
        self.app.mainloop()


if __name__ == "__main__":
    app = DatabaseBackupApp()
    app.run()
