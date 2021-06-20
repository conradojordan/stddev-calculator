import tkinter as tk

VERSION = 0.7


class Application:
    def __init__(self, parent):
        self.header = Header(parent)
        self.content = Content(parent)
        self.footer = Footer(parent)


class Header(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(side=tk.TOP)

        self.header_text = tk.Label(self, text="Standard Deviation Calculator")
        self.header_text["font"] = ("Helvetica", 22)
        self.header_text.pack()


class Content(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(side=tk.TOP)

        self.user_input = UserInput(self)
        self.results = Results(self)


class UserInput(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(side=tk.LEFT)

        self.insert_xi = tk.Label(self, text="Enter Xi:")
        self.insert_xi["font"] = ("Helvetica", 14)
        self.insert_xi.pack(side=tk.TOP)

        self.x = X(self)
        self.total_entries = TotalEntries(self)
        self.add_reset_help = AddResetHelp(self)

        self.calculate = tk.Button(self, text="Calculate data", bg="SeaGreen1")
        self.calculate["font"] = ("Helvetica", 14)
        self.calculate.pack(side=tk.TOP)


class X(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(side=tk.TOP)

        self.x_label = tk.Label(self, text="X = ")
        self.x_label["font"] = ("Helvetica", 12)
        self.x_label.pack(side=tk.LEFT)

        self.x_entry = tk.Entry(self)
        self.x_entry.pack(side=tk.RIGHT)
        self.x_entry.focus_force()


class TotalEntries(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(side=tk.TOP)

        self.total_entries_label = tk.Label(self, text="Total entries: ")
        self.total_entries_label["font"] = ("Helvetica", 12)
        self.total_entries_label.pack(side=tk.LEFT)

        self.total_entries_value = tk.Label(self, text="0")
        self.total_entries_value["font"] = ("Helvetica", 12)
        self.total_entries_value.pack(side=tk.RIGHT)


class AddResetHelp(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(side=tk.TOP)

        self.add = tk.Button(self, text="Adicionar")
        self.add.pack(side=tk.LEFT)

        self.reset = tk.Button(self, text="Reset", bg="IndianRed1")
        self.reset.pack(side=tk.LEFT)

        self.help = tk.Button(self, text="Help", bg="goldenrod1")
        self.help.pack(side=tk.LEFT)


class Results(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(side=tk.RIGHT)

        self.mean = Mean(self)
        self.median = Median(self)
        self.variance = Variance(self)
        self.std_dev = StdDev(self)


class Mean(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(side=tk.TOP)

        self.mean_label = tk.Label(self, text="Average - ")
        self.mean_label["font"] = ("Helvetica", 12)
        self.mean_label.pack(side=tk.LEFT)

        self.mean_value = tk.Label(self, text=" ")
        self.mean_value["font"] = ("Helvetica", 12)
        self.mean_value.pack(side=tk.RIGHT)


class Median(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(side=tk.TOP)

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

        self.header_text = tk.Label(self, text="Conrado Jordan © 2021")
        self.header_text["font"] = ("Helvetica", 10)
        self.header_text.pack()


root = tk.Tk()
myapp = Application(root)
root.winfo_toplevel().title(f"Standard Deviation Calculator v{VERSION}")
root.mainloop()