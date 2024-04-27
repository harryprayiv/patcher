import argparse
import xml.etree.ElementTree as ET
from xml.dom import minidom

def calculate_absolute_dmx_addresses(universe, dmx_start, width, quantity):
    patch_list = []
    current_absolute_address = (universe - 1) * 512 + dmx_start

    for _ in range(quantity):
        dmx_channel_end = current_absolute_address + width - 1

        patch_list.append((current_absolute_address, dmx_channel_end))
        current_absolute_address = dmx_channel_end + 1

    return patch_list

def generate_xml(patch_list, fixture_start, name_prefix, mode, width):
    root = ET.Element('MA')
    root.set('xmlns:xsi', 'http://www.w3.org/2001/XMLSchema-instance')
    root.set('xmlns', 'http://schemas.malighting.de/grandma2/xml/MA')
    root.set('xsi:schemaLocation', 'http://schemas.malighting.de/grandma2/xml/MA http://schemas.malighting.de/grandma2/xml/3.9.60/MA.xsd')
    root.set('major_vers', '3')
    root.set('minor_vers', '9')
    root.set('stream_vers', '60')
    
    layer = ET.SubElement(root, 'Layer', index="3", name="Rigged")
    
    for i, (dmx_start, dmx_end) in enumerate(patch_list):
        fixture = ET.SubElement(layer, 'Fixture', index=str(i), name=f"{name_prefix} {fixture_start + i}", fixture_id=str(fixture_start + i), channel_id=str(fixture_start + i))
        fixture_type = ET.SubElement(fixture, 'FixtureType', name=f"{width} {mode}")
        ET.SubElement(fixture_type, 'No').text = str(width)
        
        # Absolute Position section
        abs_pos = ET.SubElement(fixture, 'AbsolutePosition')
        ET.SubElement(abs_pos, 'Location', x="-2.699", y="-4.298", z="1.563")
        ET.SubElement(abs_pos, 'Rotation', x="90", y="0", z="-0")
        ET.SubElement(abs_pos, 'Scaling', x="1", y="1", z="1")

        sub_fixture = ET.SubElement(fixture, 'SubFixture', index="0", react_to_grandmaster="true", color="ffffff")
        patch = ET.SubElement(sub_fixture, 'Patch')
        ET.SubElement(patch, 'Address').text = str(dmx_start)
        
        # Replicate absolute position for subfixture if needed
        sub_abs_pos = ET.SubElement(sub_fixture, 'AbsolutePosition')
        ET.SubElement(sub_abs_pos, 'Location', x="-2.699", y="-4.298", z="1.563")
        ET.SubElement(sub_abs_pos, 'Rotation', x="90", y="0", z="-0")
        ET.SubElement(sub_abs_pos, 'Scaling', x="1", y="1", z="1")

        # Channels for the subfixture
        for channel_index in range(width):
            ET.SubElement(sub_fixture, 'Channel', index=str(channel_index))

    return root

def pretty_print_xml(element):
    rough_string = ET.tostring(element, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="    ")

def main():
    parser = argparse.ArgumentParser(description="Generate a patch list for lighting fixtures in XML format.")
    parser.add_argument("-u", "--universe", type=int, required=True, help="DMX Universe number")
    parser.add_argument("-s", "--start_dmx", type=int, required=True, help="DMX start address")
    parser.add_argument("-f", "--fixture_start", type=int, required=True, help="Fixture start number")
    parser.add_argument("-q", "--quantity", type=int, required=True, help="Number of fixtures to generate")
    parser.add_argument("-w", "--width", type=int, required=True, help="Width in terms of DMX channels per fixture")
    parser.add_argument("-m", "--mode", type=str, required=True, help="Mode of the fixtures as a string")
    parser.add_argument("-n", "--name_prefix", type=str, required=True, help="Prefix for fixture names")

    args = parser.parse_args()

    dmx_addresses = calculate_absolute_dmx_addresses(args.universe, args.start_dmx, args.width, args.quantity)
    xml_root = generate_xml(dmx_addresses, args.fixture_start, args.name_prefix, args.mode, args.width)
    xml_string = pretty_print_xml(xml_root)
    
    # Optionally write to file or print to console
    with open("Real_Fake_Fixture_Layer.xml", "w") as file:
        file.write(xml_string)
    print(xml_string)

if __name__ == "__main__":
    main()
