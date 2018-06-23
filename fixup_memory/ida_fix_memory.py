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
from const_host1x import *
from const_sysctr0 import *
from const_fuse import *
from const_display_a import *
from const_dsi import *

process_array = [tsec_values, se_values, pmc_values, clkrst_values, \
                mc_values, emc_values, tmr_values, mipi_cal_values, \
                pinmux_aux_values, gpio_values, flow_ctrl_values, \
                exec_vec_values, sysreg_values, sb_values, host1x_values, \
                sysctr0_values, fuse_values, display_a_values, dsi_values]

skip_fields = ["name", "base", "size"]

#https://github.com/Atmosphere-NX/Atmosphere/blob/master/fusee/fusee-primary/src/hwinit/t210.h
#http://switchbrew.org/index.php?title=Memory_layout
def add_segments():

    segments = []
    for start in idautils.Segments():
        segments.append(start)

    for new_segment in process_array:
        if "name" not in new_segment or "base" not in new_segment \
            or "size" not in new_segment: continue
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
    
    for pa in process_array:
        base = 0
        flags = idc.SN_PUBLIC #|idc.SN_NOWARN
        if "base" in pa:
            base = pa["base"]

        for name in pa:
            if name in skip_fields: continue
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