from setuptools import setup

package_name = 'kadabra'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ubuntu',
    maintainer_email='ubuntu@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "open_trigger = kadabra.trigger:main",
            "toggle_LED = kadabra.LED:main",
            "classify = kadabra.classifier_node:main",
            "mpu6050 = kadabra.mpu6050_node:main"
        ],
    },
)