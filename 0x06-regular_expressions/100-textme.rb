#!/usr/bin/env ruby

#Check if script is provided with log file argument
if ARGV.length != 1
  puts "Usage: #{$PROGRAM_NAME} [log file]"
  exit(1)
end

#Read log file specified in argument
log_file = File.open(ARGV[0])

#Initialize empty array to store results
results = []

#Regular expression to match sender, receiver, and flags
regex = /\[from:([\w+:]+)\] \[to:([\w+:]+)\] \[flags:([\d:-]+)\]/

#Iterate through lines of log file
log_file.each_line do |line|
  match = regex.match(line)
  if match
    sender = match[1]
    receiver = match[2]
    flags = match[3]
    resulrs << "#{sender},#{receiver},#{flags}"
  end
end

#Print results
puts results

#Close log file
log_file.close
