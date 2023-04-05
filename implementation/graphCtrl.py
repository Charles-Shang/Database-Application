import matplotlib.pyplot as plt
from CONSTANTS import base_directory
import textFormatter as tf

class Graph:
    def addlabels(self, x, y):
        for i in range(len(x)):
            plt.text(i, y[i] * 1.01, y[i])

    def draw_hist(self, data_x, data_y, x_label, y_label, title):
        plt.figure()
        plt.bar(data_x, data_y, width=0.5)
        self.addlabels(data_x, data_y)
        plt.ylabel(y_label)
        plt.xlabel(x_label)
        plt.title(title)
        plt.savefig(base_directory + f"/plot/{title.replace(' ', '_')}.png")
        print("The diagram has been exported into " + tf.yellow(base_directory + f"/plot/{title.replace(' ', '_')}.png"))
        plt.show()

    def draw_line(self, data_x, data_y, x_label, y_label, title):
        plt.figure()
        plt.plot(data_x, data_y)
        self.addlabels(data_x, data_y)
        plt.ylabel(y_label)
        plt.xlabel(x_label)
        plt.title(title)
        plt.savefig(base_directory + f"/plot/{title.replace(' ', '_')}.png")
        print("The diagram has been exported into " + tf.yellow(base_directory + f"/plot/{title.replace(' ', '_')}.png"))
        plt.show()

    def draw_pie(self, data_y, labels, title):
        def autopct_format(values):
            def my_format(pct):
                total = sum(values)
                val = int(round(pct * total / 100.0))
                return "{:.1f}%\n({v:d})".format(pct, v=val)

            return my_format

        plt.figure()
        plt.pie(data_y, labels=labels, autopct=autopct_format(data_y))
        plt.title(title)
        plt.savefig(base_directory + f"/plot/{title.replace(' ', '_')}.png")
        print("The diagram has been exported into " + tf.yellow(base_directory + f"/plot/{title.replace(' ', '_')}.png"))
        plt.show()
