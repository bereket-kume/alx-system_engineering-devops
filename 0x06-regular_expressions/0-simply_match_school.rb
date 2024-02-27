#!/usr/bin/env ruby

if ARGV.empty?
  exit
end

input = ARGV[0]

pattern = /School/

matches = input.scan(pattern)

puts matches.join
