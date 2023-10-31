#!/usr/bin/env ruby
#Check if argument matches regular expression and for capital letter
matches = ARGV[0].scan(/[A-Z]/).join

if !matches.empty?
  puts matches
end
