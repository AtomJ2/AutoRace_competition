from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'autorace_core_XROS'

data_files = [
    ('share/ament_index/resource_index/packages',
     ['resource/' + package_name]),
    ('share/' + package_name, ['package.xml']),
    (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
    ('share/' + package_name, ['best.pt']),
]

# Include 'yolov5' directory with all its files, preserving the folder structure
yolov5_dir = 'yolov5'
for dirpath, dirnames, filenames in os.walk(yolov5_dir):
    for filename in filenames:
        file_path = os.path.join(dirpath, filename)
        install_path = os.path.join('share', package_name, dirpath)
        data_files.append((install_path, [file_path]))

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=data_files,
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='atom',
    maintainer_email='atom.j2@mail.ru',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'pid_reg = autorace_core_XROS.pid_reg:main',
            'detect_line = autorace_core_XROS.detect_line:main',
            'detector_sign = autorace_core_XROS.detector_sign:main'
        ],
    },
)
