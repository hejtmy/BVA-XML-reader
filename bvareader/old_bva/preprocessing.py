import numpy as np
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
    cols_to_drop = ['arenax', 'arenay', 'arena angle', 'phase', 'pausa', 'frame.1',
                    'sector', 'sector 0 - 0', 'klavesa', 'faze repeat', 'goalno']
    block = block.rename(columns={"roomx": 'position_x', 'roomy': 'position_y', 'casms': 'timestamp'})
    # first recording seems to not be at 0, but at 0.40s
    block['logging_timestamp'] = block.frame * 1/LOGGING_FREQUENCY + 1/LOGGING_FREQUENCY
    block = block.drop(cols_to_drop, axis=1)
    block.loc[block['position_x'] == 999, ['position_x', 'position_y']] = np.nan
    return block
