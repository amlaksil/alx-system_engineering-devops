#!/usr/bin/env ruby
# A regular expression that outputs sender and receiver phone number or name
# including country code if present
puts ARGV[0].scan(/(?<=from:|to:|flags:).+?(?=\])/).join(',')
