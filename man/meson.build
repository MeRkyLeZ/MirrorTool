man_pages_out = []
man_pages_in = [
    'lmirrordist.1',
]

foreach man_page : man_pages_in
    man_pages_out += configure_file(
        input : man_page,
        output : man_page,
        configuration : conf_data
    )
endforeach

install_man(man_pages_out)

subdir('ru')
