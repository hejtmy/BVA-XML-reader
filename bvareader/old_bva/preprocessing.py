LOGGING_FREQUENCY = 25


def preprocess_blocks(blocks):
    for block in blocks:
        block = block.dropna
    block1, phases, position = blocks
    phases = preprocess_phases(phases)
    position = preprocess_position(position)

    return block1, phases, position


def preprocess_phases(block):
    cols_to_drop = ['phase', 'sector', 'mode', 'avoid', 'shape', 'rel_to', 'keytocues', 'r1', 'keytonext', 'keyfound',
                    'repeatmax', 'keyfoundbeepstop']
    block = block.drop(cols_to_drop, axis=1)
    return block


def preprocess_position(block):
    cols_to_drop = ['frame', 'roomx', 'roomy', 'arena', 'angle', 'phase', 'pausa', 'frame.1',
                    'sector', 'sector.1', '0', '-', '0.1', 'klavesa',  'faze',  'repeat', 'goalno']
    block = block.rename(columns={"arenax": 'position_x', 'arenay': 'position_y'})
    block['timestamp'] = block.frame * 1/LOGGING_FREQUENCY
    block = block.drop(cols_to_drop, axis=1)
    # calculating empty spaces defined by 999s
    return block
