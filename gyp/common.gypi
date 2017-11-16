{
    'target_defaults': {
        'default_configuration': 'Release',
        'cflags': [
            '-w', # supresses warnings
            '-fvisibility=hidden',
        ],
        'cflags!': [
            '-Wall',
            '-g',
        ],
        'xcode_settings': {
            'OTHER_CFLAGS': [
                '-w', # supresses warnings
                '-fvisibility=hidden',
            ],
            'WARNING_CFLAGS!': [
                '-W',
                '-Wall',
            ],
            'MACOSX_DEPLOYMENT_TARGET':'10.9', # some how, this does not work
        },
        'msvs_disabled_warnings': [4018, 4013, 4006, 4221], # some how, this does not work
        'conditions': [
            ['OS == "win"', {
                'defines': [
                    '_WIN32'
                ]
            }],
        ],
        'configurations': {
            'Debug': {
                'defines': [
                    'ASAN_OPTIONS=symbolize=1'
                ],
                'xcode_settings': {
                    'GCC_OPTIMIZATION_LEVEL': '0',
                    'GCC_GENERATE_DEBUGGING_SYMBOLS': 'YES',
                    'MACOSX_DEPLOYMENT_TARGET':'10.9',
                }
            },
            'Release': {
                'defines': [ 'NDEBUG' ],
                'cflags!': ['-Os'],
                'cflags': ['-O3'],
                'xcode_settings': {
                    'GCC_OPTIMIZATION_LEVEL': '3',
                    'GCC_GENERATE_DEBUGGING_SYMBOLS': 'NO',
                    'DEAD_CODE_STRIPPING': 'YES',
                    'GCC_INLINES_ARE_PRIVATE_EXTERN': 'YES',
                    'MACOSX_DEPLOYMENT_TARGET':'10.9',
                }
            }
        },
    }
}