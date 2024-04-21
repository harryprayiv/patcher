import argparse

def generate_patch(universe, dmx_start, fixture_start, quantity, width_mode, name_prefix):
    width, mode = map(int, width_mode.split('x'))
    patch_list = []

    current_universe = universe
    current_dmx_start = dmx_start

    for i in range(quantity):
        fixture_num = fixture_start + i
        dmx_channel_end = current_dmx_start + width - 1

        # Check if the current DMX end address goes beyond 512 and wrap to next universe
        if dmx_channel_end > 512:
            current_universe += 1
            current_dmx_start = 1
            dmx_channel_end = current_dmx_start + width - 1

        universe_dmx_start = f"{current_universe}.{current_dmx_start:03d}"
        universe_dmx_end = f"{current_universe}.{dmx_channel_end:03d}"
        fixture_name = f"{name_prefix} {fixture_num:03d}"

        patch_list.append((
            fixture_name, fixture_num, fixture_num, universe_dmx_start, universe_dmx_end, f'{width} "Mode {mode}"'
        ))

        # Update the start for the next fixture
        current_dmx_start = dmx_channel_end + 1
        if current_dmx_start > 512:
            current_universe += 1
            current_dmx_start = 1

    print("Name, Fixture, Channel, Universe.DMXchannelStart, Universe.DMXchannelEnd, Width Mode")
    for entry in patch_list:
        print(", ".join(map(str, entry)))

def main():
    parser = argparse.ArgumentParser(description="Generate a patch list for lighting fixtures.")
    parser.add_argument("universe", type=int, help="DMX Universe number")
    parser.add_argument("dmx_start", type=int, help="DMX start address")
    parser.add_argument("fixture_start", type=int, help="Fixture start number")
    parser.add_argument("quantity", type=int, help="Number of fixtures to generate")
    parser.add_argument("width_mode", type=str, help="DMX mode channel width in the format WIDTHxMODE")
    parser.add_argument("name_prefix", type=str, help="Prefix for fixture names")

    args = parser.parse_args()

    generate_patch(args.universe, args.dmx_start, args.fixture_start, args.quantity, args.width_mode, args.name_prefix)

if __name__ == "__main__":
    main()
