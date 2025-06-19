project(
    'mirrortool',
    'c',
    version : '1.0.0',
    license : 'GPL-2.0-or-later',
    meson_version : '>=0.58.0'
)

py_mod = import('python')
# TODO: Add "pure : not native_extensions" here instead of py.install_sources()
# when requiring Meson >=0.64.0.
py = py_mod.find_installation()

sed = find_program('sed', required : true)

system_wide = get_option('system-wide')
native_extensions = get_option('native-extensions')

eprefix = get_option('eprefix')
prefixdir = get_option('prefix')
datadir = get_option('datadir')
docdir = get_option('docdir')
mirrortool_base = get_option('mirrortool-base')
mirrortool_bindir = get_option('mirrortool-bindir')
mirrortool_datadir = get_option('mirrortool-datadir')

sysconfdir = system_wide ? get_option('sysconfdir') \
                         : datadir / 'etc'

if docdir == ''
    docdir = system_wide ? datadir / 'doc' / 'mirrortool' \
                         : datadir / 'share' / 'mirrortool' / 'doc'
endif

if mirrortool_base == ''
    # This path must be absolute when system-wide.
    mirrortool_base = system_wide ? prefixdir / 'lib' / 'mirrortool' \
                               : datadir / 'lib' / 'mirrortool'
endif

if mirrortool_bindir == ''
    mirrortool_bindir = mirrortool_base / 'bin'
endif

if mirrortool_datadir == ''
    mirrortool_datadir = system_wide ? datadir / 'mirrortool' \
                                  : datadir / 'share' / 'mirrortool'
endif

# hprefixify is copied from prefix.eclass.
dirs = '/(usr|lib(|[onx]?32|n?64)|etc|bin|sbin|var|opt|run)'
hprefixify = [
    sed, '-r',
    '-e', 's,([^[:alnum:]}\\)\\.])' + dirs + ',\\1' + eprefix.replace(',', '\\,') + '/\\2,g',
    '-e', 's,^' + dirs + ',' + eprefix.replace(',', '\\,') + '/\\1,',
    '@INPUT@'
]

# Use Portage's own code to determine the version from git, if possible.
version = run_command(
    [py, '-c', 'import mirrortool; print(mirrortool.VERSION)'],
    env : { 'PYTHONPATH' : meson.current_source_dir() / 'lib' },
    capture : true,
    check : false
)

# Fall back to the Meson project version above.
if version.returncode() == 0
    version = version.stdout().strip()
    if version == 'HEAD'
        version = ''
    endif
else
    version = ''
endif

conf_data = configuration_data({
    'VERSION' : version == '' ? meson.project_version() : version
})

if system_wide
    conf_data.set('INSTALL_TYPE', 'SYSTEM')
    conf_data.set('MIRRORTOOL_BASE_PATH', mirrortool_base)
    conf_data.set('MIRRORTOOL_BIN_PATH', mirrortool_bindir)
    conf_data.set('EPREFIX', eprefix)
else
    conf_data.set('INSTALL_TYPE', 'MODULE')
    conf_data.set('MIRRORTOOL_BASE_PATH', '')
    conf_data.set('MIRRORTOOL_BIN_PATH', '')
    conf_data.set('EPREFIX', '')
endif

subdir('bin')
subdir('lib')

if native_extensions
    subdir('src')
endif

if system_wide
	METADATA = configure_file(
		input : 'cnf/METADATA',
		output : 'METADATA',
		configuration : conf_data
	)
	install_data(
		[
			METADATA
		],
		install_dir : py.get_install_dir() / 'mirrortool-@0@.dist-info'.format(conf_data.get('VERSION'))
	)
endif

if get_option('code-only')
    subdir_done()
endif

subdir('cnf')

if not system_wide
    subdir_done()
endif

subdir('man')
