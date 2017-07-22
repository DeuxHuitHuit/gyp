{
    'targets': [{
        'target_name': 'libwebp',
        'type': 'static_library',
        'include_dirs': [
            '../third-party/libwebp/src/',
        ],
        'direct_dependent_settings': {
            'include_dirs': [
                '../third-party/libwebp/src/',
            ],
        },
        'cflags': [
            '-fvisibility=hidden',
            '-Wall',
            '-Wconstant-conversion',
            '-Wdeclaration-after-statement',
            '-Wextra',
            '-Wfloat-conversion',
            '-Wformat -Wformat-nonliteral',
            '-Wformat -Wformat-security',
            '-Wmissing-declarations',
            '-Wmissing-prototypes',
            '-Wold-style-definition',
            '-Wparentheses-equality',
            '-Wshadow',
            '-Wshorten-64-to-32',
            '-Wunreachable-code',
            '-Wunused-but-set-variable',
            '-Wunused',
            '-Wvla'
        ],
        'libraries': [
            '-lm'
        ],
        'sources': [
            '../third-party/libwebp/src/enc/webp_enc.c',
            '../third-party/libwebp/src/dec/webp_dec.c',
        ],
    }],
    'configurations': {
        'Debug': {
            'cflags': [ '-g', '-O0' ],
            'xcode_settings': {
                'OTHER_CFLAGS': [ '-g', '-O0' ]
            }
        },
        'Release': {
            'cflags': [ '-g', '-O3' ],
            'defines': [ 'NDEBUG' ],
            'xcode_settings': {
                'OTHER_CFLAGS': [ '-g', '-O3' ]
            }
        }
    },
}
