#!/usr/bin/env ruby
# A regular expression that match's only capital letters
puts ARGV[0].scan(/[A-Z]/).join
