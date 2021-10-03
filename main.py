import tkinter as tk
from math import sqrt

VERSION = "1.1"


class Application(tk.Frame):
    x_values = []
    precision = 6

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
        self.x_entry.bind("<KP_Enter>", self.add_x_value)
        self.x_entry.bind("<Shift_R>", self.reset_x_values)

    def add_x_value(self, event=None):
        self.parent.add_reset_help.add_x_value_and_calculate_data(event)

    def reset_x_values(self, event=None):
        self.parent.add_reset_help.reset_x_values(event)


class TotalEntries(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(side=tk.TOP)
        self.parent = parent

        self.current_total_entries = tk.IntVar()

        self.total_entries_label = tk.Label(self, text="Total entries (N): ")
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
    help_window_open = False

    def __init__(self, parent):
        super().__init__(parent)
        self.pack(side=tk.TOP)
        self.parent = parent

        self.add = tk.Button(
            self,
            text="Add X",
            bg="PaleGreen2",
            activebackground="pale green",
            width=self.buttons_width,
            command=self.add_x_value_and_calculate_data,
        )
        self.add.pack(side=tk.LEFT)
        self.add.bind("<Return>", self.add_x_value_and_calculate_data)
        self.add.bind("<KP_Enter>", self.add_x_value_and_calculate_data)

        self.reset = tk.Button(
            self,
            text="Reset",
            bg="pink2",
            activebackground="pink",
            width=self.buttons_width,
            command=self.reset_x_values,
        )
        self.reset.pack(side=tk.LEFT)
        self.reset.bind("<Return>", self.reset_x_values)
        self.reset.bind("<KP_Enter>", self.reset_x_values)

        self.help = tk.Button(
            self,
            text="Help",
            bg="khaki2",
            activebackground="khaki1",
            width=self.buttons_width,
            command=self.open_help_window,
        )
        self.help.pack(side=tk.LEFT)
        self.help.bind("<Return>", self.open_help_window)
        self.help.bind("<KP_Enter>", self.open_help_window)

    def add_x_value_and_calculate_data(self, event=None):
        value = self.parent.x.x_entry.get()
        if value:
            Application.x_values.append(float(value))
            curr = self.parent.total_entries.current_total_entries
            curr.set(len(Application.x_values))
            self.clean_entry()

        self.calculate_and_display_data(event)

    def reset_x_values(self, event=None):
        Application.x_values = []
        curr = self.parent.total_entries.current_total_entries
        curr.set(len(Application.x_values))
        self.clean_entry()
        self.clean_results()

    def clean_entry(self):
        self.parent.x.x_entry.delete(0, "end")

    def clean_results(self):
        self.parent.parent.results.mean.mean.set(0.0)
        self.parent.parent.results.median.median.set(0.0)
        self.parent.parent.results.variance.variance.set(0.0)
        self.parent.parent.results.std_dev.std_dev.set(0.0)

    def calculate_and_display_data(self, event=None):
        if Application.x_values:
            # Calculate values. Mean is used to calculte variance and
            # variance is used to calculate standard deviation.
            mean = self.calculate_mean()
            median = self.calculate_median()
            variance = self.calculate_variance(mean)
            std_dev = self.calculate_std_dev(variance)

            # Display values
            self.display_results(
                mean=mean, median=median, variance=variance, std_dev=std_dev
            )

    def calculate_mean(self):
        mean = sum(Application.x_values) / len(Application.x_values)

        if mean.is_integer():
            return int(mean)
        return mean

    def calculate_median(self):
        len_values = len(Application.x_values)
        sorted_values = sorted(Application.x_values)

        if len_values % 2 == 0:
            median = (
                sorted_values[len_values // 2] + sorted_values[(len_values // 2) - 1]
            ) / 2
        else:
            median = sorted_values[len_values // 2]

        if median.is_integer():
            return int(median)
        return median

    def calculate_variance(self, mean):
        len_values = len(Application.x_values)

        sum_square_differences = 0
        for value in Application.x_values:
            sum_square_differences += (value - mean) ** 2

        variance = sum_square_differences / len_values

        if variance.is_integer():
            return int(variance)
        return variance

    def calculate_std_dev(self, variance):
        std_dev = sqrt(variance)

        if std_dev.is_integer():
            return int(std_dev)
        return std_dev

    def display_results(self, mean, median, variance, std_dev):
        results = self.parent.parent.results

        results.mean.mean.set(round(mean, Application.precision))
        results.median.median.set(round(median, Application.precision))
        results.variance.variance.set(round(variance, Application.precision))
        results.std_dev.std_dev.set(round(std_dev, Application.precision))

    def open_help_window(self, event=None):
        if not AddResetHelp.help_window_open:
            help_window = HelpWindow(self)
            AddResetHelp.help_window_open = True

            def close_help_window():
                help_window.destroy()
                AddResetHelp.help_window_open = False

            help_window.protocol("WM_DELETE_WINDOW", close_help_window)


class HelpWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.geometry("440x380")

        self.title("Help")

        self.help_text = tk.Label(self, padx=10, pady=20)
        self.help_text["font"] = ("Helvetica", 12)
        self.help_text[
            "text"
        ] = """To use the program, simply enter values of X by
typing them into the input box and clicking on "Add X".
The results for the current values will automatically be
calculated and shown on screen. Make sure to enter values
using dot (.) as decimal separator. The results are rounded
to 6 decimal digits after the separator (although this value
can easily be modified in the source-code if needed).

Click on "Reset" to delete all current values and
start over.
Click on "Help" to open this window (as you may have
already noticed).

Instead of using the mouse, you can also insert values
by pressing <Enter> and you can reset them by pressing
<Right-Shift>. Entering values using the numeric
keyboard also works :)

Any issues or suggestions, feel free to send me an
e-mail at conrado.jordan@gmail.com
"""
        self.help_text.pack(side=tk.TOP)


class Results(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(side=tk.RIGHT, padx=10, ipadx=10)
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

        self.mean = tk.DoubleVar()

        self.mean_label = tk.Label(self, text="Mean - ")
        self.mean_label["font"] = ("Helvetica", 12)
        self.mean_label.pack(side=tk.LEFT)

        self.mean_value = tk.Label(self, textvariable=self.mean)
        self.mean_value["font"] = ("Helvetica", 12)
        self.mean_value.pack(side=tk.RIGHT)


class Median(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(side=tk.TOP)
        self.parent = parent

        self.median = tk.DoubleVar()

        self.median_label = tk.Label(self, text="Median - ")
        self.median_label["font"] = ("Helvetica", 12)
        self.median_label.pack(side=tk.LEFT)

        self.median_value = tk.Label(self, textvariable=self.median)
        self.median_value["font"] = ("Helvetica", 12)
        self.median_value.pack(side=tk.RIGHT)


class Variance(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(side=tk.TOP)
        self.parent = parent

        self.variance = tk.DoubleVar()

        self.median_label = tk.Label(self, text="Variance - ")
        self.median_label["font"] = ("Helvetica", 12)
        self.median_label.pack(side=tk.LEFT)

        self.median_value = tk.Label(self, textvariable=self.variance)
        self.median_value["font"] = ("Helvetica", 12)
        self.median_value.pack(side=tk.RIGHT)


class StdDev(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(side=tk.TOP)
        self.parent = parent

        self.std_dev = tk.DoubleVar()

        self.std_dev_label = tk.Label(self, text="Standard Deviation - ")
        self.std_dev_label["font"] = ("Helvetica", 12)
        self.std_dev_label.pack(side=tk.LEFT)

        self.std_dev_value = tk.Label(self, textvariable=self.std_dev)
        self.std_dev_value["font"] = ("Helvetica", 12)
        self.std_dev_value.pack(side=tk.RIGHT)


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
