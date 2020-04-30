from io import StringIO
import pandas as pd
import bvareader.old_bva.preprocessing as prep

# ' The TR3 file comes in three parts - SETTINGS, PHASES and POSITION. We separate the file as per these separating
# ' lines and thenread each appropriate text part
LOGGING_FREQUENCY = 25
POSITION_SEPARATOR = "frame         roomx         roomy         arena angle   arenax        arenay        phase         pausa"
SETTINGS_SEPARATOR = "phase         cue           cueno         laser         startpoint    segments"
PHASES_SEPARATOR = "phase         sector        mode          avoid         shape         r             r0            r1            keytonext"


def read_position(path):
    file = open(path, 'r')
    lines = file.readlines()
    position_head = next((x for x in lines if POSITION_SEPARATOR in x), [None])
    i_position = [lines.index(position_head)]
    position_lines = [lines[x] for x in range(i_position[0], len(lines))]
    text = StringIO(''.join(position_lines))
    # reads well formated textw with fixed size but unequal things in each part
    position = pd.read_fwf(text, header=0, widths=[14]*16)
    file.close()
    return position


def read_sync(path):
    pd_keys = read_keypresses(path)
    sync = pd_keys.loc[pd_keys['klavesa'] == 'e']
    sync = sync[['timestamp']]
    return sync


def read_settings(path):
    """ Reads laser/cues information from the top of the TR file
    """
    file = open(path, 'r')
    lines = file.readlines()
    position_head = next((x for x in lines if POSITION_SEPARATOR in x), [None])
    phases_head = next((x for x in lines if PHASES_SEPARATOR in x), [None])
    i_phases = [lines.index(phases_head), lines.index(position_head)]
    phases_lines = [lines[x] for x in range(i_phases[0], i_phases[1])]
    settings = pd.read_csv(StringIO(''.join(phases_lines)), header=0, sep='\\s+')
    settings['phase'] = range(0, len(settings.index))
    lasers = read_lasers(path)

    if(len(lasers.index) == len(settings.index)*2):
        lasers = lasers[['cueno', 'type', 'laser']]
        lasers = lasers.pivot(index='cueno', columns='type', values='laser')
        lasers = lasers.rename(columns={'cue': 'cue_laser', 'start': 'start_laser'})
        settings = settings.merge(lasers, left_on='phase', right_index=True)
    return settings


def read_lasers(path):
    """Reads phases settings and combines with laser information
    """
    file = open(path, 'r')
    lines = file.readlines()
    phases_head = next((x for x in lines if PHASES_SEPARATOR in x), [None])
    settings_head = next((x for x in lines if SETTINGS_SEPARATOR in x), [None])
    i_block1 = [lines.index(settings_head), lines.index(phases_head)]
    lasers_lines = [lines[x] for x in range(i_block1[0], i_block1[1])]
    lasers = pd.read_csv(StringIO(''.join(lasers_lines)), header=0, sep='\\s+')
    # potentially validate if there are only cues and starts??
    lasers['type'] = ["start" if x == 1 else "cue" for x in lasers['startpoint']]
    return lasers


def read_keypresses(path):
    position = read_position(path)
    position['logging_timestamp'] = position['frame'] * 1/LOGGING_FREQUENCY + 1/LOGGING_FREQUENCY
    position = position.rename(columns={'casms': 'timestamp'})
    pd_keys = position.loc[position['klavesa'].notna(), ['klavesa', 'frame', 'timestamp', 'logging_timestamp']]
    return pd_keys
