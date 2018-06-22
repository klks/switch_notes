#https://github.com/Atmosphere-NX/Atmosphere/blob/master/fusee/fusee-primary/src/hwinit/clock.h
clkrst_values = {
"base"                                      : 0x60006000,
"CLK_RST_CONTROLLER_SCLK_BURST_POLICY"      : 0x28,
"CLK_RST_CONTROLLER_SUPER_SCLK_DIVIDER"     : 0x2C,
"CLK_RST_CONTROLLER_CLK_SYSTEM_RATE"        : 0x30,
"CLK_RST_CONTROLLER_MISC_CLK_ENB"           : 0x48,
"CLK_RST_CONTROLLER_OSC_CTRL"               : 0x50,
"CLK_RST_CONTROLLER_CLK_SOURCE_EMC"         : 0x19C,
"CLK_RST_CONTROLLER_CLK_ENB_X_SET"          : 0x284,
"CLK_RST_CONTROLLER_RST_DEV_H_SET"          : 0x308,
"CLK_RST_CONTROLLER_CLK_ENB_H_SET"          : 0x328,
"CLK_RST_CONTROLLER_RST_DEVICES_V"          : 0x358,
"CLK_RST_CONTROLLER_RST_CPUG_CMPLX_CLR"     : 0x454,
"CLK_RST_CONTROLLER_SPARE_REG0"             : 0x55C,
"CLK_RST_CONTROLLER_PLLMB_BASE"             : 0x5E8,

#Used by SX OS
"CLK_RST_0x3B4"                             : 0x3B4,
"CLK_RST_0x20"                              : 0x20,
"CLK_RST_0x360"                             : 0x360,
"CLK_RST_0x24"                              : 0x24,
"CLK_RST_0x440"                             : 0x440,
"CLK_RST_0x388"                             : 0x388,
"CLK_RST_0x518"                             : 0x518,
"CLK_RST_0xE4"                              : 0xE4,
"CLK_RST_0xE0"                              : 0xE0
}