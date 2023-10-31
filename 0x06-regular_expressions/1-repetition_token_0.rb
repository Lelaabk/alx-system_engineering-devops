#!/usr/bin/env ruby
#Check if argument matches regular expression and print the result
puts ARGV[0].scan(/hbt{2,5}n/).join
