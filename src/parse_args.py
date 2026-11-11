import argparse

parser = argparse.ArgumentParser(
    prog='planet-term',
    description='3D planet collision simulation in the terminal!'
)

parser.add_argument(
    '-p', '--preset',
    help='Scene preset to use',
    default='earth-mars'
)

args = parser.parse_args()

preset = args.preset

VALID_PRESETS = {
    'earth-mars',
    'sun-jupiter',
    'rogue-asteroid',
    'neutron-star',
    'binary-stars'
}

if preset not in VALID_PRESETS:
    raise ValueError(f'Invalid preset: {preset}')
