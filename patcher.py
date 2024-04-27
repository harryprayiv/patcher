import argparse
import json

def calculate_dmx_addresses(universe, dmx_start, width, quantity):
    patch_list = []
    current_universe = universe
    current_dmx_start = dmx_start

    for _ in range(quantity):
        dmx_channel_end = current_dmx_start + width - 1
        # Wrap to next universe if DMX end address exceeds 512
        if dmx_channel_end > 512:
            current_universe += 1
            current_dmx_start = 1
            dmx_channel_end = current_dmx_start + width - 1

        patch_list.append((current_universe, current_dmx_start, dmx_channel_end))
        current_dmx_start = dmx_channel_end + 1
        if current_dmx_start > 512:
            current_universe += 1
            current_dmx_start = 1

    return patch_list

def generate_fixture_names(name_prefix, fixture_start, quantity):
    return [f"{name_prefix} {fixture_num:03d}" for fixture_num in range(fixture_start, fixture_start + quantity)]

def generate_patch(universe, dmx_start, fixture_start, quantity, width, mode, name_prefix):
    dmx_addresses = calculate_dmx_addresses(universe, dmx_start, width, quantity)
    fixture_names = generate_fixture_names(name_prefix, fixture_start, quantity)
    
    patch_list = [
        {
            "Name": fixture_names[i],
            "Fixture": fixture_start + i,
            "Universe.DMXchannelStart": f"{addr[0]}.{addr[1]:03d}",
            "Universe.DMXchannelEnd": f"{addr[0]}.{addr[2]:03d}",
            "Width": width,
            "Mode": mode
        }
        for i, addr in enumerate(dmx_addresses)
    ]
    
    # Serialize list to JSON
    json_output = json.dumps(patch_list, indent=4)
    print(json_output)

def main():
    parser = argparse.ArgumentParser(description="Generate a patch list for lighting fixtures in JSON format.")
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