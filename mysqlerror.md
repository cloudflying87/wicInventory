(wic.flyhomemn.com:3.8)flyhomem@mi3-ss45 [~/wic.flyhomemn.com]# pip install mysqlclient
Collecting mysqlclient
  Using cached mysqlclient-2.1.0.tar.gz (87 kB)
  Preparing metadata (setup.py) ... done
Building wheels for collected packages: mysqlclient
  Building wheel for mysqlclient (setup.py) ... error
  error: subprocess-exited-with-error
  
  × python setup.py bdist_wheel did not run successfully.
  │ exit code: 1
  ╰─> [43 lines of output]
      mysql_config --version
      ['10.3.20']
      mysql_config --libs
      ['-L/usr/lib64/mysql', '-lmariadb', '-lpthread', '-lz', '-ldl', '-lm', '-lssl', '-lcrypto']
      mysql_config --cflags
      ['-I/usr/include/mysql', '-I/usr/include/mysql/..']
      ext_options:
        library_dirs: ['/usr/lib64/mysql']
        libraries: ['mariadb', 'pthread', 'dl', 'm']
        extra_compile_args: ['-std=c99']
        extra_link_args: []
        include_dirs: ['/usr/include/mysql', '/usr/include/mysql/..']
        extra_objects: []
        define_macros: [('version_info', "(2,1,0,'final',0)"), ('__version__', '2.1.0')]
      /opt/alt/python38/lib64/python3.8/distutils/dist.py:274: UserWarning: Unknown distribution option: 'long_description_content_type'
        warnings.warn(msg)
      running bdist_wheel
      running build
      running build_py
      creating build
      creating build/lib.linux-x86_64-3.8
      creating build/lib.linux-x86_64-3.8/MySQLdb
      copying MySQLdb/__init__.py -> build/lib.linux-x86_64-3.8/MySQLdb
      copying MySQLdb/_exceptions.py -> build/lib.linux-x86_64-3.8/MySQLdb
      copying MySQLdb/connections.py -> build/lib.linux-x86_64-3.8/MySQLdb
      copying MySQLdb/converters.py -> build/lib.linux-x86_64-3.8/MySQLdb
      copying MySQLdb/cursors.py -> build/lib.linux-x86_64-3.8/MySQLdb
      copying MySQLdb/release.py -> build/lib.linux-x86_64-3.8/MySQLdb
      copying MySQLdb/times.py -> build/lib.linux-x86_64-3.8/MySQLdb
      creating build/lib.linux-x86_64-3.8/MySQLdb/constants
      copying MySQLdb/constants/__init__.py -> build/lib.linux-x86_64-3.8/MySQLdb/constants
      copying MySQLdb/constants/CLIENT.py -> build/lib.linux-x86_64-3.8/MySQLdb/constants
      copying MySQLdb/constants/CR.py -> build/lib.linux-x86_64-3.8/MySQLdb/constants
      copying MySQLdb/constants/ER.py -> build/lib.linux-x86_64-3.8/MySQLdb/constants
      copying MySQLdb/constants/FIELD_TYPE.py -> build/lib.linux-x86_64-3.8/MySQLdb/constants
      copying MySQLdb/constants/FLAG.py -> build/lib.linux-x86_64-3.8/MySQLdb/constants
      running build_ext
      building 'MySQLdb._mysql' extension
      creating build/temp.linux-x86_64-3.8
      creating build/temp.linux-x86_64-3.8/MySQLdb
      /opt/rh/devtoolset-7/root/usr/bin/gcc -Wno-unused-result -Wsign-compare -DNDEBUG -D_GNU_SOURCE -fPIC -fwrapv -O2 -fno-semantic-interposition -pthread -Wno-unused-result -Wsign-compare -ffat-lto-objects -flto-partition=none -g -std=c99 -Wextra -Wno-unused-parameter -Wno-missing-field-initializers -Werror=implicit-function-declaration -D_GNU_SOURCE -fPIC -fwrapv -D_GNU_SOURCE -fPIC -fwrapv -O2 -fno-semantic-interposition -pthread -Wno-unused-result -Wsign-compare -ffat-lto-objects -flto-partition=none -g -std=c99 -Wextra -Wno-unused-parameter -Wno-missing-field-initializers -Werror=implicit-function-declaration -D_GNU_SOURCE -fPIC -fwrapv -O2 -fno-semantic-interposition -pthread -Wno-unused-result -Wsign-compare -ffat-lto-objects -flto-partition=none -g -std=c99 -Wextra -Wno-unused-parameter -Wno-missing-field-initializers -Werror=implicit-function-declaration -fPIC -Dversion_info=(2,1,0,'final',0) -D__version__=2.1.0 -I/usr/include/mysql -I/usr/include/mysql/.. -I/opt/alt/python38/include/python3.8 -c MySQLdb/_mysql.c -o build/temp.linux-x86_64-3.8/MySQLdb/_mysql.o -std=c99
      unable to execute '/opt/rh/devtoolset-7/root/usr/bin/gcc': No such file or directory
      error: command '/opt/rh/devtoolset-7/root/usr/bin/gcc' failed with exit status 1
      [end of output]
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for mysqlclient
  Running setup.py clean for mysqlclient
Failed to build mysqlclient
Installing collected packages: mysqlclient
  Running setup.py install for mysqlclient ... error
  error: subprocess-exited-with-error
  
  × Running setup.py install for mysqlclient did not run successfully.
  │ exit code: 1
  ╰─> [43 lines of output]
      mysql_config --version
      ['10.3.20']
      mysql_config --libs
      ['-L/usr/lib64/mysql', '-lmariadb', '-lpthread', '-lz', '-ldl', '-lm', '-lssl', '-lcrypto']
      mysql_config --cflags
      ['-I/usr/include/mysql', '-I/usr/include/mysql/..']
      ext_options:
        library_dirs: ['/usr/lib64/mysql']
        libraries: ['mariadb', 'pthread', 'dl', 'm']
        extra_compile_args: ['-std=c99']
        extra_link_args: []
        include_dirs: ['/usr/include/mysql', '/usr/include/mysql/..']
        extra_objects: []
        define_macros: [('version_info', "(2,1,0,'final',0)"), ('__version__', '2.1.0')]
      /opt/alt/python38/lib64/python3.8/distutils/dist.py:274: UserWarning: Unknown distribution option: 'long_description_content_type'
        warnings.warn(msg)
      running install
      running build
      running build_py
      creating build
      creating build/lib.linux-x86_64-3.8
      creating build/lib.linux-x86_64-3.8/MySQLdb
      copying MySQLdb/__init__.py -> build/lib.linux-x86_64-3.8/MySQLdb
      copying MySQLdb/_exceptions.py -> build/lib.linux-x86_64-3.8/MySQLdb
      copying MySQLdb/connections.py -> build/lib.linux-x86_64-3.8/MySQLdb
      copying MySQLdb/converters.py -> build/lib.linux-x86_64-3.8/MySQLdb
      copying MySQLdb/cursors.py -> build/lib.linux-x86_64-3.8/MySQLdb
      copying MySQLdb/release.py -> build/lib.linux-x86_64-3.8/MySQLdb
      copying MySQLdb/times.py -> build/lib.linux-x86_64-3.8/MySQLdb
      creating build/lib.linux-x86_64-3.8/MySQLdb/constants
      copying MySQLdb/constants/__init__.py -> build/lib.linux-x86_64-3.8/MySQLdb/constants
      copying MySQLdb/constants/CLIENT.py -> build/lib.linux-x86_64-3.8/MySQLdb/constants
      copying MySQLdb/constants/CR.py -> build/lib.linux-x86_64-3.8/MySQLdb/constants
      copying MySQLdb/constants/ER.py -> build/lib.linux-x86_64-3.8/MySQLdb/constants
      copying MySQLdb/constants/FIELD_TYPE.py -> build/lib.linux-x86_64-3.8/MySQLdb/constants
      copying MySQLdb/constants/FLAG.py -> build/lib.linux-x86_64-3.8/MySQLdb/constants
      running build_ext
      building 'MySQLdb._mysql' extension
      creating build/temp.linux-x86_64-3.8
      creating build/temp.linux-x86_64-3.8/MySQLdb
      /opt/rh/devtoolset-7/root/usr/bin/gcc -Wno-unused-result -Wsign-compare -DNDEBUG -D_GNU_SOURCE -fPIC -fwrapv -O2 -fno-semantic-interposition -pthread -Wno-unused-result -Wsign-compare -ffat-lto-objects -flto-partition=none -g -std=c99 -Wextra -Wno-unused-parameter -Wno-missing-field-initializers -Werror=implicit-function-declaration -D_GNU_SOURCE -fPIC -fwrapv -D_GNU_SOURCE -fPIC -fwrapv -O2 -fno-semantic-interposition -pthread -Wno-unused-result -Wsign-compare -ffat-lto-objects -flto-partition=none -g -std=c99 -Wextra -Wno-unused-parameter -Wno-missing-field-initializers -Werror=implicit-function-declaration -D_GNU_SOURCE -fPIC -fwrapv -O2 -fno-semantic-interposition -pthread -Wno-unused-result -Wsign-compare -ffat-lto-objects -flto-partition=none -g -std=c99 -Wextra -Wno-unused-parameter -Wno-missing-field-initializers -Werror=implicit-function-declaration -fPIC -Dversion_info=(2,1,0,'final',0) -D__version__=2.1.0 -I/usr/include/mysql -I/usr/include/mysql/.. -I/opt/alt/python38/include/python3.8 -c MySQLdb/_mysql.c -o build/temp.linux-x86_64-3.8/MySQLdb/_mysql.o -std=c99
      unable to execute '/opt/rh/devtoolset-7/root/usr/bin/gcc': No such file or directory
      error: command '/opt/rh/devtoolset-7/root/usr/bin/gcc' failed with exit status 1
      [end of output]
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
error: legacy-install-failure

× Encountered error while trying to install package.
╰─> mysqlclient

note: This is an issue with the package mentioned above, not pip.
hint: See above for output from the failure.
