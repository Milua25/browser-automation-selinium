import tkinter as tk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Web Automation GUI")

        # Login Frame
        self.login_frame = tk.Frame(self.root)
        self.login_frame.pack(padx=10, pady=10)

        tk.Label(self.login_frame, text="Username:").grid(row=0, column=0, sticky=tk.W)
        tk.Label(self.login_frame, text="Password:").grid(row=1, column=0, sticky=tk.W)

        self.entry_username = tk.Entry(self.login_frame)
        self.entry_username.grid(row=0, column=1, sticky=tk.EW)
        self.entry_password = tk.Entry(self.login_frame)
        self.entry_password.grid(row=1, column=1, sticky=tk.EW)


        # Form Submission Frame
        self.form_frame = tk.Frame(self.root)
        self.form_frame.pack(padx=10, pady=10)

        tk.Label(self.form_frame, text="Full Name:").grid(row=0, column=0, sticky=tk.W)
        tk.Label(self.form_frame, text="Email:").grid(row=1, column=0, sticky=tk.W)
        tk.Label(self.form_frame, text="Current Address:").grid(row=2, column=0, sticky=tk.W)
        tk.Label(self.form_frame, text="Permanent Address:").grid(row=3, column=0, sticky=tk.W)

        self.entry_fullname = tk.Entry(self.form_frame)
        self.entry_fullname.grid(row=0, column=1, sticky=tk.EW)
        self.entry_email = tk.Entry(self.form_frame)
        self.entry_email.grid(row=1, column=1, sticky=tk.EW)
        self.entry_current_address = tk.Entry(self.form_frame)
        self.entry_current_address.grid(row=2, column=1, sticky=tk.EW)
        self.entry_permanent_address = tk.Entry(self.form_frame)
        self.entry_permanent_address.grid(row=3, column=1, sticky=tk.EW)

        # Submit and Close
        self.button_frame = tk.Frame()
        self.button_frame.pack(padx=10, pady=10)

        tk.Button(self.button_frame, text="Submit", command=self.submit_data).grid(row=0, column=0, padx=5)
        tk.Button(self.button_frame, text="Close Browser", command=self.close_browser).grid(row=0, column=1, padx=5)


    def submit_data(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        current_address = self.entry_current_address.get()
        permanent_address = self.entry_permanent_address.get()


    def close_browser(self):
        pass

root = tk.Tk()
app = App(root)
root.mainloop()
