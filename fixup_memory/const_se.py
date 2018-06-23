#http://switchbrew.org/index.php?title=Security_Engine
se_values = {
"name"          : "SE",
"base"          : 0x70012000,
"size"          : 0x2000,

"SE_OPERATION_UNK0"                 : 0x0,
"SE_OPERATION_UNK1"                 : 0x4,
"SE_OPERATION"                      : 0x8,
"SE_INT_ENABLE"                     : 0xC,
"SE_INT_STATUS"                     : 0x10,
"SE_CONFIG"                         : 0x14,
"SE_IN_LL_ADDR"                     : 0x18,
"SE_OUT_LL_ADDR"                    : 0x24,
"SE_HASH_RESULT"                    : 0x30,
"SE_CONTEXT_SAVE_CONFIG"            : 0x70,
"SE_SHA_CONFIG"                     : 0x200,
"SE_SHA_MSG_LENGTH"                 : 0x204,
"SE_SHA_MSG_UNK0"                   : 0x208,
"SE_SHA_MSG_UNK1"                   : 0x20C,
"SE_SHA_MSG_UNK2"                   : 0x210,
"SE_SHA_MSG_LEFT"                   : 0x214,
"SE_SHA_MSG_UNK3"                   : 0x218,
"SE_SHA_MSG_UNK4"                   : 0x21C,
"SE_SHA_MSG_UNK5"                   : 0x220,
"SE_AES_KEY_READ_DISABLE"           : 0x280,
"SE_AES_KEYTABLE_ACCESS"            : 0x284,
"SE_CRYPTO"                         : 0x304,
"SE_CRYPTO_CTR"                     : 0x308,
"SE_BLOCK_COUNT"                    : 0x318,
"SE_AES_KEYTABLE_ADDR"              : 0x31C,
"SE_AES_KEYTABLE_DATA"              : 0x320,
"SE_CRYPTO_KEYTABLE_DST"            : 0x330,
"SE_RNG_CONFIG"                     : 0x340,
"SE_RNG_SRC_CONFIG"                 : 0x344,
"SE_RNG_RESEED_INTERVAL"            : 0x348,
"SE_RSA_CONFIG"                     : 0x400,
"SE_RSA_KEY_SIZE"                   : 0x404,
"SE_RSA_EXP_SIZE"                   : 0x408,
"SE_RSA_KEY_READ_DISABLE"           : 0x40C,
"SE_RSA_KEYTABLE_ACCESS"            : 0x410,
"SE_RSA_KEYTABLE_ADDR"              : 0x420,
"SE_RSA_KEYTABLE_DATA"              : 0x424,
"SE_RSA_OUTPUT"                     : 0x428,
"SE_STATUS_FLAGS"                   : 0x800,
"SE_ERR_STATUS"                     : 0x804,
"SE_SPARE_0"                        : 0x80C
}