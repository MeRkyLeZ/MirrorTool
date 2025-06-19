py_bins = [
    'lmirrordist'
]

install_data(
    py_bins,
    install_dir : system_wide ? get_option('bindir') : mirrortool_bindir,
    install_mode : 'rwxr-xr-x',
)
