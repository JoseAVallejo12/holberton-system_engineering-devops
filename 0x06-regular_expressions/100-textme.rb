#!/usr/bin/env ruby
#find character chain in string
puts ARGV[0].scan(/(?<=from:|to:|flags:)[^\]]*/).join(',')
