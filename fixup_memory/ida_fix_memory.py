import idc, idautils
from const_tsec import *
from const_se import *
from const_pmc import *
from const_clkrst import *
from const_mc import *
from const_emc import *

#https://github.com/Atmosphere-NX/Atmosphere/blob/master/fusee/fusee-primary/src/hwinit/t210.h
#http://switchbrew.org/index.php?title=Memory_layout
def add_segments():
    segments_to_add = [
        {
            "name" : "TSEC",
            "base": 0x54501000,
            "size": 0x40000
        },
        {
            "name" : "PMC",
            "base": 0x7000E000,
            "size": 0x1000
        },
        {
            "name" : "SE",
            "base": 0x70012000,
            "size": 0x2000
        },
        {
            "name" : "CLKRST",
            "base": 0x60006000,
            "size": 0x1000
        },
        {
            "name" : "MC",
            "base": 0x70019000,
            "size": 0x1000
        },
        {
            "name": "EMC",
            "base": 0x7001B000,
            "size": 0x1000
        }
    ]

    segments = []
    for start in idautils.Segments():
        print(start)
        segments.append(start)

    for new_segment in segments_to_add:
        name = new_segment["name"]
        base = new_segment["base"]
        size = new_segment["size"]
        if base not in segments:
            
            print("Adding new segment {}").format(name)
            idc.add_segm_ex(base, base + size , 0,1,1,2, idc.ADDSEG_NOSREG)
            idc.set_segm_name(base, name)
        else:
            print("Segment {} exists, skipping").format(name)

def add_defines():
    process_array = [tsec_values, se_values, pmc_values, clkrst_values, \
                    mc_values, emc_values]

    for pa in process_array:
        for name in pa:
            idc.set_name(pa[name], name, idc.SN_PUBLIC|idc.SN_NOWARN)

def main():
    print("Adding segments")
    add_segments()
    print("map_memory script starting...")
    add_defines()

if __name__ == "__main__":
    main()