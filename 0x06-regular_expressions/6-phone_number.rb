#!/usr/bin/env ruby

input = ARGV[0]
pattern =  /^\d{10}$/

match = input.match(pattern)

if match
  puts input
end
