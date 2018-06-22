import idc, idautils
from const_tsec import *
from const_se import *
from const_pmc import *
from const_clkrst import *
from const_mc import *
from const_emc import *
from const_tmr import *
from const_mipi_cal import *
from const_pinmux_aux import *
from const_gpio import *
from const_flow_ctrl import *
from const_exec_vec import *
from const_sysreg import *

#https://github.com/Atmosphere-NX/Atmosphere/blob/master/fusee/fusee-primary/src/hwinit/t210.h
#http://switchbrew.org/index.php?title=Memory_layout
def add_segments():
    segments_to_add = [
        {
            "name" : "TSEC",
            "base": 0x54500000,
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
        },
        {
            "name": "DSI",
            "base": 0x54300000,
            "size": 0x1000
        },
        {
            "name": "MIPI_CAL",
            "base": 0x700E3000,
            "size": 0x1000
        },
        {
            "name": "TMR",
            "base": 0x60005000,
            "size": 0x1000
        },
        {
            "name": "PINMUX_AUX",
            "base": 0x70003000,
            "size": 0x1000
        },
        {
            "name": "GPIO",
            "base": 0x6000D000,
            "size": 0x1000
        },
        {
            "name": "FLOW_CTRL",
            "base": 0x60007000,
            "size": 0x1000
        },
        {
            "name": "EXEC_VEC",
            "base": 0x6000F000,
            "size": 0x1000
        },
        {
            "name": "SYSREG",
            "base": 0x6000C000,
            "size": 0x1000
        }
    ]

    segments = []
    for start in idautils.Segments():
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
                    mc_values, emc_values, tmr_values, mipi_cal_values, \
                    pinmux_aux_values, gpio_values, flow_ctrl_values, \
                    exec_vec_values, sysreg_values, sb_values]

    for pa in process_array:
        base = 0
        flags = idc.SN_PUBLIC #|idc.SN_NOWARN
        if "base" in pa:
            base = pa["base"]

        for name in pa:
            if name == "base": continue
            if base != 0:
                idc.set_name(base + pa[name], name, flags)
            else:
                idc.set_name(pa[name], name, flags)

def main():
    print("Adding segments")
    add_segments()
    print("map_memory script starting...")
    add_defines()

if __name__ == "__main__":
    main()