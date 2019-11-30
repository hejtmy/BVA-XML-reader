def preprocess_blocks(blocks):
    for block in blocks:
        block = block.dropna
    block1, block2, block3 = blocks
    block2 = prep_block2(block2)
    block3 = prep_block3(block3)

    return block1, block2, block3


def prep_block2(block):
    cols_to_drop = ['phase', 'sector', 'mode', 'avoid', 'shape', 'rel_to', 'keytocues', 'r1', 'keytonext', 'keyfound',
                    'repeatmax', 'keyfoundbeepstop']
    block = block.drop(cols_to_drop, axis=1)
    return block


def prep_block3(block):
    cols_to_drop = ['arena', 'angle', 'phase', 'pausa', 'frame.1', 'sector', 'sector.1', '0', '-', '0.1']
    block = block.drop(cols_to_drop, axis=1)
    # calculating empty spaces defined by 999s
    return block
