from distutils.core import setup

setup(name='ifupdown2',
      version='0.1',
      description = "ifupdown 2",
      author='Roopa Prabhu',
      author_email='roopa@cumulusnetworks.com',
      url='cumulusnetworks.com',
      packages=['ifupdown', 'ifupdownaddons'],
      scripts = ['sbin/ifupdown2'],
      install_requires = ['python-gvgen', 'python-argcomplete', 'python-ipaddr'],
      data_files=[('share/man/man8/',
                      ['man/ifup.8', 'man/ifquery.8', 'man/ifreload.8']),
                  ('share/man/man5/',
                      ['man/interfaces.5', 'man/ifupdown-addons-interfaces.5']),
                  ('/sbin/', ['sbin/ifupdown2']),
                  ('/etc/network/ifupdown2/',
                      ['config/ifupdown2.conf']),
                  ('/usr/share/doc/python-ifupdown2/examples/',
                      ['docs/examples/interfaces',
                       'docs/examples/interfaces_bridge_template_func',
                       'docs/examples/interfaces_with_template',
                       'docs/examples/interfaces_bridge_igmp_mstp']),
                  ('/usr/share/doc/python-ifupdown2/examples/vlan_aware_bridges',
                      ['docs/examples/vlan_aware_bridges/interfaces.basic',
                       'docs/examples/vlan_aware_bridges/interfaces.vlan_prune_and_access_ports',
                       'docs/examples/vlan_aware_bridges/interfaces.with_bonds',
                       'docs/examples/vlan_aware_bridges/interfaces.with_clag']),
                  ('/etc/bash_completion.d/', ['completion/ifup']),
                  ('/usr/share/ifupdownaddons/', ['addons/bridge.py',
                      'addons/ifenslave.py', 'addons/vlan.py',
                      'addons/mstpctl.py', 'addons/address.py',
                      'addons/dhcp.py', 'addons/usercmds.py',
                      'addons/ethtool.py', 'addons/loopback.py',
                      'addons/addressvirtual.py', 'addons/vxlan.py',
                      'addons/bridgevlan.py']),
                  ('/var/lib/ifupdownaddons/', ['config/addons.conf']),
                  ('/var/lib/ifupdownaddons/policy.d/', []),
                  ('/etc/network/ifupdown2/policy.d/', [])
                  ]
      )
