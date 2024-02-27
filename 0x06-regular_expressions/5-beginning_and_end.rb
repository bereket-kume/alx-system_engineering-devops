#!/usr/bin/env ruby

input = ARGV[0]

pattern = /^h.n$/

match = input.match(pattern)

if match
  puts input
else
  puts ""
end
