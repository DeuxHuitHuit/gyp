{
    'includes': [ 'common.gypi' ],
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
        'conditions': [
            ['OS == "win"', {
                'include_dirs': [
                    '../third-party/giflib'
                ],
            }],
        ],
        'sources': [
            '../third-party/giflib/lib/dgif_lib.c',
            '../third-party/giflib/lib/gifalloc.c',
            '../third-party/giflib/lib/gif_err.c',
        ],
    }],
}
