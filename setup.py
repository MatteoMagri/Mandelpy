from distutils.core import setup
setup(
  name = 'mandelpy',         
  packages = ['mandelpy'],   
  version = '1.3',      
  license='MIT',        
  description = 'Mandelbrot library for Python',   
  author = 'Matteo Magri',                   
  author_email = 'magri.matteo@outlook.com',      
  url = 'https://github.com/MatteoMagri/Mandelpy',   
  download_url = 'https://github.com/MatteoMagri/Mandelpy/archive/v1.3.tar.gz',
  keywords = ['Python', 'Mandelbrot', 'PIL', 'ART', 'Graphics'],   
  install_requires=[            
          'Pillow',
          'numpy',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      

    'Intended Audience :: Artist',     
    'Topic :: Software Development :: Build Tools',

    'License :: OSI Approved :: MIT License',   

    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
