import tkinter as tk

VERSION = 0.8


class Application(tk.Frame):
    x_values = []

    def __init__(self, parent):
        super().__init__(parent)
        self.pack()
        self.parent = parent

        self.header = Header(self)
        self.content = Content(self)
        self.footer = Footer(self)

        self.winfo_toplevel().title(f"Standard Deviation Calculator v{VERSION}")


class Header(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(side=tk.TOP)
        self.parent = parent

        self.header_text = tk.Label(self, text="Standard Deviation Calculator")
        self.header_text["font"] = ("Helvetica", 22)
        self.header_text.configure(padx=20, pady=20)
        self.header_text.pack()


class Content(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(side=tk.TOP)
        self.parent = parent

        self.user_input = UserInput(self)
        self.results = Results(self)


class UserInput(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(side=tk.LEFT, ipadx=20)
        self.parent = parent

        self.insert_xi = tk.Label(self, text="Enter Xi:")
        self.insert_xi["font"] = ("Helvetica", 14)
        self.insert_xi.pack(side=tk.TOP)

        self.x = X(self)
        self.total_entries = TotalEntries(self)
        self.add_reset_help = AddResetHelp(self)

        self.calculate = tk.Button(
            self,
            text="Calculate data",
            bg="PaleGreen2",
            activebackground="PaleGreen1",
            width=20,
        )
        self.calculate["font"] = ("Helvetica", 14)
        self.calculate.pack(side=tk.TOP)


class X(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(side=tk.TOP)
        self.parent = parent

        self.x_label = tk.Label(self, text="X = ")
        self.x_label["font"] = ("Helvetica", 12)
        self.x_label.pack(side=tk.LEFT)

        self.x_entry = tk.Entry(self)
        self.x_entry.pack(side=tk.RIGHT)
        self.x_entry.focus_force()
        self.x_entry.bind("<Return>", self.add_x_value)

    def add_x_value(self, event=None):
        value = self.x_entry.get()
        if value:
            Application.x_values.append(float(value))
            curr = self.parent.total_entries.current_total_entries
            curr.set(len(Application.x_values))
            self.clean_entry()

    def clean_entry(self):
        self.x_entry.delete(0, "end")


class TotalEntries(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(side=tk.TOP)
        self.parent = parent

        self.current_total_entries = tk.IntVar()

        self.total_entries_label = tk.Label(self, text="Total entries: ")
        self.total_entries_label["font"] = ("Helvetica", 12)
        self.total_entries_label.configure(pady=5)
        self.total_entries_label.pack(side=tk.LEFT)

        self.total_entries_value = tk.Label(
            self, textvariable=self.current_total_entries
        )
        self.total_entries_value["font"] = ("Helvetica", 12)
        self.total_entries_value.pack(side=tk.RIGHT)


class AddResetHelp(tk.Frame):
    buttons_width = 6

    def __init__(self, parent):
        super().__init__(parent)
        self.pack(side=tk.TOP)
        self.parent = parent

        self.current_total_entries = parent.total_entries.current_total_entries

        self.add = tk.Button(
            self, text="Add X", width=self.buttons_width, command=self.add_x_value
        )
        self.add.pack(side=tk.LEFT)
        self.add.bind("<Return>", self.add_x_value)

        self.reset = tk.Button(
            self,
            text="Reset",
            bg="IndianRed2",
            activebackground="IndianRed1",
            width=self.buttons_width,
            command=self.reset_x_values,
        )
        self.reset.pack(side=tk.LEFT)
        self.reset.bind("<Return>", self.reset_x_values)

        self.help = tk.Button(
            self,
            text="Help",
            bg="goldenrod2",
            activebackground="goldenrod1",
            width=self.buttons_width,
        )
        self.help.pack(side=tk.LEFT)

    def add_x_value(self, event=None):
        value = self.parent.x.x_entry.get()
        if value:
            Application.x_values.append(float(value))
            self.current_total_entries.set(len(Application.x_values))
            self.clean_entry()

    def reset_x_values(self, event=None):
        Application.x_values = []
        self.current_total_entries.set(len(Application.x_values))
        self.clean_entry()

    def clean_entry(self):
        self.parent.x.x_entry.delete(0, "end")


class Results(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(side=tk.RIGHT, padx=20)
        self.parent = parent

        self.mean = Mean(self)
        self.median = Median(self)
        self.variance = Variance(self)
        self.std_dev = StdDev(self)


class Mean(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(side=tk.TOP)
        self.parent = parent

        self.mean_label = tk.Label(self, text="Mean - ")
        self.mean_label["font"] = ("Helvetica", 12)
        self.mean_label.pack(side=tk.LEFT)

        self.mean_value = tk.Label(self, text=" ")
        self.mean_value["font"] = ("Helvetica", 12)
        self.mean_value.pack(side=tk.RIGHT)


class Median(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(side=tk.TOP)
        self.parent = parent

        self.median_label = tk.Label(self, text="Median - ")
        self.median_label["font"] = ("Helvetica", 12)
        self.median_label.pack(side=tk.LEFT)

        self.median_value = tk.Label(self, text=" ")
        self.median_value["font"] = ("Helvetica", 12)
        self.median_value.pack(side=tk.RIGHT)


class Variance(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(side=tk.TOP)
        self.parent = parent

        self.median_label = tk.Label(self, text="Variance - ")
        self.median_label["font"] = ("Helvetica", 12)
        self.median_label.pack(side=tk.LEFT)

        self.median_value = tk.Label(self, text=" ")
        self.median_value["font"] = ("Helvetica", 12)
        self.median_value.pack(side=tk.RIGHT)


class StdDev(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(side=tk.TOP)
        self.parent = parent

        self.median_label = tk.Label(self, text="Standard Deviation - ")
        self.median_label["font"] = ("Helvetica", 12)
        self.median_label.pack(side=tk.LEFT)

        self.median_value = tk.Label(self, text=" ")
        self.median_value["font"] = ("Helvetica", 12)
        self.median_value.pack(side=tk.RIGHT)


class Footer(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(side=tk.BOTTOM)
        self.parent = parent

        self.header_text = tk.Label(self, text="Conrado Jordan © 2021")
        self.header_text["font"] = ("Helvetica", 10)
        self.header_text.configure(pady=10)
        self.header_text.pack()


def center_window(window):
    w = window.winfo_reqwidth()
    h = window.winfo_reqheight()
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    if ws >= 3840:
        # Either a 4k monitor or multiple monitors; do nothing
        return
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    window.geometry("+%d+%d" % (x, y))


if __name__ == "__main__":
    root = tk.Tk()

    myapp = Application(root)
    center_window(root)

    root.mainloop()
