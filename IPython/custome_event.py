

"""
How to use : 
   In [2]: %load_ext custome_event
    ------------------------
    Variable after cell execution:
    Interactive namespace is empty.

    In [3]: a = 10
    ------------------------
    Variable after cell execution:
    Variable   Type    Data/Info
    ----------------------------
    a          int     10

    In [4]: b = [1,2,3]
    ------------------------
    Variable after cell execution:
    Variable   Type    Data/Info
    ----------------------------
    a          int     10
    b          list    n=3


"""
class VarPrinter:
    def __init__(self,ip):
        self.ip = ip

    def post_run_cell(self, result):
        print("------------------------")
        print("Variable after cell execution:")
        # %whos would give a SyntaxError!
        self.ip.run_line_magic("whos", '')


def load_ipython_extension(ip):
    vp = VarPrinter(ip)
    ip.events.register("post_run_cell", vp.post_run_cell)