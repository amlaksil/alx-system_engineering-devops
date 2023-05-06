#!/usr/bin/env ruby
# A regular expression that match a string 'hbt{1,5}n'
puts ARGV[0].scan(/hbt{2,5}n/).join
