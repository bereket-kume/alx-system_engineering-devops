#!/usr/bin/env ruby

if ARGV.empty?
  exit
end

input = ARGV[0]

pattern = /hb*tn/

matches = input.scan(pattern)

puts matches.join
