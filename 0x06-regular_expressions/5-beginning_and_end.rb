#!/usr/bin/env ruby
# A regular expression that match a string starts with h ends with n and
# any single character in between
puts ARGV[0].scan(/^h.n$/).join
