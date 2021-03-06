from distutils.core import setup, Extension
from Cython.Distutils import build_ext

def main(cythonize=False):
    ext_modules = [
        Extension('pysbf.sbf', ['pysbf/sbf.pyx', 'pysbf/c_crc.c']),
        Extension('pysbf.blocks', ['pysbf/blocks.py']),
        Extension('pysbf.parsers', ['pysbf/parsers.pyx'])
    ]
    cmdclass = {'build_ext': build_ext}

    setup(name='pysbf',
          version='0.0.1',
          description='A Python module (in C) to parse "Septentrio Binary Format" (SBF) files generated by Septentrio receivers.',
          author='Jashandeep Sohi, Marco Job',
          author_email='jashandeep.s.sohi@gmail.com, marco.job@bluewin.ch',
          url='https://github.com/marcojob/pysbf',
          license='GPLv3',
          packages = ['pysbf'],
          cmdclass = cmdclass,
          ext_modules = ext_modules
    )

if __name__ == '__main__':
    main()
