{
    'targets': [{
        'target_name': 'zlib',
        'type': 'static_library',
        'include_dirs': [
            '../third-party/zlib/'
        ],
        'direct_dependent_settings': {
            'include_dirs': [
                '../third-party/zlib/'
            ]
        },
        'cflags': [
            '-w', # supresses warnings
            '-fvisibility=hidden',
        ],
        'xcode_settings': {
            'OTHER_CFLAGS': [
                '-w', # supresses warnings
                '-fvisibility=hidden',
            ]
        },
        'sources': [
            '../third-party/zlib/adler32.c',
            '../third-party/zlib/compress.c',
            '../third-party/zlib/crc32.c',
            '../third-party/zlib/deflate.c',
            '../third-party/zlib/gzclose.c',
            '../third-party/zlib/gzlib.c',
            '../third-party/zlib/gzread.c',
            '../third-party/zlib/gzwrite.c',
            '../third-party/zlib/infback.c',
            '../third-party/zlib/inffast.c',
            '../third-party/zlib/inflate.c',
            '../third-party/zlib/inftrees.c',
            '../third-party/zlib/trees.c',
            '../third-party/zlib/uncompr.c',
            '../third-party/zlib/zutil.c'
        ]
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