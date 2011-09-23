from setuptools import setup , find_packages

setup ( name = "NorCrawler", 
        version = "0.1",
        packages = find_packages (),
        scripts = ['NorCrawler'],
        install_requires = [' BeatifulSoup '],
        package_data = { ' pynorcrawler ': [''], },
        author = " Imanol Lazkano ",
        author_email = "imanol.lazkano@gmail.com",
        description = " Crawler de Prueba ",
        license = "GPLv2",
        keywords = "",
        url = "",
        long_description = "",
        download_url = "" )
