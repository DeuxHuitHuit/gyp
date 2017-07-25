# from: https://github.com/pagespeed/page-speed/blob/master/deps/libwebp-0.2.0/libwebp.gyp
{
    'targets': [
        {
          'target_name': 'libwebp_dec',
          'type': 'static_library',
          'include_dirs': [
            '../third-party/libwebp/src/',
          ],
          'sources': [
            '../third-party/libwebp/src/dec/alpha_dec.c',
            '../third-party/libwebp/src/dec/buffer_dec.c',
            '../third-party/libwebp/src/dec/frame_dec.c',
            '../third-party/libwebp/src/dec/idec_dec.c',
            '../third-party/libwebp/src/dec/io_dec.c',
            '../third-party/libwebp/src/dec/quant_dec.c',
            '../third-party/libwebp/src/dec/tree_dec.c',
            '../third-party/libwebp/src/dec/vp8_dec.c',
            '../third-party/libwebp/src/dec/vp8l_dec.c',
            '../third-party/libwebp/src/dec/webp_dec.c',
          ],
        },
        {
          'target_name': 'libwebp_dsp',
          'type': 'static_library',
          'include_dirs': [
            '../third-party/libwebp/src/',
          ],
          'sources': [
            '../third-party/libwebp/src/dsp/alpha_processing.c',
            '../third-party/libwebp/src/dsp/alpha_processing_sse2.c',
            '../third-party/libwebp/src/dsp/argb.c',
            '../third-party/libwebp/src/dsp/argb_sse2.c',
            '../third-party/libwebp/src/dsp/cpu.c',
            '../third-party/libwebp/src/dsp/cost.c',
            '../third-party/libwebp/src/dsp/dec.c',
            '../third-party/libwebp/src/dsp/dec_sse2.c',
            '../third-party/libwebp/src/dsp/dec_clip_tables.c',
            '../third-party/libwebp/src/dsp/dec_sse2.c',
            '../third-party/libwebp/src/dsp/enc.c',
            '../third-party/libwebp/src/dsp/enc_sse2.c',
            '../third-party/libwebp/src/dsp/filters.c',
            '../third-party/libwebp/src/dsp/filters_sse2.c',
            '../third-party/libwebp/src/dsp/lossless.c',
            '../third-party/libwebp/src/dsp/lossless_sse2.c',
            '../third-party/libwebp/src/dsp/lossless_enc.c',
            '../third-party/libwebp/src/dsp/lossless_enc_sse2.c',
            '../third-party/libwebp/src/dsp/rescaler.c',
            '../third-party/libwebp/src/dsp/rescaler_sse2.c',
            '../third-party/libwebp/src/dsp/upsampling.c',
            '../third-party/libwebp/src/dsp/upsampling_sse2.c',
            '../third-party/libwebp/src/dsp/yuv.c',
            '../third-party/libwebp/src/dsp/yuv_sse2.c',
          ],
        },
        {
          'target_name': 'libwebp_enc',
          'type': 'static_library',
          'include_dirs': [
            '../third-party/libwebp/src/',
          ],
          'sources': [
            '../third-party/libwebp/src/enc/alpha_enc.c',
            '../third-party/libwebp/src/enc/analysis_enc.c',
            '../third-party/libwebp/src/enc/backward_references_enc.c',
            '../third-party/libwebp/src/enc/config_enc.c',
            '../third-party/libwebp/src/enc/cost_enc.c',
            '../third-party/libwebp/src/enc/delta_palettization_enc.c',
            '../third-party/libwebp/src/enc/filter_enc.c',
            '../third-party/libwebp/src/enc/frame_enc.c',
            '../third-party/libwebp/src/enc/histogram_enc.c',
            '../third-party/libwebp/src/enc/iterator_enc.c',
            '../third-party/libwebp/src/enc/near_lossless_enc.c',
            '../third-party/libwebp/src/enc/picture_csp_enc.c',
            '../third-party/libwebp/src/enc/picture_enc.c',
            '../third-party/libwebp/src/enc/picture_psnr_enc.c',
            '../third-party/libwebp/src/enc/picture_rescale_enc.c',
            '../third-party/libwebp/src/enc/picture_tools_enc.c',
            '../third-party/libwebp/src/enc/predictor_enc.c',
            '../third-party/libwebp/src/enc/quant_enc.c',
            '../third-party/libwebp/src/enc/syntax_enc.c',
            '../third-party/libwebp/src/enc/token_enc.c',
            '../third-party/libwebp/src/enc/tree_enc.c',
            '../third-party/libwebp/src/enc/vp8l_enc.c',
            '../third-party/libwebp/src/enc/webp_enc.c',
          ],
        },
        {
          'target_name': 'libwebp_utils',
          'type': 'static_library',
          'include_dirs': [
            '../third-party/libwebp/src/',
          ],
          'sources': [
            '../third-party/libwebp/src/utils/bit_reader_utils.c',
            '../third-party/libwebp/src/utils/bit_writer_utils.c',
            '../third-party/libwebp/src/utils/color_cache_utils.c',
            '../third-party/libwebp/src/utils/filters_utils.c',
            '../third-party/libwebp/src/utils/huffman_utils.c',
            '../third-party/libwebp/src/utils/huffman_encode_utils.c',
            '../third-party/libwebp/src/utils/quant_levels_utils.c',
            '../third-party/libwebp/src/utils/quant_levels_dec_utils.c',
            '../third-party/libwebp/src/utils/random_utils.c',
            '../third-party/libwebp/src/utils/rescaler_utils.c',
            '../third-party/libwebp/src/utils/thread_utils.c',
            '../third-party/libwebp/src/utils/utils.c',
          ],
        },
        {
        'target_name': 'libwebp',
        'type': 'none',
        'dependencies' : [
          'libwebp_dec',
          'libwebp_dsp',
          'libwebp_enc',
          'libwebp_utils',
        ],
        'direct_dependent_settings': {
            'include_dirs': [
              '../third-party/libwebp/src/',
            ],
        },
        'conditions': [
          ['OS!="win"', {'product_name': 'webp'}],
        ],
    }],
    'configurations': {
        'Debug': {
            'cflags': [ '-w', '-g', '-O0' ],
            'xcode_settings': {
                'OTHER_CFLAGS': [ '-w', '-g', '-O0' ]
            }
        },
        'Release': {
            'cflags': [ '-w', '-g', '-O3' ],
            'defines': [ 'NDEBUG' ],
            'xcode_settings': {
                'OTHER_CFLAGS': [ '-w', '-g', '-O3' ]
            }
        }
    },
}
