const_py = configure_file(
    input : 'const.py',
    output : 'const.py',
    configuration : conf_data
)

installation_py = configure_file(
    input : 'installation.py',
    output : 'installation.py',
    configuration : conf_data
)

__init__py = configure_file(
    input : '__init__.py',
    output : '__init__.py',
    configuration : conf_data
)

py.install_sources(
    [
        const_py,
        installation_py,
        __init__py,
    ],
    subdir : 'mirrortool',
    pure : not native_extensions
)

subdir('util')
subdir('_lmirrordist')
