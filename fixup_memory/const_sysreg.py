sysreg_values = {
"name"          : "SYSREG",
"base"          : 0x6000C000,
"size"          : 0x1000,

"AHB_ARBITRATION_XBAR_CTRL"         : 0xE0
}

sb_values = {
"base"                              : sysreg_values["base"] + 0x200,
"SB_CSR_0"                          : 0x00,
"SB_PIROM_START_0"                  : 0x04,
"SB_PFCFG_0"                        : 0x08,
"SB_SECURE_SPAREREG_0_0"            : 0x0C,
"SB_SECURE_SPAREREG_1_0"            : 0x10,
"SB_SECURE_SPAREREG_2_0"            : 0x14,
"SB_SECURE_SPAREREG_3_0"            : 0x18,
"SB_SECURE_SPAREREG_4_0"            : 0x1C,
"SB_SECURE_SPAREREG_5_0"            : 0x20,
"SB_SECURE_SPAREREG_6_0"            : 0x24,
"SB_SECURE_SPAREREG_7_0"            : 0x28,
"SB_AA64_RESET_LOW_0"               : 0x30,
"SB_AA64_RESET_HIGH_0"              : 0x34
}