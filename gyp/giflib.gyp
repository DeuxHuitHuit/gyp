{
    'targets': [{
        'target_name': 'giflib',
        'type': 'static_library',
        'defines': [
            'HAVE_CONFIG_H',
        ],
        'include_dirs': [
            '../third-party/giflib/lib',
        ],
        'direct_dependent_settings': {
            'include_dirs': [
                '../third-party/giflib/lib',
            ],
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
            '../third-party/giflib/lib/dgif_lib.c',
            '../third-party/giflib/lib/gifalloc.c',
            '../third-party/giflib/lib/gif_err.c',
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
