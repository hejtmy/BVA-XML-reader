from io import StringIO
import pandas as pd


def read_position(path):
   return None


def read_tr(path):
    # separate it into three distinct parts
    block1_separator = "phase         cue           cueno         laser         startpoint    segments"
    block2_separator = "phase         sector        mode          avoid         shape         r             r0            r1            keytonext"
    block3_separator = "frame         roomx         roomy         arena angle   arenax        arenay        phase         pausa"

    # Open the file
    file = open(path, 'r')
    lines = file.readlines()

    # gets the real headers (might be different from the separators)
    block1_head = next((x for x in lines if block1_separator in x), [None])
    block2_head = next((x for x in lines if block2_separator in x), [None])
    block3_head = next((x for x in lines if block3_separator in x), [None])

    # get the indices
    if all([block1_head, block2_head, block3_head]):
        i_block1 = [lines.index(block1_head), lines.index(block2_head)-1]
        i_block2 = [lines.index(block2_head), lines.index(block3_head)-1]
        i_block3 = [lines.index(block3_head)]

    # read in each part into self sustained block
    block1_lines = [lines[x] for x in range(i_block1[0], i_block1[1])]
    block2_lines = [lines[x] for x in range(i_block2[0], i_block2[1])]
    block3_lines = [lines[x] for x in range(i_block3[0], len(lines))]

    block1 = read_block1(''.join(block1_lines))
    block2 = read_block2(''.join(block2_lines))
    block3 = read_block3(''.join(block3_lines))
    file.close()
    return block1, block2, block3


def read_block1(string):
    text = StringIO(string)
    panda = pd.read_csv(text, header=0, sep='\s+')
    return panda


def read_block2(string):
    text = StringIO(string)
    panda = pd.read_csv(text, header=0, sep='\s+')
    return panda


def read_block3(string):
    text = StringIO(string)
    panda = pd.read_fwf(text, header=0)  # reads well formated textw with fixed size but unequal things in each part
    return panda
