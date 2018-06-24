#https://github.com/Atmosphere-NX/Atmosphere/blob/master/fusee/fusee-primary/src/hwinit/pmc.h
pmc_values = {
"name"          : "PMC",
"base"          : 0x7000E400,
"size"          : 0x1000,

"APBDEV_PMC_PWRGATE_TOGGLE"         : 0x30,
"APBDEV_PMC_PWRGATE_STATUS"         : 0x38,
"APBDEV_PMC_NO_IOPOWER"             : 0x44,
"APBDEV_PMC_SCRATCH20"              : 0xA0,
"APBDEV_PMC_PWR_DET_VAL"            : 0xE4,
"APBDEV_PMC_DDR_PWR"                : 0xE8,
"APBDEV_PMC_CRYPTO_OP"              : 0xF4,
"APBDEV_PMC_OSC_EDPD_OVER"          : 0x1A4,
"APBDEV_PMC_IO_DPD_REQ"             : 0x1B8,
"APBDEV_PMC_IO_DPD2_REQ"            : 0x1C0,
"APBDEV_PMC_VDDP_SEL"               : 0x1CC,
"APBDEV_PMC_TSC_MULT"               : 0x2B4,
"APBDEV_PMC_REG_SHORT"              : 0x2CC,
"APBDEV_PMC_WEAK_BIAS"              : 0x2C8,
"APBDEV_PMC_SECURE_SCRATCH21"       : 0x334,
"APBDEV_PMC_CNTRL2"                 : 0x440,
"APBDEV_PMC_IO_DPD4_REQ"            : 0x464,
"APBDEV_PMC_DDR_CNTRL"              : 0x4E4,
"APBDEV_PMC_SCRATCH188"             : 0x810,
"APBDEV_PMC_SCRATCH190"             : 0x818,
"APBDEV_PMC_SCRATCH200"             : 0x840,

#Used by SX OS
"APBDEV_PMC_0x1D0"                  : 0x1D0,
"APBDEV_PMC_0x45C"                  : 0x45C
}