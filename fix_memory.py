import idc, idautils

#http://switchbrew.org/index.php?title=TSEC
tsec_values = {
"TSEC_THI_CTXSW"                    : 0x54500020,
"TSEC_THI_METHOD0"                  : 0x54500040,
"TSEC_THI_METHOD1"                  : 0x54500044,
"TSEC_THI_INT_STATUS"               : 0x54500078,
"TSEC_THI_INT_MASK"                 : 0x5450007C,
"TSEC_THI_UNK0"                     : 0x54500084,
"TSEC_THI_SLCG_OVERRIDE_HIGH_A"     : 0x54500088,
"TSEC_THI_SLCG_OVERRIDE_LOW_A"      : 0x5450008C,
"TSEC_THI_CLK_OVERRIDE"             : 0x54500E00,
"FALCON_IRQSSET"                    : 0x54501000,
"FALCON_IRQSCLR"                    : 0x54501004,
"FALCON_IRQSTAT"                    : 0x54501008,
"FALCON_IRQMODE"                    : 0x5450100C,
"FALCON_IRQMSET"                    : 0x54501010,
"FALCON_IRQMCLR"                    : 0x54501014,
"FALCON_IRQMASK"                    : 0x54501018,
"FALCON_IRQDEST"                    : 0x5450101C,
"FALCON_SCRATCH0"                   : 0x54501040,
"FALCON_SCRATCH1"                   : 0x54501044,
"FALCON_ITFEN"                      : 0x54501048,
"FALCON_IDLESTATE"                  : 0x5450104C,
"FALCON_CURCTX"                     : 0x54501050,
"FALCON_NXTCTX"                     : 0x54501054,
"FALCON_SCRATCH2"                   : 0x54501080,
"FALCON_SCRATCH3"                   : 0x54501084,
"FALCON_CGCTL"                      : 0x545010A0,
"FALCON_ENGCTL"                     : 0x545010A4,
"FALCON_CPUCTL"                     : 0x54501100,
"FALCON_BOOTVEC"                    : 0x54501104,
"FALCON_HWCFG"                      : 0x54501108,
"FALCON_DMACTL"                     : 0x5450110C,
"FALCON_DMATRFBASE"                 : 0x54501110,
"FALCON_DMATRFMOFFS"                : 0x54501114,
"FALCON_DMATRFCMD"                  : 0x54501118,
"FALCON_DMATRFFBOFFS"               : 0x5450111C,
"FALCON_CPUCTL_ALIAS"               : 0x54501130,
"FALCON_IMFILLRNG1"                 : 0x54501154,
"FALCON_IMFILLCTL"                  : 0x54501158,
"FALCON_EXTERRADDR"                 : 0x54501168,
"FALCON_EXTERRSTAT"                 : 0x5450116C,
"FALCON_CG2"                        : 0x5450117C,
"FALCON_CODE_INDEX"                 : 0x54501180,
"FALCON_CODE"                       : 0x54501184,
"FALCON_CODE_VIRT_ADDR"             : 0x54501188,
"FALCON_DATA_INDEX0"                : 0x545011C0,
"FALCON_DATA0"                      : 0x545011C4,
"FALCON_DATA_INDEX1"                : 0x545011C8,
"FALCON_DATA1"                      : 0x545011CC,
"FALCON_DATA_INDEX2"                : 0x545011D0,
"FALCON_DATA2"                      : 0x545011D4,
"FALCON_DATA_INDEX3"                : 0x545011D8,
"FALCON_DATA3"                      : 0x545011DC,
"FALCON_DATA_INDEX4"                : 0x545011E0,
"FALCON_DATA4"                      : 0x545011E4,
"FALCON_DATA_INDEX5"                : 0x545011E8,
"FALCON_DATA5"                      : 0x545011EC,
"FALCON_DATA_INDEX6"                : 0x545011F0,
"FALCON_DATA6"                      : 0x545011F4,
"FALCON_DATA_INDEX7"                : 0x545011F8,
"FALCON_DATA7"                      : 0x545011FC,
"FALCON_ICD_CMD"                    : 0x54501200,
"FALCON_ICD_ADDR"                   : 0x54501204,
"FALCON_ICD_WDATA"                  : 0x54501208,
"FALCON_ICD_RDATA"                  : 0x5450120C,
"FALCON_SCTL"                       : 0x54501240,
"TSEC_SCP_CTL_UNK0"                 : 0x54501400,
"TSEC_SCP_CTL_UNK1"                 : 0x54501404,
"TSEC_SCP_CTL_STAT"                 : 0x54501408,
"TSEC_SCP_CTL_AUTH_MODE"            : 0x5450140C,
"TSEC_SCP_CTL_UNK2"                 : 0x54501410,
"TSEC_SCP_CTL_PKEY"                 : 0x54501418,
"TSEC_SCP_CTL_UNK3"                 : 0x54501420,
"TSEC_SCP_CTL_UNK4"                 : 0x54501428,
"TSEC_SCP_CTL_UNK5"                 : 0x54501430,
"TSEC_SCP_UNK0"                     : 0x54501454,
"TSEC_SCP_UNK1"                     : 0x54501458,
"TSEC_SCP_UNK2"                     : 0x54501470,
"TSEC_SCP_UNK3"                     : 0x54501480,
"TSEC_SCP_UNK4"                     : 0x54501490,
"TSEC_UNK0"                         : 0x54501500,
"TSEC_UNK1"                         : 0x54501504,
"TSEC_UNK2"                         : 0x5450150C,
"TSEC_UNK3"                         : 0x54501510,
"TSEC_UNK4"                         : 0x54501514,
"TSEC_UNK5"                         : 0x54501518,
"TSEC_UNK6"                         : 0x5450151C,
"TSEC_UNK7"                         : 0x54501528,
"TSEC_UNK8"                         : 0x5450152C,
"TSEC_TFBIF_MCCIF_UNK0"             : 0x54501600,
"TSEC_TFBIF_MCCIF_FIFOCTRL"         : 0x54501604,
"TSEC_TFBIF_MCCIF_UNK1"             : 0x54501608,
"TSEC_TFBIF_MCCIF_UNK2"             : 0x5450160C,
"TSEC_TFBIF_UNK0"                   : 0x54501630,
"TSEC_TFBIF_UNK1"                   : 0x54501634,
"TSEC_TFBIF_UNK2"                   : 0x54501640,
"TSEC_DMA_CMD"                      : 0x54501700,
"TSEC_DMA_ADDR"                     : 0x54501704,
"TSEC_DMA_VAL"                      : 0x54501708,
"TSEC_DMA_UNK"                      : 0x5450170C,
"TSEC_TEGRA_UNK0"                   : 0x54501800,
"TSEC_TEGRA_UNK1"                   : 0x54501824,
"TSEC_TEGRA_UNK2"                   : 0x54501828,
"TSEC_TEGRA_UNK3"                   : 0x5450182C,
"TSEC_TEGRA_CTL"                    : 0x54501838
}

#http://switchbrew.org/index.php?title=Security_Engine
se_values = {
"SE_OPERATION_UNK0"                 : 0x70012000,
"SE_OPERATION_UNK1"                 : 0x70012004,
"SE_OPERATION"                      : 0x70012008,
"SE_INT_ENABLE"                     : 0x7001200C,
"SE_INT_STATUS"                     : 0x70012010,
"SE_CONFIG"                         : 0x70012014,
"SE_IN_LL_ADDR"                     : 0x70012018,
"SE_OUT_LL_ADDR"                    : 0x70012024,
"SE_HASH_RESULT"                    : 0x70012030,
"SE_CONTEXT_SAVE_CONFIG"            : 0x70012070,
"SE_SHA_CONFIG"                     : 0x70012200,
"SE_SHA_MSG_LENGTH"                 : 0x70012204,
"SE_SHA_MSG_UNK0"                   : 0x70012208,
"SE_SHA_MSG_UNK1"                   : 0x7001220C,
"SE_SHA_MSG_UNK2"                   : 0x70012210,
"SE_SHA_MSG_LEFT"                   : 0x70012214,
"SE_SHA_MSG_UNK3"                   : 0x70012218,
"SE_SHA_MSG_UNK4"                   : 0x7001221C,
"SE_SHA_MSG_UNK5"                   : 0x70012220,
"SE_AES_KEY_READ_DISABLE"           : 0x70012280,
"SE_AES_KEYTABLE_ACCESS"            : 0x70012284,
"SE_CRYPTO"                         : 0x70012304,
"SE_CRYPTO_CTR"                     : 0x70012308,
"SE_BLOCK_COUNT"                    : 0x70012318,
"SE_AES_KEYTABLE_ADDR"              : 0x7001231C,
"SE_AES_KEYTABLE_DATA"              : 0x70012320,
"SE_CRYPTO_KEYTABLE_DST"            : 0x70012330,
"SE_RNG_CONFIG"                     : 0x70012340,
"SE_RNG_SRC_CONFIG"                 : 0x70012344,
"SE_RNG_RESEED_INTERVAL"            : 0x70012348,
"SE_RSA_CONFIG"                     : 0x70012400,
"SE_RSA_KEY_SIZE"                   : 0x70012404,
"SE_RSA_EXP_SIZE"                   : 0x70012408,
"SE_RSA_KEY_READ_DISABLE"           : 0x7001240C,
"SE_RSA_KEYTABLE_ACCESS"            : 0x70012410,
"SE_RSA_KEYTABLE_ADDR"              : 0x70012420,
"SE_RSA_KEYTABLE_DATA"              : 0x70012424,
"SE_RSA_OUTPUT"                     : 0x70012428,
"SE_STATUS_FLAGS"                   : 0x70012800,
"SE_ERR_STATUS"                     : 0x70012804,
"SE_SPARE_0"                        : 0x7001280C
}

#https://github.com/Atmosphere-NX/Atmosphere/blob/master/fusee/fusee-primary/src/hwinit/pmc.h
pmc_values = {
"APBDEV_PMC_PWRGATE_TOGGLE"         : 0x54501030,
"APBDEV_PMC_PWRGATE_STATUS"         : 0x54501038,
"APBDEV_PMC_NO_IOPOWER"             : 0x54501044,
"APBDEV_PMC_SCRATCH20"              : 0x545010A0,
"APBDEV_PMC_DDR_PWR"                : 0x545010E8,
"APBDEV_PMC_CRYPTO_OP"              : 0x545010F4,
"APBDEV_PMC_OSC_EDPD_OVER"          : 0x545011A4,
"APBDEV_PMC_IO_DPD_REQ"             : 0x545011B8,
"APBDEV_PMC_IO_DPD2_REQ"            : 0x545011C0,
"APBDEV_PMC_VDDP_SEL"               : 0x545011CC,
"APBDEV_PMC_TSC_MULT"               : 0x545012B4,
"APBDEV_PMC_REG_SHORT"              : 0x545012CC,
"APBDEV_PMC_WEAK_BIAS"              : 0x545012C8,
"APBDEV_PMC_SECURE_SCRATCH21"       : 0x54501334,
"APBDEV_PMC_CNTRL2"                 : 0x54501440,
"APBDEV_PMC_IO_DPD4_REQ"            : 0x54501464,
"APBDEV_PMC_DDR_CNTRL"              : 0x545014E4,
"APBDEV_PMC_SCRATCH188"             : 0x54501810,
"APBDEV_PMC_SCRATCH190"             : 0x54501818,
"APBDEV_PMC_SCRATCH200"             : 0x54501840
}

#https://github.com/Atmosphere-NX/Atmosphere/blob/master/fusee/fusee-primary/src/hwinit/clock.h
clkrst_values = {
"CLK_RST_CONTROLLER_SCLK_BURST_POLICY"      : 0x60006028,
"CLK_RST_CONTROLLER_SUPER_SCLK_DIVIDER"     : 0x6000602C,
"CLK_RST_CONTROLLER_CLK_SYSTEM_RATE"        : 0x60006030,
"CLK_RST_CONTROLLER_MISC_CLK_ENB"           : 0x60006048,
"CLK_RST_CONTROLLER_OSC_CTRL"               : 0x60006050,
"CLK_RST_CONTROLLER_CLK_SOURCE_EMC"         : 0x6000619C,
"CLK_RST_CONTROLLER_CLK_ENB_X_SET"          : 0x60006284,
"CLK_RST_CONTROLLER_RST_DEV_H_SET"          : 0x60006308,
"CLK_RST_CONTROLLER_CLK_ENB_H_SET"          : 0x60006328,
"CLK_RST_CONTROLLER_RST_DEVICES_V"          : 0x60006358,
"CLK_RST_CONTROLLER_RST_CPUG_CMPLX_CLR"     : 0x60006454,
"CLK_RST_CONTROLLER_SPARE_REG0"             : 0x6000655C,
"CLK_RST_CONTROLLER_PLLMB_BASE"             : 0x600065E8
}

#http://switchbrew.org/index.php?title=Memory_layout
def add_segments():
    segments_to_add = [
        {
            "name" : "HOST1X",
            "start": 0x54500000,
            "end": 0x54501000
        },
        {
            "name" : "TSEC",
            "start": 0x54501000,
            "end": 0x54502000
        },
        {
            "name" : "PMC",
            "start": 0x7000E000,
            "end": 0x7000F000
        },
        {
            "name" : "SE",
            "start": 0x70012000,
            "end": 0x70013000
        },
        {
            "name" : "CLKRST",
            "start": 0x60006000,
            "end": 0x60007000
        }
    ]

    segments = []
    for start in idautils.Segments():
        print(start)
        segments.append(start)

    for new_segment in segments_to_add:
        if new_segment["start"] not in segments:
            print("Adding new segment {}").format(new_segment["name"])
            idc.add_segm_ex(new_segment["start"], new_segment["end"], 0,1,1,2, idc.ADDSEG_NOSREG)
            idc.set_segm_name(new_segment["start"], new_segment["name"])
        else:
            print("Segment {} exists, skipping").format(new_segment["name"])

def add_defines():
    process_array = [tsec_values, se_values, pmc_values, clkrst_values]

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