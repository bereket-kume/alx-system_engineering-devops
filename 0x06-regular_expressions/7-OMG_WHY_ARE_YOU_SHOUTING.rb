#!/usr/bin/env ruby

input = ARGV[0]

pattern =/^[A-Z]+$/

matches = input.scan(pattern)

if matches.any?
  puts matches.join
end
