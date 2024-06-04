import textwrap
def wrap(string, max_width):
    w = "\n".join(textwrap.wrap(string, max_width))
    return w
     
