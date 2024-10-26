from setuptools import find_packages, setup

package_name = 'aav_test'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setusptools'],
    zip_safe=True,
    maintainer='msaud',
    maintainer_email='msaud@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    #aav_test_node is name of the executable through package
    #executable_name = package.file_name
    entry_points={
        'console_scripts': [
            "aav_test_node =  aav_test.node:main",
            "draw_circle = aav_test.draw_circle:main",
            "pose_subscriber = aav_test.pose_subscriber:main"
        ],
    },
)
