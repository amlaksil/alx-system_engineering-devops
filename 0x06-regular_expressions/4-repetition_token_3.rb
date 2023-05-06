#!/usr/bin/env ruby
# A regular expression that match a string 'hbt{0,4}n'
puts ARGV[0].scan(/hbt?{1,4}n/).join
