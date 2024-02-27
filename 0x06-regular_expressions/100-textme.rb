#!/usr/bin/env ruby
# A regular expression that is matches a given pattern
pattern= /\[from:(.*?)\]\s\[to:(.*?)\]\s\[flags:(.*?)\]/

input = ARGV[0]

matches = input.scan(pattern)

puts matches.join(',')
