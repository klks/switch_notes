#https://github.com/Atmosphere-NX/Atmosphere/blob/master/fusee/fusee-primary/src/hwinit/di.h
display_a_values = {
"name"          : "DISPLAY_A",
"base"          : 0x54200000,
"size"          : 0x4000,      #Need to find a source for this

##define _DIREG(reg) ((reg) * 4)
"DC_CMD_DISPLAY_COMMAND"                    : 0x32 * 4,
"DC_CMD_STATE_ACCESS"                       : 0x40 * 4,
"DC_CMD_STATE_CONTROL"                      : 0x41 * 4,
"DC_CMD_DISPLAY_WINDOW_HEADER"              : 0x42 * 4,
"DC_DISP_DISP_WIN_OPTIONS"                  : 0x402 * 4,
"DC_DISP_DISP_CLOCK_CONTROL"                : 0x42E * 4,
"DC_DISP_BLEND_BACKGROUND_COLOR"            : 0x4E4 * 4,
"DC_WIN_AD_WIN_OPTIONS"                     : 0xB80 * 4,
"DC_WIN_BD_WIN_OPTIONS"                     : 0xD80 * 4,
"DC_WIN_CD_WIN_OPTIONS"                     : 0xF80 * 4,

#Used by SX OS
"DC_0x0"                                    : 0x0,
"DC_0x1"                                    : 0x1 * 4,
"DC_0x28"                                   : 0x28 * 4,
"DC_0x31"                                   : 0x31 * 4,
"DC_0x36"                                   : 0x36 * 4,
"DC_0x43"                                   : 0x43 * 4,
"DC_0x300"                                  : 0x300 * 4,
"DC_0x301"                                  : 0x301 * 4,
"DC_0x302"                                  : 0x302 * 4,
"DC_0x303"                                  : 0x303 * 4,
"DC_0x304"                                  : 0x304 * 4,
"DC_0x305"                                  : 0x305 * 4,
"DC_0x306"                                  : 0x306 * 4,
"DC_0x307"                                  : 0x307 * 4,
"DC_0x308"                                  : 0x30D * 4,
"DC_0x309"                                  : 0x309 * 4,
"DC_0x30A"                                  : 0x30A * 4,
"DC_0x30B"                                  : 0x30B * 4,
"DC_0x30C"                                  : 0x30C * 4,
"DC_0x30D"                                  : 0x30D * 4,
"DC_0x30E"                                  : 0x30E * 4,
"DC_0x30F"                                  : 0x30F * 4,
"DC_0x403"                                  : 0x403 * 4,
"DC_0x404"                                  : 0x404 * 4,
"DC_0x405"                                  : 0x405 * 4,
"DC_0x406"                                  : 0x406 * 4,
"DC_0x407"                                  : 0x407 * 4,
"DC_0x408"                                  : 0x408 * 4,
"DC_0x409"                                  : 0x409 * 4,
"DC_0x40A"                                  : 0x40A * 4,
"DC_0x42F"                                  : 0x42F * 4,
"DC_0x430"                                  : 0x430 * 4,
"DC_0x431"                                  : 0x431 * 4,
"DC_0x432"                                  : 0x432 * 4,
"DC_0x480"                                  : 0x480 * 4,
"DC_0x610"                                  : 0x610 * 4,
"DC_0x611"                                  : 0x611 * 4,
"DC_0x612"                                  : 0x612 * 4,
"DC_0x613"                                  : 0x613 * 4,
"DC_0x614"                                  : 0x614 * 4,
"DC_0x615"                                  : 0x615 * 4,
"DC_0x616"                                  : 0x616 * 4,
"DC_0x617"                                  : 0x617 * 4,
"DC_0x618"                                  : 0x618 * 4,
"DC_0x619"                                  : 0x619 * 4,
"DC_0x61A"                                  : 0x61A * 4,
"DC_0x61B"                                  : 0x61B * 4,
"DC_0x700"                                  : 0x700 * 4,
"DC_0x701"                                  : 0x701 * 4,
"DC_0x702"                                  : 0x702 * 4,
"DC_0x703"                                  : 0x703 * 4,
"DC_0x704"                                  : 0x704 * 4,
"DC_0x705"                                  : 0x705 * 4,
"DC_0x706"                                  : 0x706 * 4,
"DC_0x707"                                  : 0x707 * 4,
"DC_0x708"                                  : 0x708 * 4,
"DC_0x709"                                  : 0x709 * 4,
"DC_0x70A"                                  : 0x70A * 4,
"DC_0x70B"                                  : 0x70B * 4,
"DC_0x70C"                                  : 0x70C * 4,
"DC_0x70D"                                  : 0x70D * 4,
"DC_0x70E"                                  : 0x70E * 4,
"DC_0x70F"                                  : 0x70F * 4,
"DC_0x716"                                  : 0x716 * 4,
"DC_0x800"                                  : 0x800 * 4,
"DC_0x801"                                  : 0x801 * 4,
"DC_0x802"                                  : 0x802 * 4,
"DC_0x803"                                  : 0x803 * 4,
"DC_0x804"                                  : 0x804 * 4,
"DC_0x805"                                  : 0x805 * 4,
"DC_0x806"                                  : 0x806 * 4,
"DC_0x807"                                  : 0x807 * 4,
"DC_0x808"                                  : 0x808 * 4,
"DC_0x809"                                  : 0x809 * 4,
"DC_0x80A"                                  : 0x80A * 4,
"DC_0x80B"                                  : 0x80B * 4

#228FC
}