extra_features = []

arch = host_machine.cpu_family()

arch = {
    'aarch64' : 'arm64',
    'loongarch64' : 'loong',
    'mips64' : 'mips',
    'parisc' : 'hppa',
    'riscv32' : 'riscv',
    'riscv64' : 'riscv',
    's390x' : 's390',
    'sh4' : 'sh',
    'sparc64' : 'sparc',
    'x86_64' : 'amd64'
}.get(arch, arch)

if host_machine.system() == 'freebsd'
    arch += '-fbsd'
endif

if not system_wide
    subdir_done()
endif
