from distutils.core import setup
setup(
  name = 'Mandelpy',         
  packages = ['Mandelpy'],   
  version = '1.0',      
  license='MIT',        
  description = 'Mandelbrot library for Python',   
  author = 'Matteo Magri',                   
  author_email = 'magri.matteo@outlook.com',      
  url = 'https://github.com/MatteoMagri/Mandelpy',   
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['Python', 'Mandelbrot', 'PIL', 'ART', 'Graphics'],   
  install_requires=[            # I get to this in a second
          'validators',
          'beautifulsoup4',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      

    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',

    'License :: OSI Approved :: MIT License',   

    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
