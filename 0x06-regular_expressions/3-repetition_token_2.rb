#!/usr/bin/env ruby

input = ARGV[0]

pattern = /hbt*n/

matches = input.scan(pattern)

puts matches.join
