#!/usr/bin/pup
# install a specific package 'flask' using puppet
package {'flask':
ensure	 => '2.1.0',
provider => 'pip3',
}
