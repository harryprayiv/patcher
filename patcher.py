import argparse

def generate_patch(universe, dmx_start, fixture_start, quantity, width, mode, name_prefix):
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
            fixture_name, fixture_num, fixture_num, universe_dmx_start, universe_dmx_end, f'{width} "{mode}"'
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
    parser.add_argument("-u", "--universe", type=int, required=True, help="DMX Universe number")
    parser.add_argument("-s", "--start_dmx", type=int, required=True, help="DMX start address")
    parser.add_argument("-f", "--fixture_start", type=int, required=True, help="Fixture start number")
    parser.add_argument("-q", "--quantity", type=int, required=True, help="Number of fixtures to generate")
    parser.add_argument("-w", "--width", type=int, required=True, help="Width in terms of DMX channels per fixture")
    parser.add_argument("-m", "--mode", type=str, required=True, help="Mode of the fixtures as a string")
    parser.add_argument("-n", "--name_prefix", type=str, required=True, help="Prefix for fixture names")

    args = parser.parse_args()

    generate_patch(args.universe, args.start_dmx, args.fixture_start, args.quantity, args.width, args.mode, args.name_prefix)

if __name__ == "__main__":
    main()
