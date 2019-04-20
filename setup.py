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
  download_url = 'https://github.com/MatteoMagri/Mandelpy/archive/Mandelpy-v1.0.tar.gz',
  keywords = ['Python', 'Mandelbrot', 'PIL', 'ART', 'Graphics'],   
  install_requires=[            
          'Pillow',
          'Scipy',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      

    'Intended Audience :: Developers',     
    'Topic :: Software Development :: Build Tools',

    'License :: OSI Approved :: MIT License',   

    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
