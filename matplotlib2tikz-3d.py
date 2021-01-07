def linestyle_configuration(line):
    line_style = line.get_linestyle()
    if line_style in ['None', ' ', '']:
        return "only marks"
    elif line_style in ['dashdot', '-.']:
        return "dashdotted"
    elif line_style in ['dotted', ':']:
        return "dotted"
    elif line_style == '--':
        return "dashed"
    elif line_style in ['solid','-']:
        return "solid"


def color_hex2int(string, k):
    return "\\definecolor{"  + f"color{k}" + "}{RGB}{" + \
          f"{int(string[1:3], 16)} {int(string[3:5], 16)} {int(string[5:7], 16)}" + "}"

def set_limit(bounds, axis):
    if axis == 'x' or axis=='y' or axis=='z':
        return f"{axis}min= {bounds[0]}, {axis}max={bounds[1]},"

def axis_label(string, axis):
    if axis == 'x' or axis=='y' or axis=='z':
        return f"{axis}label = {string},"

class Matplotlib3DLines2Tikz():
    def __init__(self, fig, ax, file):
        self.fig = fig 
        self.ax = ax
        self.file = file
        
    def save_code(self):
        with open(self.file, 'w+') as f:
            
            print("\\begin{tikzpicture}", file = f)
            for counter, line in enumerate(self.ax.lines):
                print(color_hex2int(line.get_color(), counter), file=f)

            print("\\begin{axis} [", file = f)

            print(axis_label(self.ax.get_xlabel(), 'x'), file = f)
            print(axis_label(self.ax.get_ylabel(), 'y'), file = f)
            print(axis_label(self.ax.get_zlabel(), 'z'), file = f)
            print(set_limit(self.ax.get_xlim(), 'x'), file = f)
            print(set_limit(self.ax.get_ylim(), 'y'), file = f)
            print(set_limit(self.ax.get_zlim(), 'z'), file = f)
            print("]", file = f)

            for counter, line in enumerate(self.ax.lines):
                print(f"\\addplot3 [color=color{counter}, {linestyle_configuration(line)}] table ", file = f)
                print("{", file = f)
                x = line.get_data_3d()[0]
                y = line.get_data_3d()[1]
                z = line.get_data_3d()[2]

                for k in range(0, len(x)):
                    print(x[k], y[k], z[k], file = f)
                print("};", file = f)

            for counter, line in enumerate(self.ax.lines):
                print("\\addlegendentry{" + f"{line.get_label()}" + "}", file = f)
            
            print("\\end{axis}", file = f)
            print("\\end{tikzpicture}", file = f)
