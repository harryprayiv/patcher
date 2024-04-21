import argparse
import json
import sys

def generate_patch(universe, dmx_start, fixture_start, quantity, width_mode, name_prefix):
    # Split the width and mode from the string 'width x mode'
    width, mode = map(int, width_mode.split('x'))
    
    # Initialize an empty list to hold each line of the patch list
    patch_list = []
    
    # Generate each fixture entry
    for i in range(quantity):
        # Calculate fixture number and DMX start/end addresses
        fixture_num = fixture_start + i
        dmx_channel_start = dmx_start + (width * i)
        dmx_channel_end = dmx_channel_start + width - 1
        
        # Format the universe and DMX start/end addresses as required
        universe_dmx_start = f"{universe}.{dmx_channel_start:03d}"
        universe_dmx_end = f"{universe}.{dmx_channel_end:03d}"
        
        # Format the name with leading zeros if needed
        fixture_name = f"{name_prefix} {fixture_num:03d}"
        
        # Append the formatted string to the list
        patch_list.append((
            fixture_name, fixture_num, fixture_num, universe_dmx_start, universe_dmx_end, f'{width} "Mode {mode}"'
        ))
    
    # Print the patch list
    print("Name, Fixture, Channel, Universe.DMXchannelStart, Universe.DMXchannelEnd, Width Mode")
    for entry in patch_list:
        print(", ".join(map(str, entry)))

# Example usage
generate_patch(1, 1, 2001, 4, '18x6', 'Vortex XXX')
