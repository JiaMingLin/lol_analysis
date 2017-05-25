def prettify_axes( ax ):
    """ takes a matplot lib axis, and removes the top and right parts of it, then increases font size """
      
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    for tick in ax.xaxis.get_major_ticks():
        tick.label.set_fontsize(14)
    for tick in ax.yaxis.get_major_ticks():
        tick.label.set_fontsize(14)

def show(plt):
    prettify_axes(plt.gca())
    #z.show(plt)
